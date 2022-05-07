Title: Obtener información del clima en una ciudad con Python  
Date: 2014-01-19 9:00  
Category: Tutorial Python  
Tags: Canaima,Debian,Python,Ubuntu,PyOWM  
lang: es  
translation: true  



Existe la librería [PyOWM](https://github.com/csparpa/pyowm) el cual es un wrapper para el API de OpenWeatherMap. 
La documentación para utilizar la librería se encuentra en el siguiente [enlace](https://github.com/csparpa/pyowm/wiki/Usage-examples).

Para poder utilizar la librería es necesario crear una cuenta en OpenWeatherMap y en el perfil del usuario buscar el APPID. En el [enlace](https://openweathermap.org/appid) explican el procedimiento.

Para instalar la librería se ejecuta `pip`:
```
#pip install pyowm
```

A continuación se muestra el código de un script que muestra el uso de la librería:
 
```python
#!/usr/bin/env python


# -*- coding: utf-8 -*-


import pyowm

#Llave del uso del API


apikey = "abcdefghijklimnopqrstuvxyz"


#Se crea la instancia OWM pasando la llave para el uso del API.


owm = pyowm.OWM(apikey)


#Se obtiene la llave de uso del API


print owm.get_API_key()


#Se define la ciudad por nombre o se pasa la coordenada.


obs = owm.weather_at('Valencia,ve')


#obs = owm.weather_at_coords(-0.107331,51.503614)


print "tiempo: ", obs.get_reception_time()


print "tiempo: ", obs.get_reception_time(timeformat='iso')


#Se Instancia los datos de la estacion meterologica.


w = obs.get_weather()


print "Fecha y hora ",w.get_reference_time(timeformat='iso')


print "Nubes:", w.get_clouds()


print  "lluvias:", w.get_rain()


print "Nieve: ", w.get_snow()


print "viento", w.get_wind()


print "humedad:",w.get_humidity()


print "presion:", w.get_pressure()


print "Temperatura:",w.get_temperature()


print "Temperatura:",w.get_temperature(unit='celsius')


print "Estatus", w.get_status()


print "Hora de salida del sol",w.get_sunrise_time("iso")


print "Hora de ocultarse el sol",w.get_sunset_time('iso')


l = obs.get_location()


print "nombre:", l.get_name()


print "Longitud: %s, Latitud: %s"   %(l.get_lon(),l.get_lat())

print "Identificador", l.get_ID()
```

Al ejecutar la aplicación se tiene lo siguiente:

```python
ernesto@heimdal:~/bin/python$ ./clima.py 

abcdefghijklimnopqrstuvxyz

tiempo:  1390165372

tiempo:  2014-01-19 21:02:52+00

Fecha y hora  2014-01-19 20:00:00+00

Nubes: 20

lluvias: {}

Nieve:  {}

viento {u'speed': 2.1, u'deg': 110}

humedad: 41

presion: {'press': 1012, 'sea_level': None}

Temperatura: {'temp_kf': None, 'temp_min': 308.15, 'temp': 308.15, 'temp_max': 308.15}

Temperatura: {'temp_kf': None, 'temp_max': 35.0, 'temp': 35.0, 'temp_min': 35.0}

Estatus clouds

Hora de salida del sol 2014-01-19 10:54:19+00

Hora de ocultarse el sol 2014-01-19 22:31:34+00

nombre: Valencia

Longitud: -68.01, Latitud: 10.16



Identificador 3625549  

```


Noten que la hora de salida y ocultamiento del sol está referente al meridiano 
de greenwich (es necesario ajustar al huso horario correspondiente).


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)