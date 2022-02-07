from flask import flash, redirect, url_for, render_template, current_app, make_response
from flask_login import current_user, login_user
from . import public_bp
from app import db
from app.models.users import Usuario
import jwt
import datetime
from app.forms.forms_user import RegistroUsuario, Login

@public_bp.route('/autentificacion', methods=['GET', 'POST'])
def acceso_usuario():

	if current_user.is_authenticated:
		return redirect(url_for('private.acceso'))

	form = RegistroUsuario()
	form2 = Login() 
	
	if form.submit.data and form.validate():
		
		user = form.usuario.data
		admin =  form.rol.data
		usuario = Usuario.query.filter_by(user=user).first()
	 
		if usuario is None:
 
			registro = Usuario(user=user, admin=admin)
			registro.set_password(form.passwd.data)
			registro.save()

			flash('Registro de usuario exitoso', 'success')	
			return redirect(url_for('public.acceso_usuario'))	

	if form2.submit1.data and form2.validate():
		user = Usuario.query.filter_by(user=form2.user.data).first()
					
		if user is not None and user.check_password(form2.password.data):
			login_user(user)
			token = jwt.encode({'public_id': user.public_id, 
							'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 
							current_app.config["SECRET_KEY"], algorithm="HS256")  
			#json_tk = jsonify({'token' : token}) 
			resp = make_response(redirect(url_for('private.acceso')))
			resp.set_cookie('token_user', token, httponly=True) # , httponly = True  
			return resp
		else:
			flash('usuario o contraseña incorrecta', 'warning')
			return redirect(url_for('public.acceso_usuario'))	 		

	return render_template("public/autentificacion.html", form=form, form2=form2)   
