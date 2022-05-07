Title: Capturar la ubicación del celular (Android) desde Linux.
Date: 2010-12-21 10:00
Category: Tutorial Python en Android
Tags: Android, Linux, Python, SMS
lang: es
translation: true

Me tome unos días para realizar la actualización de mi Milestone a Froyo gracias a la gente de androive que liberaron una versión venezolanizada de froyo que se llama [FroyoVE](http://androidve.blogspot.com/2010/12/navidad-antes-del-24-froyove-152-la.html).

Hoy escribire sobre como sacar la información que maneja el GPS desde Linux.

Lo primero que se necesita hacer es iniciar la localización, se captura la información y luego se detiene la localización.

A continuación el código del programa:



```python
#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
#Script que permite capturar la localización GPS del celular (ANDROID) desde Linux.
#Autor: Ernesto Crespo
#Correo:ecrespo@gmail.com
#Licencia: GPLv3
#Versión:0.1


#Importando el módulo android
import android
from time import sleep




#Función de envio de mensajes
def localizacion():
    #Se crea la instancia de la clase Android
    droid = android.Android()
    #Se inicia la localizacion
    droid.startLocating()
    #Se espera 15 segunfos
    sleep(15)
    #Se presenta en la consola la información de la localización
    #Se maneja la información de un diccionario.
    print "Altitud: ",droid.readLocation().result["network"]["altitude"]
    print "Proveedor: ",droid.readLocation().result["network"]["provider"]
    print "Latitud: ",droid.readLocation().result["network"]["latitude"]
    print "Longitud: ",droid.readLocation().result["network"]["longitude"]
    print "Tiempo: ",droid.readLocation().result["network"]["time"]
    print "Velocidad: ",droid.readLocation().result["network"]["speed"]
    print "Precisión: ",droid.readLocation().result["network"]["accuracy"]
    #Se detiene la localización
    droid.stopLocating()


#Ejecución del programa principal.
if __name__ == "__main__":
    #Ejecución de la función
    localizacion()
```

La ejecución desde la consola muestra lo siguiente:


```
localizacion.py

Altitud:  0
Proveedor:  network
Latitud:  8.65770805
Longitud:  -71.11786675
Tiempo:  1292944124223
Velocidad:  0
Precisión:  65
```

Con ayuda de google map reviso que la latitud y longitud que devuelve el GPS del celular está cerca de la troncal 7 en Mérida.




===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)