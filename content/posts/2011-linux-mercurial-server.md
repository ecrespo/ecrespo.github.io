Title: Compartir repositorios de Mercurial con mercurial-server
Date: 2011-08-20 09:00
Category: Tutorial de Linux
Tags: Linux,Debian, Ubuntu, Canaima,mercurial
lang: es
translation: true

Se tienen varios artículos sobre mercurial en este blog, un [tutorial de mercurial](https://www.seraph.to/control-de-versiones-con-mercurial.html) (viene una actualización), [como empaquetar para Debian con mercurial](https://www.seraph.to/manteniendo-un-paquete-debian-con-mercurial.html) (viene una actualización) y el último [como gestionar la configuración con mercurial](https://www.seraph.to/gestionar-los-archivos-de-configuracion-en-etc-con-etckeeper-y-mercurial.html).

Este artículo explicará como compartir repositorios de Mercurial con mercurial-server, este artículo se basa en el [tutorial en inglés](http://dev.lshift.net/paul/mercurial-server/docbook.html).

Mercurial-server no se autentica usando claves pero si llaves públicas con ssh. Todos los usuarios que quieran acceder al repositorio mercurial necesitan una llave pública. 

En el siguiente enlace tienen una guía de como crear las [llaves públicas](http://rafael.bonifaz.ec/blog/2011/01/ssh-con-claves-publicas-y-privadas/).

### Acceso inicial al mercurial-server.

Instalar mercurial-server:

```
aptitude install mercurial-server 
```

Conectarse al servidor grievous habilitando el forwarding.

```
ernesto@jewel:~$ ssh -A grievous
```

Agregar llave privada al agente de autenticación. 

```
ernesto@grievous:~$ ssh-add -L > my-key
```

Crear el directorio para el usuario ernesto en el mercurial-server, copiar la llave y actualizar el repositorio de autenticación. 

```
ernesto@grievous:~$ sudo mkdir -p /etc/mercurial-server/keys/root/ernesto
ernesto@grievous:~$ sudo cp my-key /etc/mercurial-server/keys/root/ernesto/jewel
ernesto@grievous:~$ sudo -u hg /usr/share/mercurial-server/refresh-auth
ernesto@grievous:~$ exit
```

Crear un repositorio.

```
 cd proyectos/pysms-send
```

Clonar el proyecto en el servidor grievous: 

```
ernesto@jewel:~/proyectos/pysms-send$ hg clone . ssh://hg@grievous/ernesto/pysms-send
searching for changes
27 changesets found
remote: adding changesets
remote: adding manifests
remote: adding file changes
remote: added 27 changesets with 52 changes to 24 files
```

Revisar si hay cambios en el repositorio.

```
ernesto@jewel:~/proyectos/pysms-send$ hg pull ssh://hg@grievous/ernesto/pysms-send
pulling from ssh://hg@grievous/ernesto/pysms-send
searching for changes
no changes found
```

Siguiente artículo se explicará como agregar usuarios al repositorio, controlar el acceso al repositorio





===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
