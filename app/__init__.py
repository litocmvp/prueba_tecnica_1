from flask import Flask, render_template, jsonify
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from app.common.error_handling import ObjectNotFound, AppErrorBaseClass

login_manager = LoginManager()
csrf = CSRFProtect()
db = SQLAlchemy()
migrate = Migrate()

def create_app(settings_module):

	app = Flask(__name__, instance_relative_config=True)

	# Carga los parámetros de configuración según el entorno
	app.config.from_object(settings_module)

	csrf.init_app(app)

	login_manager.init_app(app)
	login_manager.login_view = "public.acceso_usuario"

	db.init_app(app)
	#migrate.init_app(app, db)
	with app.app_context():
		if db.engine.url.drivername == 'sqlite':
			migrate.init_app(app, db, render_as_batch=True)
		else:
			migrate.init_app(app, db)
	
	from app.routes.public import public_bp
	app.register_blueprint(public_bp)

	from app.routes.private import private_bp
	app.register_blueprint(private_bp)

	from app.routes.api.v1 import api_v1
	app.register_blueprint(api_v1)

	# Custom error handlers
	register_error_handlers(app)

	return app

def register_error_handlers(app):
    
    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('errors/500.html'), 500

    @app.errorhandler(405)
    def error_405_handler(e):
        return jsonify({'msg': 'Method not allowed'}), 405
    
    @app.errorhandler(403)
    def error_403_handler(e):
        return jsonify({'msg': 'Forbidden error'}), 403    

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('errors/404.html'), 404	

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify({'msg': str(e)}), 500
    
    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify({'msg': str(e)}), 404    

