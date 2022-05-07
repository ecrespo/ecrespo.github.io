Title: Instalar un servidor mongodb en Debian  
Date: 2014-09-13 9:00  
Category: Linux,Desarrollo  
Tags: Canaima,Debian,General,Linux,Ubuntu,mongodb
lang: es  
translation: true  

`Mongodb` es una base de datos no relacional (nosql) que se está usando mucho en este momento y es software libre.

Para instalar el servidor y el cliente en Debian se ejecuta:
```
apt-get install mongodb mongodb-clients mongodb-server
```
Configuración de `mongodb`.
La configuración del servidor `mongodb` se encuentra en `/etc/mongodb.conf`:
```
# donde se almacena los datos
dbpath=/var/lib/mongodb
#El log se guarda en el archivo:
logpath=/var/log/mongodb/mongodb.log
#Se define agregar info al log.
logappend=true
#Se define la ip y el puerto donde escuchará mongodb
bind_ip = 127.0.0.1
port = 27017
# Se habilita el journaling, http://www.mongodb.org/display/DOCS/Journaling
journal=true
# Se habilita o deshabilita la autenticación, por defecto está deshabilitado
#noauth = true
#auth = true
```
Iniciar el servicio (como me encuentro usando systemd se usa el comando systemctl):
Iniciar el servicio:
```
systemctl start mongodb.service
```
Estatus del servicio:
```
systemctl status mongodb.service 
mongodb.service - An object/document-oriented database
   Loaded: loaded (/lib/systemd/system/mongodb.service; disabled)
   Active: active (running) since sáb 2014-09-13 21:08:10 VET; 2s ago
     Docs: man:mongod(1)
 Main PID: 5542 (mongod)
   CGroup: /system.slice/mongodb.service
           └─5542 /usr/bin/mongod --config /etc/mongodb.conf

sep 13 21:08:10 grievous systemd[1]: Starting An object/document-oriented database...
sep 13 21:08:10 grievous systemd[1]: Started An object/document-oriented database.
sep 13 21:08:10 grievous mongod[5542]: all output going to: /var/log/mongodb/mongodb.log
```

Revisar que el proceso esté arriba:
```
ps aux | grep mongo
mongodb   5542  0.4  0.9 385176 38512 ?        Ssl  21:08   0:01 /usr/bin/mongod --config /etc/mongodb.conf
```
Revisar que los puertos estén abiertos:
```
netstat -anp  | grep mongo
tcp        0      0 127.0.0.1:27017         0.0.0.0:*               LISTEN      5542/mongod     
tcp        0      0 127.0.0.1:28017         0.0.0.0:*               LISTEN      5542/mongod     
unix  2      [ ACC ]     STREAM     LISTENING     138512   5542/mongod         /tmp/mongodb-27017.soc
``` 
Conectarse al servidor mongodb:
```
#mongo
MongoDB shell version: 2.4.10
connecting to: test
>
```
Seleccionar una base de datos:
```
> db
test
```
Muestra la lista de nombres de la base de datos:
``` 
> show dbs 
local 0.078125GB
```
Cambiarse a una nueva base de datos pruebas:
``` 
> use pruebas
switched to db pruebas
```
Confirmar que la sesión se cambio a la base de datos pruebas:
```
> db
pruebas
```
Mostrar la ayuda de mongo:
```
> help
 db.help()                    help on db methods
 db.mycoll.help()             help on collection methods
 sh.help()                    sharding helpers
 rs.help()                    replica set helpers
 help admin                   administrative help
 help connect                 connecting to a db help
 help keys                    key shortcuts
 help misc                    misc things to know
 help mr                      mapreduce

 show dbs                     show database names
 show collections             show collections in current database
 show users                   show users in current database
 show profile                 show most recent system.profile entries with time >= 1ms
 show logs                    show the accessible logger names
 show log [name]              prints out the last segment of log in memory, 'global' is default
 use <db_name>                set current database
 db.foo.find()                list objects in collection foo
 db.foo.find( { a : 1 } )     list objects in foo where a == 1
 it                           result of the last line evaluated; use to further iterate
 DBQuery.shellBatchSize = x   set default number of items to display on shell
 exit                         quit the mongo shell
```
Crear 2 documentos j y k usando la sintaxis de javascript: 
```
> j = {name: 'mongo'}
{ "name" : "mongo" }
> k = {x:3}
{ "x" : 3 }
```
Insertar los documentos j y k en la colección testData:
```
> db.testData.insert( j )
> db.testData.insert( k )
```
Confirmar que la colección testData existe:
```
> show collections
system.indexes
testData
```
Confirmar que los documentos existen en la colección testData:
```
> db.testData.find()
{ "_id" : ObjectId("5414fdec21061053051d13e8"), "name" : "mongo" }
{ "_id" : ObjectId("5414fdf721061053051d13e9"), "x" : 3 }

Imprimir el json de j y k:
> printjson(j)
{ "name" : "mongo" }
> printjson(k)
{ "x" : 3 }
```

En próximo artículo explicaré como trabajar con mongo desde python.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)