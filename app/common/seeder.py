from . import PathInitial, OrderList, SearchValue, PurgarRepetidos
from . import PoblarTB

# Declaración de variables para organizar los datos a almacenar en las diferentes tablas
tipo_zonas = []
tipo_asentamientos = []
codigos_postales = []
estados = []
municipios = []
colonias = []

chains = []

with open(PathInitial()+'/static/file_SEPOMEX.txt', 'r') as f:
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

for chain in chains:

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
	"""

	tipo_zonas.append(chain[13])

	# Asentamientos
	if len(tipo_asentamientos)>1:
		OrderList(tipo_asentamientos, 'codigo')
		if not SearchValue(lista=tipo_asentamientos, valor1=chain[10], key1='codigo'):
			arb = {'codigo':chain[10], 'tipo':chain[2]}
			tipo_asentamientos.append(arb)
	else:
		arb = {'codigo':chain[10], 'tipo':chain[2]}
		tipo_asentamientos.append(arb)

	# Códigos postales
	codigos_postales.append(chain[0])

	# Estados
	arb = {'codigo':chain[7], 'nombre':chain[4]}
	estados.append(arb)

	# Municipios
	arb = {'codigo':chain[11], 'nombre':chain[3], 'cod_estado':chain[7]}
	municipios.append(arb)

	# Colonias
	arb = ({'nombre':chain[1], 'cod_postal':chain[0], 'tip_zona': chain[13], 
			'cod_asentamiento':chain[10], 'cod_estado': chain[7],
			'cod_municipio':chain[11]})
	colonias.append(arb)


#Orden de listas
OrderList(tipo_zonas)
OrderList(tipo_asentamientos, 'codigo')
OrderList(codigos_postales)
OrderList(estados, 'codigo')
#OrderList(municipios, 'codigo')
#OrderList(colonias, 'cod_estado')

zonas = PurgarRepetidos(tipo_zonas)
asent = PurgarRepetidos(tipo_asentamientos, 'codigo')
cp = PurgarRepetidos(codigos_postales)
stdo = PurgarRepetidos(estados, 'codigo')
mpio = PurgarRepetidos(municipios, 'nombre')


# Poblar Tabla tipos_zonas
PoblarTB(zonas, 1)
# Poblar Tabla tipos_asentamientos
PoblarTB(asent, 2)
# Poblar Tabla codigos_postales
PoblarTB(cp, 3)
# Poblar Tabla estados
PoblarTB(stdo, 4)
# Poblar Tabla municipios
PoblarTB(mpio, 5)	
# Poblar Colonias
PoblarTB(colonias, 6)		
