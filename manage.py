import os
from dotenv import load_dotenv
from app import create_app
from flask_script import Manager
from app.common.seeder import Seeder

load_dotenv()

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)
manager = Manager(app)

manager.add_command('seed', Seeder())

if __name__ == "__main__":
    manager.run()