from .generals_functions import OrderList, PurgarRepetidos, ClasificarListas, LeerTxt
from .poblar_db import PoblarTB
from flask_script import Command, Option

class Seeder(Command):

	'Comando para poblar Base de datos de archivo .txt'

	option_list = (Option('--eleccion', '-e', dest='eleccion'),
					Option('--ruta', '-r', dest='ruta'),)

	def run(self, ruta, eleccion):
		ruta = ruta[0:len(ruta)]
		chains= LeerTxt(ruta, 'r')
		eleccion = int(eleccion)

		"""
		Leyenda
		1 = Poblar TB tipos_zonas
		2 = Poblar TB tipos_asentamientos
		3 = Poblar TB codigos_postales
		4 = Poblar TB estados
		5 = Poblar TB municipios
		6 = Poblar TB colonias
		"""
		if eleccion == 1:
			tipo_zonas = ClasificarListas(chains, 1)
			OrderList(tipo_zonas)
			zonas = PurgarRepetidos(tipo_zonas)
			PoblarTB(zonas, 1)
		
		if eleccion == 2:	
			tipo_asentamientos = ClasificarListas(chains, 2)
			OrderList(tipo_asentamientos, 'codigo')
			asent = PurgarRepetidos(tipo_asentamientos, 'codigo')
			PoblarTB(asent, 2)

		if eleccion == 3:
			codigos_postales = ClasificarListas(chains, 3)
			OrderList(codigos_postales)
			cp = PurgarRepetidos(codigos_postales)
			PoblarTB(cp, 3)
		

		if eleccion == 4:	
			estados = ClasificarListas(chains, 4)
			OrderList(estados, 'codigo')
			stdo = PurgarRepetidos(estados, 'codigo')				
			PoblarTB(stdo, 4)

		if eleccion == 5:
			municipios = ClasificarListas(chains, 5)
			mpio = PurgarRepetidos(municipios, 'nombre')
			PoblarTB(mpio, 5)

		if eleccion == 6:
			colonias = ClasificarListas(chains, 6)
			PoblarTB(colonias, 6)		
				