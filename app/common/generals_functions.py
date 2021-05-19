import os

# Obtener ruta la instancia de la aplicación
def PathInitial():
	return os.path.abspath(os.getcwd())

# Reducir Busqueda en listas
def OrderList(lista, keyword=None):
	if len(lista) > 1:
		if type(lista[0]) is dict:
			return sorted(lista, key=lambda i: i[keyword])
		else:	
			return lista.sort()

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
		 		
