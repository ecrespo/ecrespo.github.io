Title: Compartir imágenes Docker por medio de archivos tar   
Date: 2016-02-24 10:00  
Category: Tutorial de Docker
Tags: Linux,Debian,Docker
lang: es  
translation: true  

Uno de los puntos más importantes a la hora de trabajar con Docker es el compartir imágenes Docker aparte de usar Docker Hub.

Se tiene la exportación e importación de imágenes como opción almacenando y extrayendo a partir de archivos `tar`.

Se tienen los artículos anteriores sobre Docker:

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

Lo primero es ver que contenedores se tienen ejecutándose en el equipo:
```
$docker ps 
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS              PORTS                                                                    NAMES
b0c1163d1668        gitlab/gitlab-ce:latest   "/assets/wrapper"        4 weeks ago         Up 4 hours          0.0.0.0:80->80/tcp, 0.0.0.0:443->443/tcp, 0.0.0.0:8022->22/tcp           gitlab
b4d3c96f6dc9        jenkins                   "/bin/tini -- /usr/lo"   4 weeks ago         Up 4 hours          0.0.0.0:8080->8080/tcp, 0.0.0.0:50000->50000/tcp, 0.0.0.0:8122->22/tcp   jenkins
```

Se tienen dos contenedores ejecutándose, uno de gitlab y otro de jenkins.

Se realizará respaldo del contenedor con gitlab usando el comando `docker export`, pasando el id del contenedor de gitlab que es b0c1163d1668:
```
$docker export b0c1163d1668 > gitlab.tar
```
Al ejecutar `ls` se tiene el archivo `gitlab.tar`:  
```
ls -l
total 2201820
-rw-r--r-- 1 ernesto ernesto 1409662976 feb 24 16:15 gitlab.tar
```

Para usar la imagen a partir del archivo `tar` se importa la imagen: 
```
$ docker import - gitlab2 < gitlab.tar
sha256:020ea830b267080ce092f42b1b0f1a2d520b21b8a3393696f5271f42e4bd8d79
```
El nombre de la imagen es gitlab2, ahora se listan las imágenes que se tienen en el equipo:
```
$ docker images | grep gitlab
gitlab2                        latest              020ea830b267        About a minute ago   1.344 GB
gitlab/gitlab-ce               latest              db1c29be1030        6 weeks ago          1.326 GB
sameersbn/gitlab               latest              47d53c4a820a        10 weeks ago         675.7 MB
```
Si se quiere compartir la imagen con alguien, se puede subir el archivo `tar` a un servidor web y de ahí se puede bajar.  

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
