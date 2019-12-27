Title: Usar Jupyter Notebook desde un contenedor de Docker  
Date: 2016-03-26 11:00  
Category: Tutorial Python  
Tags: Python, Docker, Jupyter Notebook, DevOps
lang: es  
translation: true  

Jupyter Notebook es una aplicación web que permite crear y compartir documentos que  contienen código, gráficos y texto. Sus usos incluyen limpieza y transformación de datos, simulación numérica, modelado estadístico, machine learning y mucho más. Más información lo pueden ver en este [enlace](https://jupyter.org/).

La idea es ejecutar `jupyter notebook` desde un contenedor docker donde se guardarán los archivos generados en el directorio definido por medio de volumen.

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

Existe varias imagenes de Docker de la gente de jupyter, la que se va a usar es la de [jupyter notebook](https://hub.docker.com/r/jupyter/notebook/).  

Para ejecutar el contenedor ejecutamos lo siguientes comandos:
```
$docker run --rm -it -p 8888:8888 -v "$(pwd):/notebooks" jupyter/notebook
```
Al ejecutar el comando se tiene lo que muestra la siguiente imagen:

![](./images/usarjupyternotebookdesdeuncontenedordedocker-1.png)

El puerto externo al contenedor será el 8888, igual que el interno, el volumen se maneja desde el directorio donde se ejecuta el comando anterior. 

Desde un navegador se abre el siguiente enlace: http://localhost:8888/ .

![](./images/usarjupyternotebookdesdeuncontenedordedocker-2.png)

Se crea un documento donde se realiza una serie de instrucciones de python y se salva con nombre prueba-python:

![](./images/usarjupyternotebookdesdeuncontenedordedocker-3.png)

Al ejecutar un `ls -l` en el directorio donde se inició el contenedor se tiene el archivo `prueba-python.ipynb`:
```
 ls -l notebooks/
total 4
-rw-r--r-- 1 root root 1390 mar 26 20:04 prueba-python.ipynb
```
Por medio de la opción de volumen se está compartiendo el directorio notebooks del contenedor en el equipo anfitrión.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
