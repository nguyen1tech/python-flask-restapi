import os

from dotenv import load_dotenv

load_dotenv()


def get_env_variable(name: str) -> str:
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set".format(name)
        raise Exception(message)


class Config:
    SECRET_KEY = get_env_variable("SECRET_KEY")
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = get_env_variable("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = get_env_variable("SQLALCHEMY_DATABASE_URI")
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
