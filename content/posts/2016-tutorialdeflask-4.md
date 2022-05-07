Title: Tutorial de Flask parte 4 (base de datos sqlite3)
Date: 2016-09-12 09:00  
Category: Tutorial Python
Tags: Python,Flask,Docker, Sqlite3
lang: es  
translation: true 

Continuando con la serie de tutoriales sobre Flask, en este caso se tocará el tema de base de datos, usando sqlite3. 

Este artículo se basa en el artículo en Inglés de [The Flask Mega tutorial, Part IV: Database.](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)

Los artículos anteriores son:

1. [Tutorial de Flask parte 1.](https://www.seraph.to/tutorial-de-flask-parte-1.html#tutorial-de-flask-parte-1)

2. [Tutorial de Flask parte 2 (plantilla html).](https://www.seraph.to/tutorial-de-flask-parte-2-plantillas-html.html#tutorial-de-flask-parte-2-plantillas-html)

3. [Tutorial de Flask parte 3 (formulario web).](https://www.seraph.to/tutorial-de-flask-parte-3-formulario-web.html#tutorial-de-flask-parte-3-formulario-web)


```
tutorial-flask/
├── app
│   ├── forms.py
│   ├── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── base.html
│   │   ├── index.html
│   │   └── login.html
│   └── views.py
├── config.py
├── db_create.py
├── db_downgrade.py
├── db_migrate.py
├── db_upgrade.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── run.py
└── tmp
```

Los archivos nuevos o modificados son los siguientes:  
- `config.py`.  
- `db_create.py`: Script para crear la base de datos.  
- `db_migrate.py`: Script para migrar la base de datos.  
- `db_upgrade.py`: Script para actualizar la base de datos.  
- `db_downgrade.py`: Script para revertir actulización de la base de datos.  
- `__init__.py`  
- `models.py`: Módulo donde se define las tablas de la base de datos.  

Archivo `config.py`: 

```python
#Se importa os


import os


#Se define el directorio base del proyecto


basedir = os.path.abspath(os.path.dirname(__file__))


#Se habilita CSRF


CSRF_ENABLED = True


#Se define la clave secreta


SECRET_KEY = 'pruea'



PROVEEDORES_OPENID = [


    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},


    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'}]



#Se define el uri de la base de datos sqlite app.db


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')


#Se define el repositorio para migracion de la base de datos app.db


SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

```

Archivo `__init__.py`:
```python
#Se importa Flask

from flask import Flask

#Se importa SQLALchemy

#from flask.ext.sqlalchemy import SQLAlchemy

from flask_sqlalchemy import SQLAlchemy

#Se crea la instancia de flask

app = Flask(__name__)

#Se define la configuracion

app.config.from_object('config')

#SE instancia la base de datos

db = SQLAlchemy(app)

#Se importa views y models de app

from app import views, models

```
Archivo `models.py`:
```python
#de app se importa db
from app import db

#Se crea la tabla User que hereda de db.Model
class User(db.Model):
    #Se crea la columna id como clave primaria e integer
    id = db.Column(db.Integer, primary_key=True)
    #Se crea la columna nickname como string de tamagn 64, como unico.
    usuario = db.Column(db.String(64), index=True, unique=True)
    #Columna correo, de 120 de tamagno del string y unico.
    correo = db.Column(db.String(120), index=True, unique=True)
    #Posts. que tiene relacion con la clase Post (tabla post),
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % (self.usuario)

#Tabla Post que hereda de model
class Post(db.Model):
    #Se crea el id del post como entero y clave primaria
    id = db.Column(db.Integer, primary_key=True)
    #Se crea la columna body como string de 140 caracteres
    cuerpo = db.Column(db.String(140))
    #Se define la marca de tiempo.
    timestamp = db.Column(db.DateTime)
    #Se define el id del usuario, es una clave foranea de la tabla usuario
    #Columna id.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.cuerpo)
```

Archivo `db_create.py`: 

```
#!/usr/bin/env python


#de migrate.versioning se importa api


from migrate.versioning import api


#De config se importa el uri


from config import SQLALCHEMY_DATABASE_URI


#De config se importa el repo de migrate


from config import SQLALCHEMY_MIGRATE_REPO


#De app se importa db


from app import db





#Se importa os.path


import os.path


#Se crea la base de datos.


db.create_all()


#Si el directorio del migrate no existe se crea y se usa,


#Si no se usa. 


if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):


    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')


    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)


else:


    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,


                        api.version(SQLALCHEMY_MIGRATE_REPO))

```

Archivo `db_migrate.py`:
```python

#!/usr/bin/env python

#se importa api.

from migrate.versioning import api

#Se importa el uri y el migrate.

from config import SQLALCHEMY_DATABASE_URI

from config import SQLALCHEMY_MIGRATE_REPO

#se define la version de la db para las migraciones.

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

#Se baja una version.

api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)

#Se vuelva a definir el uri y migrate de la vesion.

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

#Se muestra en pantalla la version actual.

print('Current database version: ' + str(v))

```
Archivo `db_upgrate.py`:
```python
#!/usr/bin/env python
#Se importa api.
from migrate.versioning import api
#De config se importa URI y el repo.
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
#Se actualiza el api.
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se define la version del api.
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#Se muestra la nueva version.
print('Current database version: ' + str(v))
```

Archivo `db_downgrade.py`:
```
#!/usr/bin/env python

#se importa api.

from migrate.versioning import api

#Se importa el uri y el migrate.

from config import SQLALCHEMY_DATABASE_URI

from config import SQLALCHEMY_MIGRATE_REPO



#se define la version de la db para las migraciones.

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

#Se baja una version.

api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, v - 1)

#Se vuelva a definir el uri y migrate de la vesion.

v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)

#Se muestra en pantalla la version actual.

print('Current database version: ' + str(v))
```


Construir la imagen docker por medio de `docker-compose`:

```
docker-compose build
```

Ahora toca ejecutar el contenedor:

```
docker-compose up
Creating tutorialflask_web_1
Attaching to tutorialflask_web_1
web_1  |  * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
web_1  |  * Restarting with stat
web_1  |  * Debugger is active!
web_1  |  * Debugger pin code: 201-487-104

```



Ahora para crear la base de datos se usa docker desde otra consola en el mismo directorio del proyecto:


Primero un `docker ps`:

```
docker ps 
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS                    NAMES
52bf03d39d06        tutorialflask_web   "/bin/sh -c 'python r"   About a minute ago   Up About a minute   0.0.0.0:5000->5000/tcp   tutorialflask_web_1

```


Ya se tiene el ID del contenedor, ahora  a ejecutar `docker exec`:

```
docker exec -ti 52bf03d39d06 ./db_create.py
```

Ahora se ejecuta un `ls -l` y se tiene lo siguiente:

```
drwxr-xr-x 4 ernesto ernesto 4096 sep 12 20:07 app
-rw-r--r-- 1 root    root    7168 sep 12 22:31 app.db
-rw-r--r-- 1 ernesto ernesto  620 sep 12 22:14 config.py
-rwxr-xr-x 1 ernesto ernesto  773 sep 12 20:29 db_create.py
-rwxr-xr-x 1 ernesto ernesto  619 sep 12 20:31 db_downgrade.py
-rwxr-xr-x 1 ernesto ernesto 1530 sep 12 20:37 db_migrate.py
drwxr-sr-x 4 root    root    4096 sep 12 22:31 db_repository
-rwxr-xr-x 1 ernesto ernesto  456 sep 12 20:52 db_upgrade.py
-rw-r--r-- 1 ernesto ernesto   67 sep  4 17:27 docker-compose.yml
-rw-r--r-- 1 ernesto ernesto  480 sep  4 17:27 Dockerfile
drwxr-xr-x 2 root    root    4096 sep 12 22:29 __pycache__
-rw-r--r-- 1 ernesto ernesto    0 sep  4 17:27 README.md
-rw-r--r-- 1 ernesto ernesto   79 sep  4 17:27 run.py
drwxr-xr-x 2 ernesto ernesto 4096 sep 19  2014 tmp

```

Se crearon el archivo `app.db` y el directorio `__py__cache__`.


Ahora se ejecutará la primera migración: 

```
docker exec -ti 52bf03d39d06 ./db_migrate.py 
New migration saved as /code/db_repository/versions/001_migration.py
Current database version: 1
```

Se salvó la primera migración y el número de versión es 1. Al listar los archivos


y directorios se tiene lo siguiente:

```
drwxr-xr-x 4 ernesto ernesto 4096 sep 12 20:07 app
-rw-r--r-- 1 root    root    7168 sep 12 22:33 app.db
-rw-r--r-- 1 ernesto ernesto  620 sep 12 22:14 config.py
-rwxr-xr-x 1 ernesto ernesto  773 sep 12 20:29 db_create.py
-rwxr-xr-x 1 ernesto ernesto  619 sep 12 20:31 db_downgrade.py
-rwxr-xr-x 1 ernesto ernesto 1530 sep 12 20:37 db_migrate.py
drwxr-sr-x 4 root    root    4096 sep 12 22:31 db_repository
-rwxr-xr-x 1 ernesto ernesto  456 sep 12 20:52 db_upgrade.py
-rw-r--r-- 1 ernesto ernesto   67 sep  4 17:27 docker-compose.yml
-rw-r--r-- 1 ernesto ernesto  480 sep  4 17:27 Dockerfile
drwxr-xr-x 2 root    root    4096 sep 12 22:29 __pycache__
-rw-r--r-- 1 ernesto ernesto    0 sep  4 17:27 README.md
-rw-r--r-- 1 ernesto ernesto   79 sep  4 17:27 run.py
drwxr-xr-x 2 ernesto ernesto 4096 sep 19  2014 tmp

```

Ahora se tiene el directorio `db_repository`.


Ahora se trabajará con la base de datos de manera interactiva, se ejecuta `docker exec`:

```python
docker exec -ti 52bf03d39d06 python


Python 3.5.2 (default, Aug 22 2016, 21:04:27) 
[GCC 4.9.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>

```


De la aplicación se importa db y models:
```python

>>> from app import db, models
```

Se crea un usuario:

```python
>>> u = models.User(usuario='john', correo='john@email.com')
>>> db.session.add(u)
>>> db.session.commit()
```

Se crea otro usuario:

```python
>>> u = models.User(usuario='jane', correo='jane@email.com')
>>> db.session.add(u)                                       
>>> db.session.commit()
```

Se hace una consulta de los usuarios:

```python
>>> users = models.User.query.all()
>>> users
[<User 'john'>, <User 'jane'>]


>>> for user in users:
...     print (user)  
... 
<User 'john'>
<User 'jane'>

```

Obtener información del usuario con id 1:

```python
>>> u = models.User.query.get(1)
>>> u
<User 'john'>
```

Ahora se agregarán unos posts:

```python
>>> import datetime
>>> u = models.User.query.get(1)
>>> p = models.Post(cuerpo='mi primer post!', timestamp=datetime.datetime.utcnow(), author=u)            
>>> db.session.add(p)                               
>>> db.session.commit()
```python


Se sale del interprete de comandos.

Ahora se usará `sqlitebrowser` para revisar la base de datos `app.db`:


En la figura se muestra la pantalla principal de la aplicación donde se ve las sentencias SQL para la 


creación de las tablas:

![](./images/tutorialdeflask4-1.png)

Ahora se muestra los datos, la tabla usuario y la tabla de post:

![](./images/tutorialdeflask4-2.png)

![](./images/tutorialdeflask4-3.png)

Para detener el contenedor se ejecuta:

```
docker-compose down

```

El código fuente de este artículo se encuentra en [gitlab en la rama articulo4](https://gitlab.com/ecrespo/tutorial-flask/tree/articulo4).



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)




