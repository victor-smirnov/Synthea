# syntax=docker/dockerfile:1
# Builds synthea-mcp with embedded Dolt (CGO). Dolt source is cloned at DOLT_REF
# and wired via go.mod replace (same idea as local ../../dolt/go).

ARG GO_VERSION=1.25.6
FROM golang:${GO_VERSION}-bookworm AS builder

ARG DOLT_REF=v1.84.0

RUN apt-get update && apt-get install -y --no-install-recommends \
    git ca-certificates gcc libc6-dev libicu-dev \
    && rm -rf /var/lib/apt/lists/*

RUN git clone --depth 1 --branch "${DOLT_REF}" https://github.com/dolthub/dolt.git /dolt-src

WORKDIR /src
COPY go.mod go.sum ./

# Drop dev-only replace to ../../dolt/go; point at the cloned tree.
RUN sed -i '/^replace github.com\/dolthub\/dolt\/go/d' go.mod \
    && go mod edit -replace github.com/dolthub/dolt/go=/dolt-src/go \
    && go mod download

COPY . .

# COPY restores go.mod from the repo (with ../../dolt/go replace); re-apply for Docker.
RUN sed -i '/^replace github.com\/dolthub\/dolt\/go/d' go.mod \
    && go mod edit -replace github.com/dolthub/dolt/go=/dolt-src/go \
    && go mod download

RUN CGO_ENABLED=1 go build -trimpath -ldflags="-s -w" -o /synthea-mcp .

FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates curl \
    libgcc-s1 \
    libicu72 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /synthea-mcp /usr/local/bin/synthea-mcp

ENV SYNTHEA_MCP_TRANSPORT=http
ENV SYNTHEA_MCP_HTTP_ADDR=:8787
ENV SYNTHEA_MCP_DATA=/data

EXPOSE 8787

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
    CMD curl -fsS http://127.0.0.1:8787/health || exit 1

ENTRYPOINT ["/usr/local/bin/synthea-mcp"]
