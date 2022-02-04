# Prueba Técnica de API-REST, Creación de Seeder DB, Scripts y JWT

Demo técnica que implementa distintos métodos y herramientas para la integración de datos que consume un cliente a través de una API-REST con autentificación JWT, registrando y consultando colonias, cp, estados y municipios del país de México, ofrecidos por un archivo en formato txt que deberá ser descargado desde la siguiente url: https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx
Con este formato los datos podrán ser registrados en una base de datos por medio de un Seeder, con ayuda de Flask Script, para la integración de creación de comandos en CLI.

## Comenzando
Dentro de la ruta local de tu computador en donde desees obtener una copia de este repositorio, coloca la siguiente instrucción en el CLI de Git:

    git clone https://github.com/litocmvp/prueba_tecnica_1.git

Una vez obtenido procedemos a entrar al directorio del repositorio por CLI y creamos un entorno virtual en Python (preferentemente en la versión 3.8). con el siguiente comando:

    python3 -m venv enviroment_name # En Linux / MacOS
    py -3 -m venv enviroment_name # En Windows  
###### Nota: "enviroment_name" se refiere al nombre que deseemos colocarle al entorno virtual
Al crearse procedemos a entrar al entorno virtual con la siguiente instrucción:

    . enviroment_name/bin/activate # En Linux / MacOS
     enviroment_name\Scripts\activate # En Windows
Ya adentro del entorno virtual , procedemos a instalar los requerimientos con la instrucción:

    pip3 install -r requeriments.txt # En Linux / MacOS
    pip install -r requeriments.txt # En Windows
Ya instalado los requerimientos, podremos estar a un paso de ejecutar la aplicación, solo nos faltaría, declarar las siguientes variables del entorno virtual, en el CLI:

    # En Linux / MacOS
	    export FLASK_APP = "entrypoint.py"
	    export FLASK_ENV = "development" # Opcional 
	    export FLASK_RUN_PORT = 80
	    export APP_ENV = "config.dev" || "config.prod"
	# En Windows (PowerShell)
		$env:FLASK_APP="entrypoint.py"
	    $env:FLASK_ENV="development" # Opcional 
	    $env:FLASK_RUN_PORT=80
	    $env:APP_ENV="config.dev" || "config.prod"

### Pre-requisitos

Para que la aplicación funcione de manera optima, requerirá crear un archivo llamado ".env", que almacenará otras variables de entorno esenciales para la aplicación, los cuales se encuentrán detallados en los archivos "dev.py" y "prod.py", de la carpeta "config".
Los nombres de las variables de entorno que deberas colocar en el archivo ".env" son los siguientes:

 - KEY 
 - PATH_DB
 
 En donde "KEY" será una clave secreta para uso de la aplicación en Flask, la cual podrá ser cualquier contraseña que desees ej. "12345_esta_es_mi_password" o si deseas generar una aleatoria, sigue las siguientes instrucciones en un CLI:
 
    py
    import os
    print(os.urandom(byte_length))
##### Nota: "byte_length" es el número de longitud de la cifra que deseemos, ej: 24 
Como resultado el CLI nos imprimiría por ejemplo este resultado: `b'KG\xe2"\x89\xb4\x88G\x05\x91\x8bWLdu$1\xdc\x84\x00\x8b\xbe5\x9d'`
El cual podrías usar para el valor de la variable KEY.

La variable "PATH_DB" se refiere a la ruta o dirección de conexión de la base de datos, como consejo, sugiero que uses sqlite para esta demo, por ejemplo podrias colocar el siguiente valor a esta variable, como ruta de la base de datos:

    # En Linux / MacOS
	    'sqlite://///home/username/repositoryfolder/db_prueba.db'
    # En Windows
	    'sqlite:///C:\\Users\\UserName\\Desktop\\RepositoryFolder\\db_prueba.db'
   
Ya creado el archivo ".env" dentro de la carpeta del repositorio, es igual necesario crear la Base de datos (solamente vacía), para que el PATH_DB, generé localice la BD y más adelante se pueda generar las tablas.

Como ultimo y para que surtan efectos estas variables necesitaremos salirnos del entorno virtual, previamente creado y volver a ingresar, para detectar las variables de entorno dentro del archivo ".env"; esto lo logramos con la siguiente instrucción en el CLI: 

    deactivate
    . enviroment_name/bin/activate # En Linux / MacOS
     enviroment_name\Scripts\activate # En Windows

### Creación de Tablas
Antes de ejecutar la aplicación, se requiere generar las tablas, para ello usamos las siguientes instrucciones, dentro de la ruta del repositorio en el CLI:

    flask db init
    flask db migrate -m "Inciando Migración por primera vez"
    flask db upgrade
Con estas tres instrucciones podemos generar las tablas dentro de la base de datos, la cual definimos su ruta en el archivo "PATH_DB"

## Ejecutando las Pruebas

Para poblar la base de datos requerimos de las siguientes instrucciones:

    python manage.py seed --eleccion --ruta
En donde "--eleccion" es el número de tabla a poblar y "--ruta" es la dirección absoluta del archivo txt, descargado de la url: https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx
##### Nota: para ver el número de elecciones que corresponde a las tablas, visita el archivo "seeder.py" dentro de la carpeta "app/common" que se encuentra en la carpeta del repositorio.
##### Nota 2: Debido al gran volumen de datos a almacenar, es importante esperar a que la ejecución del comando finalice, para una correcta integración a la BD.

Ahora que ya hemos poblado la BD, procedemos a ejecutar la aplicación con la siguiente instrucción en el CLI:

    flask run
Con ello podremos acceder a traves de un navegador y visitar "localhost"

### Analice la autentificiación sin estado (Stateless)
Al acceder a la interfaz de usuario, podremos registrar nuevas colonias, gracias al JSON Web Token (JWT), que nos devolverá el usuario a traves de la API-REST, para ello se requiere registrarse como un usuario con privilegios de registro, que se tendra que seleccionar en el checkbox del formulario de registro. 
Una vez registrado, tendremos que iniciar sesión y si los datos de nombre de usuario y contraseña son encontrados en la BD podremos a traves del inspeccionador de desarrollo del navegador, corroborar que recibimos como respuesta de la API-REST un token, compuesto por un encabezado, un contenido y una firma, que nos servirá para poder registrar nuevas colonias o denegarnos este permiso (si es que no se activo el checkbox del formulario del registro). 

## Construido con

 - Microframework Flask
 - Flask Migrate
 - Flask Script
 - Flask SQLAlchemy
 - Flask Jinja
 - Flask WTForms
 - PyJWT
 - Python dotenv
 - UUID

## Wiki

Para más detalles técnicos, visite las siguientes documentación técnica:

 - [Welcome to Flask — Flask Documentation (2.0.x) (palletsprojects.com)](https://flask.palletsprojects.com/en/2.0.x/)
 - [Flask-Migrate — Flask-Migrate documentation](https://flask-migrate.readthedocs.io/en/latest/)
 - [Flask-Script — Flask-Script 0.4.0 documentation](https://flask-script.readthedocs.io/en/latest/)
 - [Flask-SQLAlchemy — Flask-SQLAlchemy Documentation (2.x) (palletsprojects.com)](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
 - [Jinja — Jinja Documentation (3.0.x) (palletsprojects.com)](https://jinja.palletsprojects.com/en/3.0.x/)
 - [Flask-WTF — Flask-WTF Documentation (1.0.x)](https://flask-wtf.readthedocs.io/en/1.0.x/)
 - [Welcome to PyJWT — PyJWT 2.3.0 documentation](https://pyjwt.readthedocs.io/en/stable/)
 - [python-dotenv · PyPI](https://pypi.org/project/python-dotenv/)
 - [uuid — UUID objects according to RFC 4122 — Python 3.10.2 documentation](https://docs.python.org/3/library/uuid.html)

## Autor
Carlos Mario Vázquez Pérez 

> www.cmvp.me

## Expresiones de Gratitud
Este repositorio dirige sus gratitudes por haber compartido sus conocimientos a los siguientes autores:

 - Juan José Lozano Gómez (J2Logo) -[El blog de Python - Aprende Python en español de principiante a experto (j2logo.com)](https://j2logo.com/)
 - Julian Nash [Julian Nash - YouTube](https://www.youtube.com/channel/UC5_oFcBFlawLcFCBmU7oNZA)
 - Anthony [Pretty Printed - YouTube](https://www.youtube.com/channel/UC-QDfvrRIDB6F0bIO4I4HkQ)
 - [CodelyTV - Redescubre la programación - YouTube](https://www.youtube.com/c/CodelyTv/about)

Y muchos otros autores, que se me han pasado fuera de la mente, al redactar este apartado, pero que les agradezco por sus publicaciones, ya sea que se identifiquen en la web con un nombre o permanezcan en el anonimato, les agradezco por todo su tiempo y esfuerzo en ayudar a los demas.

> Muchas Gracias Att. Carlos Mario Vázquez Pérez (CMVP)
