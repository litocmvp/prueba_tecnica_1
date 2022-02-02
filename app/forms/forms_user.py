from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import InputRequired, EqualTo

class RegistroUsuario(FlaskForm):
	usuario = StringField('Nombre de Usuario', validators=[InputRequired()])
	passwd = PasswordField('Contraseña', validators=[InputRequired(), EqualTo('passwd2', \
		message='Contraseñas diferentes')])
	passwd2 = PasswordField('Repetir', validators=[InputRequired()])
	rol = BooleanField('¿Privilegios para realizar registros?')
	submit = SubmitField('Registrar')

class Login(FlaskForm):
	user = StringField('Email', validators=[InputRequired()])
	password = PasswordField('Password', validators=[InputRequired()])
	remember_me = BooleanField('Recuérdame')
	submit1 = SubmitField('Acceder')  
