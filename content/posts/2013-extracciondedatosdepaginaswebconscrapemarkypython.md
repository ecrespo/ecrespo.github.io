Title: Extracción de datos de páginas web con Scrapemark y Python
Date: 2013-10-26 10:00
Category: Tutorial Python
Tags: Canaima,Debian,General,Linux,Python,Ubuntu,webscraping, Scrapermark
lang: es
translation: true

Continuando con los artículos sobre [webscraping](https://www.seraph.to/tag/webscraping.html), ahora es el turno de `scrapermark`.

Se sigue usando como página de ejemplo timeanddate.com. `Scrapermark` usa expresiones regulares internamente lo que le da velocidad en la busqueda, utiliza un lenguaje parecido al HTML.

Para bajar scrapermark se puede bajar el egg o el fuente desde el siguiente [enlace](https://arshaw.com/scrapemark/download/).

Para el caso del `egg` se ejecuta:
```python
#easy_install scrapemark-0.9-py2.7.egg
```
Para el caso del fuente se descomprime el archivo .tar.gz :
```
#tar -xvf scrapemark-0.9.tar.gz
```
Luego se cambia al directorio y se ejecuta la instalación por medio del `setup.py`:
```python
#cd scrapemark-0.9/
#python setup.py install
```

En el siguiente [enlace](https://arshaw.com/scrapemark/) se muestra un ejemplo de como se usa, para más ejemplos puede visitar este [enlace](https://arshaw.com/scrapemark/docs/examples/).

En este [artículo](http://blog.crespo.org.ve/2013/10/webscraping-o-extraccion-de-datos-de.html) se explica como buscar la información que se necesita extraer de la página antes [mencionada](www.timeanddate.com/worldclock/astronomy.html?n=58).

La idea es extraer las hora de salida y ocultamiento del sol para Venezuela.
A continuación se muestra el código:

```python
#!/usr/bin/env python


#Se importa sys para pasar como argumento al programa


#el url del sitio timeanddate


import sys


#Se importa pprint para mostrar la informacion en la


#consola


from pprint import pprint


#se importa scrape


from scrapemark import scrape





#se ejecuta scrape pasando el tag  html de la tabla


#donde se encuentra la fila de la informacion de la salida


#y ocultamiento del sol.


#se le pasa como argumento en la linea de comandos


#el url de timeanddate.


resultado = scrape("""


    <table class="spad">


     <tbody>


      {*


       <tr>


          <td>{{[].day}}</td>


          <td>{{[].sunrise}}</td>


          <td>{{[].sunset}}</td>


      {# ... #}


     </tr>


     *}


 </tbody>


    </table>


""",url=sys.argv[1] )





#Se muestra el resultado en pantalla


pprint (resultado)
```
El resultado de la ejecución del script es el siguiente:
```python
ernesto@grievous:~$ python ej5.py http://www.timeanddate.com/worldclock/astronomy.html?n=58

fetching http://www.timeanddate.com/worldclock/astronomy.html?n=58 ...

DONE fetching.

[{'day': u'24 Oct 2013', 'sunrise': u'05:47', 'sunset': u'17:36'},

 {'day': u'25 Oct 2013', 'sunrise': u'05:47', 'sunset': u'17:36'},

 {'day': u'26 Oct 2013', 'sunrise': u'05:48', 'sunset': u'17:35'},

 {'day': u'27 Oct 2013', 'sunrise': u'05:48', 'sunset': u'17:35'},

 {'day': u'28 Oct 2013', 'sunrise': u'05:48', 'sunset': u'17:35'},

 {'day': u'29 Oct 2013', 'sunrise': u'05:48', 'sunset': u'17:34'},

 {'day': u'30 Oct 2013', 'sunrise': u'05:48', 'sunset': u'17:34'}]
```

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)