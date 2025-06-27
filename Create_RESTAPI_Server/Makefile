# Makefile for FastAPI local development

.PHONY: run makemigrations upgrade test coverage clean

APP_MODULE=app.main:app
ENV_FILE=.env

makemigrations:
	alembic revision --autogenerate -m "Auto migration"

upgrade:
	alembic upgrade head

run:
	uvicorn $(APP_MODULE) --reload --env-file $(ENV_FILE)

test:
	pytest tests/ --disable-warnings

coverage:
	pytest --cov=app --cov-report=term-missing tests/

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +