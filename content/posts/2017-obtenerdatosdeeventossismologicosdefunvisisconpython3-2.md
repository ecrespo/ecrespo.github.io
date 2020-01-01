Title:  Obtener datos de eventos sismológicos de Funvisis con Python3 (segunda versión)
Date: 2017-06-24 11:00
Category: Tutorial de Python
Tags: Python,Webscraping,Request
lang: es
translation: true

El primer artículo sobre [obtener los datos sismológicos de Funvisis con Python](https://www.seraph.to/obtener-datos-de-eventos-sismologicos-de-funvisis-con-python.html), se usó la librería `python-mechanize`, en este caso se usará la librería `request` y `Python 3.* `.

El código se muestra a continuación:

```python
#!/usr/bin/env python3


#Se importa beautifulSoup

from bs4 import BeautifulSoup

#Se importa la fecha

from datetime import datetime

import requests

import sys

import json



class Sismo(object):

    def __init__(self,url="http://www.funvisis.gob.ve/",home="index.php",referer='http://www.cantv.com.ve'):

        headers = {'User-agent': 'Mozilla/5.0',\

            'SSL_VERIFYHOST': 'False',\

            'FRESH_CONNECT':'True',\

            'RETURNTRANSFER':'True',\

            'SSL_VERIFYPEER': 'False',\

            'Referer': referer

            }

        self.__url = url

        self.__home = home

        self.__urlhome = self.__url + self.__home

        self.__session = requests.Session()

        self.__session.headers.update(headers)



    def GetData(self):

        #Se  obtiene la pagina por medio de session.

        try:

            self.__r = self.__session.get(self.__urlhome)

            self.__page = self.__r.content

        except (requests.exceptions.SSLError):

            print("SSL Error")

            sys.exit(0)

        except (requests.exceptions.ConnectionError):

            print("Connection Error")

            sys.exit(0)

        #Se le pasa la pagina a beautifulsoup usando lxml de parser.

        self.__soup = BeautifulSoup(self.__page,"lxml")

        #Se crea el diccionario que almacena los datos

        self.__sismo = {}



        #SE obtiene el primer  div que tengan class module

        for row in self.__soup('div', {'class': 'module'})[0]:

            #Se obtiene el tag a para luego obtener el href y tener el url

            #del gif del sitio de funvisis que tiene la imagen del sitio donde

            #fue el sismo.

            trs = row.find('a')

            if trs == -1:

                continue

            self.__sismo['urlref'] = self.__url  + trs.get('href',None)



            trs = row.find('tr')

            if trs == -1:

                continue

            #Obtiene los datos del sismo del sitio de funvisis

            datos = trs.find('td').getText().split('&nbsp;')

            self.__sismo['fecha'] = datos[0].split('\n\t')[0].split('\xa0')[1]

            self.__sismo['hora'] = datos[0].split('\n\t')[2].split(" ")[-2]

            self.__sismo['magnitud'] = datos[0].split('\n\t')[4].split(" ")[-1]

            mag = datos[0].split('\n\t')[6].split(" ")[-1].split('\xa0')

            self.__sismo['profundidad'] = mag[0] + " "+ mag[1]

            lat = datos[0].split('\n\t')[8].split(" ")

            self.__sismo["latitud"] = lat[-2] + " " + lat[-1]

            lon =  datos[0].split('\n\t')[10].split(" ")

            self.__sismo['longitud'] = lon[-2] + " "+ lon[-1]

            self.__sismo['epicentro'] = datos[0].split('\n\t')[11].split(":")[1].split('\xa0')[-1]

        return self.__sismo


  def ToJSON(self):

        self.__sismojson = json.dumps(self.GetData())

        return self.__sismojson





if __name__ == '__main__':

sismo = Sismo(

)

print


(

sismo.ToJSON())
```

Al ejecutar el script se tiene de resultado:
```
{"epicentro": "30 Km al sur de Guiria", "hora": "07:51", "latitud": "10.39 \u00baN", "longitud": "-62.32 \u00baO", "fecha": "24/06/2017", "magnitud": "2.8", "urlref": "http://www.funvisis.gob.ve/images/reportes/2017/06/reporte_7489.gif", "profundidad": "9.1 km"}
```

El código se puede ver en el [repositorio en gitlab](https://gitlab.com/mangoosta/sismux/blob/master/sismux_getdata.py) .

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
