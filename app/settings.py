from enum import Enum
import os
from dotenv import load_dotenv
from pathlib import Path


env_folder = Path(__file__).parent.parent
env_file = env_folder / f".env.{os.getenv('ENV', 'dev')}"

load_dotenv(env_file)


class ModeEnum(str, Enum):
    development = "development"
    production = "production"
    testing = "testing"


class Settings:
    MODE = ModeEnum.development
    BASE_DIR = Path(__file__).parent.parent.parent
    DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@db/{os.getenv('DATABASE_DB')}"
    # DATABASE_URL = "postgresql+asyncpg://postgres:postgres@0.0.0.0:6543/exampledb" # ---> Migrations Alembic Locally


settings = Settings()
