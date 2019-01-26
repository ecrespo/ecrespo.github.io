Title: Creación de Código QR desde Python
Date: 2011-07-20 09:00
Category: Tutorial de Python y PyQt
Tags: Código QR, Python, PyQt
lang: es
translation: true

En los artículos que he escrito sobre script en python para Android siempre he dejado una imagen que contiene una especie de código de barras pero en 2 dimensiones, este código se llama Código QR (Quick Response Barcode), más información sobre esté código lo pueden leer en [wikipedia](http://es.wikipedia.org/wiki/Codigo_QR).

En el artículo de como compartir script en Android hay un [enlace](https://www.seraph.to/compartir-scripts-para-android.html) de una página que permite generar el código QR a partir de una información dada.

La idea es crear el código desde Linux y el programa que permite hacerlo se llama qrencode.

Para instalarlo en Debian simplemente se ejecuta aptitude:

```
aptitude install qrencode
```

El comando para generar un archivo con la imagen del código QR se muestra a continuación:

```
qrencode -o output.png 'Hola mundo!'
```

Este ejemplo genera un archivo png llamado output con el código QR de "Hola Mundo!"

También existe un módulo para python que permite generar código directamente, este paquete en Debian se llama python-qrencode, para instalarlo se ejecuta aptitude:

```
aptitude install python-qrencode

```

La página del proyecto python-qrencode se encuentra en github en este [enlace](https://github.com/Arachnid/pyqrencode). 

De este módulo se usará la función encode, se le pasa un string como dato y devuelve una tupla con 3 valores, la versión, tamaño de la imagen y la imagen.

Está imagen es un objeto de Imagen, se puede salvar dicha imagen en un archivo.

El código de ejemplo del uso de python-qrencode se muestra a continuación:

```python 
#!/usr/bin/env python


#modulo qrencode
from qrencode import encode

#El texto a convertir en codigo QR
texto = """Esta es uan prueba de generacion de codigo QR\n
desde python usando el modulo qrencode."""

#Se crea el codigo QR del texto,la funcion encode 
#genera una tupla donde el ultimo elemento es un
#objeto Imagen.

imagen = encode(texto)[2]

#Se salva la imagen en el archivo
#archivoprueba.png
imagen.save("/home/ernesto/archivoprueba.png")
```






===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
