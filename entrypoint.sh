#!/bin/bash

export PGPASSWORD=${POSTGRES_PASSWORD}

# Esperar a que el servicio de base de datos esté listo
while ! pg_isready -h db -U ${POSTGRES_USER}; do
    sleep 1
done

# Crear la base de datos si no existe
if ! psql -h db -U ${POSTGRES_USER} -lqt | cut -d \| -f 1 | grep -qw ${POSTGRES_DB}; then
    createdb -h db -U ${POSTGRES_USER} ${POSTGRES_DB}
fi

# Aplicar migraciones
alembic upgrade head

# Iniciar la aplicación
exec "$@"