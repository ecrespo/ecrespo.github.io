Title: Uso de docker-machine.  
Date: 2016-05-06 09:00
Category: Tutorial de Docker    
Tags: Canaima,Debian,Linux,Ubuntu, Docker, Docker-machine
lang: es  
translation: true

Docker-machine se usa para equipos con Windows o MACOSX, o para equipos que no se le puede instalar docker (engine). Se usa como un cliente para un servidor docker.

Este artículo se basa en la documentación oficial en inglés que se encuentra en el siguiente [enlace](https://docs.docker.com/machine/get-started/), y en el siguiente [tutorial](https://devopscube.com/docker-machine-tutorial-getting-started-guide/).

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

17. [Ejecutar una prueba de unittest en Python con un contenedor Docker.](https://www.seraph.to/ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker.html#ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker) 

18. [Montar una Plataforma como servicio (PaaS) con Dokku (docker)](https://www.seraph.to/montar-una-plataforma-como-servicio-paas-con-dokku-docker.html#montar-una-plataforma-como-servicio-paas-con-dokku-docker).  

Para probar el uso de `docker-machine`, se tiene una máquina virtual con IP 192.168.1.102 donde se tiene unas imagenes de docker, y un equipo donde se instalará el `docker-machine` (qué será mí equipo local).

En el equipo se instalará `docker-machine` de la siguiente manera:
```
#curl -L https://github.com/docker/machine/releases/download/v0.4.0/docker-machine_linux-amd64 > /usr/local/bin/docker-machine

#chmod a+x  /usr/local/bin/docker-machine
```

Para probar que funciona se ejecuta la versión de `docker-machine`:
```
#docker-machine -v
docker-machine version 0.4.0 (9d0dc7a)
```

Crear un `docker-machine` en virtualbox:
```
$ docker-machine create --driver virtualbox test
```
En este caso se crea un contenedor docker que se conecta a virtualbox llamado test.

A continuación se muestra la salida del comando anterior:

![](./images/usodedockermachine-1.png)

Como lo muestra la imagen, se crea el docker test, se baja una imagen iso llamada boot2docker.

En la siguiente imagen se muestra a virtualbox con la máquina virtual test:

![](./images/usodedockermachine-2.png)

Al acceder a la máquina virtual desde virtualbox se tiene lo siguiente:

![](./images/usodedockermachine-3.png)

Para ver como se conecta a la máquina se ejecuta el siguiente comando:
```
$docker-machine env test
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.100:2376"
export DOCKER_CERT_PATH="/home/ernesto/.docker/machine/machines/test"
export DOCKER_MACHINE_NAME="test"
## Run this command to configure your shell: 
## eval "$(docker-machine env test)"
```
Para configurar el shell se ejecuta el siguiente comando:
```
eval "$(docker-machine env test)"
```
Para listar las máquinas se ejecuta el siguiente comando:
```
docker-machine ls
NAME   ACTIVE   DRIVER       STATE     URL                         SWARM
test   *        virtualbox   Running   tcp://192.168.99.100:2376
```

Para ver la IP que está usando test se ejecuta:
```
$ docker-machine ip test
192.168.99.100
```
Correr un servidor nginx en el puerto 8000 en un contenedor:
```
docker run -d -p 8000:80 nginx
```
Para ver el servidor se ejecuta el siguiente comando:
```
curl $(docker-machine ip test):8000
```
Y el resultado es:

![](./images/usodedockermachine-4.png)

Para terminar se detiene el `docker-machine` y se elimina:
```
$docker-machine stop test
$ernesto@jewel:~$ docker-machine rm test
Successfully removed test
```

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
