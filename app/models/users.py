from flask import request, jsonify, current_app
from flask_login import UserMixin
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
import uuid
import jwt
from functools import wraps

class Usuario(db.Model, UserMixin):
	""" Modelo para la tabla usuarios """

	__tablename__ = 'usuarios'

	id = db.Column(db.Integer, primary_key=True)
	public_id = db.Column(db.Integer, unique=True)
	user = db.Column(db.String, unique=True, nullable=False)
	password = db.Column("pass", db.String, nullable=False)
	admin = db.Column(db.Boolean, default=False)   

	def __repr__(self):
		return f'{self.user}'

	def set_password(self, password):
		self.password = generate_password_hash(password,  method='sha256')

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def save(self):
		if not self.id:
			self.public_id = str(uuid.uuid4())
			db.session.add(self)
			saved = False
			while not saved:
				try:
					db.session.commit()
					saved = True
				except IntegrityError:
					self.public_id = str(uuid.uuid4())

	def get(id):
		return Usuario.query.get(id)		

	def token_required(f):

		@wraps(f)
		def decorator(*args, **kwargs):
			token = None

			if 'x-access-tokens' in request.headers:
				token = request.headers['x-access-tokens']
			#elif not request.cookies.get('token_user') is None:
			#	token = request.cookies.get('token_user') 	

			if not token:
				return jsonify({'mensaje': 'Falta un token valido'})

			try:
				data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
				current_user = Usuario.query.filter_by(public_id=data['public_id']).first()
			except:
				return jsonify({'mensaje': 'Token invalido'})

			return f(current_user, *args, **kwargs)
		return decorator		