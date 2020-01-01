Title: Instalar Docker en Ubuntu Server Xenial 16.04  
Date: 2016-09-09 09:00  
Category: Tutorial de Linux
Tags: Docker, Linux, Ubuntu
lang: es  
translation: true 

Está guía es para usuarios Ubuntu que quieren instalar Docker.

La instalación se realizará en Ubuntu Server Xenial:

Este tutorial se basa en la [documentación oficial en inglés](https://docs.docker.com/install/linux/docker-ee/ubuntu/).

Instalación  
Trabajaremos como superusuario:  
```
sudo -s
```

Lo primero que se tiene que revisar es cual es la versión del Kernel que se tiene:
```
uname -r 
4.4.0-31-generic
```

Para el Caso de Ubuntu Xenial 16.04 se recomienda tener los paquetes del kernel : `linux-image-extra-* .`
```
sudo apt-get update

sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual
```


Para poder usar los repositorios de docker en ubuntu es necesario tener el soporte de `https` para los repos:
```
sudo apt-get install apt-transport-https ca-certificates
```

Agregar la llave del repositorio Docker en Ubuntu:
```
sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
```

Crear el archivo `docker.list` para agregar los repositorios de Docker en Ubuntu:
```
sudo vim /etc/apt/sources.list.d/docker.list
```
Para el caso de Ubuntu Xenial la línea que se tiene que agregar en el archivo es la siguiente:
```
deb https://apt.dockerproject.org/repo ubuntu-xenial main
```
Se hace un update:
```
apt-get update
```
Se elimina cualquier paquete de ubuntu sobre docker:
```
sudo apt-get purge lxc-docker 
```

Se verifica que se está buscando los paquetes de Docker en los repositorios correctos:
```
sudo apt-cache policy docker-engine
docker-engine:
  Instalados: (ninguno)
  Candidato:  1.12.1-0~xenial
  Tabla de versión:
     1.12.1-0~xenial 500
        500 https://apt.dockerproject.org/repo ubuntu-xenial/main amd64 Packages
     1.12.0-0~xenial 500
        500 https://apt.dockerproject.org/repo ubuntu-xenial/main amd64 Packages
     1.11.2-0~xenial 500
        500 https://apt.dockerproject.org/repo ubuntu-xenial/main amd64 Packages
     1.11.1-0~xenial 500
        500 https://apt.dockerproject.org/repo ubuntu-xenial/main amd64 Packages
     1.11.0-0~xenial 500
        500 https://apt.dockerproject.org/repo ubuntu-xenial/main amd64 Packages
```

Instalación de Docker:  
```
sudo apt-get install docker-engine
```
Se inicia el servicio docker:
```
sudo service docker start
```
Se verifica que docker se instaló correctamente:
```
docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c04b14da8d14: Pull complete 
Digest: sha256:0256e8a36e2070f7bf2d0b0763dbabdd67798512411de4cdcf9431a1feb60fd9
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker Hub account:
 https://hub.docker.com

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

Configuraciones adicionales
Crear el grupo Docker:
```
sudo groupadd docker
```

Agregar el usuario del equipo al grupo Docker:  
```
sudo usermod -aG docker $USER
```

Reiniciar el servicio docker:
```
service docker restart
```
Ahora como un usuario sin privilegios se prueba que se puede usar docker:
```
docker run hello-world
docker: Cannot connect to the Docker daemon. Is the docker daemon running on this host?.
See 'docker run --help'.
```
Si sale el mensaje anterior, es necesario reiniciar el equipo:

Se vuelve a probar:  
```
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker Hub account:
 https://hub.docker.com

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

Iniciar docker al iniciar el equipo:
```
systemctl enable docker
```

Para hacer más configuraciones adicionales como: firewall y DNS u otras versiones de Ubuntu,  pueden revisar el enlace que se encuentra al inicio del artículo de la documentación oficial de Docker para Ubuntu.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)



