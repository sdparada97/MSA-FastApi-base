import os
from dotenv import load_dotenv
from pathlib import Path


env_folder = Path(__file__).parent.parent
env_file = env_folder / f".env.{os.getenv('ENV', 'dev')}"

load_dotenv(env_file)


class Settings:
    DATABASE_URL = f"postgresql+asyncpg://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost/{os.getenv('POSTGRES_DB')}"


settings = Settings()
