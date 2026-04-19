# syntax=docker/dockerfile:1

FROM rust:1.81 AS backend-builder
WORKDIR /app/backend
COPY backend/Cargo.toml backend/Cargo.lock* ./
COPY backend/crates ./crates
RUN cargo test --workspace --locked || cargo test --workspace

FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/trade-app/package.json trade-app/
COPY frontend/designer-app/package.json designer-app/
COPY frontend/trade-app/tsconfig.json trade-app/
COPY frontend/trade-app/src trade-app/src
COPY frontend/designer-app/tsconfig.json designer-app/
COPY frontend/designer-app/src designer-app/src
COPY frontend/shared shared/
RUN cd trade-app && npm install --no-package-lock --silent && npm run typecheck
RUN cd designer-app && npm install --no-package-lock --silent && npm run typecheck

FROM debian:bookworm-slim AS runtime
WORKDIR /srv
COPY --from=backend-builder /app/backend /srv/backend
COPY --from=frontend-builder /app/frontend /srv/frontend
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 CMD test -f /srv/backend/Cargo.toml || exit 1
CMD ["/bin/sh", "-c", "echo GANE unified image ready && sleep infinity"]
