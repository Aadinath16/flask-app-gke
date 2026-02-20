import os
from dotenv import load_dotenv

load_dotenv()


class BaseConfig:
    APP_ENV = os.getenv("APP_ENV", "dev")

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    DB_CONN_NAME = os.getenv("DB_CONN_NAME")


class DevConfig(BaseConfig):
    DEBUG = True


class ProdConfig(BaseConfig):
    DEBUG = False


def get_config():
    env = os.getenv("APP_ENV", "dev")

    if env == "prod":
        return ProdConfig

    return DevConfig
