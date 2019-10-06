Title: Habilitar autenticación en un servidor mongodb
Date: 2015-05-08 9:00
Category: Tutorial Linux
Tags: Canaima,Debian,General,Linux,Ubuntu,Mongodb
lang: es
translation: true

En el artículo sobre la instalación de un [servidor mongodb](https://www.seraph.to/instalar-un-servidor-mongodb-en-debian.html#instalar-un-servidor-mongodb-en-debian) faltó definir la autentcación de usuarios que puedan conectarse a dicho servidor.

En este caso se habilitará dicha autenticación para el acceso al servidor.

Lo primero es deshabilitar la autenticación en el archivo `/etc/mongodb.conf`:
```
# Turn on/off security.  Off is currently the default
#noauth = true
#auth = true
```
Se inicia el servicio de `mongodb`:
```
 systemctl start  mongodb.service
```
Se revisa si levanto:
```
systemctl status  mongodb.service
● mongodb.service - An object/document-oriented database
   Loaded: loaded (/lib/systemd/system/mongodb.service; enabled)
   Active: active (running) since vie 2015-05-08 11:44:26 VET; 5s ago
     Docs: man:mongod(1)
 Main PID: 3405 (mongod)
   CGroup: /system.slice/mongodb.service
           └─3405 /usr/bin/mongod --config /etc/mongodb.conf

may 08 11:44:26 grievous mongod[3405]: all output going to: /var/log/mongodb/mongodb.log
```
Se accede al shell de `mongodb`:
```
mongo
MongoDB shell version: 2.4.10
connecting to: test
>
```

Se cambia a la base de datos `admin`:
```
> use admin
switched to db admin
```
Se crea el usuario admin con clave 123456 (sólo de manera didactica) y rol lectura y escritura dbAdmin.

```
> db.addUser("admin","123")
{
 "user" : "admin",
 "readOnly" : false,
 "pwd" : "9f3121efccbe3fef09a799d5e63077c2",
 "_id" : ObjectId("554cf1405cf1b965e6f5c10f")
}
```

Se sale de la base de datos:
```
> exit
bye
```

Ahora se edita el archivo `/etc/mongodb.conf`  para habilitar la autenticación:
```
# Turn on/off security.  Off is currently the default
#noauth = true
auth = true
```
Se reinicia `mongodb`:
```
systemctl stop  mongodb.service
systemctl stop  mongodb.service
systemctl status   mongodb.service
● mongodb.service - An object/document-oriented database
   Loaded: loaded (/lib/systemd/system/mongodb.service; enabled)
   Active: active (running) since vie 2015-05-08 11:58:44 VET; 4s ago
     Docs: man:mongod(1)
 Main PID: 4188 (mongod)
   CGroup: /system.slice/mongodb.service
           └─4188 /usr/bin/mongod --config /etc/mongodb.conf

may 08 11:58:44 grievous mongod[4188]: all output going to: /var/log/mongodb/mongodb.log
```
Se ejecuta el shell de `mongodb` y se intentan visualizar las bases de datos:
```
> show dbs
Fri May  8 12:06:19.122 listDatabases failed:{ "ok" : 0, "errmsg" : "unauthorized" } at src/mongo/shell/mongo.js:46
```
Se nota que no se tiene autorización para ver la lista de bases de datos.

Para ingresar y autenticar al usuario se hace lo siguiente:
```
> use admin
switched to db admin
> db.auth("admin", "123")
1
```
Listar bases de datos:
```
> show dbs
admin 0.203125GB
local 0.078125GB
personasdb 0.203125GB
```
Listar usuarios:  
```
> db.system.users.find()
{ "_id" : ObjectId("554ce337c597c2dbd0089d74"), "user" : "admin", "pwd" : "95ec4261124ba5951720b199908d892b", "roles" : [  "readWrite",  "dbAdmin" ] }  
```


Para más información se tienen los siguientes enlaces:

1. [https://dezkareid.wordpress.com/2013/07/29/control-de-usuarios-en-mongodb/](http://blog.crespo.org.ve/2014/09/instalar-un-servidor-mongodb-en-debian.html)
2. [https://carlosazaustre.es/blog/como-conectarte-remotamente-a-tu-base-de-datos-mongodb/](https://carlosazaustre.es/blog/como-conectarte-remotamente-a-tu-base-de-datos-mongodb/)
3. [http://docs.mongodb.org/v2.4/tutorial/add-user-to-database/](http://docs.mongodb.org/v2.4/tutorial/add-user-to-database/)
4. [http://juanvicenteherrera.es/2011/12/20/mongodb-conceptos-de-seguridad/](http://juanvicenteherrera.es/2011/12/20/mongodb-conceptos-de-seguridad/)
5. [https://alexanderae.com/mongodb-autenticacion-autorizacion.html](https://alexanderae.com/mongodb-autenticacion-autorizacion.html)



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
