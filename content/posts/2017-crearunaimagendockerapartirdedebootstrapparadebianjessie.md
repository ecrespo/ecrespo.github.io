Title: Crear una imagen Docker a partir de debootstrap para Debian Jessie
Date: 2017-03-27 09:00
Category: Tutorial de Linux
Tags: Linux,Debian,Ubuntu,Docker,debootstrap
lang: es
translation: true

Antes de empezar a tocar el tema sobre crear una imagen Docker a partir de debootstrap de Debian, les dejo el enlace de los [artículos sobre docker del blog](https://www.seraph.to/tag/docker.html).

Lo primero que se tiene que hacer es instalar `debootstrap`:
```
#apt-get install debootstrap
```
A continuación se crea un directorio para construir la jaula `debootstrap`:
```
mkdir debian-jaula
```
Ahora se ejecuta `debootstrap` pasando la distribución a bajar, el directorio donde se crea la jaula y el repositorio a usar:
```
debootstrap jessie debian-jaula/ http://ftp.debian.org/debian
I: Retrieving Release 
I: Retrieving Release.gpg 
I: Checking Release signature
I: Valid Release signature (key id 75DDC3C4A499F1A18CB5F3C8CBF8D6FD518E17E1)
I: Validating Packages 
I: Resolving dependencies of required packages...
I: Resolving dependencies of base packages...
I: Found additional required dependencies: acl adduser dmsetup insserv libaudit-common libaudit1 libbz2-1.0 libcap2 libcap2-bin libcryptsetup4 libdb5.3 libdebconfclient0 libdevmapper1.02.1 libgcrypt20 libgpg-error0 libkmod2 libncursesw5 libprocps3 libsemanage-common libsemanage1 libslang2 libsystemd0 libudev1 libustr-1.0-1 procps systemd systemd-sysv udev 
I: Found additional base dependencies: libdns-export100 libffi6 libgmp10 libgnutls-deb0-28 libgnutls-openssl27 libhogweed2 libicu52 libidn11 libirs-export91 libisc-export95 libisccfg-export90 libmnl0 libnetfilter-acct1 libnettle4 libnfnetlink0 libp11-kit0 libpsl0 libtasn1-6 
I: Checking component main on http://ftp.debian.org/debian...
I: Validating acl 2.2.52-2
I: Retrieving libacl1 2.2.52-2
I: Validating libacl1 2.2.52-2
........................
..............
I: Configuring isc-dhcp-client...
I: Configuring tasksel...
I: Configuring tasksel-data...
I: Configuring libc-bin...
I: Configuring systemd...
I: Base system installed successfully.
```

Ahora se muestra el contenido del directorio:
```
ls debian-jaula/
bin/  boot/  dev/  etc/  home/  lib/  lib64/  media/  mnt/  opt/  proc/  root/  run/  sbin/  srv/  sys/  tmp/  usr/  var/
```
Ahora se crea la imagen por medio de `tar` y de `docker import`:
```
tar -C debian-jaula/ -c . | docker import - ecrespo/debian
sha256:49ad34e39c5f9ede2c1c57994895065236a5965496631e8fcab00b00778d85fa
```
Como se puede ver, se genera la imagen y el ID de la misma en sha256, se coloca en subrayado la parte que identifica la imagen y lista las imagenes.

Al hacer `docker images` se tiene lo siguiente:
```
REPOSITORY                                        TAG                 IMAGE ID            CREATED             SIZE
ecrespo/debian                                    latest              49ad34e39c5f        2 minutes ago       272.7 MB
```

Al tener la jaula lista se puede hacer personalizaciones y adaptaciones a fin de crear la imagen docker.

Este artículo se basa en la documentación del [wiki de Debian sobre debootstrap](http://wiki.debian.org/Debootstrap) y en un artículo sobre [imagen base de docker](http://docs.docker.com/engine/userguide/eng-image/baseimages/). 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
