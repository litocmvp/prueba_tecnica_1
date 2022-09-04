from flask import jsonify, request, current_app
from . import api_v1
from app import db
from app.models.users import Usuario
from app.models.places import Estado, Municipio, Colonia
from app.common.generals_functions import OrderList, PurgarRepetidos
from app.common.error_handling import ObjectNotFound
import jwt
import datetime

@api_v1.route('/api/v1/signup', methods=['POST'])
def api_v1_signup():

	user = request.json['usuario']
	admin =  request.json['admin']
	password = request.json['pass']
	usuario = Usuario.query.filter_by(user=user)

	if usuario is None:

		registro = Usuario(user=user, admin=admin)
		registro.set_password(password)
		usuario.save()

		return jsonify({'result': 'Registro exitoso'})
	else:
		return jsonify({'result': 'Usuario ya registrado'})

@api_v1.route('/api/v1/login', methods=['GET', 'POST'])
def api_v1_login():

	auth = request.authorization

	if not auth or not auth.username or not auth.password:
		return jsonify({'result': 'Falta apartado de autorizacion'})

	usuario = Usuario.query.filter_by(user=auth.username).first()

	if usuario is not None and usuario.check_password(auth.password):
		token = jwt.encode({'public_id': usuario.public_id,
							'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
							current_app.config["SECRET_KEY"], algorithm="HS256")
		return jsonify({'token' : token})
	else:
		return jsonify({'result' : 'Usuario o contraseña incorrecta'})

@api_v1.route('/api/v1/user/<string:keyword>', methods=['GET'])
def api_v1_get_user(keyword):

	busqueda = Usuario.query.filter_by(user=keyword).first()

	result = False
	if not busqueda is None:
		result = True

	return jsonify({'result':result})

######################################################################

@api_v1.route('/api/v1/colonia/<string:keyword>', methods=['GET'])
def api_v1_get_colonia(keyword):

	if keyword.isdigit(): # Buscar colonia por CP

		busqueda = Colonia.query.filter_by(fk_cp=int(keyword)).all()

		lista = []
		for result in busqueda:
			municipio = Municipio.query.filter_by(id=result.fk_municipio).first()
			estado = Estado.query.filter_by(id=municipio.fk_estado).first()

			data = ({'id_colonia': result.id, 'colonia': result.nombre, 'cp': result.fk_cp,
					'municipio':municipio.nombre,
					'estado':estado.nombre})
			lista.append(data)

		if len(lista)>0:
			return jsonify({'result': lista})
		else:
			raise ObjectNotFound('No hay ninguna colonia con este CP')
			#return jsonify({'result': 'No encontrado'})

	else: # Buscar colonia por nombre

		busqueda = db.session.execute("SELECT * FROM colonias WHERE nombre LIKE '"+keyword+"%'")

		lista = []
		for result in busqueda:
			municipio = Municipio.query.filter_by(id=result.fk_municipio).first()
			estado = Estado.query.filter_by(id=municipio.fk_estado).first()

			data = ({'id_colonia': result.id, 'colonia': result.nombre, 'cp': result.fk_cp,
					'municipio':municipio.nombre,
					'estado':estado.nombre})
			lista.append(data)

		if len(lista)>0:
			return jsonify({'result': lista})
		else:
			raise ObjectNotFound('No hay ninguna colonia con este nombre')
			#return jsonify({'result': 'No encontrado'})


@api_v1.route('/api/v1/municipio/<string:keyword>', methods=['GET'])
def api_v1_get_municipio(keyword):

	busqueda = db.session.execute("SELECT * FROM municipios WHERE nombre LIKE '"+keyword+"'")

	lista = []
	for result in busqueda:
		estado = Estado.query.filter_by(id=result.fk_estado).first()

		data = {'id_municipio': result.id, 'municipio': result.nombre,
				'estado':estado.nombre}
		lista.append(data)

	if len(lista)>0:
		return jsonify({'result': lista})
	else:
		raise ObjectNotFound('No hay ningún municipio con este nombre')
		#return jsonify({'result': 'No encontrado'})


@api_v1.route('/api/v1/estado/<string:keyword>', methods=['GET'])
def api_v1_get_estado(keyword):

	busqueda = db.session.execute("SELECT * FROM estados WHERE nombre LIKE '"+keyword+"%'")

	lista = []
	for result in busqueda:
		data = {'id_estado': result.id, 'estado': result.nombre}
		lista.append(data)

	if len(lista)>0:
		return jsonify({'result': lista})
	else:
		raise ObjectNotFound('No hay ningún estado con este nombre')
		#return jsonify({'result': 'No encontrado'})

@api_v1.route('/api/v1/municipios/<int:id>', methods=['GET'])
def api_v1_get_municipios(id):

	busqueda = Municipio.query.filter_by(fk_estado=id).all()

	lista = []
	for result in busqueda:
		data = {'id': result.id, 'nombre': result.nombre}
		lista.append(data)

	return jsonify({'result': lista})

@api_v1.route('/api/v1/cps/<int:id>', methods=['GET'])
def api_v1_get_cps(id):

	busqueda = Colonia.query.filter_by(fk_municipio=id).all()

	lista = []
	for result in busqueda:
		lista.append(result.fk_cp)

	OrderList(lista)
	lista2 = PurgarRepetidos(lista)

	return jsonify({'result': lista2})
