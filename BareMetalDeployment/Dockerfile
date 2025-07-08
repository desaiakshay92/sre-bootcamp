# syntax=docker/dockerfile:1

# ------------------------------
# Stage 1: Build dependencies
# ------------------------------
FROM python:3.13-slim AS builder

WORKDIR /app

# Reduce noise and improve caching
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_CREATE=false

# System-level dependencies for builds
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# ------------------------------
# Stage 2: Runtime
# ------------------------------
FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

# Create non-root user for security
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Copy installed Python packages from builder
COPY --from=builder /usr/local /usr/local

# Copy source code
COPY . .

EXPOSE 8000

# Healthcheck for production robustness
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl --fail http://localhost:8000/healthcheck || exit 1

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
