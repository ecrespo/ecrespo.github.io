Title: Crear una imagen Docker para MongoDB 3  
Date: 2016-05-22 09:00  
Category: Tutorial de Docker
Tags: Canaima,Debian,Linux,Ubuntu,Docker,MongoDB
lang: es  
translation: true


En Docker hub, la gente de MongoDB tiene una imagen oficial para varias versiones de [mongo](https://hub.docker.com/_/mongo/).

Pero para los que quieren crear y probar imágenes les dejo [una imagen creada a partir de Debian](https://hub.docker.com/r/ecrespo/mongo3-custom/).

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

El archivo Dockerfile se encuentra en github en el siguiente [enlace](https://github.com/ecrespo/mongodb3). Su contenido es el siguiente:
```
FROM debian
MAINTAINER Ernesto Crespo <ecrespo@gmail.com> 
USER root
WORKDIR /code
RUN echo "deb http://ftp.debian.org/debian jessie main contrib non-free" > /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.0 main" |  tee /etc/apt/sources.list.d/mongodb-org-3.0.list
RUN apt-get update && apt-get install -y mongodb-org
RUN apt-get install -y sudo vim less mc locate
RUN apt-get clean
RUN mkdir -p /data/db
RUN echo "mongodb ALL=NOPASSWD: ALL" >> /etc/sudoers

EXPOSE 27017
ENTRYPOINT ["/usr/bin/mongod"]
```
Para construir la imagen se ejecuta:
``` 
docker build -t <nombreImagen> .
```
En este caso fue:
```
docker build -t mongo3-custom .
```
Para quien quiera bajar la imagen ejecuta:
```
docker pull ecrespo/mongo3-custom
```
Para correr un contenedor usando persistencia de datos en `/srv/data/db` se ejecuta:
```
docker run -p 27017:27017 -v /srv/data/db:/data/db:rw --name mongo_instance_001 -d mongo-custom3 --smallfiles
```
Para ver el log del contenedor se ejecuta `docker logs <idcontenedor|nombrecontenedor>`

![](./images/crearunaimagendockerparamongodb3-1.png)

Para ver el contenedor corriendo se ejecuta `docker ps`:

![](./images/crearunaimagendockerparamongodb3-2.png)

Para acceder a mongo se ejecuta:
```
mongo
```

![](./images/crearunaimagendockerparamongodb3-3.png)

Para ver la información del contenedor se ejecuta el comando `docker inspect`:
```
docker inspect mongo_instance_001
[
    {
        "Id": "d981736358770a23b5123ca1e6490c35bacf40ecf571b265bf98296420b97131",
        "Created": "2016-05-22T00:01:48.049849422Z",
        "Path": "/usr/bin/mongod",
        "Args": [
            "--smallfiles"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 3984,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2016-05-22T17:47:36.658752846Z",
            "FinishedAt": "2016-05-22T16:53:45.66317329Z"
        },
        "Image": "sha256:a17c12c4f560fbc39e8e30bf561c76d86947e2926112bc87d12744e63be7eaa7",
        "ResolvConfPath": "/var/lib/docker/containers/d981736358770a23b5123ca1e6490c35bacf40ecf571b265bf98296420b97131/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/d981736358770a23b5123ca1e6490c35bacf40ecf571b265bf98296420b97131/hostname",
        "HostsPath": "/var/lib/docker/containers/d981736358770a23b5123ca1e6490c35bacf40ecf571b265bf98296420b97131/hosts",
        "LogPath": "/var/lib/docker/containers/d981736358770a23b5123ca1e6490c35bacf40ecf571b265bf98296420b97131/d981736358770a23b5123ca1e6490c35bacf40ecf571b265bf98296420b97131-json.log",
        "Name": "/mongo_instance_001",
        "RestartCount": 0,
        "Driver": "aufs",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": [
                "/srv/data/db:/data/db:rw"
            ],
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "27017/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "27017"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "StorageOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": null,
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DiskQuota": 0,
            "KernelMemory": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": -1,
            "OomKillDisable": false,
            "PidsLimit": 0,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "BlkioIOps": 0,
            "BlkioBps": 0,
            "SandboxSize": 0
        },
        "GraphDriver": {
            "Name": "aufs",
            "Data": null
        },
        "Mounts": [
            {
                "Source": "/srv/data/db",
                "Destination": "/data/db",
                "Mode": "rw",
                "RW": true,
                "Propagation": "rprivate"
            }
        ],
        "Config": {
            "Hostname": "d98173635877",
            "Domainname": "",
            "User": "root",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "27017/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "--smallfiles"
            ],
            "Image": "mongo-custom3",
            "Volumes": null,
            "WorkingDir": "/code",
            "Entrypoint": [
                "/usr/bin/mongod"
            ],
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "9aff46c57baeb071a5762c2fcdac37ab5612901c15d78f61f5188185757699bd",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "27017/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "27017"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/9aff46c57bae",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "f548e847fd8d031f26ebe687c24c709332efa10a2d5752679e6458cf1fbad356",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "b0796b4ed424447971b67d367f762d83141a38e0aacb0a8bc37e70a965d36ac0",
                    "EndpointID": "f548e847fd8d031f26ebe687c24c709332efa10a2d5752679e6458cf1fbad356",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02"
                }
            }
        }
    }
]

```


Se muestra la información del nombre del contenedor, el puerto que se tiene para acceder al mismo, su IP, su dirección mac entre otras cosas.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
