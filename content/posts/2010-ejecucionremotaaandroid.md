Title: Ejecución remota de scripts python desde Linux a un celular con Android
Date: 2010-10-23 10:00
Category: Tutorial de Python en Android
Tags: Android, Python, Debian, Linux
lang: es
translation: true

Existe la forma  de ejecutar scripts así sea de python,perl, ruby, bash,etc de forma remota (desde Linux) a un celular con Android.

Al instalar SL4A y python se tiene la posibilidad de iniciar un servicio de SL4A para escuchar en un puerto específico del celular Android, se tiene la opción pública o privada, para el primer caso se tiene que tener conectado el celular a una red wifi donde levanta el servicio en un puerto específico, para el caso de conexión privada el celular debe estar conectado vía puerto USB con la opción de depuración USB conectada y el celular en modo Portal y Herramientas.

Este post se basa en el artículo de control remoto de SL4A que se encuentra [aquí](http://code.google.com/p/android-scripting/wiki/RemoteControl) .

En este momento explicaré la conexión remota pública, primero se tiene que conectar el celular a una red wifi.

En el equipo que estoy utilizando le asigno la IP 192.168.10.19.

Luego ejecutar SL4A en el celular, luego se le da menú, se selecciona ver, luego a interpretes, luego otra vez al menú, se selecciona iniciar servidor, en este momento se le pide seleccionar entre servidor público o privado, se selecciona al primero.

El celular coloca un mensaje en el área de notificación de Android mencionando que el servidor se ha iniciado, se despliega la información y este dice se arranco un servidor SL4A en la IP 192.168.10.19 con puerto 52834.

A continuación se utilizará el sdk de android en Linux ejecutando adb.
Se inicia el servidor adb.

```
./adb start-server
* daemon not running. starting it now on port 5037 *
* daemon started successfully *
```

Note que el servidor levanta en el puerto 5037.


Ahora se redirecciona los puertos del servicio adb.

```
./adb forward tcp:9999 tcp:52834

```

Donde el puerto 9999 se redirecciona al puerto donde escucha el celular que es el 52834 en este caso.

A continuación se configura la variable de ambiente de la IP y puerto del celular con Android que tiene funcionan el servidor SL4A.

```
export AP_PORT=52834
export AP_HOST=192.168.10.19
```

Asegurarse que tiene en el path de python2.6 la ruta del módulo de python para android. Este lo puede bajar en este [enlace](http://android-scripting.googlecode.com/hg/python/ase/android.py).

A continuación se muestra un script en python que pide escriba el nombre de usuario en el celular y lo muestra en Linux y en el celular:

```python
#Importar módulo android
import android
#Se crea el objeto droid de la clase Android con la IP y puerto del servicio iniciado en el celular.
droid = android.Android(('192.168.10.19', 52834))
#Se solicita al usuario que escriba su nombre
texto = droid.getInput("Escriba su nombre","Nombre:")
#Se imprime el nombre del usuario en la consola de Linux
print "El nombre escrito en el celular es: %s" %texto[1]
#Se presenta un saludo al usuario en el celular
droid.makeToast('Hola %s' %texto[1])
```

Para ejecutar el programa se coloca el script prueba-remota.py donde se encuentra el módulo de SL4A android.py en el mismo directorio o se coloca en el path de python2.6.
Se ejecuta con python2.6:

```
$ python2.6 prueba-remota.py 

```

El nombre escrito en el celular es: ernesto


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)