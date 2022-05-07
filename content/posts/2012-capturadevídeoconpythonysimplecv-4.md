Title: Captura de vídeo con Python y SimpleCV. Parte 4. 
Date: 2012-07-31 9:00 
Category: Tutorial Python
Tags: Camara,Canaima,Debian,General,Gnome,Linux,Python,Ubuntu, Videos,SimpleCV
lang: es
translation: true

En este artículo se muestra como generar un vídeo usando la webcam del computador con python y `SimpleCV`.

El script simplemente define la captura de vídeo, genera un ciclo donde se captura el vídeo y se muestra en pantalla. Cuando se presiona la tecla espaciadora se hace una captura de una imagen y se salva, al presionar la tecla Escape se finaliza el ciclo de captura de vídeo.

El código se muestra a continuación:
```python
#!/usr/bin/env python

#Se importa cv2.

import cv2

# se crea la instancia de la captura de Video.

video = cv2.VideoCapture(0)

#Se define un ciclo.

while True:

    #Se captura el video de la webcam

    ret,im = video.read()

    #Se muestra el video  donde se pasa im que es la lectura del video de la webcam.

    cv2.imshow('Prueba de video',im)

    #Se captura la tecla de escape del teclado

    tecla = cv2.waitKey(10)

    if tecla == 27:

        #Si es la tecla escape se termina el ciclo

        break

    #Si la tecla es el espacio en blanco se captura una imagen del video.

    if tecla == ord(' '):

        cv2.imwrite('captura_img.jpg',im)

```

A continuación se muestra el vídeo:

https://youtu.be/XF9BjxYKiEo

En la siguiente imagen se muestra la captura de la foto al grabar el vídeo:

![](./images/capturadevideoconpythonysimplecv4-1.jpg) 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)