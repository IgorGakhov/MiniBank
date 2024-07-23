import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    DB_HOST = os.getenv("DB_HOST", "minibank_db")
    DB_PORT = os.getenv("DB_PORT", 5432)
    DB_NAME = os.getenv("DB_NAME", "minibank")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASS = os.getenv("DB_PASS", "root")
    REDIS_HOST = os.getenv("REDIS_HOST", "minibank_cache")
    REDIS_PORT = os.getenv("REDIS_PORT", "6379")
    REDIS_DB = os.getenv("REDIS_DB", "")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def REDIS_URL(self):
        return f"redis://{self.REDIS_HOST}"


settings = Settings()
