import os
from .default import *

SECRET_KEY = os.getenv('KEY')

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = os.getenv('PATH_DB')
