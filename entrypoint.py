import os
from dotenv import load_dotenv
from app import create_app

load_dotenv()
settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)


