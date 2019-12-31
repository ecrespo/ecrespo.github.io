Title: Ejecutar una prueba de unittest en Python con un contenedor Docker.  
Date: 2016-03-27 09:00  
Category: Tutorial Python  
Tags: Python,unittest,Docker  
lang: es  
translation: true

En este artículo prácticamente se hará lo mismo que el artículo [anterior](https://www.seraph.to/ejecutar-una-prueba-de-doctest-con-un-contenedor-docker.html#ejecutar-una-prueba-de-doctest-con-un-contenedor-docker), pero se creará un archivo donde se define una clase la cual hará las pruebas unitarias.

La parte de pruebas unitarias se basa de un post anterior que se llama [Pruebas unitarias con unittest en Python](https://www.seraph.to/pruebas-unitarias-en-python-con-unittest.html).

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

16. [Ejecutar una prueba de doctest con un contenedor Docker](https://www.seraph.to/ejecutar-una-prueba-de-doctest-con-un-contenedor-docker.html#ejecutar-una-prueba-de-doctest-con-un-contenedor-docker).

Ahora se tendrán los siguientes archivos en el directorio `pruebas-doctest`:
```
pruebas-doctest
├── Dockerfile
├── raizcuadrada.py
├── raizcuadrada_test.py
└── raizcuadrada.txt
```
El Dockerfile, `raizcuadrada.py` y `raizcuadrada.txt` son los mismos del artículo [anterior](http://blog.crespo.org.ve/2016/03/ejecutar-una-prueba-de-doctest-con-un.html).

El archivo `raizcuadrada_test.py` tiene lo siguiente:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Se importa el módulo unittest y math
import unittest
#Se importa la funcion Raiz del modulo raizcuadrada
from raizcuadrada import Raiz

class RaizTest(unittest.TestCase):

    def test_Raiz(self):
        """Test para la raiz de nueve que devuelve 3 que debe pasar."""
        self.assertEqual(3, Raiz(9))

    def test_zero(self):
        """Test para la raiz de 0 que devuelve 0, que debe pasar."""
        self.assertEqual(0, Raiz(0))

        
    def test_negative(self):
        """Test para la raiz de un número negativo, que debe fallar."""
        # Este debe devolver un ValueError, pero se espera un IndexError.
        self.assertRaises(IndexError, Raiz(-10))


if __name__ == '__main__':
    #Se ejecuta la prueba unitaria
    unittest.main()

```
Ahora se reconstruye  la imagen de Docker:
```
docker build -t pruebas-doctest .
Sending build context to Docker daemon  7.68 kB
Step 1 : FROM python:3.4
 ---> c40d327867e9
Step 2 : MAINTAINER Ernesto Crespo
 ---> Using cache
 ---> 3b1aced33b5e
Step 3 : WORKDIR /app
 ---> Using cache
 ---> 7dd09842cf61
Step 4 : COPY . /app
 ---> 842cd3bd051f
Removing intermediate container 140eaaf7935f
Successfully built 842cd3bd051f

```
Y se ejecuta la prueba:
```
docker run pruebas-doctest python raizcuadrada_test.py
.E.
======================================================================
ERROR: test_negative (__main__.RaizTest)
Test para la raiz de un número negativo, que debe fallar.
----------------------------------------------------------------------
Traceback (most recent call last):
  File "raizcuadrada_test.py", line 25, in test_negative
    self.assertRaises(IndexError, Raiz(-10))
  File "/app/raizcuadrada.py", line 22, in Raiz
    raise ValueError("a debe ser >= 0")
ValueError: a debe ser >= 0

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (errors=1)

```
Está primera prueba se preparó para que fallara, ahora se comenta el método de prueba negativa, se reconstruye la imagen y se vuelve a ejecutar:
```
docker build -t pruebas-doctest .
Sending build context to Docker daemon  7.68 kB
Step 1 : FROM python:3.4
 ---> c40d327867e9
Step 2 : MAINTAINER Ernesto Crespo
 ---> Using cache
 ---> 3b1aced33b5e
Step 3 : WORKDIR /app
 ---> Using cache
 ---> 7dd09842cf61
Step 4 : COPY . /app
 ---> 609702415974
Removing intermediate container e2174beb4f7c
Successfully built 609702415974

docker run pruebas-doctest python raizcuadrada_test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK

```

![](./images/ejecutarunapruebadeunittestenpythonconuncontenedordocker-1.png)


Se ejecutaron 2 test y pasaron. 

Ya con esta imagen de Docker se puede reusar en varios computadores teniendo el mismo ambiente de desarrollo. 


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
