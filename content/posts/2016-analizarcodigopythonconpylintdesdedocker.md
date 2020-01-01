Title: Analizar código python con pylint desde Docker  
Date: 2016-06-12 09:00  
Category: Tutorial de Docker
Tags: Canaima,Linux,Python,Ubuntu,pylint,Docker 
lang: es  
translation: true  


Hace un tiempo escribí un artículo sobre [analizar código python con pylint](https://www.seraph.to/analizando-codigo-python-con-pylint.html).

En este caso se tomará el artículo de [pruebas unitarias con Docker](https://www.seraph.to/ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker.html#ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker) y el de pylint para mostrar como se ejecuta el análisis de código python con Docker.


Los artículos anteriores sobre Docker son:

1. [Instalar Docker en Debian Jessie](https://www.seraph.to/instalar-docker-en-debian-jessie.html)  

2. [Uso de Docker en Debian Jessie (parte 1)](https://www.seraph.to/uso-de-docker-en-debian-jessie-parte-1.html)  

3. [Uso de Docker en Debian Jessie (parte 2)](https://www.seraph.to/uso-de-docker-en-debian-jessie-parte-2.html)  

4. [Crear una imagen Docker a partir de un archivo Dockerfile](https://www.seraph.to/crear-una-imagen-docker-a-partir-de-un-archivo-dockerfile.html)  

5. [Iniciando Django usando Docker](https://www.seraph.to/iniciando-django-usando-docker.html)  

6. [Instalar Gitlab por medio de Docker](https://www.seraph.to/instalar-gitlab-por-medio-de-docker.html)  

7. [Ejecutando microservicios con docker usando docker-compose](https://www.seraph.to/ejecutando-micros-servicios-con-docker-usando-docker-compose.html)  

8. [Docker en Docker (DinD)](https://www.seraph.to/docker-en-docker-dind.html)

9. [Iniciando Django con docker usando docker-compose con postgresql como microservicio.](https://www.seraph.to/iniciando-django-con-docker-usando-docker-compose-con-postgresql-como-microservicio.html)

10. [Importar un contenedor Docker en Python.](https://www.seraph.to/importar-un-contenedor-docker-en-python.html#importar-un-contenedor-docker-en-python) 

11. [Compartir imagenes Docker por medio de archivos tar](https://www.seraph.to/compartir-imagenes-docker-por-medio-de-archivos-tar.html#compartir-imagenes-docker-por-medio-de-archivos-tar).

12. [Crear un registro de imagenes Docker privado.](https://www.seraph.to/crear-un-registro-de-imagenes-docker-privado.html#crear-un-registro-de-imagenes-docker-privado)

13. [Usar Anaconda desde un contenedor Docker.](https://www.seraph.to/usar-anaconda-desde-un-contenedor-docker.html#usar-anaconda-desde-un-contenedor-docker)  

14. [Crear un entorno de Integración y Despligue continue con Docker para node.js.](https://www.seraph.to/crear-un-entorno-de-integracion-y-despligue-continue-con-docker-para-nodejs.html#crear-un-entorno-de-integracion-y-despligue-continue-con-docker-para-nodejs)  

15. [Usar Jupyter Notebook desde un contenedor Docker.](https://www.seraph.to/usar-jupyter-notebook-desde-un-contenedor-de-docker.html#usar-jupyter-notebook-desde-un-contenedor-de-docker)  

16. [Ejecutar una prueba de doctest con un contenedor Docker](https://www.seraph.to/ejecutar-una-prueba-de-doctest-con-un-contenedor-docker.html#ejecutar-una-prueba-de-doctest-con-un-contenedor-docker).

17. [Ejecutar una prueba de unittest en Python con un contenedor Docker.](https://www.seraph.to/ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker.html#ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker) 

18. [Montar una Plataforma como servicio (PaaS) con Dokku (docker)](https://www.seraph.to/montar-una-plataforma-como-servicio-paas-con-dokku-docker.html#montar-una-plataforma-como-servicio-paas-con-dokku-docker).  

19. [Uso de docker-machine.  ](https://www.seraph.to/uso-de-docker-machine.html#uso-de-docker-machine)

20. [Proveer un cluster con docker swarm y docker-machine.](https://www.seraph.to/proveer-un-cluster-con-docker-swarm-y-docker-machine.html#proveer-un-cluster-con-docker-swarm-y-docker-machine)

21. [Instalar Jenkins por medio de Docker y crear una imagen Docker de Jenkins](https://www.seraph.to/instalar-jenkins-por-medio-de-docker-y-crear-una-imagen-docker-de-jenkins.html#instalar-jenkins-por-medio-de-docker-y-crear-una-imagen-docker-de-jenkins) 

22. [Automatizar la construcción de imágenes Docker con github.](https://www.seraph.to/automatizar-la-construccion-de-imagenes-docker-con-github.html#automatizar-la-construccion-de-imagenes-docker-con-github) 

23. [Crear una imagen Docker para MongoDB3.](https://www.seraph.to/crear-una-imagen-docker-para-mongodb-3.html#crear-una-imagen-docker-para-mongodb-3)

24. [Crear un contenedor Docker como entorno de desarrollo para Sails.js.](https://www.seraph.to/crear-un-contenedor-docker-como-entorno-de-desarrollo-para-sailsjs.html#crear-un-contenedor-docker-como-entorno-de-desarrollo-para-sailsjs)

25. [Correr aplicaciones de escritorio desde un contenedor Docker.](https://www.seraph.to/correr-aplicaciones-de-escritorio-desde-un-contenedor-docker.html#correr-aplicaciones-de-escritorio-desde-un-contenedor-docker)

26. [Usar dockerui para la gestión de imágenes y contenedores de Docker](https://www.seraph.to/usar-dockerui-para-la-gestion-de-imagenes-y-contenedores-de-docker.html#usar-dockerui-para-la-gestion-de-imagenes-y-contenedores-de-docker) 

27. [Crear una imagen Docker de RethinkDB](https://www.seraph.to/crear-una-imagen-docker-de-rethinkdb.html#crear-una-imagen-docker-de-rethinkdb)

El archivo `Dockerfile` cambió un poco con respecto al usado con las pruebas unitarias, ahora se usará como base a Debian, se instalará pylint por medio de apt-get y lo demás queda igual que en el artículo de pruebas unitarias. 

A continuación el archivo `Dockerfile`:
```
FROM debian
MAINTAINER Ernesto Crespo

RUN apt-get update 
RUN apt-get install -y pylint
RUN apt-get clean 

WORKDIR /app
COPY . /app
```

Los archivos que se usarán son los mismos utilizados en el de pruebas unitarias que se encuentra en el repositorio de [github](https://github.com/ecrespo/raizcuadrada).
```
raizcuadrada
├── Dockerfile
├── LICENSE
├── raizcuadrada.py
├── raizcuadrada_test.py
└── README.md
```

El módulo `raizcuadrada.py` tiene lo siguiente:

```
#!/usr/bin/env python3


# -*- coding: utf-8 -*-


"""


Se importa el módulo math para calcular la raiz cuadrada.


"""


import math


#Función raiz cuadrada.


def Raiz(a):


    """Si a es mayor o igual a cero se calcula la raiz cuadrada"""


    if a >= 0:


        return math.sqrt(a)


    #Si es menor a cero se genera una excepción donde se informa que a debe ser mayor o igual a cero.


    else:


        raise ValueError("a debe ser >= 0")


if __name__ == '__main__':


    #Se importa el módulo doctest


    import doctest


    #Se realiza la prueba al archivo raizcuadra.txt


    doctest.testfile("raizcuadrada.txt")


```
La construcción de la imagen Docker se hace con el siguiente comando:
```
docker build -t prueba-python .
```
Para ejecutar el análisis desde docker se ejecuta:
```
docker run  -v "$PWD:/app" -ti prueba-python  pylint raizcuadrada.py
```
Y el resultado es el siguiente:

```

docker run  -v "$PWD:/app" -ti prueba-python  pylint raizcuadrada.py



No config file found, using default configuration



************* Module raizcuadrada


C: 16, 0: Line too long (101/80) (line-too-long)


C: 12, 0: Invalid function name "Raiz" (invalid-name)


C: 12, 0: Invalid argument name "a" (invalid-name)


Report


======


9 statements analysed.





Messages by category


--------------------





+-----------+-------+---------+-----------+


|type       |number |previous |difference |


+===========+=======+=========+===========+


|convention |3      |NC       |NC         |


+-----------+-------+---------+-----------+


|refactor   |0      |NC       |NC         |


+-----------+-------+---------+-----------+


|warning    |0      |NC       |NC         |


+-----------+-------+---------+-----------+


|error      |0      |NC       |NC         |


+-----------+-------+---------+-----------+



Messages


--------





+--------------+------------+


|message id    |occurrences |


+==============+============+


|invalid-name  |2           |


+--------------+------------+


|line-too-long |1           |


+--------------+------------+



Global evaluation


-----------------


Your code has been rated at 6.67/10





Raw metrics


-----------





+----------+-------+------+---------+-----------+


|type      |number |%     |previous |difference |


+==========+=======+======+=========+===========+


|code      |9      |36.00 |NC       |NC         |


+----------+-------+------+---------+-----------+


|docstring |4      |16.00 |NC       |NC         |


+----------+-------+------+---------+-----------+


|comment   |3      |12.00 |NC       |NC         |


+----------+-------+------+---------+-----------+


|empty     |9      |36.00 |NC       |NC         |


+----------+-------+------+---------+-----------+

Statistics by type


------------------



+---------+-------+-----------+-----------+------------+---------+


|type     |number |old number |difference |%documented |%badname |


+=========+=======+===========+===========+============+=========+


|module   |1      |NC         |NC         |100.00      |0.00     |


+---------+-------+-----------+-----------+------------+---------+


|class    |0      |NC         |NC         |0           |0        |


+---------+-------+-----------+-----------+------------+---------+


|method   |0      |NC         |NC         |0           |0        |


+---------+-------+-----------+-----------+------------+---------+


|function |1      |NC         |NC         |100.00      |100.00   |


+---------+-------+-----------+-----------+------------+---------+


Duplication


-----------



+-------------------------+------+---------+-----------+


|                         |now   |previous |difference |


+=========================+======+=========+===========+


|nb duplicated lines      |0     |NC       |NC         |


+-------------------------+------+---------+-----------+


|percent duplicated lines |0.000 |NC       |NC         |


+-------------------------+------+---------+-----------

```

De esta forma se puede ejecutar el análisis del código python con pylint usando Docker.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)


