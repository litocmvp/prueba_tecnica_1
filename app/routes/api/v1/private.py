from flask import request, jsonify
from . import api_v1
from app import db
from app.models.users import Usuario
from app.models.places import Colonia, Municipio

@api_v1.route('/api/v1/colonia/', methods=['POST'])
@Usuario.token_required
def api_v1_post_colonia(current_user):

	nombre = request.json['nombre']
	#estado = request.json['estado']
	municipio = request.json['municipio']
	cp = request.json['cp']
	asentamiento = request.json['asentamiento']
	zona = request.json['zona']

	buscar = Colonia.query.filter_by(fk_cp=cp).all()
	continuar = False

	for i in buscar:
		if i.fk_municipio == municipio:
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
