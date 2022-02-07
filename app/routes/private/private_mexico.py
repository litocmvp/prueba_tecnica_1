from flask import request, render_template, flash, redirect, url_for, abort
from . import private_bp
from app import db
from app.models.places import Colonia
from app.forms.forms_places import RegColonia
from flask_login import current_user, login_required

@private_bp.route('/usuario/acceso', methods=['GET', 'POST'])
@login_required
def acceso():
	if not current_user.admin : return abort(403)
	form = RegColonia()

	if form.submit.data and form.validate():
		nombre = form.nombre.data
		municipio = request.form['municipio']
		cp = request.form['cp']
		asentamiento = request.form['asentamiento']
		zona = request.form['zona']

		buscar = Colonia.query.filter_by(fk_cp=cp).all()
		continuar = True

		for i in buscar:
			if i.nombre == nombre:
				continuar = False
				break

		if continuar:		
			registro = Colonia(nombre=nombre, fk_municipio =municipio, fk_cp=cp, 
								fk_asentamiento=asentamiento, fk_zona=zona)
			db.session.add(registro)
			db.session.commit()

			flash('Registro de nueva colonia exitosa', 'success')	
			return redirect(url_for('private.acceso'))
		
		else:
			flash('Esta colonia ya fue registrada!', 'danger')	
			return redirect(url_for('private.acceso'))	
		
	return render_template("private/nueva_colonia.html", form=form) 
