# Template-Base-Microservicio-FastAPI

![Logo base](/assets/Logo_Base.png)

## :ledger: Index

- [Template-Base-Microservicio-FastAPI](#template-base-microservicio-fastapi)
  - [:ledger: Index](#ledger-index)
  - [:beginner: Descripción](#beginner-descripción)
  - [:zap: Uso](#zap-uso)
    - [:whale: Instalación por Docker](#whale-instalación-por-docker)
      - [Paso 1: Construir imagenes](#paso-1-construir-imagenes)
      - [Paso 2: Realizar migraciones de los modelos](#paso-2-realizar-migraciones-de-los-modelos)
      - [Paso 3: Actualizar migración actual](#paso-3-actualizar-migración-actual)
      - [Paso 4: Levantar proyecto](#paso-4-levantar-proyecto)
    - [:desktop\_computer: Instalación Localmente](#desktop_computer-instalación-localmente)
      - [Paso 1: Instalar librerias del proyecto](#paso-1-instalar-librerias-del-proyecto)
      - [Paso 2: Creación de Base de Dasto](#paso-2-creación-de-base-de-dasto)
      - [Paso 3: Cambiar la URL de Base de Datos en el `settings.py`](#paso-3-cambiar-la-url-de-base-de-datos-en-el-settingspy)
      - [Paso 4: Realizar migraciones y actualizar la migración](#paso-4-realizar-migraciones-y-actualizar-la-migración)
      - [Paso 4.5: Devolver la ultima migración y actualizar la migración](#paso-45-devolver-la-ultima-migración-y-actualizar-la-migración)
      - [Paso 5: Levantar proyecto](#paso-5-levantar-proyecto)
  - [:wrench: Desarrollo](#wrench-desarrollo)
      - [Paso 1: Clonar el repositorio](#paso-1-clonar-el-repositorio)
      - [Paso 2: Crear Repositorio para el nuevo repositorio y copiar el proyecto dentro.](#paso-2-crear-repositorio-para-el-nuevo-repositorio-y-copiar-el-proyecto-dentro)
      - [Paso 3: Configurar Bases de Datos para el nuevo microservicio](#paso-3-configurar-bases-de-datos-para-el-nuevo-microservicio)
      - [Paso 4: Solicitar despliegue](#paso-4-solicitar-despliegue)
    - [:notebook: Pre-Requisitos - Programas a instalar](#notebook-pre-requisitos---programas-a-instalar)
    - [:nut\_and\_bolt: Entorno de Desarollo](#nut_and_bolt-entorno-de-desarollo)
    - [:file\_folder: Estructura de Directorios](#file_folder-estructura-de-directorios)
    - [:cactus: Ramas](#cactus-ramas)
      - [Configuración Inicial](#configuración-inicial)
      - [Branching (Explicación)](#branching-explicación)
    - [Ramas de características, corrección de errores, hotfix y versiones:](#ramas-de-características-corrección-de-errores-hotfix-y-versiones)
    - [Flujo de Trabajo Recomendado](#flujo-de-trabajo-recomendado)
      - [Desarrollo de una nueva característica:](#desarrollo-de-una-nueva-característica)
      - [Corrección de errores:](#corrección-de-errores)
      - [Arreglos urgentes (hotfix):](#arreglos-urgentes-hotfix)
      - [Preparación de una versión para producción:](#preparación-de-una-versión-para-producción)
    - [:exclamation: lineamentos](#exclamation-lineamentos)
  - [:page\_facing\_up: Recursos](#page_facing_up-recursos)
  - [:camera: Galeria](#camera-galeria)

##  :beginner: Descripción
Este proyecto está estructurado para desarrollar microservicios utilizando FastAPI, un framework web moderno y de alto rendimiento para construir APIs con Python 3.7+ basado en estándares abiertos como HTTP/2 y WebSockets. La estructura del proyecto refleja una organización modular y escalable, adecuada para aplicaciones de microservicios.

Este proyecto está diseñado para ser escalable y fácil de mantener, siguiendo las mejores prácticas de desarrollo de software y utilizando herramientas modernas como FastAPI, Docker, y Poetry.

## :zap: Uso

### :whale: Instalación por Docker
Para la instalación del proyecto base en tu ambiente LOCAL con Docker ejecuta los siguientes pasos:

**ANTES DE REALIZAR ESTOS PASOS TENER CUENTA LA CREACION DEL ARCHIVO `.env.local` COMO ESTA ACTUALIZADA LAS VARIABLE DENTRO DEL `.ENV.TEMPLATE`**

Antes de seguir los pasos ver la seccion [ [:nut\_and\_bolt: Entorno de Desarollo](#nut_and_bolt-entorno-de-desarollo) ]

#### Paso 1: Construir imagenes
Teniendo en cuenta el Makefile ejecutar el siguiente comando:

```bash
$ make build-local
```
#### Paso 2: Realizar migraciones de los modelos
Teniendo en cuenta el Makefile ejecutar el siguiente comando:

```bash
$ make make-migrations
```

#### Paso 3: Actualizar migración actual
Teniendo en cuenta el Makefile ejecutar el siguiente comando:

```bash
$ make migrate
```

#### Paso 4: Levantar proyecto
Teniendo en cuenta el Makefile ejecutar el siguiente comando:

```bash
$ make up-local
```

### :desktop_computer: Instalación Localmente
Para la instalación del proyecto base en tu ambiente LOCAL ejecuta los siguientes pasos:

**ANTES DE REALIZAR ESTOS PASOS TENER CUENTA LA CREACION DEL ARCHIVO `.env.local` COMO ESTA ACTUALIZADA LAS VARIABLE DENTRO DEL `.ENV.TEMPLATE`**

Antes de seguir los pasos ver la seccion [ [:nut\_and\_bolt: Entorno de Desarollo](#nut_and_bolt-entorno-de-desarollo) ]

#### Paso 1: Instalar librerias del proyecto
Teniendo en cuenta ejecutar el siguiente comando:

```bash
$ poetry install --with dev
```
#### Paso 2: Creación de Base de Dasto
Teniendo en cuenta ejecutar el siguiente comando:

```sql
$ CREATE DATABASE nombre_base_de_datos;
```

#### Paso 3: Cambiar la URL de Base de Datos en el `settings.py`
Teniendo en cuenta ejecutar el siguiente comando:

```PYTHON
$ DATABASE_URL = "postgresql+asyncpg://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_DB')}" # ---> By Migrations Alembic Locally
```

#### Paso 4: Realizar migraciones y actualizar la migración
Teniendo en cuenta ejecutar el siguiente comando:

```bash
$ alembic revision --autogenerate -m "MENSAJE"
$ alembic upgrade head
```
#### Paso 4.5: Devolver la ultima migración y actualizar la migración
Si se tiene algun problema con la migración ejecutar el siguiente comando:

```bash
$ alembic downgrade -1
$ alembic upgrade head
```

#### Paso 5: Levantar proyecto
Teniendo en cuenta ejecutar el siguiente comando:

```bash
$ python -m uvicorn app.main:app --port 8000 --reload --access-log
```

##  :wrench: Desarrollo
Al ser un template para realizar microservicios lo primero que deberas de hacer los siguientes pasos:

#### Paso 1: Clonar el repositorio

```sh
$ git clone <URL-PROYECTO>
```
**( No olvidar despues de clonar eliminar el directorio `.git/` )**
#### Paso 2: Crear Repositorio para el nuevo repositorio y copiar el proyecto dentro.
Solicitar la creación del repositorio al SRE y ajustar el repositorio con las ramas que indica la sección [:cactus: Ramas](#cactus-ramas).

#### Paso 3: Configurar Bases de Datos para el nuevo microservicio
Solicitar la creación de las diferentes Bases de datos en los distintos ambientes y añadiendo las variables de entorno en los diferentes `.env.<ambiente>`.

#### Paso 4: Solicitar despliegue
Solcitar la creación de la infra necesaria para levantar mediante imagenes Docker, tener en cuenta para el despligue los siguientes puntos:

- Los dominios de la IPs por ambiente
- El balanceador de carga
- La configuración de las instancias
- Las configuraciones CORS
- Las variables de entornos por ambiente
- La configuración de las migraciones hacia la base de datos
- La configuracion del directorio para los logs
- La configuración de las pipelines segun corresponda

### :notebook: Pre-Requisitos - Programas a instalar
1. WINDOWS
   - WSL2
   - Pyenv
   - Python 3.7+
   - Docker
   - Poetry
   - Pre-commit
   - VSCode
   - DBeaver
   - Postman
   - Postgresql (Opcional:PGAdmin)

2. LINUX
   - Pyenv
   - Python 3.7+
   - Docker
   - Poetry
   - Pre-commit
   - VSCode
   - DBeaver
   - Postman
   - Postgresql (Opcional:PGAdmin)

3. MAC
   - HomeBrew 
   - Pyenv
   - Python 3.7+
   - Docker
   - Poetry
   - Pre-commit
   - VSCode
   - DBeaver
   - Postman
   - Postgresql (Opcional:PGAdmin)

###  :nut_and_bolt: Entorno de Desarollo

Para configurar tu entorno de desarollo local python para tu proyecto en VSCode es importante saber en que sistema operativo estas:

LINUX / MAC / WSL2 : [ :snake: PYENV](https://realpython.com/intro-to-pyenv/#build-dependencies) 

WINDOWS :  [ :snake: PYENV](https://medium.com/@diego.coder/instalar-m%C3%BAltiples-versiones-de-python-en-windows-con-pyenv-d6c3d006d83d) 

Despues de seguir los pasos generar un Entorno virtual con PYENV con los siguientes especificaciones:

```sh
$ pyenv virtualenv 3.10.13 MSA-base-env
```

###  :file_folder: Estructura de Directorios
La siguiente estructura de proyecto en FastAPI está organizada de manera modular y sigue el patron de arquitectura limpia para el desarrollo de aplicaciones orientadas a microservicios con este framework.

```
.
├── app
│   ├── database.py
│   ├── deps.py
│   ├── log_config.py
│   ├── main.py
│   ├── migrations
│   │   ├── README
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   ├── models
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── example.py
│   ├── repositories
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── example.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── api_router.py
│   │   └── examples.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── example.py
│   ├── services
│   │   ├── __init__.py
│   │   └── examples.py
│   ├── settings.py
│   └── utils
│       └── __init__.py
├── assets
│   └── Logo_Base.png
├── test
│   └── __init__.py
├── logs
├── Makefile
├── README.md
├── alembic.ini
├── Dockerfile
├── docker-compose-prod.yml
├── docker-compose.yml
├── poetry.lock
├── pyproject.toml
├── pyproject.toml
```

| Nombre Directorio/Archivo | Descripción
|:------------:|-------|
| ***app*** | ***Este directorio contiene el código principal de la aplicación FastAPI***
| migrations | Contiene scripts de migración de base de datos generados por Alembic.
| models | Define los modelos de datos utilizados por la aplicación.
| repositories | Contiene la lógica para interactuar con la base de datos, separada de los modelos para seguir el patrón de repositorio.
| routes | Define las rutas de la API y los controladores asociados.
| schemas | Define los esquemas Pydantic para la validación de datos de entrada y salida.
| services | Contiene la lógica de negocio de la aplicación, separada de las rutas y los modelos.
| utils | Contiene funciones y clases de utilidad que pueden ser utilizadas en toda la aplicación.
| assets | Contiene recursos estáticos como imágenes para el README o Documentación
| test | Contiene los tests unitarios y de integración para la aplicación.
| logs | Almacena los archivos de log generados por la aplicación.
| database.py | Gestiona la conexión a la base de datos y el manejo de la sesion.
| deps.py |  Define las dependencias que se pueden inyectar en las rutas y controladores
| log_config.py | Configura el logging para la aplicación.
| main.py | Es el punto de entrada de la aplicación, donde se crea y configura el servidor FastAPI.
| settings.py | Contiene configuraciones globales de la aplicación, como variables de entorno y configuraciones específicas.
|  | 
| Makefile | Contiene comandos útiles para construir, ejecutar y probar la aplicación.
| README.md |  Documentación del proyecto, incluyendo cómo instalar, configurar y ejecutar la aplicación.
| alembic.ini| Configuración para Alembic, una herramienta de migración de bases de datos.
| Dockerfile |  Define cómo construir la imagen Docker de la aplicación.
| docker-compose-prod.yml docker-compose.yml | Definen cómo ejecutar la aplicación y sus dependencias en contenedores Docker, con configuraciones específicas para producción y desarrollo.
| poetry.lock y pyproject.toml | Gestión de dependencias y configuración del proyecto utilizando Poetry.
| pre-commit-config.yaml | Definir y configurar los hooks de pre-commit que se ejecutarán automáticamente antes de cada commit en un repositorio de código.

### :cactus: Ramas

#### Configuración Inicial

Cuando hayas hecho la clonación y la creación de tu proyecto ejecutar los siguientes comandos para activar los hooks del proyecto:

```bash
$ git config -f .gitconfig core.hooksPath .githooks
$ git config --local include.path ../.gitconfig
$ chmod +x .githooks/commit-msg
```
Eso con el fin para que valide la convención que se esta usando en el proyecto

#### Branching (Explicación)

En este proyecto, se utilizan cuatro tipos principales de ramas, cada una con un propósito específico:

1. Rama `develop`
     - Propósito: Ambiente de desarrollo.
     - Formato: `develop`

2. Rama `qa`
     - Propósito: Ambiente de pruebas (QA).
     - Formato: `qa`

3. Rama `master`
     - Propósito: Ambiente de producción.
     - Formato: `master`

### Ramas de características, corrección de errores, hotfix y versiones:

Formato: 
Seguir el nombramiento de la ramas segun los siguiente ejemplos:

Ejemplos:

* `feature/CAPPS-124-nueva-caracteristica`
* `bugfix/CAPPS-125-correccion-error`
* `hotfix/CAPPS-126-arreglo-rapido`
* `release/CAPPS-127-preparando-version`

Commits
Los mensajes de commit deben seguir el siguiente formato:

```bash
$ git commit -m "feat(CAPPS-<Número de ticket>): <Mensaje descriptivo>"
```
Ejemplo:

`feat(CAPPS-124): Agrega funcionalidad de autenticación`

Asegúrate de incluir el número de ticket relacionado con el trabajo realizado y proporcionar un mensaje descriptivo y claro sobre los cambios realizados en el commit.

### Flujo de Trabajo Recomendado
#### Desarrollo de una nueva característica:

- Crear una rama de características:
```bash
$ git checkout -b feature/CAPPS-<Número>-descripcion
``` 
- Realizar cambios y commits: 
```bash
$ git commit -m "feat(CAPPS-<Número>): <Mensaje>"
``` 
- Fusionar la rama de características con develop al completar la tarea.

#### Corrección de errores:

- Crear una rama de corrección de errores:
```bash
$ git checkout -b bugfix/CAPPS-<Número>-descripcion
```
- Realizar cambios y commits:
```bash
$ git commit -m "fix(CAPPS-<Número>): <Mensaje>"
```
- Fusionar la rama de corrección de errores con develop al completar la tarea.

#### Arreglos urgentes (hotfix):

- Crear una rama de hotfix: 
```bash
$ git checkout -b hotfix/CAPPS-<Número>-descripcion"
```
- Realizar cambios y commits:
```bash
$ git commit -m "hotfix(CAPPS-<Número>): <Mensaje>"
```
- Fusionar la rama de hotfix con master y develop al completar la tarea.

#### Preparación de una versión para producción:

- Crear una rama de release: git checkout -b release/CAPPS-<Número>-descripcion

- Realizar cambios y commits según sea necesario.

- Fusionar la rama de release con master y develop al completar la tarea.

***Importante: Antes de realizar cualquier fusión, asegúrate de que tu código esté actualizado con la rama objetivo.***

### :exclamation: lineamentos



##  :page_facing_up: Recursos
- Propuestas de mejora PYTHON (PEPs): https://peps.python.org/
- Patrones de diseño PYTHON (Desing Patterns): https://python-patterns.guide/
- Patrones de diseño Async IO (Async/Await): https://realpython.com/async-io-python/#async-io-design-patterns 

##  :camera: Galeria

![Swagger](/assets/Swagger.png)
![Redoc](/assets/Redocs.png)

