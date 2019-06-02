Title: Sqlite con python
Date: 2012-04-04 09:00
Category: Tutorial de Python 
Tags:  General,Python
lang: es
translation: true

El programa `pysms-send` tendrá algunas mejoras, entre ellas manejará libreta de contactos.

Para ello se probará con `sqlite3` o con `mongoDB`. Para esté artículo se trabajará con `sqlite3`. Se crearán 2 tablas, una de contactos y otra de grupos. La de contactos tiene los campos de id, nombre del contacto, telefono y grupo. La tabla grupo tendrá los campos id, nombre del grupo y descripción del grupo.

En la tabla contactos el campo grupo es una referencia al id de la tabla grupo de esa forma cada contacto está relacionado a un grupo.


El archivo `contactos.sql` contiene lo siguiente:  
```
create table contactos (
id integer primary key,
nombre text not null,
grupo integer references grupos(id)
on delete restrict
deferrable initially deferred,
telefono text not null default 'Desconocido',
unique (nombre,telefono));

create table grupos (
id integer primary key,
nombre text not null,  
descripcion text not null CHECK(descripcion !=''),
unique (nombre)); 
```

En la tabla `contactos` se tiene el campo id que es entero y clave primaria, luego el campo nombre es no nulo, el campo grupo hace referencia a la tabla grupos al campo id, el campo telefono es un texto no nulo con valor por defecto desconocido, los valores únicos son el nombre y el teléfono, con eso se evita que existan números de teléfonos repetidos.

En la tabla `grupos` tiene el campo id es un entero y es clave primaria, el campo nombre es texto no nulo, el campo descripción es no nulo y se verifica que no sea un string vacio, el campo único es el nombre.

Para generar la base de datos se ejecuta la siguiente instrucción:  

```
sqlite3 sms.db < sms.sql
```

De está manera se crea la base de datos `sqlite` en el archivo `sms.db`.

Si se desea interactuar con la base de datos se ejecuta `sqlite3` con el nombre de la base de datos, se abrirá un interprete:
```
ecrespo@jewel:~/bin/python$ sqlite3 sms.db 
SQLite version 3.7.11 2012-03-20 11:35:50
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

A continuación se agrega un grupo a la tabla `grupos`:  

```
sqlite> insert into grupos (nombre,descripcion) values ('Guacara','Ciudad del Estado Carabobo');
```

Ahora se agrega un contacto a la tabla `contactos`:  

```
insert into contactos (nombre,grupo,telefono) values ('Ernesto Crespo',1,'04315633119');
```


Se consulta a la tabla `grupos` y luego a la tabla `contactos`:  
```
sqlite> select * from grupos;
1|Guacara|Ciudad del Estado Carabobo
sqlite> select * from contactos ;
1|Ernesto Crespo|1|04315633119
```

Para eliminar el `contacto` se ejecuta:  

```
sqlite> delete from contactos where id=1;
```

Se uso el id para eliminar el contacto.

A continuación  se crearán una serie de scripts en python que permitirán insertar datos a la base de datos, consultar datos y eliminarlos (las acciones básicas en una base de datos).
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Se importa el modulo sqlite3
import sqlite3

#Se crea la funcion main
def main():
#Se establece la instancia connect a la base de datos sms.db
con = sqlite3.connect("sms.db")
#Se crea el cursor que permite la ejecucion de instrucciones sql
cur = con.cursor()

#Se crea una lista con tuplas como sus elementos.
#Las tuplas contienen los datos a insertar en la tabla grupos.
datos =[('valencia' ,'Capital Estado Carabobo'),
('Maracay','Capital Estado Aragua'),
('Barquisimeto','Capital del Estado Lara'),]
#Se recorre la lista
for t in datos:
cur.execute('insert into grupos (nombre,descripcion) values (?,?)',t)
#Se realiza la transaccion.
con.commit()

#Ahora se lista los datos de la tabla grupos
cur.execute('select * from grupos')
#Se captura uno
fila = cur.fetchone()
#Se recorre cada fila
while fila:
#Se muestra los elementos nombre y descripcion.
print fila[1],fila[2]
#Se pasa a la siguiente fila
fila = cur.fetchone()

#Se cierra el cursor
cur.close()
#Se cierra la conexion.
con.close()

#Se sale de la funcion .
return 0

if __name__ == '__main__':
main()
```
    
Al ejecutar el script devuelve la lista de `grupos` con su descripción:
```
ecrespo@jewel:~/bin/python$ python grupos-sms.py 
Guacara Ciudad del Estado Carabobo
valencia Capital Estado Carabobo
Maracay Capital Estado Aragua
Barquisimeto Capital del Estado Lara
```

##  ##
===
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:


![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
    
