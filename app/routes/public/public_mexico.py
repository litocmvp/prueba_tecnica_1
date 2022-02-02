from flask import render_template
from flask_login import current_user
from . import public_bp

@public_bp.route('/', methods=['GET'])
def index():
	name=""
	if current_user.is_active:
		name = str(current_user)+", "

	return render_template("public/index.html", user=name) 
