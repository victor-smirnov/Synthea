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
package main

import (
	"context"
	"path/filepath"
	"strings"
	"testing"
)

func TestOpenEmbeddedEngineAndEchoProcedure(t *testing.T) {
	ctx := context.Background()
	base := t.TempDir()
	repoDir := filepath.Join(base, "memory")
	homeDir := filepath.Join(base, "home")

	se, err := openEmbeddedEngine(ctx, repoDir, homeDir)
	if err != nil {
		t.Fatal(err)
	}
	defer se.Close()

	out, err := runQuery(ctx, se, `CALL synthea_echo('probe')`)
	if err != nil {
		t.Fatal(err)
	}
	if !strings.Contains(out, "synthea_echo: probe") {
		t.Fatalf("unexpected output: %s", out)
	}
}
