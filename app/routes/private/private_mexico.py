from flask import request, jsonify
from . import private_bp
from app import db
from app.models.places import Colonia

@private_bp.route('/registrar/colonia', methods=['POST'])
@token_required
def RegistrarColonia(keyword):

	nombre = request.json['nombre']
	ciudad = request.json['ciudad']
	cp = request.json['cp']
	asentamiento = request.json['asentamiento']
	zona = request.json['zona']

	registro = Colonia(nombre=nombre, fk_ciudad=ciudad, fk_cp=cp, fk_asentamiento=asentamiento, 
						fk_zona=zona)
	db.session.add(registro)
	db.session.commit()


	return jsonify({'result': 'Registro exitoso'})