from flask import jsonify
from . import public_bp
from app import db
from app.models.places import Estado, Municipio, Ciudad, Colonia
from app.models.features_colonies import Zona, Asentamiento

@public_bp.route('/buscar/colonia/<String:keyword>', methods=['GET'])
def BuscarColonia(keyword):

	if "cp_" in keyword: # Buscar colonia por CP
		cp = keyword.split('cp_')

		if cp[1].isdigit():
			busqueda = Colonia.query.filter_by(fk_cp=cp[1]).all()
			
			if not busqueda is None:
				lista = []
				for result in busqueda:
					ciudad = Ciudad.query.filter_by(id=result.fk_ciudad).first()
					municipio = Municipio.query.filter_by(id=ciudad.fk_municipio).first()
					estado = Estado.query.filter_by(id=municipio.fk_estado).first()

					data = {'id_colonia': result.id, 'colonia': result.nombre, 'cp': result.fk_cp
					'ciudad': ciudad.nombre, 'municipio':municipio.nombre, 'estado':estado.nombre}
					lista.append(data)

				return jsonify({'result': lista})
			else:
				return jsonify({'result': 'No encontrado'})	 
		else:
			return jsonify({'result': 'Entrada invalida'})

	else: # Buscar colonia por nombre

		busqueda = db.session.execute("SELECT * FROM colonias WHERE nombre LIKE '"+keyword+"'")
			
			if not busqueda is None:
				lista = []
				for result in busqueda:
					ciudad = Ciudad.query.filter_by(id=result.fk_ciudad).first()
					municipio = Municipio.query.filter_by(id=ciudad.fk_municipio).first()
					estado = Estado.query.filter_by(id=municipio.fk_estado).first()

					data = {'id_colonia': result.id, 'colonia': result.nombre, 'cp': result.fk_cp
					'ciudad': ciudad.nombre, 'municipio':municipio.nombre, 'estado':estado.nombre}
					lista.append(data)

				return jsonify({'result': lista})
			else:
				return jsonify({'result': 'No encontrado'})	


@public_bp.route('/buscar/municipio/<String:keyword>', methods=['GET'])
def BuscarMunicipio(keyword):

	busqueda = db.session.execute("SELECT * FROM municipios WHERE nombre LIKE '"+keyword+"'")
			
			if not busqueda is None:
				lista = []
				for result in busqueda:
					estado = Estado.query.filter_by(id=result.fk_estado).first()

					data = {'id_municipio': result.id, 'municipio': result.nombre, 
							'estado':estado.nombre}
					lista.append(data)

				return jsonify({'result': lista})
			else:
				return jsonify({'result': 'No encontrado'})	


@public_bp.route('/buscar/estado/<String:keyword>', methods=['GET'])
def BuscarEstado(keyword):

	busqueda = db.session.execute("SELECT * FROM estados WHERE nombre LIKE '"+keyword+"'")
			
			if not busqueda is None:
				lista = []
				for result in busqueda:

					data = {'id_estado': result.id, 'estado': result.nombre}
					lista.append(data)

				return jsonify({'result': lista})
			else:
				return jsonify({'result': 'No encontrado'})					