.PHONY: build up down migrate

# Variables
DOCKER_COMPOSE = docker-compose

# Construye la imagen Docker
build:
	$(DOCKER_COMPOSE) build

# Inicia los contenedores
up:
	$(DOCKER_COMPOSE) up -d

# Detiene y elimina los contenedores
down:
	$(DOCKER_COMPOSE) down

# Ejecuta las migraciones de Alembic
migrate:
	$(DOCKER_COMPOSE) run --rm web alembic upgrade head

# Ejecuta las migraciones de Alembic en modo de desarrollo
migrate-dev:
	$(DOCKER_COMPOSE) run --rm web alembic upgrade head --sql
	$(DOCKER_COMPOSE) run --rm web alembic upgrade head

# Ejecuta las migraciones de Alembic para revertir al estado anterior
migrate-down:
	$(DOCKER_COMPOSE) run --rm web alembic downgrade -1

# Ejecuta las migraciones de Alembic para revertir al estado anterior en modo de desarrollo
migrate-down-dev:
	$(DOCKER_COMPOSE) run --rm web alembic downgrade -1 --sql
	$(DOCKER_COMPOSE) run --rm web alembic downgrade -1