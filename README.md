# Prueba Técnica de API-REST, Creación de Seeder DB, Scripts y JWT

Demo técnica que implementa distintos métodos y herramientas para la integración de datos que consume un cliente a través de una API-REST con autentificación JWT, registrando y consultando colonias, cp, estados y municipios del país de México.

Registrados en una base de datos por medio de un Seeder, con ayuda de Flask Script, para la integración de creación de comandos en CLI.

## Comenzando
Dentro de la ruta local de tu computador en donde desees obtener una copia de este repositorio, coloca la siguiente instrucción en el CLI de Git:

    git clone https://github.com/litocmvp/prueba_tecnica_1.git

Una vez obtenido procedemos a entrar al directorio del repositorio por CLI y creamos un entorno virtual en Python (preferentemente en la versión 3.8). con el siguiente comando:

    python3 -m venv enviroment_name # En Linux / MacOS
    py -3 -m venv enviroment_name # En Windows  

__Nota:__ *"enviroment_name" se refiere al nombre que deseemos colocarle al entorno virtual*

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
__Nota:__ *"byte_length" es el número de longitud de la cifra que deseemos, ej: 24*

Como resultado el CLI nos imprimiría por ejemplo este resultado: `b'KG\xe2"\x89\xb4\x88G\x05\x91\x8bWLdu$1\xdc\x84\x00\x8b\xbe5\x9d'`
El cual podrías usar para el valor de la variable KEY.

La variable "PATH_DB" se refiere a la ruta o dirección de conexión de la base de datos, como consejo, sugiero que uses sqlite para esta demo, por ejemplo podrias colocar el siguiente valor a esta variable, como ruta de la base de datos:

    # En Linux / MacOS
	    'sqlite://///home/username/repositoryfolder/db_prueba.db'
    # En Windows
	    'sqlite:///C:\\Users\\UserName\\Desktop\\RepositoryFolder\\db_prueba.db'
   
Ya creado el archivo ".env" dentro de la carpeta del repositorio, es igual necesario crear la Base de datos (solamente vacía), para que el PATH_DB, localice la BD y más adelante se puedan generar las tablas.

O si deseas, puedes descargar la base de datos previamente cargada con las tablas y los registros, dando clic [AQUI](https://1drv.ms/u/s!AkZJq0nr4WTrhOFoaUnp__5cc9cHeQ?e=zApmal), saltandose asi las secciones __Creación de Tablas__ y __Ejecutando las Pruebas__ del presente documento.

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
En donde "--eleccion" es el número de tabla a poblar y "--ruta" es la dirección absoluta del archivo txt, que se encuentra dentro del repositorio en la ruta "/app/static/file_SEPOMEX.txt".

__Nota:__ *para ver el número de elecciones que corresponde a las tablas, visita el archivo "seeder.py" dentro de la carpeta "app/common" que se encuentra en la carpeta del repositorio.*

__Nota 2:__ *Debido al gran volumen de datos a almacenar, es importante esperar a que la ejecución del comando finalice, para una correcta integración a la BD.*

Ahora que ya hemos poblado la BD, procedemos a ejecutar la aplicación con la siguiente instrucción en el CLI:

    flask run
Con ello podremos acceder a traves de un navegador y visitar "localhost"

### Analice la autentificiación sin estado (Stateless)
En esta prueba técnica se implementó una interfaz web para que el usuario pueda registrar nuevas colonias, por medio de la autentificación del usuario que tendrá que ser previamente registrado con permisos de administrador; despues de la autentificación se creará un JSON Web Token (JWT), y será almacenada en una cookie con el nombre de "__token_user__", con este token, podremos realizar las pruebas pertinentes del consumo de la REST-API con un software que nos permita realizar pruebas API, como ejemplo "__Postman__". Con este tipo de software podremos de igual forma registrar nuevas colonias e registrar usuario, y autentificarse para obtener un token.  

__Nota:__ *al registrar el usuario por interfaz web, debera hacer clic en el checkbox del formulario para poder registrar nuevas colonias, sino, el usuario no tendra los permisos necesarios y será denegado.*

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
