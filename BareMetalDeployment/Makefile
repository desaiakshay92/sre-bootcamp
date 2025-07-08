DOCKER_COMPOSE = docker-compose
DB_SERVICE = db
API_SERVICES = fastapi1 fastapi2
VERSION := $(shell git describe --tags --abbrev=0 2>/dev/null || echo "latest")
DOCKER_TAG = fastapi_app:$(VERSION)

.PHONY: db-start db-migrate build-api run-api stop clear logs

# Start only the database service
db-start:
	@echo "🔄 Starting database container..."
	@$(DOCKER_COMPOSE) up -d $(DB_SERVICE)

# Run Alembic migrations inside one of the API containers
db-migrate:
	@echo "⚙️ Running Alembic migrations..."
	@$(DOCKER_COMPOSE) run --rm fastapi1 alembic upgrade head

# Build the API docker image
build-api:
	@echo "🔨 Building API Docker image..."
	@docker build -t $(DOCKER_TAG) .

# Start full app (DB, Migrations, APIs, Nginx)
run-api: db-start build-api
	@echo "⏳ Waiting for DB to become healthy..."
	@until [ "`docker inspect -f '{{.State.Health.Status}}' my_pgdb`" = "healthy" ]; do \
		echo "⏳ Waiting for db..."; sleep 2; \
	done
	@echo "✅ DB is healthy. Running migrations..."
	@$(MAKE) db-migrate
	@echo "🚀 Starting API and Nginx containers..."
	@$(DOCKER_COMPOSE) up -d fastapi1 fastapi2 nginx

# View logs
logs:
	@$(DOCKER_COMPOSE) logs -f

# Stop all containers
stop:
	@echo "🛑 Stopping and removing containers..."
	@$(DOCKER_COMPOSE) down

# Remove containers, images, volumes, networks
clear:
	@echo "🔥 Removing containers, images, volumes..."
	@$(DOCKER_COMPOSE) down --volumes --rmi all --remove-orphans