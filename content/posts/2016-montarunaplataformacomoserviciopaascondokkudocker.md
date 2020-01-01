Title: Montar una Plataforma como servicio (PaaS) con Dokku (docker).  
Date: 2016-05-05 09:00  
Category: Tutorial de Docker 
Tags: Canaima,Debian,Linux,Ubuntu,Docker, Dokku, PaaS,DevOps  
lang: es  
translation: true


Continuando con los artículos sobre Docker.

En este caso se explicará como montar y usar [Dokku](https://github.com/dokku/dokku) el cual es una herramienta que facilita montar una Plataforma como Servicio ([PaaS](https://es.wikipedia.org/wiki/Computaci%C3%B3n_en_la_nube#Plataforma_como_servicio)) al estilo [Heroku](https://www.heroku.com/) en Linux (en este caso Debian Jessie).

Para este caso no se tiene un servidor de DNS y un nombre al equipo, se usará la IP 192.168.1.102.

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


Para instalar y usar `Dokku` estaré trabajando con una máquina virtual (para no usar directamente mí equipo), para ello se instalo en dicha máquina virtual docker ([ver artículo 1](http://blog.crespo.org.ve/2015/12/instalar-docker-en-debian-jessie.html)).

El procedimiento de instalación de `Dokku` lo pueden encontrar en su proyecto en [github](https://github.com/dokku/dokku) o en el siguiente [enlace](http://dokku.viewdocs.io/dokku/getting-started/advanced-installation/).

Instalación (para este procedimiento se instala `docker-engine`):
```
wget https://raw.githubusercontent.com/dokku/dokku/v0.5.6/bootstrap.sh
chmod a+x bootstrap.sh
sudo DOKKU_TAG=v0.5.6 bash bootstrap.sh
```
Otra opción para instalar es bajarse el repositorio de `dokku`:
```
git clone https://github.com/progrium/dokku.git
cd dokku
sudo make install ; #es necesario tener make instalado; sudo apt-get install make
```

Para ver que versión se tiene:
```
dokku version
v0.5.6-7-g851ca59
```

Configurar la llave ssh:  
1. Ir a la máquina local, ir al directorio `.ssh`, si no se tiene una llave RSA generada, se genera una:  
```
cd .ssh
ssh-keygen -t rsa
```  
2. Ver la llave pública:
```
cat id_rsa.pub
```  
3. Se copia el contenido de la llave.  
4. En el servidor, como un usuario se ejecuta lo siguiente:  
```
echo "ssh-rsa ..... ernesto@crespo.org.ve"| sudo sshcommand acl-add dokku ernesto
```

Subir una aplicación de `node.js` y `express.js`:
Para ello se tiene un repositorio github con una aplicación en node.js y express.js que tiene una página con un hola mundo.

Se clonan el repo (desde el equipo local):
```
git clone https://github.com/ecrespo/prueba-nodeexpress.git
```

La estructura de archivos y directorios son:
```
prueba-nodeexpress/
├── app.json
├── index.js
├── LICENSE
└── package.json
```

En el siguiente [enlace](https://github.com/ecrespo/prueba-nodeexpress) se tiene el repositorio de github.

Se agrega el repo remoto de `dokku` (192.168.1.102):
```
git remote add dokku dokku@192.168.1.102:prueba-nodeexpress
```
Se modifica el archivo `index.html`, y se sube al repositorio de `dokku`:
```
git add public/index.html 
git commit -m"Agregado texto" 
git push dokku master 
```
Al hacer push se tiene la siguiente salida:
```
....
-----> Discovering process types
       Default types for  -> web
-----> Releasing prueba-nodeexpress (dokku/prueba-nodeexpress:latest)...
-----> Deploying prueba-nodeexpress (dokku/prueba-nodeexpress:latest)...
-----> Attempting to run scripts.dokku.predeploy from app.json (if defined)
-----> App Procfile file found (/home/dokku/prueba-nodeexpress/DOKKU_PROCFILE)
-----> DOKKU_SCALE file not found in app image. Generating one based on Procfile...
-----> New DOKKU_SCALE file generated
=====> web=1
-----> Running pre-flight checks
       For more efficient zero downtime deployments, create a file CHECKS.
       See http://dokku.viewdocs.io/dokku/checks-examples.md for examples
       CHECKS file not found in container: Running simple container check...
-----> Waiting for 10 seconds ...
-----> Default container check successful!
-----> Running post-deploy
-----> Attempting to run scripts.dokku.postdeploy from app.json (if defined)
=====> renaming container (2dacd928c2bb) clever_tesla to prueba-nodeexpress.web.1
=====> no global VHOST set. disabling vhost support
-----> Setting config vars
       NO_VHOST: 1
-----> no nginx port set. setting to random open high port
-----> Setting config vars
       DOKKU_NGINX_PORT: 53541
-----> Creating http nginx.conf
-----> Running nginx-pre-reload
       Reloading nginx
-----> Setting config vars
       DOKKU_APP_RESTORE: 1
=====> Application deployed:
       http://192.168.1.102:53541 (nginx)

To dokku@192.168.1.102:prueba-nodeexpress
 * [new branch]      master -> master

```
Al abrir el navegador en http://192.168.1.102:53541 se tiene lo siguiente:


![](./images/montarunaplataformacomoserviciopaascondokkudocker-1.png)


Para la instalación de plugins se puede revisar el siguiente [enlace](http://dokku.viewdocs.io/dokku/community/plugins/).

Existen otras herramientas parecidas a `dokku`:

- [flynn.io](https://flynn.io/).  
- [deis.io](https://azure.microsoft.com/en-us/services/kubernetes-service/).  
- [dokku-alt](https://github.com/dokku-alt/dokku-alt)

De esta forma se hace una pequeña demostración de como tener un entorno de despliegue parecido a Heroku.



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
