from flask import jsonify, request, flash, redirect, url_for, render_template
from . import public_bp
from app import db
from app.models.users import Usuario
import uuid

@public_bp.route('/usuario', methods=['GET', 'POST'])
def AccesoUsuario():

	form = RegistroUsuario()
	form2 = Login() 
	
	if form.validate_on_submit():
		
		user = form.user.data
		admin =  form.rol.data
		usuario = Usuario.query.filter_by(user=user)
	 
		if usuario is None:
 
			registro = Usuario(public_id=str(uuid.uuid4()), user=user, admin=admin)
			registro.set_password(form.passwd.data)
			usuario.save()

			flash('Registro de usuario exitoso', 'success')	
			return redirect(url_for('public.AccesoUsuario'))

	if form2.validate_on_submit():
				user = Usuario.query.filter_by(user=form2.user.data).first()
							
				if user is not None and user.check_password(form.password.data):
					login_user(user)  
					return redirect(url_for('private.acceso'))
				else:
					flash('usuario o contraseña incorrecta', 'warning')
					return redirect(url_for('public.AccesoUsuario'))	
			
			return render_template("admin/login.html", form=form) 		

	return render_template("autentificacion.html", form=form)   

@public_bp.route('/registrar/usuario', methods=['POST'])
def RegistroUsuario():

	user = request.json['usuario']
	admin =  request.json['admin']
	password = request.json['pass']
	usuario = Usuario.query.filter_by(user=user)
 
	if usuario is None:

		registro = Usuario(public_id=str(uuid.uuid4()), user=user, admin=admin)
		registro.set_password(password)
		usuario.save()

		return jsonify({'result': 'Registro exitoso'})
	else:
		return jsonify({'result': 'Usuario ya registrado'})	

@public_bp.route('/autentificar/usuario', methods=['GET'])
def AutentificarUsuario():

	user = request.json['usuario']
	admin =  request.json['admin']
	password = request.json['pass']
	usuario = Usuario.query.filter_by(user=user)
 
	if usuario is not None and usuario.check_password(password):
		login_user(usuario)
		token = jwt.encode({'public_id': usuario.public_id, 
							'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, 
							current_app.config["SECRET_KEY"])  
		return jsonify({'token' : token.decode('UTF-8')}) 
	else:
					

