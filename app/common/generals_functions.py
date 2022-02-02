import os

# Obtener ruta la instancia de la aplicación
def PathInitial():
	return os.path.abspath(os.getcwd())

# Leer Txt de SEPOMEX
def LeerTxt(file_path, modo):
	chains = []
	with open(file_path, modo) as f:
	    lines = f.readlines()

	    # Iniciar por la linea 3, en el archivo .txt ya que de aqui al final son datos a almacenar en la BD 
	    for i in range(2, len(lines), 1):
	    	subchain = lines[i].split('|')
	    	chains.append(subchain) 

	    f.close()	

	# Eliminar espacios en blancos
	for i in chains:
		for j in range(0, len(i), 1):
			if j == len(i)-1:
				i[j].replace('\n', '')
			i[j] = i[j].strip()	

	return chains

# Obtener lista de TXT
def ClasificarListas(chains, get_list):
	"""
	Leyenda de Indices almacenados en keyword 'chain'
	[0] = d_codigo (Codigo postal)
	[1] = d_asenta (Colonia)
	[2] = d_tipo_asenta (Tipo de Asentamiento)
	[3] = D_mnpio (Municipio)
	[4] = d_estado (Estado)
	[7] = c_estado (Código del estado) 
	[10] = c_tipo_asenta (Código de Tipo de Asentamiento)
	[11] = c_mnpio (Código del municipio)
	[13] = d_zona (Tipo de zona)

	Leyenda de get_list
	1 = Zonas
	2 = Asentamientos
	3 = Codigos postales
	4 = Estados
	5 = Municipio
	6 = Colonias
	"""
	lista = []

	if get_list == 1: 
		for chain in chains:
			lista.append(chain[13])
	if get_list == 2:
		for chain in chains:
			# Asentamientos
			if len(lista)>1:
				OrderList(lista, 'codigo')
				if not SearchValue(lista=lista, valor1=chain[10], key1='codigo'):
					arb = {'codigo':chain[10], 'tipo':chain[2]}
					lista.append(arb)
			else:
				arb = {'codigo':chain[10], 'tipo':chain[2]}
				lista.append(arb)
	if get_list == 3:
		for chain in chains:
			# Códigos postales
			lista.append(chain[0])
	if get_list == 4:
		for chain in chains:		
			# Estados
			arb = {'codigo':chain[7], 'nombre':chain[4]}
			lista.append(arb)
	if get_list == 5:
		for chain in chains:		
			# Municipios
			arb = {'codigo':chain[11], 'nombre':chain[3], 'cod_estado':chain[7]}
			lista.append(arb)
	if get_list == 6:
		for chain in chains:		
			# Colonias
			arb = ({'nombre':chain[1], 'cod_postal':chain[0], 'tip_zona': chain[13], 
					'cod_asentamiento':chain[10], 'cod_estado': chain[7],
					'cod_municipio':chain[11]})
			lista.append(arb)

	return lista			

# Ordenar listas para reducir Busqueda
def OrderList(lista, keyword=None):
	if len(lista) > 1:
		if type(lista[0]) is dict:
			return sorted(lista, key=lambda i: i[keyword])
		else:	
			return lista.sort()

# NOTA: La lista debe de estar previamente ordenada
def PurgarRepetidos(lista, keyword=None):

	pivote = 0
	indices_iguales = []

	for i in range(1, len(lista), 1):
		if ((lista[pivote].get(keyword) if type(lista[i]) is dict else lista[pivote]) == 
			(lista[i].get(keyword) if type(lista[i]) is dict else lista[i])):
			indices_iguales.append(i)
		else:
			pivote = i

	indices_iguales.reverse()
	for i in indices_iguales:
		lista.pop(i)

	return lista

# Buscar valor en lista 
def SearchValue(lista, valor1=None, valor2=None, key1=None, key2=None):

	es_diccionario = False
	if type(lista[0]) is dict:
			es_diccionario = True

	if len(lista)>99:

		"""	
			# Obtener solo los valores esenciales para la busqueda
			if type(lista[0]) is dict:
				es_diccionario = True
				lista2 = []
				if not key2 is None:
					for l in lista:
						arb = {key1: l.get(key1), key2: l.get(key2)}
						lista2.append(arb)
				else:
					for l in lista:
						lista2.append(l.get(key1))	
				lista = lista2			
		"""
		lista_busqueda = [] # Lista a reducir para una busqueda rapida
		lista_busqueda2 = [] # Lista complementaria a reducir para una busqueda rapida
		mitad = 0 # Obtencion de longitud para reducir lista
		inicio = 0 # Indice inicial de variable lista para reducir lista_busqueda
		fin = len(lista)-1 # Indice final de variable lista para reducir lista_busqueda	
			
		# Reducir lista para buscar el valor
		if valor1 != (lista[0].get(key1) if es_diccionario else lista[0]):
			while not len(lista_busqueda)>0 and len(lista_busqueda)<11:
				
				# Obtener la mitad de la longitud de la lista
				mitad = (fin-inicio)//2
				mitad = inicio + mitad		

				# Verificar si el elemento buscado es mayor o menor en el indice condicionado	
				if valor1 > (lista[mitad].get(key1) if es_diccionario else lista[mitad]):
					inicio = mitad+1 
					lista_busqueda = lista[inicio:fin]
				elif valor1 < (lista[mitad].get(key1) if es_diccionario else lista[mitad]):
					fin = mitad-1
					lista_busqueda = lista[inicio:fin]
				else:
					if valor2 is None or valor2 == lista[mitad].get(key2):		 
						lista_busqueda = lista[mitad] 	
						return True	# Se encontro el elemento en la lista
					else:
						lista_busqueda = lista[inicio:fin]
						lista_busqueda2 = lista[(fin-mitad):inicio]
						break 		
		else:
			return True	# Se encontro el elemento en la lista	

		# Buscamos el valor en lista reducida
		if es_diccionario:
			# Busqueda en diccionarios
			for val in lista_busqueda:
				if valor1 == val.get(key1):
					if not valor2 is None:
						if valor2 == val.get(key2):
							return True	# Se encontro el elemento en la lista
						else:
							continue		
					return True	# Se encontro el elemento en la lista
			
			if lista_busqueda2: # Forma Implicita
				for val in lista_busqueda2:
					if valor1 == val.get(key1) and valor2 == val.get(key2):
						return True	# Se encontro el elemento en la lista
				 		
		else:
			# Busqueda en listas
			for val in lista_busqueda:
				if valor1 == val:
					return True	# Se encontro el elemento en la lista				

	else: # Busqueda Secuencial

		if es_diccionario:
			for l in lista:
				if valor1 == l.get(key1):
					if not valor2 is None:
						if valor2 == l.get(key2):
							return True	# Se encontro el elemento en la lista
						else:
							continue
					return True	# Se encontro el elemento en la lista
		else:
			for l in lista:
				if valor1 == l:	
					return True	# Se encontro el elemento en la lista

	return False # No se encontro el elemento en la lista					
						