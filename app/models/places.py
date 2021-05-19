from app import db

class Estado(db.Model):
	"""Modelo para la tabla estados"""

	__tablename__ = "estados"

	id = db.Column('c_estado', db.Integer, primary_key=True)
	nombre = db.Column(db.String(30), unique=True, nullable=False)
	
	relacion_municipio = db.relationship("Municipio", backref='municipios', lazy=True, 
		cascade="all, delete, update", passive_deletes=True)

	def __repr__(self):
		return f'{self.nombre}'
	
class Municipio(db.Model):
	"""Modelo para la tabla municipios"""

	__tablename__ = "municipios"

	id = db.Column(db.Integer, primary_key=True)
	clave = db.Column("c_mnpio", db.Integer, nullable=False)
	nombre = db.Column(db.String(70), nullable=False)
	fk_estado = db.Column(db.Integer, db.ForeignKey('estados.id', ondelete="CASCADE", 
		onupdate="CASCADE"), nullable=False)
	
	#relacion_ciudad = db.relationship("Ciudad", backref='ciudades', lazy=True, 
	#	cascade="all, delete, update", passive_deletes=True)
	relacion_colonia = db.relationship("Colonia", backref='colonias', lazy=True, 
		cascade="all, delete, update", passive_deletes=True)

	def __repr__(self):
		return f'{self.nombre}'		

class Colonia(db.Model):
	"""Modelo para la tabla colonias"""

	__tablename__ = "colonias"

	id = db.Column(db.Integer, primary_key=True)
	#clave = db.Column("id_asenta_cpcons", db.Integer, nullable=False)
	nombre = db.Column(db.String(150), nullable=False)
	fk_municipio = db.Column(db.Integer, db.ForeignKey('municipios.id', ondelete="CASCADE", 
		onupdate="CASCADE"), nullable=False)
	fk_cp = db.Column(db.Integer, db.ForeignKey('codigos_postales.id', ondelete="CASCADE", 
		onupdate="CASCADE"), nullable=False)
	fk_asentamiento = db.Column(db.Integer, db.ForeignKey('tipos_asentamientos.id', ondelete="CASCADE", 
		onupdate="CASCADE"), nullable=False)
	fk_zona = db.Column(db.Integer, db.ForeignKey('tipos_zonas.id', ondelete="CASCADE", 
		onupdate="CASCADE"), nullable=False)

	def __repr__(self):
		return f'{self.nombre}'						