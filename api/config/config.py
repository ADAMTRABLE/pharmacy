from distutils.command.config import config
import os
from decouple import config
from typing import cast 
class Config:
    SECRET_KEY=config('SECRET_KEY','secret')
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class DevConfig(Config):
    DEBUG=config('DEBUG',cast=bool)
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:adam@localhost/orders'



class TestConfig(Config):
    pass

class ProdConfig(Config):
    pass

config_dict={

    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig, 
}

