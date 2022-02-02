from app import db

class Zona(db.Model):
	"""Modelo para la tabla tipos_zonas"""

	__tablename__ = "tipos_zonas"

	id = db.Column(db.Integer, primary_key=True)
	tipo = db.Column(db.String(15), unique=True, nullable=False)
	
	relacion_colonia = db.relationship("Colonia", backref='tipos_zonas', lazy=True, 
		cascade="all, delete", passive_deletes=True)

	def __repr__(self):
		return f'{self.tipo}'			

class Asentamiento(db.Model):
	"""Modelo para la tabla tipos_asentamientos"""

	__tablename__ = "tipos_asentamientos"

	id = db.Column(db.Integer, primary_key=True)
	tipo = db.Column(db.String(15), unique=True, nullable=False)
	
	relacion_colonia = db.relationship("Colonia", backref='tipos_asentamientos', lazy=True, 
		cascade="all, delete", passive_deletes=True)

	def __repr__(self):
		return f'{self.tipo}'	

class CodigoPostal(db.Model):
	"""Modelo para la tabla codigos_postales"""

	__tablename__ = "codigos_postales"

	id = db.Column(db.Integer, primary_key=True)
	
	relacion_colonia = db.relationship("Colonia", backref='codigos_postales', lazy=True, 
		cascade="all, delete", passive_deletes=True)

	def __repr__(self):
		return f'{self.id}'				