Title: Proveer un cluster con docker swarm y docker-machine.  
Date: 2016-05-09 09:00
Category: Tutorial de Docker 
Tags: Canaima,Debian,Linux,Ubuntu,Docker, docker-swarm, docker-machine  
lang: es  
translation: true

Se puede usar docker-machine para proveer un cluster con docker swarm.

Este artículo se basa de los siguientes artículos en inglés:

- [Provision a Swarm cluster with Docker Machine.](https://docs.docker.com/swarm/provision-with-machine/)
- [How to Use Docker Machine to Create a Swarm Cluster.](https://www.linux.com/learn/how-use-docker-machine-create-swarm-cluster)

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

Este artículo usará comandos ya explicados en el artículo sobre "[Uso de docker-machine](https://www.seraph.to/uso-de-docker-machine.html#uso-de-docker-machine)".

En el artículo anterior se usó virtualbox, se seguirá usando, pero también se pueden usar servicios en la nube o un host local ([los drivers soportados](https://docs.docker.com/machine/drivers/)): amazon web services, Microsoft Azure, Digital Ocean, Exoscale, Google Compute Engine, Genérico, OpenStack entre otros. 

Se crea un host (virtualbox) para generar el token de `swarm`:
```
docker-machine create -d virtualbox local
```
Para configurar el shell que acceda a local se ejecuta:
```
eval "$(docker-machine env local)"
```
Cada host `swarm` tiene un token instalado dentro de la configuración del motor. Para crear el token se crea la imagen de `swarm`:
```
docker run swarm create
Unable to find image 'swarm:latest' locally
latest: Pulling from library/swarm

eada7ab697d2: Pull complete 
afaf40cb2366: Pull complete 
7495da266907: Pull complete 
a3ed95caeb02: Pull complete 
Digest: sha256:12e3f7bdb86682733adf5351543487f581e1ccede5d85e1d5e0a7a62dcc88116
Status: Downloaded newer image for swarm:latest
99cd781ad7e0f3682747d94edff87f49
```

El token es la salida que se muestra subrayada.

Creando los nodos del cluster:

Todos los nodos de un cluster deben tener el engine instalado, con el token del cluster se puede proveer un host con engine y configurarlo como un nodo `swarm`.

Para crear un manejador de nodo swarm se ejecuta el siguiente comando:
```
docker-machine create -d virtualbox --swarm --swarm-master --swarm-discovery token://99cd781ad7e0f3682747d94edff87f49 swarm-manager
```
Para ver las variables y luego configurar el shell:
```
docker-machine env swarm-manager
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.101:2376"
export DOCKER_CERT_PATH="/home/ernesto/.docker/machine/machines/swarm-manager"
export DOCKER_MACHINE_NAME="swarm-manager"
# Run this command to configure your shell: 
# eval "$(docker-machine env swarm-manager)"


eval "$(docker-machine env swarm-manager)"
```
Ahora se crea el primer nodo, el nodo-01, se le pasa también el token:
```
docker-machine create -d virtualbox --swarm --swarm-discovery token://99cd781ad7e0f3682747d94edff87f49 nodo-01
```
Y un nodo-02:
```
docker-machine create -d virtualbox --swarm --swarm-discovery token://99cd781ad7e0f3682747d94edff87f49 nodo-02
```
Conectar los nodos con la máquina:

Para conectar el ambiente del host con la máquina se usa el comando eval con la opción a docker-machine de env, algo así: 
```
eval "$(docker-machine env local)"
```
En este caso docker-machine provee una opción `--swarm` para conectar los nodos `swarm`:
```
docker-machine env --swarm swarm-manager
export DOCKER_TLS_VERIFY="1"
export DOCKER_HOST="tcp://192.168.99.101:3376"
export DOCKER_CERT_PATH="/home/ernesto/.docker/machine/machines/swarm-manager"
export DOCKER_MACHINE_NAME="swarm-manager"
# Run this command to configure your shell: 
# eval "$(docker-machine env swarm-manager)"
```
Para conectarse el nodo `swarm` llamado `swarm-manager` se ejecuta:
```
eval "$(docker-machine env swarm-manager)"
```

Ahora se puede ejecutar `docker info` para interacturar con los nodos:
```
$docker info 
Containers: 2
 Running: 2
 Paused: 0
 Stopped: 0
Images: 1
Server Version: 1.11.1-rc1
Storage Driver: aufs
 Root Dir: /mnt/sda1/var/lib/docker/aufs
 Backing Filesystem: extfs
 Dirs: 12
 Dirperm1 Supported: true
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins: 
 Volume: local
 Network: host bridge null
Kernel Version: 4.4.8-boot2docker
Operating System: Boot2Docker 1.11.1-rc1 (TCL 7.0); HEAD : 903a352 - Tue Apr 26 14:18:06 UTC 2016
OSType: linux
Architecture: x86_64
CPUs: 1
Total Memory: 995.9 MiB
Name: swarm-manager
ID: 6LXP:RTPR:4MRE:OGLK:EDED:EQBP:JQRH:RHLW:5YUG:SELK:MUDN:YVSA
Docker Root Dir: /mnt/sda1/var/lib/docker
Debug mode (client): false
Debug mode (server): true
 File Descriptors: 20
 Goroutines: 45
 System Time: 2016-05-09T20:36:18.825810618Z
 EventsListeners: 1
Username: ecrespo
Registry: https://index.docker.io/v1/
Labels:
 provider=virtualbox
```

O listar las máquinas con `docker-machine ls`:
```
docker-machine ls
NAME            ACTIVE   DRIVER       STATE     URL                         SWARM
local                    virtualbox   Running   tcp://192.168.99.100:2376   
nodo-01                  virtualbox   Running   tcp://192.168.99.102:2376   swarm-manager
nodo-02                  virtualbox   Running   tcp://192.168.99.103:2376   swarm-manager
swarm-manager   *        virtualbox   Running   tcp://192.168.99.101:2376   swarm-manager (master)
```
Como pueden notar los nodos nodo-01 y nodo-02 están asociados a swarm-manager y este es el master.

A continuación dejo captura de pantalla de swarm-manager, nodo-01 y nodo-02:

![](./images/proveerunclustercondockerswarmydockermachine-1.png)

![](./images/proveerunclustercondockerswarmydockermachine-2.png)

![](./images/proveerunclustercondockerswarmydockermachine-3.png)

A continuación les dejo unos enlaces de referencia:

- [Use Docker Machine to provision hosts on cloud providers.](https://docs.docker.com/machine/get-started-cloud/)
- [Example: Use Docker Machine to provision cloud hosts.](https://docs.docker.com/engine/installation/cloud/cloud-ex-machine-ocean/)

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
