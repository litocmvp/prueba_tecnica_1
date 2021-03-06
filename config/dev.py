import os
from dotenv import load_dotenv
from .default import *

load_dotenv()

APP_ENV = APP_ENV_DEVELOPMENT

SECRET_KEY = os.getenv('KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('PATH_DB')

