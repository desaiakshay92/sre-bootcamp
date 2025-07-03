DOCKER_COMPOSE = docker compose
DB_SERVICE = db
API_SERVICE = fastapi-service
VERSION := $(shell git describe --tags --abbrev=0)
DOCKER_TAG = $(API_SERVICE):$(VERSION)

.PHONY: db-start db-migrate build-api run-api check-db

# Start only the database service
db-start:
	@echo "🔄 Starting database container..."
	@$(DOCKER_COMPOSE) up -d $(DB_SERVICE)

# Run Alembic migrations inside the API container
db-migrate:
	@echo "⚙️ Running Alembic migrations..."
	@$(DOCKER_COMPOSE) run --rm $(API_SERVICE) alembic upgrade head

# Build the API docker image
build-api:
	@echo "🔨 Building API Docker image..."
	@docker build -t $(DOCKER_TAG) .

# Start full app (DB, Migrations, API)
run-api: db-start build-api
	@echo "⏳ Waiting for DB to become healthy..."
	@until [ "`docker inspect -f '{{.State.Health.Status}}' my_pgdb`" = "healthy" ]; do \
		echo "⏳ Waiting for db..."; sleep 2; \
	done
	@echo "✅ DB is healthy. Running migrations..."
	@$(MAKE) db-migrate
	@echo "🚀 Starting FastAPI container..."
	@$(DOCKER_COMPOSE) up -d $(API_SERVICE)

# Stop all containers
stop:
	@echo "🛑 Stopping and removing containers..."
	@$(DOCKER_COMPOSE) down

# Remove containers, images, volumes, networks
clear:
	@echo "🔥 Removing containers, images, volumes..."
	@$(DOCKER_COMPOSE) down --volumes --rmi all --remove-orphans
