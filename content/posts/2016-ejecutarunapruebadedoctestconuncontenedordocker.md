Title: Ejecutar una prueba de doctest con un contenedor Docker.   
Date: 2016-03-27 10:00  
Category: Tutorial Python  
Tags: Python, Docker, Jupyter Notebook, DevOps, Doctest  
lang: es  
translation: true  

Ahora se mostrará como usar un contenedor de Docker para hacer pruebas doctest, este artículo se basa en un post anterior del blog llamado [Separar código de pruebas de la documentación (doctest,2da parte)](https://www.seraph.to/separar-codigo-de-pruebas-de-la-documentacion-doctest-2da-parte.html).

Los artículos anteriores sobre docker son:  
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


Se tendrán 3 archivos en un directorio que se llamará `pruebas-doctest` con lo siguiente:
```
pruebas-doctest
├── Dockerfile
├── raizcuadrada.py
└── raizcuadrada.txt
```
El archivo `Dockerfile` contendrá lo siguiente:
```
FROM python:3.4
MAINTAINER Ernesto Crespo

WORKDIR /app
COPY . /app
```
Se usará python 3.4, el mantenedor es Ernesto Crespo, el directorio de trabajo será app y se copiará todo lo que está en el directorio al directorio de trabajo.

Se tiene el archivo `raizcuadrada.py` con lo siguiente:

```python
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


Y el último de los archivos es `raizcuadrada.txt` el cual tendrá las pruebas de doctest:

```python


Modulo raiz cuadrada


=====================


Usando  'raizcuadrada'


------------------------------


Primero se importa la función:





>>> from raizcuadrada import Raiz





Ejemplos de calculo de raiz cuadrada:





>>> Raiz(4)


2.0





>>> Raiz(9)


3.0





>>> Raiz(25)


5.0





>>> Raiz(0)


0.0





>>> Raiz(16)


5.0





>>> Raiz(-1)


Traceback (most recent call last):


...


ValueError: a debe ser >= 0

```


El archivo tiene un error intencional en el cálculo de la raíz cuadrada de 16 que debe dar 4 y se coloco que da 5.


Ahora se construye la imagen con nombre `pruebas-doctest`:
```
docker build -t pruebas-doctest .
Sending build context to Docker daemon  5.12 kB
Step 1 : FROM python:3.4
3.4: Pulling from library/python
fdd5d7827f33: Downloading 11.35 MB
fdd5d7827f33: Pull complete 
a3ed95caeb02: Pull complete 
0f35d0fe50cc: Pull complete 
7b40647e93b7: Pull complete 
ce5207842c4c: Pull complete 
da7994e536a7: Pull complete 
09482b8dda8a: Pull complete 
5ba79222c836: Pull complete 
Digest: sha256:8bcba46a3dbf4803c80074c0e543d98eeb3cb4f9cc35ff52f88c53cc0a1c30c3
Status: Downloaded newer image for python:3.4
 ---> c40d327867e9
Step 2 : MAINTAINER Ernesto Crespo
 ---> Running in de81df2565f3
 ---> 3b1aced33b5e
Removing intermediate container de81df2565f3
Step 3 : WORKDIR /app
 ---> Running in f1901c2490d7
 ---> 7dd09842cf61
Removing intermediate container f1901c2490d7
Step 4 : COPY . /app
 ---> 788ad6d153ed
Removing intermediate container b32ba65862d9
Successfully built 788ad6d153ed
```

Ahora se ejecuta la prueba pasando `python -m doctest -v raizcuadrada.txt`:
```
docker run pruebas-doctest python -m doctest -v raizcuadrada.txt
Trying:
    from raizcuadrada import Raiz
Expecting nothing
ok
Trying:
    Raiz(4)
Expecting:
    2.0
ok
Trying:
    Raiz(9)
Expecting:
    3.0
ok
Trying:
    Raiz(25)
Expecting:
    5.0
ok
Trying:
    Raiz(0)
Expecting:
    0.0
ok
Trying:
    Raiz(16)
Expecting:
    5.0
**********************************************************************
File "raizcuadrada.txt", line 23, in raizcuadrada.txt
Failed example:
    Raiz(16)
Expected:
    5.0
Got:
    4.0
Trying:
    Raiz(-1)
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: a debe ser >= 0
ok
**********************************************************************
1 items had failures:
   1 of   7 in raizcuadrada.txt
7 tests in 1 items.
6 passed and 1 failed.
***Test Failed*** 1 failures.
```

El resultado es que se logró pasar 6 pruebas y una no paso, se arregla el valor que debe devolver en el archivo `raizcuadrada.txt` y se vuelve a ejecutar la construcción y ejecución :
```
docker build -t pruebas-doctest .
Sending build context to Docker daemon 4.608 kB
Step 1 : FROM python:3.4
 ---> c40d327867e9
Step 2 : MAINTAINER Ernesto Crespo
 ---> Using cache
 ---> 3b1aced33b5e
Step 3 : WORKDIR /app
 ---> Using cache
 ---> 7dd09842cf61
Step 4 : COPY . /app
 ---> 47a9b0467413
Removing intermediate container 8a375d3abc0c
Successfully built 47a9b0467413

docker run pruebas-doctest python -m doctest -v raizcuadrada.txt
Trying:
    from raizcuadrada import Raiz
Expecting nothing
ok
Trying:
    Raiz(4)
Expecting:
    2.0
ok
Trying:
    Raiz(9)
Expecting:
    3.0
ok
Trying:
    Raiz(25)
Expecting:
    5.0
ok
Trying:
    Raiz(0)
Expecting:
    0.0
ok
Trying:
    Raiz(16)
Expecting:
    4.0
ok
Trying:
    Raiz(-1)
Expecting:
    Traceback (most recent call last):
    ...
    ValueError: a debe ser >= 0
ok
1 items passed all tests:
   7 tests in raizcuadrada.txt
7 tests in 1 items.
7 passed and 0 failed.
Test passed.
```

Ahora si se logró pasar todas las pruebas de doctest.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
