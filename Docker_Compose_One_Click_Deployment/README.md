# 🚀 FastAPI Project

## 📦 Quickstart

1. Clone this repo.




# 🚀 FastAPI + PostgreSQL Dockerized Project

This project contains a REST API built with FastAPI and a PostgreSQL database. Services are managed with Docker Compose, and build/run operations are streamlined using a Makefile.

---

## 🔧 Prerequisites

Make sure the following tools are installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Make](https://www.gnu.org/software/make/)

Verify with:


docker --version
docker compose version
make --version


🧪 Manual Step-by-Step Execution

make db-start       # Start database container
make db-migrate     # Run Alembic DB migrations
make build-api      # Build the API image
make run-api        # Launch the API container

