from app.models.features_colonies import Zona, Asentamiento, CodigoPostal
from app.models.places import Estado, Municipio, Colonia
from app import db

# Funcion para poblar Tablas en DB
def PoblarTB(lista, tb):

	"""
	Valorees de tb para poblar diferentes tablas
	1 = tipos_zonas
	2 = tipos_asentamientos
	3 = codigos_postales
	4 = estados
	5 = municipios
	6 = colonias
	"""

	if tb.isdigit():
		try:
		 	if tb ==1: # tipos_zonas
		 		for i in lista:
				Buscar = Zona.query.filter_by(tipo=i).first()
				if Buscar is None:
					registro = Zona(tipo=i)
					db.session.add(registro)
					db.session.commit()

		 	if tb ==2: # tipos_asentamientos
		 		for i in lista:
				Buscar = Asentamiento.query.filter_by(id=i.get('codigo')).first()
				if Buscar is None:
					registro = Asentamiento(id=i.get('codigo'), tipo=i.get('tipo'))
					db.session.add(registro)
					db.session.commit()

		 	if tb ==3: # codigos_postales
		 		for i in lista:
				Buscar = CodigoPostal.query.filter_by(id=i).first()
				if Buscar is None:
					registro = CodigoPostal(id=i)
					db.session.add(registro)
					db.session.commit()

		 	if tb ==4: # estados
		 		for i in lista:
				Buscar = Estado.query.filter_by(id=i.get('codigo')).first()
				if Buscar is None:
					registro = Estado(id=i.get('codigo'), nombre=i.get('nombre'))
					db.session.add(registro)
					db.session.commit()	

		 	if tb ==5: # municipios
		 		for i in lista:
				Buscar = Municipio.query.filter_by(clave=i.get('codigo')).all()
				if Buscar is None:
					registro = Municipio(clave=i.get('codigo'), nombre=i.get('nombre'), 
											fk_estado=i.get('cod_estado'))
					db.session.add(registro)
					db.session.commit()	
				if not Buscar is None:
					Continuar = True
					for j in Buscar:
						if j.fk_estado == i.get('cod_estado'):
							Continuar = False
							break  	
					if Continuar:
						registro = Municipio(clave=i.get('codigo'), nombre=i.get('nombre'), 
												fk_estado=i.get('cod_estado'))
						db.session.add(registro)
						db.session.commit()

		 	if tb ==6: # colonias
		 		for i in lista:
					id_municipio = 0
					
					Buscar = Municipio.query.filter_by(fk_estado=i.get('cod_estado')).all()
					for j in Buscar:
						if j.clave == i.get('cod_municipio'):
							id_municipio = j.id
							break	

					fk_zona = Zona.query.filter_by(tipo=i.get('tip_zona')).first()

					
					Buscar3 = Colonia.query.filter_by(nombre=i.get('nombre')).all()
					if Buscar3 is None:
						registro = Colonia(nombre=i.get('nombre'), fk_municipio=id_municipio, 
											fk_cp=i.get('cod_postal'), 
											fk_asentamiento=i.get('cod_asentamiento'), fk_zona=fk_zona.id)
						db.session.add(registro)
						db.session.commit()
					if not Buscar3 is None:
						Continuar = True
						for j in Buscar3:
							if j.fk_cp == i.get('cod_postal'):
								Continuar = False
								break
						if Continuar:
							registro = Colonia(nombre=i.get('nombre'), fk_municipio=id_municipio, 
												fk_cp=i.get('cod_postal'),
												fk_asentamiento=i.get('cod_asentamiento'), 
												fk_zona=fk_zona.id)
							db.session.add(registro)
							db.session.commit()	

		except Exception as e:
		 	print(e)
		 	