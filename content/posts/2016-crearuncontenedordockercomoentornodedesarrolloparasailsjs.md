Title: Crear un contenedor Docker como entorno de desarrollo para sails.js
Date: 2016-05-24 09:00
Category: Tutorial de Docker  
Tags: Canaima,Debian,Linux,Ubuntu,Docker, Sails.js
lang: es
translation: true

Este artículo toca el tema de usar un contenedor Docker como entorno de Desarrollo.

La idea es tener las dependencias del proyecto en el contenedor y poder desarrollar la aplicación fuera del contenedor por medio de persistencia como un volumen.

Este artículo se basa en la info del siguiente repositorio en [github](https://github.com/mwhahaha/docker-sails-test).

En este artículo se usa el framework sails.js, pero  no en profundidad, simplemente crear el proyecto y ejecutarlo. Para más información pueden revisar el siguiente [tutorial](https://code.tutsplus.com/tutorials/introduction-to-sailsjs--net-35390).

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

Se tiene un directorio `ProyectoNuevo` el cual es el proyecto `sails.js` creado con el comando:
```
sails new ProyectoNuevo

ProyectoNuevo
├── api
│   ├── controllers
│   ├── models
│   ├── policies
│   │   └── sessionAuth.js
│   ├── responses
│   │   ├── badRequest.js
│   │   ├── created.js
│   │   ├── forbidden.js
│   │   ├── notFound.js
│   │   ├── ok.js
│   │   └── serverError.js
│   └── services
├── app.js
├── assets
│   ├── favicon.ico
│   ├── images
│   ├── js
│   │   └── dependencies
│   │       └── sails.io.js
│   ├── robots.txt
│   ├── styles
│   │   └── importer.less
│   └── templates
├── config
│   ├── blueprints.js
│   ├── bootstrap.js
│   ├── connections.js
│   ├── cors.js
│   ├── csrf.js
│   ├── env
│   │   ├── development.js
│   │   └── production.js
│   ├── globals.js
│   ├── http.js
│   ├── i18n.js
│   ├── locales
│   │   ├── de.json
│   │   ├── en.json
│   │   ├── es.json
│   │   ├── fr.json
│   │   └── _README.md
│   ├── local.js
│   ├── log.js
│   ├── models.js
│   ├── policies.js
│   ├── routes.js
│   ├── session.js
│   ├── sockets.js
│   └── views.js
├── Gruntfile.js
├── package.json
├── README.md
├── tasks
│   ├── config
│   │   ├── clean.js
│   │   ├── coffee.js
│   │   ├── concat.js
│   │   ├── copy.js
│   │   ├── cssmin.js
│   │   ├── jst.js
│   │   ├── less.js
│   │   ├── sails-linker.js
│   │   ├── sync.js
│   │   ├── uglify.js
│   │   └── watch.js
│   ├── pipeline.js
│   ├── README.md
│   └── register
│       ├── build.js
│       ├── buildProd.js
│       ├── compileAssets.js
│       ├── default.js
│       ├── linkAssetsBuild.js
│       ├── linkAssetsBuildProd.js
│       ├── linkAssets.js
│       ├── prod.js
│       └── syncAssets.js
└── views
    ├── 403.ejs
    ├── 404.ejs
    ├── 500.ejs
    ├── homepage.ejs
    └── layout.ejs
```
El directorio donde se encuentra el proyecto se llama `sailsjs` con el siguiente contenido:
```
sailsjs
├── Dockerfile
├── ProyectoNuevo
└── run.sh
```
El contenido de ProyectoNuevo se mostró arriba.

El archivo run.sh contiene un script para levantar sails por medio de sails lift:
```
#!/bin/bash

cd /app/ProyectoNuevo
sails lift
```

El archivo Dockerfile contiene lo siguiente:

```
#Se usa la imagen de nodejs de google
FROM google/nodejs
#El mantenedor de la imagen
MAINTAINER Ernesto Crespo <ecrespo@gmail.com>
#El usuario del contenedor
USER root
#Se define el directorio de trabajo
WORKDIR /app
#Se copia el ProyectoNuevo a /app/
ADD ProyectoNuevo /app/
#Se instala sails en el contenedor
RUN npm -g install sails
#Se copia el script run.sh al directorio de trabajo
ADD run.sh /app/run.sh
#Se coloca el script con permiso de ejecución
RUN chmod a+x /app/run.sh

#Se expone el puerto 8080
EXPOSE 8080
#Se ejecuta el script
CMD ["/app/run.sh"] 
```

Para construir la imagen se ejecuta:
```
docker build -t sails-prueba . 
```
Para correr la imagen se ejecuta:
```
docker run -p 8080:8080 -v $PWD:/app  -ti sails-prueba
```
A continuación se muestra una imagen luego de la ejecución del comando:

![](./images/crearuncontenedordockercomoentornodedesarrolloparasailsjs-1.png)

Se listan los contenedores:

![](./images/crearuncontenedordockercomoentornodedesarrolloparasailsjs-2.png)

Se está ejecutando el contenedor de sails junto al de mongodb ya explicado en el capítulo [anterior](http://blog.crespo.org.ve/2016/05/crear-una-imagen-docker-para-mongodb-3.html).

Ahora se abre el navegador en localhost al puerto 8080:

![](./images/crearuncontenedordockercomoentornodedesarrolloparasailsjs-3.png)

La idea al colocar el directorio persistente es que se pueda ir modificando el directorio del proyecto, levantar el contenedor sin necesidad de reconstruir la imagen del mismo. 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
