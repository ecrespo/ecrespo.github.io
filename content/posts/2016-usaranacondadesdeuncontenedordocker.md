Title: Usar Anaconda desde un contenedor Docker.   
Date: 2016-03-26 09:00    
Category: Tutorial Python   
Tags: Python,Docker,Anaconda,Ingeniería de Datos,Ciencia de Datos,Dockerhub  
lang: es  
translation: true 

Continuando con artículos relacionados con Docker. Está vez se mostrará como correr Anaconda desde una imagen Docker.

A continuación les dejo los artículos anteriores:
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




Lo primero que se estarán preguntando es, ¿Qué es Anaconda?. 

La respuesta se la pueden conseguir en el enlace oficial del sitio [continuum](http://abirtone.com/docker/2015/07/28/uso-de-docker-en-aplicacion-de-nodejs/):

Anaconda es un manejador de paquetes (libre y fácil de instalar),manejo de entorno, distribución de Python, y una colección de más de 720 paquetes opensource con soporte comunitario. Además se puede instalar más de mil paquetes con el comando `conda install <paquete>`, funciona en Linux, Windows y OSX.  Anaconda es la herramienta hecha para cientificos de datos.  

¿Quienes más usan anaconda? 
- Científicos de Datos.  
- Desarrolladores.  
- Ingenieros de Datos.  
- DevOps.  
- Analistas de negocios.   
- 
El procedimiento para usar anaconda lo explican en este [enlace](https://docs.continuum.io/new-anaconda-start-here).

Las imágenes existentes de anaconda la pueden ver en este [enlace](https://hub.docker.com/).

Para ver las imágenes de la gente de continuum se realiza una búsqueda con docker:
```
$docker search continuumio

NAME                                   DESCRIPTION                                           STARS     OFFICIAL   AUTOMATED
continuumio/anaconda                 Powerful and flexible python distribution    27                   [OK]
continuumio/miniconda                Powerful and flexible package manager     14                   [OK]
continuumio/anaconda3                                                                               10                   [OK]
continuumio/miniconda3                                                                                5                    [OK]
continuumio/memex_explorer      memex explorer app                                   1                    
continuumio/solr                          solr 10.4.2 + tika                                       0                    
continuumio/tika                          Tika 1.9                                                     0                    
continuumio/binstar-build-linux64                                                                  0                    [OK]
continuumio/kibana                                                                                       0                    
continuumio/imagecat                   Docker Container for ImageCat                0                    
continuumio/banana                                                                                      0
```
Luego se bajará la imagen miniconda:
```
$ docker pull continuumio/miniconda

Using default tag: latest
latest: Pulling from continuumio/miniconda
a3ed95caeb02: Pull complete 
79362e2488a1: Pull complete 
41938770486e: Pull complete 
1c66b99d17cb: Pull complete 
33e1cf31bc39: Pull complete 
Digest: sha256:5d27e59a93068184fc6dd63043746ad35aa15dd2862ff0babd391bc3c05a5fc4
Status: Downloaded newer image for continuumio/miniconda:latest
```
Ahora se puede iniciar un contenedor a partir de la imagen que se descargó:
```
$ docker run -t -i continuumio/miniconda /bin/bash
root@f7115572fad4:/# 
```
Se prueba que conda está instalado en ese contenedor:
```
ernesto@jewel:~/dockerfiles$ docker run -t -i continuumio/miniconda /bin/bash
root@f7115572fad4:/# conda info
Current conda install:

             platform : linux-64
        conda version : 3.19.0
  conda-build version : not installed
       python version : 2.7.11.final.0
     requests version : 2.9.0
     root environment : /opt/conda  (writable)
  default environment : /opt/conda
     envs directories : /opt/conda/envs
        package cache : /opt/conda/pkgs
         channel URLs : https://repo.continuum.io/pkgs/free/linux-64/
                        https://repo.continuum.io/pkgs/free/noarch/
                        https://repo.continuum.io/pkgs/pro/linux-64/
                        https://repo.continuum.io/pkgs/pro/noarch/
          config file : None
    is foreign system : False

```

Ahora se instalará `scipy` vía el comando `conda`:
```
root@f7115572fad4:/# conda install scipy
Fetching package metadata: ....
Solving package specifications: ....................
Package plan for installation in environment /opt/conda:

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    libgfortran-3.0            |                0         261 KB
    mkl-11.3.1                 |                0       121.2 MB
    openssl-1.0.2g             |                0         3.2 MB
    sqlite-3.9.2               |                0         3.9 MB
    numpy-1.10.4               |           py27_1         6.0 MB
    requests-2.9.1             |           py27_0         605 KB
    setuptools-20.3            |           py27_0         452 KB
    wheel-0.29.0               |           py27_0          81 KB
    conda-4.0.5                |           py27_0         185 KB
    pip-8.1.1                  |           py27_0         1.5 MB
    scipy-0.17.0               |      np110py27_2        30.1 MB
    ------------------------------------------------------------
                                           Total:       167.3 MB

The following NEW packages will be INSTALLED:

    libgfortran: 3.0-0             
    mkl:         11.3.1-0          
    numpy:       1.10.4-py27_1     
    scipy:       0.17.0-np110py27_2

The following packages will be UPDATED:

    conda:       3.19.0-py27_0 --> 4.0.5-py27_0      
    openssl:     1.0.2d-0      --> 1.0.2g-0          
    pip:         7.1.2-py27_0  --> 8.1.1-py27_0      
    requests:    2.9.0-py27_0  --> 2.9.1-py27_0      
    setuptools:  18.8.1-py27_0 --> 20.3-py27_0       
    sqlite:      3.8.4.1-1     --> 3.9.2-0           
    wheel:       0.26.0-py27_1 --> 0.29.0-py27_0     

Proceed ([y]/n)? y
```
Otra opción es bajar continuumio/anaconda, que tiene la paqueteria base:
```
$ docker pull continuumio/anaconda
```
Y se ejecuta el contenedor:
```
ernesto@jewel:~/dockerfiles$ docker run -t -i continuumio/anaconda /bin/bash
root@f7115572fad4:/#
```
##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
