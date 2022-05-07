Title: Crear una imagen Docker de Redis 
Date: 2016-07-16 11:00
Category: Tutorial de Docker
Tags: Linux,Python,Ubuntu,Docker, Redis
lang: es
translation: true

Redis es un motor de base de datos en memoria, basado en almacenamiento en tablas hash(clave/valor) ([tomado de wikipedia](https://es.wikipedia.org/wiki/Redis)).

En este artículo se construirá la imagen de Redis a partir de una imagen base de Debian, el artículo se basa en un [artículo en inglés del sitio de Docker](https://docs.docker.com/engine/examples/running_redis_service/). 

Para subir la imagen a docker hub se sigue el artículo de [uso de docker en debian jessie parte 1](https://www.seraph.to/uso-de-docker-en-debian-jessie-parte-1.html).

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

29. [Instalar gitlab-runner de gitlab-ci por medio de Docker](https://www.seraph.to/ejecutar-una-prueba-de-integracion-continua-con-gitlab-ci-y-gitlab-runner.html#ejecutar-una-prueba-de-integracion-continua-con-gitlab-ci-y-gitlab-runner)

30. [Crear datos JSON a partir de un diccionario en Flask (parte 1) (actualización- Docker)](https://www.seraph.to/crear-datos-json-a-partir-de-un-diccionario-en-flask-parte-1-actualizacion-docker.html#crear-datos-json-a-partir-de-un-diccionario-en-flask-parte-1-actualizacion-docker)

31. [Correr sonarqube desde un contenedor Docker](https://www.seraph.to/correr-sonarqube-desde-un-contenedor-docker.html#correr-sonarqube-desde-un-contenedor-docker)


El archivo `Dockerfile` contendrá lo siguiente:
```
#Se usa debian como imagen base
FROM debian
#Se define el mantenedor de la imagen
MAINTAINER Ernesto Crespo <ecrespo@gmail.com>
#Se actualiza la lista de paquetes
RUN apt-get update
#Se instala redis-server y redis-tools
RUN apt-get install -y redis-server redis-tools 
#Se limpia la cache de paquetes deb
RUN apt-get clean

#Se expone el puerto 6379
EXPOSE      6379
#Inicio del servicio redis
ENTRYPOINT  ["/usr/bin/redis-server"]
```

Ahora se consruye la imagen (asociandolo a mi cuenta de docker hub):
```
docker build -t ecrespo/redis .
```
Se listan las imágenes: 
```
docker images 
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
ecrespo/redis       latest              841b6e9266f8        3 minutes ago       136.9 MB
redis               latest              4465e4bcad80        4 weeks ago         185.7 MB
debian              latest              1b088884749b        5 weeks ago         125.1 MB
```

Correr el servicio ejecutando:
```
docker run --name redis -d --restart always -p 6379:6379 ecrespo/redis 
```

Al listar los procesos se tiene redis corriendo:
```
docker ps 
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
0af1cdf134d7        ecrespo/redis       "/usr/bin/redis-serve"   9 seconds ago       Up 4 seconds        0.0.0.0:6379->6379/tcp   redis
```
Para probar redis se instala en el equipo `redis-tools`:
```
#apt-get install redis-tools
```
Desde la línea de comandos se ejecuta `redis-cli`, a continuación se muestra una figura del ejemplo: 

![](./images/crearunaimagendockerderedis-1.png)

Se hace un commit con el contendor de redis que está corriendo:
```
docker commit 0af1cdf134d7 ecrespo/redis
```
Luego se sube a docker hub:
```
docker push   ecrespo/redis
```

Ahora se creará un contenedor para la aplicación, se enlazará el contenedor redis con el contenedor cliente: 
```
docker run --link redis:db -i -t debian /bin/bash
```
Dentro del contenedor se ejecutan los siguientes comandos:
```
apt-get update  
apt-get install redis-tools  
service redis-server stop  
```
Como se enlazó el contenedor actual con el contenedor de redis, este contenedor contiene unas variables de ambiente, para visualizarlas se ejecuta el siguiente comando:
```
env | grep DB_
DB_NAME=/tiny_poincare/db
DB_PORT_6379_TCP_PORT=6379
DB_PORT=tcp://172.17.0.2:6379
DB_PORT_6379_TCP=tcp://172.17.0.2:6379
DB_PORT_6379_TCP_ADDR=172.17.0.2
DB_PORT_6379_TCP_PROTO=tcp
```

Para conectarse desde el contenedor que corre Debian al de redis se ejecuta:
```
redis-cli -h $DB_PORT_6379_TCP_ADDR
172.17.0.2:6379> set docker "Conectandose desde un contenedor debian al contenedor redis"
OK
172.17.0.2:6379> get docker
"Conectandose desde un contenedor debian al contenedor redis"
172.17.0.2:6379> 
```
A continuación se muestra una figura de la ejecución:

![](./images/crearunaimagendockerderedis-2.png)


Y se listan los contenedores ejecutándose:

![](./images/crearunaimagendockerderedis-3.png)


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)


