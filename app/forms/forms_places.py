from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models.places import Estado
from app.models.features_colonies import Asentamiento, Zona

class RegColonia(FlaskForm):
	nombre = StringField('Nombre', validators=[InputRequired(), 
						Length(max=1000, message='Máximo 100 Carácteres')]) 
	estado = QuerySelectField(label='Estado',  query_factory=lambda: Estado.query.all(),
									get_pk=lambda x: x.id, get_label=lambda nombre: nombre, 
									allow_blank=True, blank_text=(u'- Selecciona -'))
	municipio = SelectField('Municipio', choices=[('__None', '- Seleccione -')])
	cp = SelectField('Código Postal', choices=[('__None', '- Seleccione -')])
	asentamiento = QuerySelectField(label='Tipo de Asentamiento',  
									query_factory=lambda: Asentamiento.query.all(),
									get_pk=lambda x: x.id, get_label=lambda tipo: tipo, 
									allow_blank=True, blank_text=(u'- Selecciona -'))
	zona = QuerySelectField(label='Tipo de Zona', query_factory=lambda: Zona.query.all(),
							get_pk=lambda x: x.id, get_label=lambda tipo: tipo, 
							allow_blank=True, blank_text=(u'- Selecciona -'))
	submit = SubmitField('Registrar')
