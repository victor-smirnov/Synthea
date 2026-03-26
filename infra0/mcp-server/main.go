// Copyright (c) 2025 Victor Smirnov.
// AI-assisted contributions: Synthea, under the same license.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.
//
// Synthea MCP: embedded Dolt + Go stored procedure + MCP tools (stdio and/or streamable HTTP).
package main

import (
	"context"
	"errors"
	"flag"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"os/signal"
	"path/filepath"
	"syscall"
	"time"

	"github.com/dolthub/dolt/go/cmd/dolt/commands/engine"
	"github.com/dolthub/dolt/go/cmd/dolt/doltversion"
	"github.com/dolthub/dolt/go/libraries/doltcore/doltdb"
	"github.com/dolthub/dolt/go/libraries/doltcore/env"
	"github.com/dolthub/dolt/go/libraries/doltcore/sqle"
	"github.com/dolthub/dolt/go/libraries/utils/config"
	"github.com/dolthub/dolt/go/libraries/utils/filesys"
	noms "github.com/dolthub/dolt/go/store/types"
	"github.com/dolthub/go-mysql-server/sql"
	gmstypes "github.com/dolthub/go-mysql-server/sql/types"
	"github.com/modelcontextprotocol/go-sdk/mcp"
	"log/slog"
)

// syntheaEcho is a Go-backed stored procedure (ExternalStoredProcedureDetails).
func syntheaEcho(ctx *sql.Context, message string) (sql.RowIter, error) {
	out := fmt.Sprintf("synthea_echo: %s", message)
	return sql.RowsToRowIter(sql.Row{out, int64(1)}), nil
}

func openEmbeddedEngine(ctx context.Context, repoDir, homeDir string) (*engine.SqlEngine, error) {
	if err := os.MkdirAll(repoDir, 0o755); err != nil {
		return nil, err
	}
	if err := os.MkdirAll(homeDir, 0o755); err != nil {
		return nil, err
	}

	fs, err := filesys.LocalFilesysWithWorkingDir(repoDir)
	if err != nil {
		return nil, err
	}
	hdp := func() (string, error) { return homeDir, nil }

	dEnv := env.Load(ctx, hdp, fs, doltdb.LocalDirDoltDB, doltversion.Version)
	if dEnv.CfgLoadErr != nil {
		return nil, dEnv.CfgLoadErr
	}
	if !dEnv.HasDoltDir() {
		cfg, ok := dEnv.Config.GetConfig(env.GlobalConfig)
		if !ok {
			return nil, fmt.Errorf("global dolt config not found")
		}
		if err := cfg.SetStrings(map[string]string{
			config.UserNameKey:  "Synthea MCP",
			config.UserEmailKey: "synthea-mcp@local",
		}); err != nil {
			return nil, err
		}
		if err := dEnv.InitRepo(ctx, noms.Format_Default, "Synthea MCP", "synthea-mcp@local", env.DefaultInitBranch); err != nil {
			return nil, err
		}
	}
	if !dEnv.Valid() {
		return nil, fmt.Errorf("dolt env invalid: dbLoad=%v rsLoad=%v", dEnv.DBLoadError, dEnv.RSLoadErr)
	}

	mrEnv, err := env.MultiEnvForSingleEnv(ctx, dEnv)
	if err != nil {
		return nil, err
	}

	seCfg := &engine.SqlEngineConfig{
		ServerUser:        "root",
		ServerHost:        "localhost",
		ClusterController: nil,
	}
	se, err := engine.NewSqlEngine(ctx, mrEnv, seCfg)
	if err != nil {
		return nil, err
	}
	if err := se.InitStats(ctx); err != nil {
		return nil, err
	}

	pro, ok := se.GetUnderlyingEngine().Analyzer.Catalog.DbProvider.(*sqle.DoltDatabaseProvider)
	if !ok {
		return nil, fmt.Errorf("expected *sqle.DoltDatabaseProvider")
	}
	pro.RegisterProcedure(sql.ExternalStoredProcedureDetails{
		Name: "synthea_echo",
		Schema: sql.Schema{
			{Name: "reply", Type: gmstypes.LongText, Nullable: false},
			{Name: "ok", Type: gmstypes.Int64, Nullable: false},
		},
		Function: syntheaEcho,
	})

	return se, nil
}

func runQuery(ctx context.Context, se *engine.SqlEngine, q string) (string, error) {
	sqlCtx, err := se.NewLocalContext(ctx)
	if err != nil {
		return "", err
	}
	defer sql.SessionEnd(sqlCtx.Session)
	sql.SessionCommandBegin(sqlCtx.Session)
	defer sql.SessionCommandEnd(sqlCtx.Session)

	schema, iter, _, err := se.Query(sqlCtx, q)
	if err != nil {
		return "", err
	}
	defer iter.Close(sqlCtx)

	var lines []string
	for {
		row, err := iter.Next(sqlCtx)
		if err != nil {
			if err == io.EOF {
				break
			}
			return "", err
		}
		lines = append(lines, fmt.Sprint(row))
	}
	if len(schema) > 0 {
		return fmt.Sprintf("%v | rows: %v", schema, lines), nil
	}
	return fmt.Sprintf("%v", lines), nil
}

func newMCPServer(se *engine.SqlEngine) *mcp.Server {
	srv := mcp.NewServer(&mcp.Implementation{Name: "synthea-mcp", Version: "0.0.1"}, nil)

	type pingArgs struct {
		Message string `json:"message" jsonschema:"optional test payload"`
	}
	mcp.AddTool(srv, &mcp.Tool{
		Name:        "synthea_echo_proc",
		Description: "Calls the Go-registered stored procedure synthea_echo(message) in embedded Dolt.",
	}, func(ctx context.Context, req *mcp.CallToolRequest, args pingArgs) (*mcp.CallToolResult, any, error) {
		msg := args.Message
		if msg == "" {
			msg = "hello"
		}
		q := fmt.Sprintf("CALL synthea_echo(%s)", quoteSQLString(msg))
		out, err := runQuery(ctx, se, q)
		if err != nil {
			return nil, nil, err
		}
		return &mcp.CallToolResult{
			Content: []mcp.Content{&mcp.TextContent{Text: out}},
		}, map[string]any{"raw": out}, nil
	})

	type sqlArgs struct {
		Query string `json:"query" jsonschema:"read-only SQL to run against embedded Dolt"`
	}
	mcp.AddTool(srv, &mcp.Tool{
		Name:        "dolt_sql",
		Description: "Run a single read-only SQL statement (explore). Prefer SELECT / CALL for this spike.",
	}, func(ctx context.Context, req *mcp.CallToolRequest, args sqlArgs) (*mcp.CallToolResult, any, error) {
		if args.Query == "" {
			return nil, nil, fmt.Errorf("query is required")
		}
		out, err := runQuery(ctx, se, args.Query)
		if err != nil {
			return nil, nil, err
		}
		return &mcp.CallToolResult{
			Content: []mcp.Content{&mcp.TextContent{Text: out}},
		}, map[string]any{"raw": out}, nil
	})

	return srv
}

func runHTTP(ctx context.Context, srv *mcp.Server, addr string) error {
	logger := slog.New(slog.NewJSONHandler(os.Stderr, &slog.HandlerOptions{}))

	// One MCP Server instance for every HTTP session (multi-session streamable transport).
	mcpHandler := mcp.NewStreamableHTTPHandler(func(_ *http.Request) *mcp.Server {
		return srv
	}, &mcp.StreamableHTTPOptions{
		Logger: logger,
	})

	mux := http.NewServeMux()
	mux.HandleFunc("/health", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodGet {
			http.Error(w, "method not allowed", http.StatusMethodNotAllowed)
			return
		}
		w.Header().Set("Content-Type", "text/plain; charset=utf-8")
		w.WriteHeader(http.StatusOK)
		_, _ = io.WriteString(w, "ok\n")
	})
	mux.Handle("/mcp", mcpHandler)
	mux.Handle("/mcp/", mcpHandler)

	httpServer := &http.Server{
		Addr:              addr,
		Handler:           mux,
		ReadHeaderTimeout: 30 * time.Second,
	}

	errCh := make(chan error, 1)
	go func() {
		log.Printf("synthea-mcp HTTP listening on %s — MCP streamable endpoint: /mcp", addr)
		errCh <- httpServer.ListenAndServe()
	}()

	select {
	case <-ctx.Done():
		shutdownCtx, cancel := context.WithTimeout(context.Background(), 15*time.Second)
		defer cancel()
		_ = httpServer.Shutdown(shutdownCtx)
		err := <-errCh
		if err != nil && err != http.ErrServerClosed {
			return err
		}
		return nil
	case err := <-errCh:
		if err != nil && err != http.ErrServerClosed {
			return err
		}
		return nil
	}
}

func main() {
	transportFlag := flag.String("transport", "", "stdio | http (default: stdio, or SYNTHEA_MCP_TRANSPORT)")
	httpAddrFlag := flag.String("http-addr", "", "listen address for HTTP transport (default :8787, or SYNTHEA_MCP_HTTP_ADDR)")
	flag.Parse()

	transport := *transportFlag
	if transport == "" {
		transport = os.Getenv("SYNTHEA_MCP_TRANSPORT")
	}
	if transport == "" {
		transport = "stdio"
	}

	httpAddr := *httpAddrFlag
	if httpAddr == "" {
		httpAddr = os.Getenv("SYNTHEA_MCP_HTTP_ADDR")
	}
	if httpAddr == "" {
		httpAddr = ":8787"
	}

	setupCtx := context.Background()

	dataRoot := os.Getenv("SYNTHEA_MCP_DATA")
	if dataRoot == "" {
		dataRoot = filepath.Join(".", "mcp-data")
	}
	repoDir := filepath.Join(dataRoot, "memory")
	homeDir := filepath.Join(dataRoot, "home")

	se, err := openEmbeddedEngine(setupCtx, repoDir, homeDir)
	if err != nil {
		log.Fatalf("embedded dolt: %v", err)
	}
	defer se.Close()

	srv := newMCPServer(se)

	runCtx, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
	defer stop()

	switch transport {
	case "stdio":
		if err := srv.Run(runCtx, &mcp.StdioTransport{}); err != nil && !errors.Is(err, context.Canceled) {
			log.Fatal(err)
		}
	case "http":
		if err := runHTTP(runCtx, srv, httpAddr); err != nil {
			log.Fatal(err)
		}
	default:
		log.Fatalf("unknown -transport %q (use stdio or http)", transport)
	}
}

func quoteSQLString(s string) string {
	b := []byte{'\''}
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c == '\'' {
			b = append(b, '\'', '\'')
		} else {
			b = append(b, c)
		}
	}
	b = append(b, '\'')
	return string(b)
}
