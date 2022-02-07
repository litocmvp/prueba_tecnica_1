from flask import request, jsonify, abort
from . import api_v1
from app import db, csrf
from app.models.users import Usuario
from app.models.places import Colonia

@api_v1.route('/api/v1/acceso', methods=['POST'])
@csrf.exempt
@Usuario.token_required
def api_v1_post_colonia(current_user):
	if not current_user.admin : return abort(403)
	nombre = request.json['nombre']
	municipio = request.json['municipio']
	cp = request.json['cp']
	asentamiento = request.json['asentamiento']
	zona = request.json['zona']

	buscar = Colonia.query.filter_by(fk_cp=cp).all()
	continuar = False

	for i in buscar:
		if i.fk_municipio == int(municipio):
			continuar = True
			break

	if continuar:		
		for i in buscar:
			if i.nombre == nombre:
				continuar = False
				break
					
		if continuar:	
			registro = Colonia(nombre=nombre, fk_municipio=municipio, fk_cp=cp, fk_asentamiento=asentamiento, 
								fk_zona=zona)
			db.session.add(registro)
			db.session.commit()

			return jsonify({'result': 'Registro exitoso'})	
		else:
			return jsonify({'result': 'Colonia ya registrada'})	
	else:
		return jsonify({'result': 'El CP no pertenece al municipio ingresado'})			
