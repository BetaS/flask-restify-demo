# -*- coding: utf-8 -*-


__DEFAULT_KEY__ = "!change_me!"


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = __DEFAULT_KEY__
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    JWT_SECRET = __DEFAULT_KEY__
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = True


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_ECHO = False


class QueryDebugConfig(DevelopmentConfig):
    SQLALCHEMY_ECHO = True
