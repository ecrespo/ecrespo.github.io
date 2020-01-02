Title: Instalar Docker en Debian Stretch (actualización 2017).
Date: 2017-07-09 09:00
Category: Tutorial de Linux
Tags: Linux,Debian,Ubuntu, Docker
lang: es
translation: true

El primer artículo de la [serie  de artículos sobre Docker](https://www.seraph.to/tag/docker.html) fue, el de la [Instalación de Docker en Debian Jessie](https://www.seraph.to/instalar-docker-en-debian-jessie.html), ahora explicaré el proceso de instalación de Docer CE para Debian Stretch. La guía en inglés de instalación de docker para Debian la pueden encontrar en el siguiente [enlace](https://docs.docker.com/engine/installation/linux/docker-ce/debian/).

El procedimiento es el siguiente:

1. Instalación de paquetes necesarios para soporte de https en `apt-get`:
```
#apt-get install apt-transport-https ca-certificates curl gnupg2 software-properties-common
```

2. Agregar llave `gpg` oficial de Docker:
```
# curl -fsSL https://download.docker.com/linux/debian/gpg |  apt-key add -
OK
```
Si devuelve "OK" se bajo la llave y la agregó sin problemas.

3. Verificar la llave:
```
# apt-key fingerprint 0EBFCD88
pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid           Docker Release (CE deb) <docker@docker.com>
sub   rsa4096 2017-02-22 [S]
```
4. Se agrega el repositorio Estable para la versión de Debian que se tiene en el equipo:
```
add-apt-repository \
>    "deb [arch=amd64] https://download.docker.com/linux/debian \
>    $(lsb_release -cs) \
>    stable"
```
5. Se actualiza la lista de paquetes:
```
#apt-get update
```
6. Se instala `docker-ce`:
```
# apt-get install docker-ce
```
7. Se verifica que `docker-ce` se instaló correctamente:
```
# docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
b04784fba78d: Pull complete 
Digest: sha256:f3b3b28a45160805bb16542c9531888519430e9e6d6ffc09d72261b0d26ff74f
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

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```

8. Instalar docker-compose:
```
#apt-get install  docker-compose
```


Manejar docker como un usuario normal:

1. Crear el grupo docker:
```
$sudo groupadd docker
```
2. Agregar el usuario al grupo docker:
```
$sudo usermod -aG docker $USER
```
3. Verificar que se puede usar docker desde el usuario:
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

Share images, automate workflows, and more with a free Docker ID:
 https://cloud.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/

```

Configurar Docker para que inicie en el arranque del equipo:

1. Habilitar Docker:
```
$ sudo systemctl enable docker
Synchronizing state of docker.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable docker
```

Si requieren detalles de configuración lo pueden ver en la [documentación de docker](https://docs.docker.com/engine/installation/linux/linux-postinstall/#your-kernel-does-not-support-cgroup-swap-limit-capabilities).

Para terminar se prueba el arranque de cloud9 ya explicado en un [artículo anterior](http://blog.crespo.org.ve/2017/04/entorno-de-desarrollo-en-la-nube-cloud9.html).
```
$docker run -it -d -p 9080:80 -v /home/ernesto/worksplace/:/workspace/ kdelfour/cloud9-docker
99cfe3af5bf4480ac456ec43916612317a49da111ab27e32a361639984eb2128
```
La siguiente captura de pantalla muestra cloud9 en funcionamiento:

![](./images/instalardockerendebianstretchactualizacion2017-1.png)

En el diectorio worksplace se guarda los proyectos que se editan desde cloud9.
```
$ tree worksplace
worksplace
├── hola.py
├── New Folder
│   ├── mvc1.py
│   ├── New Folder
│   └── usuario.py
└── trabajo.txt

2 directories, 4 files
```


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
