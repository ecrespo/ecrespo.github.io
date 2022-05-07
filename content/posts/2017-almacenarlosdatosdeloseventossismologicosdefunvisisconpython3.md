Title: Almacenar los datos de los eventos sismológicos de Funvisis con Python3
Date: 2017-07-24 09:00
Category: Tutorial de Python
Tags: Python,Webscraping,BeautifulSoup,Request,MongoDB,Pymongo
lang: es
translation: true

En el artículo sobre la [captura de datos de eventos sismológicos de funvisis](https://www.seraph.to/obtener-datos-de-eventos-sismologicos-de-funvisis-con-python3-segunda-version.html)  solamente se trabajó el orenamiento de los datos, pero hace falta almacenar la información en una base de datos, este es el tema del artículo.

Ahora se tienen varios módulos:

- `sismux_getdata.py`: Es el módulo que hace el webscraping de la página de funvisis.  
- `sismux_mongo.py`: Es el módulo que implementa un CRUD para mongoDB a MongoLab.  
- `sismux_main.py`: Es el módulo principal que consulta cada 5 min la página de Funvisis para guardar la información en la base de datos si no existe.  
- `sismux_apirest.py`: Es el módulo que implementa un API rest(próximo artículo).  
- `sismux_graphql.py`: Es el módulo que implementa un API con GraphQL (próximo artículo).  

Del artículo anterior [artículo anterior](https://www.seraph.to/obtener-datos-de-eventos-sismologicos-de-funvisis-con-python3-segunda-version.html) se muestra el código de `sismux_getdata.py`:

```python

#!/usr/bin/env python3





#Se importa beautifulSoup

from bs4 import BeautifulSoup

#Se importa la fecha

import datetime

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

            datos = trs.find('td').getText().split('&nbsp;')[0].split('\n\t')

            self.__sismo['fecha'] = datos[0].split('\xa0')[1]

            date = self.__sismo['fecha'].split("/")

            self.__sismo['hora'] = datos[2].split(" ")[-2]

            time= self.__sismo['hora'].split(":")

            self.__sismo['datetime'] = datetime.datetime(int(date[2]),int(date[1]),int(date[0]), int(time[0]), int(time[1]))

            self.__sismo['magnitud'] = datos[4].split(" ")[-1]

            mag = datos[6].split(" ")[-1].split('\xa0')

            self.__sismo['profundidad'] = mag[0] + " "+ mag[1]

            lat = datos[8].split(" ")

            self.__sismo["latitud"] = lat[-2] + " " + lat[-1]

            lon =  datos[10].split(" ")

            self.__sismo['longitud'] = lon[-2] + " "+ lon[-1]

            self.__sismo['epicentro'] = datos[11].split(":")[1].split('\xa0')[-1]

            self.__sismo['loc'] = {'type':'Point','coordinates' : [ float(lat[-2]) , float(lon[-2]) ]}

        return self.__sismo


```


El código del módulos `sismux_mongo.py` se muestra a continuación: 

```python


#!/usr/bin/env python3
import pymongo

from pymongo import MongoClient


#Se define el uri de la conexion a mongolab

uri = 'mongodb://usuario:clave@ds045064.mlab.com:45064/basedatos'

#Se define la base de datos y la cole

#ccion


basedatos = "sismux"

coleccion = "sismos"


#Se crea la clase BaseDatos que simplemente implemente un crud.
class BaseDatos(object):

    #Se define la intancia de mongoclient, se define la base de datos y

    #la coleccion

    def __init__(self,uri=uri,basedatos=basedatos,coleccion=coleccion):

        self.__client = MongoClient(uri)

        self.__db = self.__client[basedatos]

        self.__coleccion = self.__db[coleccion]


  def ConsultarTodos(self):

        #Traer todos los elementos de la consulta.

        elementos = []

        for i in self.__coleccion.find():

            elementos.append(i)

        return i


  def Consultar(self,patron):

        #Se devuelve la consulta de un elemento

        return self.__coleccion.find_one(patron)


  def Insertar(self,documento):

        #Se inserta un documento

        self.__coleccion.insert(documento)


  def Finalizar(self):

        #Se cierra la conexion con la base de datos
        self.__client.close()

```


A continuación se muestra `sismux_main.py`:

```python

#!/usr/bin/env python3
from sismux_getdata import Sismo
import json
import time
import sys

from sismux_mongo import BaseDatos
import datetime
import logging

bd = BaseDatos()
sismo  = Sismo()
datos = sismo.GetData()
#bd.Insertar(datos)
#datos['datetime']
datime = datetime.datetime(2017,5,25, 20, 51)
#print(bd.Consultar({'datetime': datie}m))
def main():

   #Se crea la instancia a la base de datos
   bd = BaseDatos()
   #Se crea la instancia del webscraping
   sismo = Sismo()
   #Se optiene los datos de la pagina de funvisis
   datos = sismo.GetData()
   #Se consulta si ya existe el dato guardado en la base de datos
   query1 = bd.Consultar({'datetime': datos['datetime']})
   query2 = bd.Consultar({'loc': {'coordinates': datos['loc']['coordinates']}})
   if (query1 != None):
        return False
   else:
       #Si no existe se inserta en la base de datos.
       bd.Insertar(datos)
       return True

#Se crea un ciclo para consultar cada 5 min

def ciclo(tim=300):
    #Se define el log
    logging.basicConfig(filename="sismux.log",level=logging.DEBUG,format='%(asctime)s %(message)s')

    

while True:
        #Se ejecuta main.
       result = main()
       #Se guarda el resultado de main en el log
       logging.info(result)
       #Se espera 5 min (por defecto)
       time.sleep(tim)



if __name__ == '__main__':
   #Se ejecuta la funcion ciclo
   ciclo()
```


Para ejecutar el programa se corre:
```python
python3 sismux_main.py 
```
Al ejecutarlo se crea un archivo `log` y en el se tiene lo siguiente:
```
tail -f sismux.log 
2017-07-24 11:42:43,149 Starting new HTTP connection (1): www.funvisis.gob.ve
2017-07-24 11:42:43,821 http://www.funvisis.gob.ve:80 "GET /index.php HTTP/1.1" 200 14319
2017-07-24 11:42:56,560 False
2017-07-24 11:47:56,637 Starting new HTTP connection (1): www.funvisis.gob.ve
2017-07-24 11:47:57,466 http://www.funvisis.gob.ve:80 "GET /index.php HTTP/1.1" 200 14319
2017-07-24 11:48:12,086 False
2017-07-24 11:53:12,209 Starting new HTTP connection (1): www.funvisis.gob.ve
2017-07-24 11:53:12,976 http://www.funvisis.gob.ve:80 "GET /index.php HTTP/1.1" 200 14319
2017-07-24 11:53:18,516 False
2017-07-24 11:58:18,605 Starting new HTTP connection (1): www.funvisis.gob.ve
2017-07-24 11:58:30,984 http://www.funvisis.gob.ve:80 "GET /index.php HTTP/1.1" 200 14319
2017-07-24 11:58:57,034 False
```

Como muestra el `log` ya se tiene el último sismo en la base de datos.

En la siguiente figura se muestra un documento almacenado en la base de datos:

![](./images/almacenarlosdatosdeloseventossismologicosdefunvisisconpython3-1.png)

Para el siguiente artículo se desarrollará el API. 

Nota: En un futuro artículo se muestra la creación de un demonio y como ponerlo a funcionar con `SystemD` y el empaquetado de todo los módulos desarrollados. 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
