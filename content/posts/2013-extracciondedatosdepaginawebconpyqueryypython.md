Title: Extracción de datos de página web con pyquery y Python
Date: 2013-10-27 9:00
Category: Tutorial Python
Tags: Canaima,Debian,General,Linux,Python,Ubuntu,Webscraping
lang: es
translation: true

Continuando con los [artículos de webscraping](https://www.seraph.to/tag/webscraping.html) ahora toca el turno a [pyquery](https://pypi.org/project/pyquery/).

Ya la explicación de ubicación de la información que se desea obtener fue explicada en este [artículo](http://blog.crespo.org.ve/2013/10/webscraping-o-extraccion-de-datos-de.html) artículo.

Pyqueary es una librería que permite hacer consultas de jquery y en documentos xml. 

La idea es obtener la información de la salida y ocultamiento del sol ya explicado en artículos anteriores. 

A continuación se muestra el código:

```python
#!/usr/bin/env python

#importar pyquery

from pyquery import *

#Se Crea la instancia de la Clase PyQuery pasando el url de

#timeanddate.

html = PyQuery(url='http://www.timeanddate.com/worldclock/astronomy.html?n=58')

#Se busca el tag html de la tabla.

#Recibe todos los elementos de la tabla.

trs = html('table.spad tbody tr')

#Se muestra los elementos de la tabla.

print trs

#Se recorre los elementos de la tabla

for tr in trs:

    tds = tr.getchildren()

    print tds[1].text, tds[2].text

```

El resultado de la ejecución del script se muestra a continuación:
```
05:47 17:36

05:47 17:36

05:48 17:35

05:48 17:35

05:48 17:35

05:48 17:34

05:48 17:34

```

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)