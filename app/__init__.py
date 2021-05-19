from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
import logging

login_manager = LoginManager()
csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

def create_app(settings_module):
	
	app = Flask(__name__, instance_relative_config=True)

	# Carga los parámetros de configuración según el entorno
	app.config.from_object(settings_module)

	# Carga la configuración del directorio instance
	#app.config.from_pyfile('config.py', silent=True)

	configure_logging(app)
	
	csrf.init_app(app)

	login_manager.init_app(app)
	login_manager.login_view = "public.AccesoUsuario"

	db.init_app(app)
	migrate.init_app(app, db)

	from app.routes.public import public_bp
	app.register_blueprint(public_bp)

	from app.routes.private import private_bp
	app.register_blueprint(private_bp)

	# Custom error handlers
	register_error_handlers(app)

	return app

def register_error_handlers(app):
    
    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('errors/404.html'), 404	

