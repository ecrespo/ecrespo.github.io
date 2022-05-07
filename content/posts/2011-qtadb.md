Title: Qtadb programa para controlar un celular Android desde el PC
Date: 2011-06-19 09:00
Category: Aplicación Android
Tags: Linux,Qtadb,Android,Debian,
lang: es
translation: true

En la página de elandroidlibre.com publicaron un artículo donde hablan del programa QtADB el cual permite manejar el sistema de archivos del celular, ver la lista de paquetes instalado, realizar capturas de pantalla, ejecutar la consola del celular, recovery y otras opciones. El enlace de el androidelibre.com lo tienen [acá](http://www.elandroidelibre.com/2011/05/android-commander-y-qtadb-los-2-mejores-programas-para-controlar-android-desde-el-pc.html).

Es necesario tener instalado el SDK de Android, este se puede bajar en este [enlace](http://developer.android.com/sdk/index.html).

Es necesario instalar el paquete [apk](http://www.mediafire.com/file/ck36odjkkqgr4an/qtadb.apk) (qtadb.apk) en el celular y bajar el paquete QtADB para Linux en este caso para 32 bits lo pueden bajar en este [enlace](http://www.mediafire.com/file/q3fqe9hutvfugdh/QtADB_0.8.0_linux32.tar.gz).

La página de qtadb se encuentra en el siguiente [enlace](http://qtadb.wordpress.com/).


El procedimiento para instalar el SDK de Android en Linux lo pueden seguir [acá](https://www.seraph.to/instalacion-del-sdk-de-android-en-linux.html).

Al tener instalado el SDK de Android en Linux se conecta el celular y se inicia el servicio de adb:

```
ernesto@jewel:~/bin$ adb devices 
* daemon not running. starting it now on port 5037 *
* daemon started successfully *
List of devices attached 
0403725B09015010 device
```

Pero para lograr esto es necesario habilitar el celular con conexión USB como Portal y Herramientas, la siguiente figura muestra la opción:

![Qtadb 1](./images/qtadb1.png)

Para instalar el paquete apk en el celular se ejecuta el comando adb para la instalación de paquetes como se muestra:

```
ernesto@jewel:~/bin$adb install qtadb.apk 
44 KB/s (24316 bytes in 0.531s)
 pkg: /data/local/tmp/qtadb.apk
Success
```

En la siguiente figura se muestra el programa instalado en el celular:

![Qtadb 2](./images/qtadb2.png)

Al darle clip a QtADB se mostrará 2 botones uno para iniciar el servicio y otro para detenerlo como lo muestra la siguiente figura:

![Qtadb 3](./images/qtadb3.png)

Se inicia el servicio y lo que queda es iniciar el QtADB para Linux.

Al iniciar la aplicación lo primero que se muestra es el administrador de archivos como lo muestra la siguiente figura:

![Qtadb 4](./images/qtadb4.png)

Se puede listar las aplicaciones instaladas en el celular, actualizar aplicaciones, desintalarlas y realizar respaldos de las mismas.

![Qtadb 5](./images/qtadb5.png)

Se puede ver información del celular como el operador de telefonía celular, modelo, número de serie, ROM y el espacio de las particiones.

![Qtadb 6](./images/qtadb6.png)

Se pueden realizar capturas de pantalla en el celular.

![Qtadb 7](./images/qtadb7.png)

Se puede ejecutar un shell del celular:

![Qtadb 8](./images/qtadb8.png)

Se puede visualizar los logs del celular:

![Qtadb 9](./images/qtadb9.png)


Por último también se puede visualizar los mensajes de texto:
Para que funcione revisar los mensajes es necesario activar y conectar el celular a la red wifi y en la aplicación activar wifi también.

![Qtadb 10](./images/qtadb10.png)


En la siguiente figura se muestra los mensajes de texto almacenados en el celular:

![Qtadb 11](./images/qtadb11.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
