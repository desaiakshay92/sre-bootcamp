APP_NAME = fastapi-service
VERSION := $(shell git describe --tags --abbrev=0)
DOCKER_TAG = $(APP_NAME):$(VERSION)

.PHONY: build run tag-latest hadolint

build:
	docker build -t $(DOCKER_TAG) .

start-db:
	docker run --rm --name fastapi-postgres \
      -e POSTGRES_DB=testdb \
      -e POSTGRES_USER=demo \
      -e POSTGRES_PASSWORD=demo \
      -p 5433:5432 \
      -d postgres:15-alpine
run:
	docker run -p 8000:8000 --env-file .env $(DOCKER_TAG)

tag-latest:
	docker tag $(DOCKER_TAG) $(APP_NAME):latest

hadolint:
	docker run --rm -i hadolint/hadolint hadolint --ignore DL3008 - < Dockerfile