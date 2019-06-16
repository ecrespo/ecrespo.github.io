Title: Manejo de sesión en el ORM sqlalchemy
Date: 2013-09-18 9:00
Category: General
Tags: General,Python
lang: es
translation: true
 
Hace tiempo explique como crear unas tablas para la base de datos `sqlite3`, insertar datos, removerlos y consultarlos,el artículo se llama [Abstracción del motor de Base de Datos con el ORM Sqlalchemy y python](http://blog.crespo.org.ve/2012/04/abstraccion-del-motor-de-base-de-datos.html).

Antes de comenzar a probar lo que se escribe en este artículo es necesario que realicen pruebas con el artículo mencionado anteriormente para que tengan la base de datos con sus datos listas para ser utilizadas en este artículo.

Ahora se explica como usar unas tablas con sus datos ya creada, creando una sesión para la base de datos.

Este artículo se basa en un [tutorial en inglés de sqlalchemy](mapfish.org/doc/tutorials/sqlalchemy.html) o el [tutorial paso a paso de sqlalchemy](http://www.rmunn.com/sqlalchemy-tutorial/tutorial.html).

Lo primero que se hará es crear un archivo `model.py` que contendrá el modelo de la base de datos.
```python
#Se importa el módulo datetime

import datetime

#Se importa schema y tupes de sqlalchemy

from sqlalchemy import schema, types



#Se instancia la clase MetaData.

metadata = schema.MetaData()



#Se crea la función now que devuelve la hora actual.

def now():

    return datetime.datetime.now()



#Se crea la instancia table con los campos de la tabla grupos

grupos_table = schema.Table('grupos',metadata,

        schema.Column('id',types.Integer,primary_key=True),

        schema.Column('grupo',types.String(300),nullable=False),

        schema.Column('descripcion',types.String(500),nullable=False),

)


#Se crea la instancia table con los campos de la tabla contactos

contactos_table = schema.Table('contactos',metadata,

        schema.Column('id',types.Integer,primary_key=True),

        schema.Column('nombre',types.String(100),nullable=False),

        schema.Column('telefono',types.String(11),nullable=False),

        schema.Column('grupo_id',types.Integer,nullable=False),

)



#Se crea la clase Contactos y Grupos que heredan de object y sólo tienen pass.

class Contactos(object): pass

class Grupos(object): pass



#Se mapea la Clase Contactos con la tabla contactos_table

orm.mapper(Contactos, contactos_table)

#Se mapea la Clase Grupos con la tabla grupos_table

orm.mapper(Grupos,grupos_table)
```

Ya con este código se logra el mapeo de las tablas existentes con sus campos.

Ahora se crea un archivo llamado `prueba-db.py` que va a realizar la sesión a la base de datos por medio del módulo `model.py`  donde se realizará unas consultas, inserciones y remociones de datos.
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-



import model

from sqlalchemy import orm

from sqlalchemy import create_engine



#Crear un engine y crear todas las tablas necesarias

engine = create_engine('sqlite:///tutorial.db', echo=False)

model.metadata.bind = engine

model.metadata.create_all()



# Configurar la sesion



sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False,

            expire_on_commit=True)

session = orm.scoped_session(sm)



#Se realiza una consulta a la tabla grupos

print "Consulta inicial de la tabla contactos"

consulta = session.query(model.Contactos).all()

for lista in consulta:

    print lista.nombre,lista.telefono

print "--------------------------------"





#Agregar un contacto

contacto = model.Contactos()

contacto.nombre = u"Luisa Gonzalez"

contacto.telefono = u"04155555555"

contacto.grupo_id = 2

session.add(contacto)

session.flush()

session.commit()





#Se realiza una consulta a la tabla grupos

print "Consulta la tabla contactos con el dato incorporado"

consulta = session.query(model.Contactos).all()

for lista in consulta:

    print lista.nombre,lista.telefono

print "--------------------------------"

    



#Borrar un contacto

session.delete(contacto)

session.flush()

session.commit()



#Se realiza una consulta a la tabla grupos

print "Consulta la tabla contactos luego de borrar el dato"

consulta = session.query(model.Contactos).all()

for lista in consulta:

    print lista.nombre,lista.telefono

print "--------------------------------"
```

El resultado de ejecutar el script `pruebas-db.py` se muestra a continuación:
```
Consulta inicial de la tabla contactos

Ernesto Crespo 04155673029

Pedro Perez 0295212223

Jhon Doe 04184488484

Jane Doe 04184488482

Pepito de los palotes 04184588484

--------------------------------

Consulta la tabla contactos con el dato incorporado

Ernesto Crespo 04155673029

Pedro Perez 0295212223

Jhon Doe 04184488484

Jane Doe 04184488482

Pepito de los palotes 04184588484

Luisa Gonzalez 04155555555

--------------------------------

Consulta la tabla contactos luego de borrar el dato

Ernesto Crespo 04155673029

Pedro Perez 0295212223

Jhon Doe 04184488484

Jane Doe 04184488482

Pepito de los palotes 04184588484

--------------------------------
```

De esta forma se puede realizar consultas, remociones e inserciones por medio de `sqlalchemy` con sesiones.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)