Title: Utilizando mongodb por medio de python.   
Date: 2014-09-21 9:00  
Category: Tutorial Python  
Tags: Canaima,Debian,Linux,Python,Ubuntu,mongodb 
lang: es  
translation: true

En artículo [anterior](https://www.seraph.to/instalar-un-servidor-mongodb-en-debian.html#instalar-un-servidor-mongodb-en-debian) explique como iniciar un servidor `mongodb` y unos ejemplos de uso.

Ahora explicaré el uso de `mongodb` por medio de python con `pymongo`.

Para instalar `pymongo` se tienen dos vías, una a lo distribuciones basadas en Debian:
Para Python 2:
```
apt-get install python-pymongo python-pymongo-doc python-pymongo-ext
```
Para Python 3:
```
apt-get install python3-pymongo python3-pymongo-ext
```
O con `pip`:
```
pip install pymongo
```
La idea es mostrar como se conecta python a `mongodb`, como se crea la base de datos, como se insertan documentos, se listan y se borran.

A continuación el código del script:

```python
#!/usr/bin/env python3


# -*- coding: utf-8 -*-

from pymongo import Connection

#conexion a mongodb

con = Connection('localhost')

#Listas las base de datos

print(con.database_names())

#Conectarse a la base de datos pruebas.

db = con.pruebasdb

#Se crea una coleccion que se llama estados

estados = db.estados

#Lista de estados.

listaestados = [{'nombre': 'Carabobo', 'region':'centro','ciudades': 10},


    {'nombre': 'Lara', 'region':'centro occidente','ciudades': 8},


    {'nombre':'Merida','region':'andes','ciudades':6},


    {'nombre':'Aragua','region':'centro','ciudades':13}]

#Insertar los datos en el documento


for lista in listaestados:


    estados.insert(lista)

#Se lista un simple documento


print("Se lista un simple documento")


print("---------------------------")


print(estados.find_one({'nombre':'Carabobo'}))


#Se remueve el documento del estado Carabobo


estados.remove({"nombre" : "Carabobo"})


print("Se lista todos los documentos")


print("-----------------------------")


#Listar los datos


for i in estados.find():


    print(i)

#

print("Se cuenta la cantidad de documentos")


print("-----------------------------------")


print(estados.count())


#Borrar todos los datos


estados.drop()


con.close()


```

El resultado de la ejecución se muestra a continuación:
```
['otradb', 'pruebas', 'pruebasdb', 'nuevadb', 'local']

Se lista un simple documento

---------------------------

{'_id': ObjectId('541f0ce123d1e1604504e0e6'), 'region': 'centro', 'nombre': 'Carabobo', 'ciudades': 10}

Se lista todos los documentos

-----------------------------

{'_id': ObjectId('541f0ce123d1e1604504e0e7'), 'region': 'centro occidente', 'nombre': 'Lara', 'ciudades': 8}

{'_id': ObjectId('541f0ce123d1e1604504e0e8'), 'region': 'andes', 'nombre': 'Merida', 'ciudades': 6}

{'_id': ObjectId('541f0ce123d1e1604504e0e9'), 'region': 'centro', 'nombre': 'Aragua', 'ciudades': 13}

Se cuenta la cantidad de documentos

-----------------------------------

3

```


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)