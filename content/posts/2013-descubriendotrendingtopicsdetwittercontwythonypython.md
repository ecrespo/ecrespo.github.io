Title:  Descubriendo Trending Topics de Twitter con twython y python
Date: 2013-09-22 9:00
Category: Tutorial Python
Tags: Canaima,Debian,General,Linux,Python,Twitter,Ubuntu
lang: es
translation: true

Siguiendo con los artículos sobre [librerías de python para twitter](https://www.seraph.to/tag/twitter.html), hace poco se mostró en un artículo como [ver los Trending Topics usando la librería python-twitter](https://www.seraph.to/descubriendo-trending-topics-de-twitter-con-python-twitter.html#descubriendo-trending-topics-de-twitter-con-python-twitter) , ahora se mostrará como desplegar los topics usando la librería twython.

El script mostrará la conexión a twitter, luego despliega los identificadores de las ciudades que tienen Trending Topics en Venezuela y por último se despliega los Trending Topics de Venezuela en este momento.

Para saber como obtener el valor del token de la aplicación o de acceso se recomienda revisar el [artículo anterior](http://blog.crespo.org.ve/2013/09/probando-la-libreria-twython-para.html).

El código se muestra a continuación:
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Se define el token de la aplicacion

CONSUMER_KEY = 'xxxxx'

CONSUMER_SECRET = 'xxxxx'

#Se define el acceso al usuario

ACCESS_KEY = 'xxxxx'

ACCESS_SECRET = 'xxxxx'

#Se importa twython y de time a  sleep

from twython import Twython

from time import sleep

#Se define los argumentos del cliente, la ip y puerto del proxy, el tiempo de intento de la conexion y el nombre de la

#aplicacion cliente

client_args = {'headers': {'User-Agent': 'cmdtweetpy'},'proxies': {'http': '127.0.0.1:xxx'},'timeout': 300}

#Conectar a twitter y enviar un tweet,

#Si no se logra la conexion se devuelve un mensaje.

try:

    api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET,client_args = client_args)

    print(u"Autenticación con exito")

except twython.exceptions.TwythonAuthError:

    print(u"Error de autenticación")

print ""

trending = api.get_available_trends()

print u"Identificación de woeid de Venezuela"

print "-------------------------------------"

c = 0   

pos = 0

woeid = 0

#Se despliega los woeid de las ciudades de Venezuela y de Venezuela en si


for i in trending:


    if i[u'countryCode'] == u'VE':


        print i[u'name'],i[u'woeid']


        #Se toma el woeid de Venezuela


        woeid = i[u'woeid']


        pos = c


    c += 1


print ""


#Se despliega los topics de Venezuela.


print "Lista de Trending Topics en Venezuela"


print "-------------------------------------"


for i in api.get_place_trends(id=woeid):


    for k in i[u'trends']:


        print k[u'name']
```

A continuación se muestra el resultado de la ejecución del script:

```python
Identificación de woeid de Venezuela


-------------------------------------


Caracas 395269


Maracaibo 395270


Maracay 395271


Valencia 395272


Barcelona 395273


Ciudad Guayana 395275


Turmero 395277


Barquisimeto 468382


Maturín 468384


Venezuela 23424982





Lista de Trending Topics en Venezuela


-------------------------------------


#10CosasQueOdio


#AlfombraRojaE


#EmmysPorWarner


#ChavezElGranArquitecto


#ObamaNervioso


Angela Merkel


Titanic


Kenia


GNB


Sofia Vergara
```

Como se ve, se puede obtener el topics de cada ciudad o País al obtener el `woeid`.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)