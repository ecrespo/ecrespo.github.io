Title: Modificar imagen con simpleCV(binarización). Parte 3.
Date: 2012-07-30 9:00 
Category: Tutorial Python
Tags: Camara,Canaima,Debian,General,gnome,Linux,Python,Ubuntu,SimpleCV
lang: es
translation: true



Este artículo se explicará como convertir una imagen a dos colores, osea tomar una foto normal y convertirla en blanco y negro.

Se usará la función binarized, se puede pasar un valor entre 0 y 255 (donde cero es negro y 255 es blanco).

Se toma la imagen y luego se pasa la función a la imagen.

A continuación se muestra la imagen original:

![](./images/modificarimagenconsimplecvbinarizacion-1.png) 

El código se muestra a continuación:  

```python
#!/usr/bin/env python

#Se importa Image de SimpleCV

from SimpleCV import Image

#Se crea la instancia Imagen tomando la imagen

#imagen1.png

imagen = Image('imagen1.png')

#Se ejecuta binarize a la imagen

#sin argumentos.

imgBin = imagen.binarize()

#Se salva la imagen como resultado3.jpg

imgBin.save("resultado.jpg")
```

La imagen generada se muestra a continuación:

![](./images/modificarimagenconsimplecvbinarizacion-2.jpg) 


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)