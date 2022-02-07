from . import private_bp
from app import login_manager
from app.models.users import Usuario
from flask_login import login_required, logout_user
from flask import redirect, url_for

@login_manager.user_loader
def load_user(user_id):
	try:
		return Usuario.get(user_id)
	except:
		return None    

@private_bp.route('/usuario/logout')
@login_required
def logout():

	logout_user()
	return redirect(url_for('public.index'))    	