Title: Usar dockerui para la gestión de imágenes y contenedores de Docker  
Date: 2016-05-26 11:00  
Category: Tutorial de Docker  
Tags: Canaima,Debian,Linux,Ubuntu, Docker,Dockerui
lang: es
translation: true

Docker UI es una interfaz web que permite administrar las imágenes de Docker, correr contenedores.

Se explicará el proceso de instalación y uso de dockerui.

Este artículo se basa de un artículo en inglés que lo pueden revisar en el siguiente enlace.

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

El proceso de instalación para Debian Jessie lo pueden ver en el primer artículo, pero, sí usa otra distribución puede leer el enlace en inglés del cual se basa este artículo que explican la instalación para Fedora u otras distros.

DockerUI se puede bajar como una imagen Docker, para correr el contenedor se ejecuta el siguiente comando: 
```
docker run -d -p 9000:9000 --privileged -v /var/run/docker.sock:/var/run/docker.sock dockerui/dockerui
```
Nota: El repositorio se encuentra en Docker Hub, se usó otro repositorio de dockerui.
```
docker run -d -p 9000:9000 --privileged -v /var/run/docker.sock:/var/run/docker.sock abh1nav/dockerui
```
La aplicación web corre en el puerto 9000, se le da todos los privilegios y se accede al socker del docker que corre en el equipo anfitrión. 


A continuación se muestra la página principal de dockerui:


![](./images/usardockeruiparalagestiondeimagenesycontenedoresdedocker-1.png)

![](./images/usardockeruiparalagestiondeimagenesycontenedoresdedocker-2.png)


Al darle a la sección de imágenes se listan todas las imágenes que se tienen en el equipo, allí se pueden remover imágenes:

![](./images/usardockeruiparalagestiondeimagenesycontenedoresdedocker-3.png)

Al darle click a una imagen aparecerá el botón crear:

![](./images/usardockeruiparalagestiondeimagenesycontenedoresdedocker-4.png)

Luego aparece una ventana donde se le define el comando a ejecutar, el nombre del contenedor, cuanta memoria y memoria swap va a usar, y el volumen:

![](./images/usardockeruiparalagestiondeimagenesycontenedoresdedocker-5.png)

En la sección de contenedores se puede, iniciar, reiniciar, detener, matar o remover los contenedores:

![](./images/usardockeruiparalagestiondeimagenesycontenedoresdedocker-6.png)


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
