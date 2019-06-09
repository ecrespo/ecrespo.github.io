Title: Captura de imágen desde la webcam con el framework SimpleCV. Parte 1.
Date: 2012-07-08 9:00
Category: 
Tags: Canaima,Debian,Linux,Python,Ubuntu,SimpleCV
lang: es
translation: true

`SimpleCV` es una framework para la construcción de aplicaciones de Visión por el computador "Computer Vision", es un conjunto de librerias que permiten capturar imágenes por medio de camaras (webcam) o camaras IP para obtener información a partir de dichas imágenes.

La página del proyecto SimpleCV se puede visitar desde este [enlace](http://www.simplecv.org/).

Para instalar `SimpleCV` se usará las herramientas de instalación de python `easy_install` o `pip`.
```
pip install simplecv
```
El ejemplo que se desarrollará es una simple aplicación que capture la imágen de la webcam, la presente en pantalla por unos segundos y la salve en un archivo con formato png.

El código es el siguiente:
```python
#!/usr/bin/env python

#Importar los modulos Camera, Display e Image.

from SimpleCV import Camera, Display, Image

#Se importa sleep para darle unos segundos a la 

#aplicacion a que muestra la captura en pantalla.

from time import sleep

#Se crea una instancia de Camera.

#Se inicializa la camara

camara = Camera()

#Se crea una instancia de Display

#se inicializa display

pantalla = Display()

#Se captura una imagen usando la camara

imagen = camara.getImage()

#Muestra la imagen en pantalla

imagen.save(pantalla)

#Se salva la imagen en un archivo

imagen.save("captura.png")

sleep(2)
```
Al ejecutar el programa se muestra una pantalla con la captura que hace la webcam y la guarda en un archivo.  

A continuación se muestra la imágen capturada:  

![](./images/capturadeimagendesdelawebcamconelframeworksimplecv1-1.png) 


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)