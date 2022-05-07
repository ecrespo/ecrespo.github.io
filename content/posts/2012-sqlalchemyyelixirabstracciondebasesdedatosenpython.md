Title: Sqlalchemy y Elixir: Abstracción de Bases de Datos en Python
Date:  2012-04-08 08:30
Category: Tutorial de Python 
Tags: Debian,General, Python,Ubuntu
lang: es
translation: true

En el artículo [anterior](https://www.seraph.to/sqlite-con-python.html) se explica como usar `Sqlalchemy` para acceder y manipular una base de datos abstrayendo el motor de la base de datos a utilizar.

Existe una herramienta que facilita aun más el trabajo de crear tablas, insertar, consultar o remover datos de dichas tablas; [Elixir](http://elixir.ematia.de/trac/wiki) crea una capa declarativa sobre `slqalchemy` que permite usar la declaración de clases directamente a las tablas de entidad relación.

Igual que en el ejemplo anterior se usará las tablas Grupos y Contactos, la diferencia será que no será necesario definir un campo id para cada tabla, además la forma de declarar cual campo es primary key o foreign key es con la declaración de uno a muchos o de muchos a uno.

Este ejemplo crea las tablas, se realiza una inserción de datos a ambas tablas, se realiza unas consultas de datos y al final se elimina y dato de la tabla Contactos y se muestra que ya se elimino de dicha tabla.

El código python se muestra a continuación:  
```
#!/usr/bin/env python

from elixir import metadata, Entity, Field
from elixir import Unicode, UnicodeText
from elixir import *

#Se asocia el metadato con la base de datos sqlite
metadata.bind = "sqlite:///prueba.db"
#Se activa el echo de los resultados de los comandos.
metadata.bind.echo = False

#Se crea la clase Grupos que hereda Entity, 
#se crea los campos grupo (unicode 150),
#descripcion (unicode 200) y
#contactos que es una referencia uno a muchos de la 
#clase Contactos.
class Grupos(Entity):
grupo = Field(Unicode(150))
descripcion = Field(Unicode(200))
contactos = OneToMany('Contactos')

#Devuelve la informacion de los grupos
def __repr__(self):
return '<Grupos "%s" (%s)>' % (self.grupo,self.descripcion)

#Se crea la clase contactos que hereda de Entity.
#se tiene el campo nombre (unicode 100),
#telefono (string 11) y el campo grupo muchos a uno de grupos.
class Contactos(Entity):
nombre = Field(Unicode(100))
telefono = Field(String(11))
grupo = ManyToOne('Grupos')

#Devuelve la informacion de los contactos
def __repr__(self):
return '<Contactos- nombre: "%s", telefono: "%s", grupo: "%s">' % (self.nombre,self.telefono,self.grupo)


if __name__ == "__main__":
#Se importa create_all, setup_all y session de elixir.
from elixir import create_all, setup_all, session
#Se crea las clases segun los modelos.
setup_all()
#Se crea las tablas en la base de datos segun los modelos definidos
create_all()

#Se insertan datos en la tabla grupos
#En este caso se agregan ciudades del pais.
Guacara = Grupos(grupo='Guacara',descripcion='Ciudad del Estado Carabobo')
Valencia = Grupos(grupo="Valencia",descripcion="Capital del Estado Carabobo")
Barquisimeto = Grupos(grupo="Barquisimeto",descripcion="Capital del Estado Lara")
Caracas = Grupos(grupo="Caracas",descripcion="Distrito Capital")
Maracaibo = Grupos(grupo="Maracaibo",descripcion="Capital del Estado Zulia")
Merida = Grupos(grupo="Merida",descripcion="Capital del Estado Merida")
Barcelona = Grupos(grupo="Barcelona",descripcion="Capital de Anzoategui")
PuertoOrdaz = Grupos(grupo="Puerto Ordaz",descripcion="Ciudad del Estado Bolivar")
Barinas = Grupos(grupo="Barinas",descripcion="Capital del Estado Barinas")
Maracay = Grupos(grupo="Maracay",descripcion="Capital del Estado Aragua")
LosTeques = Grupos(grupo="Los Teques",descripcion="Capital del Estado Miranda")

#Se hace el commit para insertar los datos de la tabla grupos en la base de datos.
session.commit()

#Se insertan datos en la tabla contactos, cada contacto hace referencia a un grupo de 
#la tabla grupos.
Contactos(nombre='Ernesto Nadir Crespo Avila',telefono='04205873118',grupo=Guacara)
Contactos(nombre='Jhon Doe',telefono='04295333131',grupo=Valencia)
Contactos(nombre='Jane Doe',telefono='04399991919',grupo=Caracas)
Contactos(nombre='Pedro Perez',telefono='04596661617',grupo=Caracas)
Contactos(nombre='Maria Perez',telefono='04194445445',grupo=Barquisimeto)
#Se hace el commit para insertar los datos en la tabla contactos en la base de datos.
session.commit()

#Se realiza una consulta buscando los contactos del grupo Caracas
#Y se presentan en pantalla
registros = Contactos.query.filter(Contactos.grupo == Caracas).all()
print "Contactos de Caracas"
for registro in registros:
print "-" * 20
print registro.nombre
print registro.telefono
print registro.grupo
print "*-" *20

#Se muestra en pantalla todos los contactos.
registros = Contactos.query.all()
print "Todos los Contactos"
for registro in registros:
print "-" * 20
print registro.nombre
print registro.telefono
print registro.grupo
print "*-" *20
#Se muestra en pantalla todos los grupos, con sus contactos
#asociados.
registros = Grupos.query.all()
for registro in registros:
print "-" * 20
print registro.grupo
print registro.descripcion
print registro.contactos
print "*-" *20
#Se consulta la tabla contactos buscando al usuario Maria Perez
#Se muestra en pantalla la informacion de ese contacto
consulta = Contactos.query.filter_by(nombre=u'Maria Perez')
registro = consulta.first()
print "%s , %s :(%s)" % (registro.nombre,registro.telefono, registro.grupo)
# Se borra ese contacto de la tabla contactos y se actualiza la base de datos.
registro.delete()
session.commit()

#Se muestra en pantalla todos los contactos
#para hacer notar que ya el contacto Maria Perez no existe
#en la base de datos.
registros = Contactos.query.all()
print "Contactos, luego de eliminar a Maria Perez"
for registro in registros:
print "-" * 20
print registro.nombre
print registro.telefono
print registro.grupo
```

El código SQL generado a partir del modelo es el siguiente:
```
CREATE TABLE __main___grupos (
id INTEGER NOT NULL, 
grupo VARCHAR(150), 
descripcion VARCHAR(200), 
PRIMARY KEY (id)
)


CREATE TABLE __main___contactos (
id INTEGER NOT NULL, 
nombre VARCHAR(100), 
telefono VARCHAR(11), 
grupo_id INTEGER, 
PRIMARY KEY (id), 
CONSTRAINT __main___contactos_grupo_id_fk FOREIGN KEY(grupo_id) REFERENCES __main___grupos (id)
)
```
Con respecto al modelo el código `SQL` si tiene los campos `id` como `PRIMARY KEY` en cada tabla y se define cuales son `FOREIGN KEY`, gracias a `Elixir` se ahorra trabajo en la definición de campos y al usar `OneToMany` o `ManyToOne` se está definiendo quienes son primary o foreign key.

El resultado del script se muestra a continuación:  
```
Contactos de Caracas
--------------------
Jane Doe
04399991919
<Grupos "Caracas" (Distrito Capital)>
--------------------
Pedro Perez
04596661617
<Grupos "Caracas" (Distrito Capital)>
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Todos los Contactos
--------------------
Ernesto Nadir Crespo Avila
04205873118
<Grupos "Guacara" (Ciudad del Estado Carabobo)>
--------------------
Jhon Doe
04295333131
<Grupos "Valencia" (Capital del Estado Carabobo)>
--------------------
Jane Doe
04399991919
<Grupos "Caracas" (Distrito Capital)>
--------------------
Pedro Perez
04596661617
<Grupos "Caracas" (Distrito Capital)>
--------------------
Maria Perez
04194445445
<Grupos "Barquisimeto" (Capital del Estado Lara)>
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
--------------------
Guacara
Ciudad del Estado Carabobo
[<Contactos- nombre: "Ernesto Nadir Crespo Avila", telefono: "04205873118", grupo: "<Grupos "Guacara" (Ciudad del Estado Carabobo)>">]
--------------------
Valencia
Capital del Estado Carabobo
[<Contactos- nombre: "Jhon Doe", telefono: "04295333131", grupo: "<Grupos "Valencia" (Capital del Estado Carabobo)>">]
--------------------
Barquisimeto
Capital del Estado Lara
[<Contactos- nombre: "Maria Perez", telefono: "04194445445", grupo: "<Grupos "Barquisimeto" (Capital del Estado Lara)>">]
--------------------
Caracas
Distrito Capital
[<Contactos- nombre: "Jane Doe", telefono: "04399991919", grupo: "<Grupos "Caracas" (Distrito Capital)>">,  
<Contactos- nombre: "Pedro Perez", telefono: "04596661617", grupo: "<Grupos "Caracas" (Distrito Capital)>">]
--------------------
Maracaibo
Capital del Estado Zulia
[]
--------------------
Merida
Capital del Estado Merida
[]
--------------------
Barcelona
Capital de Anzoategui
[]
--------------------
Puerto Ordaz
Ciudad del Estado Bolivar
[]
--------------------
Barinas
Capital del Estado Barinas
[]
--------------------
Maracay
Capital del Estado Aragua
[]
--------------------
Los Teques
Capital del Estado Miranda
[]
*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Maria Perez , 04194445445 :(<Grupos "Barquisimeto" (Capital del Estado Lara)>)
Contactos, luego de eliminar a Maria Perez
--------------------
Ernesto Nadir Crespo Avila
04205873118
<Grupos "Guacara" (Ciudad del Estado Carabobo)>
--------------------
Jhon Doe
04295333131
<Grupos "Valencia" (Capital del Estado Carabobo)>
--------------------
Jane Doe
04399991919
<Grupos "Caracas" (Distrito Capital)>
--------------------
Pedro Perez
04596661617
<Grupos "Caracas" (Distrito Capital)>
```

Las herramientas `sqlalchemy` y `Elixir` facilitan el trabajo de abstraer el motor de base de datos y la creación de las tablas con sus respectivos campos en dichas base de datos.  De está forma se puede crear aplicaciones donde se puede facilitar el uso de varios motores de base de datos realizando cambios mínimos en la aplicación.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
