Title: Instalar Docker en Debian Jessie
Date: 2015-12-25 8:00
Category: Tutorial Linux
Tags: canaima,Debian,General,Linux,Ubuntu
lang: es
translation: true

Hace un tiempo me toco dictar un curso de empaquetado para Debian y un compañero preparo una máquina virtual de Virtualbox con [vagrant](https://www.vagrantup.com/) (un tutorial lo pueden revisar en el siguiente [enlace](https://styde.net/como-crear-un-entorno-de-desarrollo-virtual-con-vagrant/)).

Hubo un momento que dañamos algunos paquetes y recuperamos la imagen de forma rápida para continuar con el curso.

En mi caso como mi máquina personal no tengo como manejar varias máquinas virtuales con virtualbox preferí irme hacía la tecnología de contenedores con [Docker](https://www.docker.com/). [Pueden revisar wikipedia para saber más de docker.](https://es.wikipedia.org/wiki/Docker_(software))

La guía de instalación para Debian Jessie en inglés lo pueden encontrar en el siguiente [enlace](https://docs.docker.com/config/daemon/); y la guía de usuario en el siguiente [enlace](https://docs.docker.com/config/daemon/). El repositorio donde se alojan imágenes lo pueden revisar en este [enlace](https://hub.docker.com/).

0. Instalar soporte de https para los repositorios:
```
#apt-get install apt-transport-https
```
1. Borrar paquetes viejos o de lxc:
```
#apt-get purge lxc-docker* 
#apt-get purge docker.io*
```
2. Agregar la llave gpg de docker.io:
```
#apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys  58118E89F3A912897C070ADBF76221572C52609D 
```
3. Agregar el repositorio al `sources.list.d`:
```
vim /etc/apt/sources.list.d/docker.list

deb https://apt.dockerproject.org/repo debian-jessie main

```
4. Actualizar la lista de repositorios: 
```
#apt-get update
```
5. Verificar que se baja el paquete del repositorio correcto: 
```
#apt-cache policy docker-engine
```
6. Instalar docker:
```
#apt-get install docker-engine
```
7. Iniciar el demonio docker:
```
#service docker start
```
8. Verificar que se instaló correctamente:
```
# docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b901d36b6f2f: Pull complete 
0a6ba66e537a: Pull complete 
Digest: sha256:8be990ef2aeb16dbcb9271ddfe2610fa6658d13f6dfb8bc72074cc1ca36966a7
Status: Downloaded newer image for hello-world:latest

Hello from Docker.
This message shows that your installation appears to be working correctly.
``` 
9. Dar acceso de docker a usuarios no root:

9.1 Agregar el grupo docker si no existe:
```
$sudo groupadd docker
```
9.2 Agregar al usuario al grupo docker:
```
$ sudo gpasswd -a ${USER} docker
```
9.3 Reiniciar el demonio docker:
```
$sudo service docker restart
```
En siguientes artículos se mostrará el uso de docker, como crear imágenes y por último se creará un entorno para empaquetar para Debian.
Dejaré por acá las referencias para usarlas en un futuro:
Referencias:
1. [Instalación de docker en Debian.](https://docs.docker.com/install/linux/docker-ce/debian/)    
2. [Empaquetar con docker.](https://wiki.debian.org/PackagingWithDocker?highlight=%28%28Docker%29%29)  
3. [Docker intro and installation.](https://wiki.debian.org/PackagingWithDocker?highlight=%28%28Docker%29%29)  
4. [Docker image building.](https://docs.google.com/document/d/1f8iflnFSZxAU9FhoLQPEVlSKhVPXbtCaqTVPTTJb9yo/edit)  
5. [Docker Advanced volumes.](https://docs.google.com/document/d/1tgzbbc76tV82nxJCpHTSb-Y5tns8Uim8sLDExy12e5k/edit)  
6. [Debian/Ubuntu Package Developing with Docker.](https://sfxpt.wordpress.com/2013/11/10/debianubuntu-package-developing-with-docker/)    
7. [Debian/Ubuntu Package Developing with Docker, Continued.](https://sfxpt.wordpress.com/2013/11/17/debianubuntu-package-developing-with-docker-continued/)  
8. [Create docker image.](https://wiki.debian.org/Cloud/CreateDockerImage)  
9. [Artículo en español sobre docker y como cambiar los despliegues de docker. ](https://magmax.org/blog/docker/)
10. Algunos artículos del blog de Javier Garzas:   
10.1 [¿Qué es Docker? ¿Para qué se utiliza? Explicado de forma sencilla](http://www.javiergarzas.com/2015/07/que-es-docker-sencillo.html)  
10.2 [Entendiendo Docker. Conceptos básicos: Imágenes, Contenedores, Links… ](http://www.javiergarzas.com/2015/07/entendiendo-docker.html)  
10.3 [Para los que empiezan: crear y ejecutar una imagen propia en un contenedor Docker (1/2)](http://www.javiergarzas.com/2015/11/para-los-que-empiezan-crear-y-ejecutar-una-imagen-propia-en-un-contenedor-docker-12.html)
10.4 [Para los que empiezan: crear y ejecutar una imagen propia en un contenedor Docker (2/2)](http://www.javiergarzas.com/2015/11/para-los-que-empiezan-crear-y-ejecutar-una-imagen-propia-en-un-contenedor-docker-22.html)  
10.5 [¿Y si queremos orquestar varios contenedores Docker? Microservicios, Docker Compose, Yaml… ¡Qué jaleo! (1/2)](http://www.javiergarzas.com/2015/11/y-si-queremos-orquestar-varios-contenedores-docker-microservicios-docker-compose-yaml-que-jaleo-12.html)  
10.6 [¿Y si queremos orquestar varios contenedores Docker? Microservicios, Docker Compose, Yaml… ¡Qué jaleo! (2/2)](http://www.javiergarzas.com/2015/12/y-si-queremos-orquestar-varios-contenedores-docker-microservicios-docker-compose-yaml-que-jaleo-22.html)  
11. [CONTAINERIZE YOUR WEB DEVELOPMENT: HOW DOCKER IS SOLVING REAL WORLD PROBLEMS FOR WEB DEVELOPERS!](https://usersnap.com/blog/docker-for-web-developers/?utm_source=quora&utm_medium=referral&utm_campaign=quora_docker)  
12. [Continuous Inspection en Java](https://sites.google.com/site/practicadesarrollosoft/temario/continuous-inspection/continuous-inspection-en-java)  
13. [Imagen docker de sonarqube](https://hub.docker.com/_/sonarqube/)  
14. [Imagen docker de Jenkins](https://hub.docker.com/_/jenkins/)  
15. [Imagen docker para debian jessie](https://hub.docker.com/_/debian/)  
16. [AUDITORÍA Y ANÁLISIS DE VULNERABILIDADES EN DOCKER](http://www.securitybydefault.com/2015/12/auditoria-y-analisis-de.html)  
17. [Docker en la ejecución de test de integración en NodeJS](http://abirtone.com/docker/2015/07/28/uso-de-docker-en-aplicacion-de-nodejs/)  
18. [Docker Explicado: Cómo crear Contenedores de Docker corriendo en Memcached](https://www.digitalocean.com/community/tutorials/docker-explicado-como-crear-contenedores-de-docker-corriendo-en-memcached-es)

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)