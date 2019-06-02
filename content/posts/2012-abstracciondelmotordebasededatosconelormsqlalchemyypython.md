Title: Abstracción del motor de Base de Datos con el ORM Sqlalchemy y python
Date: 2012-04-07 09:00
Category: Tutorial de Python
Tags: Debian,General,Linux,Python,Ubuntu
lang: es
translation: true

`ORM` o Mapeo de Objeto Relacional es una técnica de programación para convertir datos entre el sistema de tipos utilizando lenguajes de programación orientado a objetos y el utilizado en una Base de Datos Relacional (tomado de la [wikipedia](https://es.wikipedia.org/wiki/ORM)).

`Sqlalchemy` es una herramienta `ORM` para python que da flexibilidad en el desarrollo con SQL.

Tomando el artículo anterior de [sqlite con python](https://www.seraph.to/sqlite-con-python.html#sqlite-con-python), se cambiará el módulo de `sqlite3` para python por el `ORM Sqlalchemy`, de esa forma se abstrae las distintas instrucciones existentes para diferentes motores de base de datos como `postgresql`, `mysql`, `sqlite` y se puede así utilizar cualquier motor de base de datos realizando mínimos cambios en el programa.

A continuación el código donde se muestra el uso de `sqlalchemy` en una base de datos `sqlite3`:  

```python 
#!/usr/bin/env python

#Se importa sqlalchemy
from sqlalchemy import *

#Se crea la instancia del motor de la base de datos y se asocia con un
#archivo
db = create_engine('sqlite:///tutorial.db')
#se coloca la base de datos en modo no mostrar resultados 
#de las instrucciones en pantalla.
db.echo = False

#Se asocia el archivo de la base de datos a la instancia de metadatos.
metadata = MetaData(db)


#Se crea la tabla contactos tal cual el mismo ejemplo de 
#sqlite.
contactos = Table(
'contactos',metadata,
Column('id',Integer,primary_key=True),
Column('nombre', Unicode(100)),
Column('telefono',String(11)),
Column('grupo_id', ForeignKey('grupos.id')))

#Se crea la tabla de grupos tal cual el mismo ejemplo de 
#sqlite
grupos = Table(
'grupos',metadata,
Column('id',Integer,primary_key=True),
Column('grupo',Unicode(300)),
Column('descripcion',Unicode(500)))

#Se crea todas las tablas.
metadata.create_all()

#Se inserta datos en la tabla grupos.
i = grupos.insert()
i.execute(grupo='Guacara',descripcion='Ciudad de Carabobo')
i.execute({'grupo':'Valencia','descripcion':'Capital de Carabobo'},
{'grupo':'Maracay','descripcion':'Capital de Aragua'},
{'grupo':'Merida','descripcion':'Capital de Merida'})

#Se inserta datos en la tabla contactos
u = contactos.insert()
u.execute(nombre='Ernesto Crespo',telefono='04155673029',grupo_id=1)
u.execute(nombre='Pedro Perez',telefono='0295212223',grupo_id=2)
u.execute(nombre='Jhon Doe',telefono='04184488484',grupo_id=2)
u.execute(nombre='Jane Doe',telefono='04184488482',grupo_id=1)
u.execute(nombre='Pepito de los palotes',telefono='04184588484',grupo_id=3)

#Se hace consulta de la tabla contactos
s = contactos.select()
rs = s.execute()

#Se hace consultas de la tabla grupos.
t = grupos.select()
ts = t.execute()

#Se muestra la tabla grupos
print "GRUPOS"
print "-------------------------------------"
for fila in ts:
print "id: %s,Grupo: %s, Descripcion:%s" %(fila[0],fila[1],fila[2])
print "--------------------------------------"

del fila
#Se muestra la tabla contactos.
print "CONTACTOS"
print "-------------------------------------"
for fila in rs:
print "Nombre: %s, telefono %s, Grupo %s" %(fila[1],fila[2],fila[3]) 
print "--------------------------------------"

#Se borra la fila del id 1 de la tabla grupos
t = grupos.delete(text("id=1"))
t.execute()

#Se realiza una consulta de la tabla grupos
q = grupos.select()
qs = q.execute()

#Se muestra la tabla grupos, 
#ahora no tiene la fila del grupo Guacara.
print "GRUPOS"
print "-------------------------------------"
for fila in qs:
print "id: %s,Grupo: %s, Descripcion:%s" %(fila[0],fila[1],fila[2])
print "--------------------------------------"


#Se muestra los contactos del grupo 2.
print "Mostrar contactos del grupo 2"
del q
del qs
q = contactos.select(text("grupo_id=2"))
qs = q.execute()
print "-------------------------------------"
for fila in qs:
print "Nombre: %s, telefono %s, Grupo %s" %(fila[1],fila[2],fila[3]) 
print "--------------------------------------"
```    

El resultado de ejecutar el script se muestra a continuación:  
```
GRUPOS
-------------------------------------
id: 1,Grupo: Guacara, Descripcion:Ciudad de Carabobo
id: 2,Grupo: Valencia, Descripcion:Capital de Carabobo
id: 3,Grupo: Maracay, Descripcion:Capital de Aragua
id: 4,Grupo: Merida, Descripcion:Capital de Merida
--------------------------------------
CONTACTOS
-------------------------------------
Nombre: Ernesto Crespo, telefono 04155673029, Grupo 1
Nombre: Pedro Perez, telefono 0295212223, Grupo 2
Nombre: Jhon Doe, telefono 04184488484, Grupo 2
Nombre: Jane Doe, telefono 04184488482, Grupo 1
Nombre: Pepito de los palotes, telefono 04184588484, Grupo 3
--------------------------------------
GRUPOS
-------------------------------------
id: 2,Grupo: Valencia, Descripcion:Capital de Carabobo
id: 3,Grupo: Maracay, Descripcion:Capital de Aragua
id: 4,Grupo: Merida, Descripcion:Capital de Merida
--------------------------------------
Mostrar contactos del grupo 2
-------------------------------------
Nombre: Pedro Perez, telefono 0295212223, Grupo 2
Nombre: Jhon Doe, telefono 04184488484, Grupo 2
--------------------------------------
```

De está manera se facilita el trabajo de acceder a una base de datos sin estar usando directamente su API y facilita también poder utilizar cualquier motor de base de datos en la aplicación que se esté desarrollando.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
