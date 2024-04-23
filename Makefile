.PHONY: build up down migrate make-migrations

# Variables
DOCKER_COMPOSE = docker-compose

# Construye la imagen Docker
build-server:
	$(DOCKER_COMPOSE) build

build-local:
	$(DOCKER_COMPOSE) --env-file .env.dev build --no-cache

# Inicia los contenedores
up-server:
	$(DOCKER_COMPOSE) up -d

up-local:
	$(DOCKER_COMPOSE) --env-file .env.dev up -d

# Detiene y elimina los contenedores
down-server:
	$(DOCKER_COMPOSE) down

down-local:
	$(DOCKER_COMPOSE) --env-file .env.dev down

clear:
	docker system prune -a

define make_migrations
if [ -z "$(message)" ]; then \
	echo "Por favor, proporciona un mensaje para la migración con message='tu_mensaje'"; \
else \
	$(DOCKER_COMPOSE) run --rm app alembic revision --autogenerate -m "$(mesaage)"; \
fi
endef

# Hace las migraciones de Alembic
make-migrations:
	$(call make_migrations)

# Ejecuta las migraciones de Alembic en modo de desarrollo
migrate:
	$(DOCKER_COMPOSE) run --rm app alembic upgrade head

# Ejecuta las migraciones de Alembic para revertir al estado anterior
migrate-down:
	$(DOCKER_COMPOSE) run --rm app alembic downgrade -1
