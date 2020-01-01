Title: Instalar gitlab-runner de gitlab-ci por medio de Docker
Date: 2016-06-13 11:00 
Category: Tutorial de Docker
Tags: Canaima,Linux,General,Python,Ubuntu,gitlab,gitlab-ci,Docker
lang: es  
translation: true  

En un artículo anterior se explicó como instalar gitlab-ce por medio de Docker ([enlace](https://www.seraph.to/instalar-gitlab-por-medio-de-docker.html)).


El problema es que al gitlab le falta configurar lo de Integración Continua (CI), para ello es necesario instalar gitlab-runner (en el mismo equipo, en otro equipo o como un contenedor aparte). 


La descripción sobre las características de gitlab-ci la pueden ver en el siguiente [enlace](https://about.gitlab.com/product/continuous-integration/).


La guía para instalar gitlab-runner lo pueden revisar en el siguiente [enlace](https://gitlab.com/gitlab-org/gitlab-runner#installation).

Para el caso de docker se puede ver la documentación [siguiente](https://about.gitlab.com/2016/05/23/gitlab-container-registry/).


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

28. [Analizar código python con pylint desde Docker](https://www.seraph.to/analizar-codigo-python-con-pylint-desde-docker.html#analizar-codigo-python-con-pylint-desde-docker)

Lo primero que se tiene que hacer es bajar la imagen de Docker para gitlab-runner:
```
docker pull gitlab/gitlab-runner
```
Luego se inicia el servicio de registro de gitlab-runner:
```
docker run -d --name gitlab-runner --restart always -v /srv/gitlab-runner/config:/etc/gitlab-runner -v /var/run/docker.sock:/var/run/docker.sock gitlab/gitlab-runner
```
De esta forma el gitlab-runner usará el docker que se encuentra en la máquina anfitrión, se tiene acceso a la configuración de gitlab-runner desde la máquina anfitrión.

Al ejecutar un `docker ps` se tiene lo siguiente:
```
docker ps 
CONTAINER ID        IMAGE                     COMMAND                  CREATED             STATUS              PORTS                                                            NAMES
13ffb573fadf        gitlab/gitlab-runner      "/entrypoint run --us"   3 hours ago         Up 3 hours                                                                           gitlab-runner
b483b38fe29e        gitlab/gitlab-ce:latest   "/assets/wrapper"        12 days ago         Up 4 hours          0.0.0.0:22->22/tcp, 0.0.0.0:443->443/tcp, 0.0.0.0:9080->80/tcp   gitlab1
```
Como se nota ya se tienen activo gitlab-ce y gitlab-runner.

Para registrar un proyecto se ejecuta en la máquina el siguiente comando:
```
docker exec -ti  13ffb573fadf  gitlab-runner register 
```
Lo que viene a continuación es registrar un proyecto que se encuentre en gitlab. En este caso se va a crear un proyecto en gitlab-ce y se va a la configuración del mismo, ahí se selecciona la parte de runners:

Se tiene el proyecto `prueba-nodejs`:

![](./images/instalargitlabrunnerdegitlabcipormediodedocker-1.png)

Los datos importantes son:
```
URL:http://192.168.0.60:9080/ci
TOKEN:6kN_Uo_j2YitsJkh7q94
```
A continuación se ejecuta el register:
```
docker exec -ti  13ffb573fadf  gitlab-runner register 
```
Y se pasan los datos que pide (la siguiente figura muestra la configuración del registro del proyecto):

![](./images/instalargitlabrunnerdegitlabcipormediodedocker-2.png)

Se le pasó el url, el token, luego pregunta la descripción del proyecto en este caso `prueba-nodejs`, luego unas etiquetas del mismo, se va a usar docker y por último la imagen base de Docker que se va a usar.

Para terminar se muestra una imagen de la configuración del runner que indica que el runner y gitlab se encuentran conectados:

![](./images/instalargitlabrunnerdegitlabcipormediodedocker-3.png)

Y la información de esa conexión:

![](./images/instalargitlabrunnerdegitlabcipormediodedocker-4.png)

En próximo artículo se explicará como correr una prueba de CI. 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
