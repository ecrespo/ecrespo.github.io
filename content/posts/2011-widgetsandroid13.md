Title: Visualización de las coordenadas del gps del celular desde Android
Date: 2011-04-18 09:00
Category: Tutorial Python en Android
Tags: Android, Python
lang: es
translation: true

En artículo anterior expliqué [como capturar información de la posición del celular en Linux](https://www.seraph.to/capturar-la-ubicacion-del-celular-android-desde-linux.html), en este artículo más sencillo que la versión anterior lo hace directamente en android.

En el artículo mencionado se captura la información de la posición del celular con la la función readLocation(), en esta versión se usará  función getLastKnownLocation() . Note diferencias entre una función y la otra, en la última si pude tomar la posición correcta que muestra googlemap, en cambio con la primera función marcaba la posición que donde el celular se encontraba hace unos días, es necesario investigar más de la API de SL4A  o de Android para ver la razón de esta característica.

Lo otro nuevo en el programa es que se visualiza directamente en el celular la posición, esto se logra usando la función webviewShow(), se mostró su uso en el artículo sobre webview. En ese artículo se abre una página web desde la memoria SD del celular, en este caso se abrirá la página de googlemaps pasandole la lontitud y latitud y el navegador mostrará la ubicación del celular en el mapa.

Adicional a la  información de latitud y longitud se puede capturar información de:

* tiempo
* altitud
* velocidad
* precisión

El código se muestra a continuación:

```python
#Importando el modulo android
import android
from time import sleep



#Se crea la instancia de la clase Android
droid = android.Android()
#Se inicia la localizacion
droid.startLocating()
#Se espera 15 segundos
sleep(15)
#Se presenta en la consola la informaci?n de la localizaci?n
#Se maneja la informacion de un diccionario.
resultado = droid.getLastKnownLocation()


latitud = resultado[1]["passive"]["latitude"]
longitud = resultado[1]["passive"]["longitude"]
altitud = resultado[1]["passive"]["altitude"]
#Se detiene la localizacion
droid.stopLocating()
#Se muestra googlemaps en el navegador en android
droid.webViewShow("http://maps.google.com/maps?q=%s,%s" %(latitud,longitud))
```

La siguiente figura muestra la ejecución del script.

![Ubicación GPS Android](./images/gpsandroid.png)

El código QR del script se muestra en la siguiente figura:

![Código QR](./images/gps.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
