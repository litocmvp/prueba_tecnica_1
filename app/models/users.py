from flask import request
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Usuario(db.Model, UserMixin):
	""" Modelo para la tabla usuarios """

	__tablename__ = 'usuarios'

	id = db.Column(db.Integer, primary_key=True)
	public_id = db.Column(db.Integer)
	user = db.Column(db.String, unique=True, nullable=False)
	password = db.Column("pass", db.String, nullable=False)
	admin = db.Column(db.Boolean, default=False)   

	def __repr__(self):
		return f'<Usuario {self.user}>'

	def set_password(self, password):
		self.password = generate_password_hash(password,  method='sha256')

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def save(self):
		if not self.id:
			db.session.add(self)
			db.session.commit()

	def token_required(f):

		@wraps(f)
		def decorator(*args, **kwargs):
			token = None

			if 'x-access-tokens' in request.headers:
				token = request.headers['x-access-tokens']

			if not token:
				return jsonify({'mensaje': 'Falta un token valido'})

			try:
				data = jwt.decode(token, current_app.config["SECRET_KEY"])
				current_user = Usuario.query.filter_by(public_id=data['public_id']).first()
			except:
				return jsonify({'mensaje': 'Token invalido'})

			return f(current_user, *args, **kwargs)
		return decorator		