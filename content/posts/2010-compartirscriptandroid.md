Title: Compartir scripts para android
Date: 2010-07-03 10:00
Category: Tutorial Android
Tags: Android, Python
lang: es
translation: true

En este artículo se explicará el proceso de compartir archivos para Android, la guía en inglés se encuentra en el sitio de [ASE](http://code.google.com/p/android-scripting/wiki/SharingScripts). 

El proceso se basa en la generación de un código de barras QR. Se tiene el enlace del proyecto ZXing que permite generar los códigos de barra desde internet, el enlace para generar el código lo tienen [aquí](http://zxing.appspot.com/generator/).

El proceso para compartir scripts de python, perl, tcl, bash,ruby o lua es el siguiente:
Generar Código de Barras QR: 

1. Entre al generador de código en línea del proyecto ZXing.
2. Seleccione text en el contenido
3. En el campo de texto agregue en la primera línea el nombre del script por ejemplo prueba.py
4. En las siguientes líneas coloque el código del programa
5. Seleccione el tamaño del código de barras a L
6. Dele clip a generar
7. Comparta la imagen del código de barras o incruste el enlace generado

Bajar el script al celular:

1. Ejecute ASE y vuelva a la lista de scripts
2. Presione el botón Menú
3. Seleccione agregar (add)
4. Seleccione escanear código de barras (scan barcode)
5. Escanee el código generado anteriormente y se agregará el script a la lista de scripts


Hay que tomar en cuenta que los scripts tienen que ser pequeños ya que QR sólo soporta 4.296 caracteres.

A continuación agrego los códigos QR de los scripts explicados en los artículos anteriores:

* Enviar mensajes de texto desde Android con python

![chart1](./images/chart1.png)

* Envío de correos desde Android con python.

![Correo](./images/chart_correo.png)

* Lector de código de barras hecho en python.

![Código de Barras](./images/codigobarras.png)

* Escaneado de redes inalámbricas con python desde Android. 

![Scan wifi](./images/scan_wifi.png)

Ya en los siguientes artículos sobre scripts para Android se colocarán los Códigos QR para facilitar el uso de los scripts.



===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)