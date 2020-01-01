Title: Crear una imagen Docker de RethinkDB  
Date: 2016-06-10 09:00   
Category: Tutorial de Docker
Tags: Canaima,Linux,Python,Ubuntu,Docker, RethinkDB
lang: es   
translation: true   

RethinkDB es una base de datos NoSQL, opensource, es una base de datos que almacena documentos en formato JSON, facilita la inserción, actualización y busqueda en tiempo real (más info en el sitio de [rethinkDB](https://www.rethinkdb.com/) y en [wikipedia](https://en.wikipedia.org/wiki/RethinkDB)).

La idea es construir una imagen de Docker por medio de un archivo Dockerfile, tomando como base Debian Jessie. Aunque se puede usar directamente la imagen de RethinkDB que se encuentra en el [hub de docker](https://hub.docker.com/_/rethinkdb/).

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

El archivo Dockerfile toma parte del archivo oficial del sitio de RethinkDB, la idea es crear la imagen a partir de Debian Jessie (el dockerfile lo pueden ver en el siguiente [enlace](https://github.com/rethinkdb/rethinkdb-dockerfiles/blob/d129775a6b33cb9e9a3ced40edda31ba9016a647/jessie/2.3.4/Dockerfile)). 

El archivo `Dockerfile` es el siguiente:
```
#Base de Debian Jessie
FROM debian
#Mantenedor
MAINTAINER Ernesto Crespo <ecrespo@gmail.com>


# instalar RethinkDB
RUN apt-get update
RUN apt-get install -y software-properties-common
RUN apt-get install -y wget 
RUN sh -c 'echo "deb http://download.rethinkdb.com/apt `lsb_release -cs` main" | tee /etc/apt/sources.list.d/rethinkdb.list'
RUN sh -c 'wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | apt-key add -'
RUN apt-get update
RUN apt-get install -y rethinkdb

#Se define el volumen donde se almacena los datos
VOLUME ["/data"]

#Se define el directorio de trabajo
WORKDIR /data

#Se ejecuta rethinkdb asociando todas las interfaces existentes en el contenedor
CMD ["rethinkdb", "--bind", "all"]

#   proceso, cluster webui
EXPOSE 28015 29015 8080
```

Para construir la imagen se ejecuta:
```
docker build -t debian-rethinkdb . 
```
Y para correr el contenedor (se asocia el volumen `/data` al directorio donde se ejecuta el contenedor):
```
docker run --name some-rethink -v "$PWD:/data" -d debian-rethinkdb
```
Para ver la interfaz administrativa vía web de rethingDB se ejecuta (caso chromium):
```
chromium "http://$(docker inspect --format  '{{ .NetworkSettings.IPAddress }}' some-rethink):8080"
```
A continuación se muestra una captura de pantalla de la aplicación web:

![](./images/crearunaimagendockerderethinkdb-1.png)

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)



