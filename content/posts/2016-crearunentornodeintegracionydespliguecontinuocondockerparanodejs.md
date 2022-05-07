Title: Crear un entorno de Integración y Despligue continue con Docker para node.js   
Date: 2016-03-26 09:00  
Category: Tutorial Python  
Tags: Python,node.js,Docker,Despliegue Continuo,DevOps,Integración Continua
lang: es  
translation: true 

Continuando con los artículos de Docker, está vez se muestra como tener un entorno de integración continua CI y de despliegue continuo CD con Docker para una aplicación web con node.js.

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

Se creo un directorio llamado `nodejs` que contendrá lo siguiente:
```
nodejs
├── app.js
├── Dockerfile
└── package.json
```
Dentro del directorio se tiene el archivo javascript llamado `app.js`, se tiene el archivo `Dockerfile` y el otro el `package.json`. 

El archivo `app.js` contiene lo siguiente:
```
// se crea la instancia de http
var http = require('http');
// Se crea la instancia del servidor donde se define el tipo del Content-type como text/plain
//Devuelve un hola mundo particular.
var server = http.createServer(function (request, response) {
        response.writeHead(200, {"Content-Type": "text/plain"});
        response.end("Hola mundo desde un contenedor Docker con nodejs.");
});
//El servidor escuchará el puerto 8000.
server.listen(8000);
//se devuelve un mensaje en la consola que se ejecuta el servidor web.
console.log("Server running at http://127.0.0.1:8000/");
```
El archivo `package.json` contiene lo siguiente:
```
{
    "name": "hola-mundo",
    "description": "hola mundo",
    "version": "0.0.1",
    "private": true,
    "dependencies": {
        "express": "3.x"

    },
    "scripts": {"start": "node app.js"}

}
```
Se le da el nombre de la aplicación, su descripción, la versión, que es privada y en las dependencias se instala express la versión 3.x, por último el script inicia la aplicación `app.js`.

Ahora se explicará el archivo `Dockerfile`:
```
FROM google/nodejs
MAINTAINER Ernesto Crespo <ecrespo@gmail.com>
WORKDIR /app
ADD package.json /app/
RUN npm install
ADD . /app
EXPOSE 8000
CMD []
ENTRYPOINT ["/nodejs/bin/npm", "start"]
```

Se descargará `nodejs` del repositorio que maneja google, se define el mantenedor de la imagen, el directorio de trabajo es `/app`, se agrega el archivo `package.json` al directorio de trabajo, se ejecuta `npm install`, se agrega el directorio app que se encuentra en la estructura de directorio ya explicada, se expone el puerto 8000, CMD se pasa [] y el entrypoint inicia npm. .

Para construir la imagen se ejecuta:
```python
docker build -t nodejs_img .
```
Al ejecutar `docker images` se tiene la imagen `nodejs_img`:
```
docker images 
REPOSITORY                    TAG                 IMAGE ID            CREATED              SIZE
nodejs_img                    latest              38d1802c8726        About a minute ago   501.6 MB
```

Ahora se ejecuta el contenedor:
```python
docker run -p 8000:8000 nodejs_img

> hola-mundo@0.0.1 start /app
> node app.js

Server running at http://127.0.0.1:8000/
```

Al abrir el navegador en esa dirección se tiene:

![](./images/crearunentornodeintegracionydespliguecontinuocondockerparanodejs-1.png)

Se puede modificar el archivo `app.js` agregando lo siguiente:
```
var http = require('http');
var server = http.createServer(function (request, response) {
        response.writeHead(200, {"Content-Type": "text/plain"});
        response.end("Hola mundo desde un contenedor Docker con nodejs, prueba modificando al vuelo");
});

server.listen(8000);

console.log("Server running at http://127.0.0.1:8000/");
```
Se detiene el contenedor y se vuelve a ejecutar:
```python
docker ps 
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
ee8395c6c1b0        nodejs_img          "/nodejs/bin/npm star"   4 minutes ago       Up 4 minutes        0.0.0.0:8000->8000/tcp   clever_shirley

docker stop ee8395c6c1b0
ee8395c6c1b0
```

Para que se refleje los cambios del archivo `app.js` se reconstruye la imagen del docker y luego se vuelve a iniciar el contenedor:
```python
docker build -t nodejs_img .
docker run -p 8000:8000 -v "$PWD":/app nodejs_img 

> hola-mundo@0.0.1 start /app
> node app.js


Server running at http://127.0.0.1:8000/
```
Y al abrir el navegador en el url:

![](./images/crearunentornodeintegracionydespliguecontinuocondockerparanodejs-2.png)

Se puede crear script para parar, borrar y reconstruir las imagenes haciendo más fácil el proceso de integración continua y despliegue continuo.

Más información la pueden conseguir en el artículo: [Docker en la ejecución de test de integración en NodeJS](http://abirtone.com/docker/2015/07/28/uso-de-docker-en-aplicacion-de-nodejs/)


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
