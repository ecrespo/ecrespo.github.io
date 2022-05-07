Title: Instalar python en Android
Date: 2010-06-06 13:00
Category: Tutorial Python
Tags: Linux, Android, Debian, Python
lang: es
translation: true



Este artículo explicará como instalar python en Android desde el emulador para poder mostrar las capturas de pantalla y ese procedimiento es el mismo para instalar python desde el celular.

Lo primero que se necesita hacer es iniciar el emulador como se explico en el artículo de [instalación del SDK de Android](https://www.seraph.to/instalacion-del-sdk-de-android-en-linux.html#instalacion-del-sdk-de-android-en-linux).


Al ejecutar adb devices encontrarán un dispositivo virtual funcionando.


```
ernesto@zvezda:~/android-sdk-linux_86/tools$ ./adb devices List of devices attached emulator-5554 device
```


Luego se baja el programa ASE desde el [siguiente enlace](http://code.google.com/p/android-scripting/downloads/detail?name=ase_r24.apk).

```
ernesto@zvezda:~/android-sdk-linux_86/tools$ ./adb install ../../Descargas/ase_r22.apk 868 KB/s (217639 bytes in 0.244s) pkg: /data/local/tmp/ase_r22.apk Success
```

Esto indica que se instalo sin problemas el programa ASE.


En la siguiente figura se muestra el home del emulador con ASE instalado.


![Python en Android 1](./images/pythonandroid1.png)

Al darle clip al icono de ASE aparece la una información donde nos pide que se agreguen scripts o interpretes presionando el botón menú como lo muestra la siguiente figura:

![Python en Android 2](./images/pythonandroid2.png)


Al darle menú aparecen varias opciones como lo son: Agregar, Ver, Preferencias, Ayuda, Actualizar. Siguiente figura:

![Python en Android 3](./images/pythonandroid3.png)

Al darle View o Ver aparecerá un menú donde se tiene varias opciones para visualizar, en este caso se quiere visualizar interpretes. Siguiente figura:

![Python en Android 4](./images/pythonandroid4.png)

Al darle clip a Interpretes aparecerá sólo como interprete Shell y las opciones Agregar, Iniciar servidor, Preferencias y Ayuda. En este caso se va a agregar un interprete nuevo.

![Python en Android 5](./images/pythonandroid5.png)

Al darle clip a agregar aparecerá una lista de interpretes que en este caso se instalará python. Siguiente figura:

![Python en Android 6](./images/pythonandroid6.png)

Al seleccionar Python 2.6.2 se inicia el proceso de instalación del interprete y de algunos scripts como lo muestran las 2 siguientes figuras:

![Python en Android 7](./images/pythonandroid7.png)


![Python en Android 8](./images/pythonandroid8.png)

Ahora aparece Python aparte de Shell en la lista de interpretadores como lo muestra la siguiente figura:

![Python en Android 9](./images/pythonandroid9.png)

Para probar que todo está funcionando se selecciona el interpretador y este se ejecutará como lo muestra la figura:

![Python en Android 10](./images/pythonandroid10.png)

Por último se lista los scripts en python de ejemplo para trabajar con Android:

![Python en Android 11](./images/pythonandroid11.png)


En siguientes artículos se explicará el uso de los scripts para ir creando una aplicación para Android.


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)