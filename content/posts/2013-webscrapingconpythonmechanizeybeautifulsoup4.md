Title: Webscraping con Python Mechanize y BeautifulSoup4
Date: 2013-10-29 9:00
Category: Tutorial Python
Tags: Canaima,Debian,Linux,Python,Ubuntu,Webscraping,Mechanize,Beautiful Soup
lang: es
translation: true

Ahora se utilizará a [Python Mechanize](https://www.seraph.to/emulando-la-navegacion-en-python-con-mechanize-parte-1.html)  con [BeautifulSoup4](https://www.seraph.to/una-introduccion-a-beautiful-soup-4-en-python.html) para extraer la información de la salida y ocultamiento del sol en Venezuela con un breve cambio para mostrar el dinamismo que se le puede dar a la extracción de datos de una página web.

En este caso se extraerá información del mismo sitio [timeanddate](https://www.timeanddate.com/astronomy/venezuela/caracas), la diferencia es que en vez de sólo pasarle el código de Venezuela (58), se le pasará el mes y el año.

El código muestra la información del amanecer y atardecer de todo el mes de Octubre y Noviembre.

A continuación se muestra el código:

```python
#!/usr/bin/env python

#Se importa mechanize y cookielib

import mechanize

import cookielib

#Se importa beautifulSoup

from BeautifulSoup import BeautifulSoup

def DefinirUrl(mes,agno):


    #Se pasa el url del sitio timeanddate con la informacion


    #de la salida y ocultamiento del sol en Venezuela.


    return "http://www.timeanddate.com/worldclock/astronomy.htmln=58&month=%s&year=%s&obj=sun&afl=-11&day=1" %(mes,agno)

def CapturarInformacion(mes,agno):


    #Se crea una instancia de Browser


    br = mechanize.Browser()


    #Se crea una instancia para la Cookie


    cj = cookielib.LWPCookieJar()


    #Se asocia la instancia del cookie con el navegador.


    br.set_cookiejar(cj)


    #Se deshabilita el manejo de robots.txt


    br.set_handle_robots(False)


    #Se define el tiempo de refrescamiento


    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)


    #Se pasa el url del sitio timeanddate con la informacion


    url = DefinirUrl(mes,agno)


    #de la salida y ocultamiento del sol en Venezuela.


    #Se define las cabeceras del navegador, en este caso se le esta diciendo


    # que el navegador es un firefox desde Linux Debian


    br.addheaders = [('User-agent',


         'Mozilla/5.0 (X11; U; Linux i686; es-VE; rv:1.9.0.1)Gecko/2008071615 Debian/6.0 Firefox/9')]


    #Se abre el url


    r = br.open(url)


    #Se lee el htmml de la pagina


    html = br.response().read()


    #Se crea una instancia de BeautifulSoup pasando el html


    #a verificar


    soup = BeautifulSoup(html)


    #Se busca la palabra table, y de ahi class y se


    #busca el contenido


    #de cada columna de la tabla.


    for row in soup('table', {'class': 'spad'})[0].tbody('tr'):


        tds = row('td')


        #Se muestra la fecha y hora de la salida del sol


        print tds[0].string, tds[1].string,tds[2].string


if __name__== "__main__":


    print "Se muestra la informacion del mes de Octubre"


    print "--------------------------------------------"


    CapturarInformacion(10,2013)


    print "Se muestra la informacion del mes de Noviembre"


    print "--------------------------------------------" 

    CapturarInformacion(11,2013)
```

A continuación se muestra el resultado del script:

Se muestra la informacion del mes de Octubre
```
--------------------------------------------

1 Oct 2013 05:46 17:48

2 Oct 2013 05:46 17:47

3 Oct 2013 05:46 17:47

4 Oct 2013 05:46 17:46

5 Oct 2013 05:46 17:45

6 Oct 2013 05:46 17:45

7 Oct 2013 05:46 17:44

8 Oct 2013 05:46 17:44

9 Oct 2013 05:46 17:43

10 Oct 2013 05:46 17:43

11 Oct 2013 05:46 17:42

12 Oct 2013 05:46 17:42

13 Oct 2013 05:46 17:41

14 Oct 2013 05:46 17:41

15 Oct 2013 05:46 17:40

16 Oct 2013 05:46 17:40

17 Oct 2013 05:46 17:39

18 Oct 2013 05:47 17:39

19 Oct 2013 05:47 17:38

20 Oct 2013 05:47 17:38

21 Oct 2013 05:47 17:37

22 Oct 2013 05:47 17:37

23 Oct 2013 05:47 17:36

24 Oct 2013 05:47 17:36

25 Oct 2013 05:47 17:36

26 Oct 2013 05:48 17:35

27 Oct 2013 05:48 17:35

28 Oct 2013 05:48 17:35

29 Oct 2013 05:48 17:34

30 Oct 2013 05:48 17:34

31 Oct 2013 05:48 17:34

Se muestra la informacion del mes de Noviembre

--------------------------------------------

1 Nov 2013 05:49 17:33

2 Nov 2013 05:49 17:33

3 Nov 2013 05:49 17:33

4 Nov 2013 05:49 17:33

5 Nov 2013 05:50 17:33

6 Nov 2013 05:50 17:32

7 Nov 2013 05:50 17:32

8 Nov 2013 05:51 17:32

9 Nov 2013 05:51 17:32

10 Nov 2013 05:51 17:32

11 Nov 2013 05:51 17:32

12 Nov 2013 05:52 17:32

13 Nov 2013 05:52 17:32

14 Nov 2013 05:53 17:31

15 Nov 2013 05:53 17:31

16 Nov 2013 05:53 17:31

17 Nov 2013 05:54 17:31

18 Nov 2013 05:54 17:31

19 Nov 2013 05:54 17:32

20 Nov 2013 05:55 17:32

21 Nov 2013 05:55 17:32

22 Nov 2013 05:56 17:32

23 Nov 2013 05:56 17:32

24 Nov 2013 05:57 17:32

25 Nov 2013 05:57 17:32

26 Nov 2013 05:58 17:32

27 Nov 2013 05:58 17:32

28 Nov 2013 05:59 17:33

29 Nov 2013 05:59 17:33

30 Nov 2013 06:00 17:33
```

Como se muestra ya se puede agregar dinamismo a las busquedas que se quiera realizar en una página web, extrayendo su información al pasarle datos al url. Además se muestra como usar `Python Mechanize` para la captura de la página web y `BeautifulSoup4` para capturar la información necesaria.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)