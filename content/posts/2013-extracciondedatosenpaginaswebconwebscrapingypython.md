Title: Extracción de datos en páginas web con Webscraping y Python
Date:  2013-10-25 9:00
Category: Tutorial Python
Tags: Canaima,Debian,General,Linux,Python,Ubuntu,Webscraping
lang: es
translation: true

Continuando con la extracción de datos en la página timeanddate, la información de amanecer y atardecer en Venezuela.
En este caso se usará la librería webscraping. Para su instalación se usa el comando `pip`:
```
#pip install webscraping
```
En el artículo [anterior](https://www.seraph.to/webscraping-o-extraccion-de-datos-de-paginas-web-con-beautifulsoup4-y-python.html#webscraping-o-extraccion-de-datos-de-paginas-web-con-beautifulsoup4-y-python) se muestra como se ubica la información que se requiere.

A continuación se muestra el código:

```python
#!/usr/bin/env python


#De webscraping se importa download y xpath


from webscraping import download, xpath


#Se define la instancia Download


D = download.Download()

#Se obtiene la informacion de la salida y ocultamiento del

#sol en Venezuela desde la pagina timeanddate.

html = D.get('http://www.timeanddate.com/worldclock/astronomy.html?n=58')


#Se busca la informacion en la tabla donde se muestra.


for row in xpath.search(html, '//table[@class="spad"]/tbody/tr'):


    #Se busca en la fila el tag /td


    cols = xpath.search(row, '/td')


    #Se muestra la informacion en pantalla


    print 'Amanecer: %s, Atardecer: %s' % (cols[1], cols[2])
```

A continuación se muestra el resultado de la ejecución del script:
```
Amanecer: 05:47, Atardecer: 17:36

Amanecer: 05:47, Atardecer: 17:36

Amanecer: 05:47, Atardecer: 17:36

Amanecer: 05:48, Atardecer: 17:35

Amanecer: 05:48, Atardecer: 17:35

Amanecer: 05:48, Atardecer: 17:35

Amanecer: 05:48, Atardecer: 17:34
```
##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)