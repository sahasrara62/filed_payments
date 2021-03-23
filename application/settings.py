# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""

from environs import Env

env = Env()
env.read_env()

FLASK_APP = env.str("FLASK_APP")
SECRET = env.str("SECRET")
APP_SETTINGS = env.str("APP_SETTINGS")
FLASK_RUN_HOST = env.str("FLASK_RUN_HOST")
FLASK_RUN_PORT = env.int("FLASK_RUN_PORT")
