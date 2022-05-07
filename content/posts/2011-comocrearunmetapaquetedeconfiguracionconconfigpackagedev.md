Title: Como crear un metapaquete de configuración con config-package-dev
Date: 2011-11-13 09:00
Category: Linux,Empaquetado 
Tags: Canaima,Debian,Empaquetado,General,ssh,Ubuntu 
lang: es
translation: true

Anteriormente se explicó como crear un metapaquete con `equivs`, se tiene también el paquete `config-package-dev` el cual permite crear paquetes de configuración donde se puede cambiar la configuración de otros archivos dentro del directorio `/etc/` .

Este artículo se basa en el [tutorial del MIT sobre creación de paquetes de configuración para Debian y una guía en el wiki de Debian](https://debathena.mit.edu/config-package-dev/) y una guía en el [wiki de Debian](https://wiki.debian.org/ConfigPackages). El proceso de como adoptar un paquete y empaquetar se explica en una guía que se encuentra en el [wiki de Debian](https://wiki.debian.org/AdoptarUnPaquete).

Como ejemplo se usará el paquete `openssh-server` que crea un archivo con el nombre  `/etc/ssh/sshd_config` . Este archivo contiene la configuración necesaria para arrancar un servidor `ssh`.


Instalando `openssh-server`:  

```
apt-get install openssh-server config-package-dev
```

El contenido del archivo es el siguiente:  

```
Port 22
Protocol 2
HostKey /etc/ssh/ssh_host_rsa_key
HostKey /etc/ssh/ssh_host_dsa_key
HostKey /etc/ssh/ssh_host_ecdsa_key
UsePrivilegeSeparation yes
KeyRegenerationInterval 3600
ServerKeyBits 768
SyslogFacility AUTH
LogLevel INFO
LoginGraceTime 120
PermitRootLogin yes
StrictModes yes
RSAAuthentication yes
PubkeyAuthentication yes
IgnoreRhosts yes
RhostsRSAAuthentication no
HostbasedAuthentication no
PermitEmptyPasswords no
ChallengeResponseAuthentication no
X11Forwarding yes
X11DisplayOffset 10
PrintMotd no
PrintLastLog yes
TCPKeepAlive yes
AcceptEnv LANG LC_*
Subsystem sftp /usr/lib/openssh/sftp-server
```

Este archivo tiene el siguiente hash md5.  

```
8caefdd9e251b7cc1baa37874149a870  /etc/ssh/sshd_config
```

La idea es modificar este archivo para que no permita que el usuario `root` se conecte por `ssh` y no permitir reenvío de aplicaciones gráficas.

#### Procedimiento para crear paquete de configuración `sshd-config`:

##### 1.Crear el directorio de trabajo  
 
```
mkdir canaima-sshd-config-0.1
```

##### 2. Cambiarse a dicho directorio

```
cd canaima-sshd-config-0.1
```

##### 3. Crear los directorios debian y files

```
mkdir -p debian files
```

##### 4. En `files` crear el directorio `etc`, luego dentro de él, el directorio `ssh` y copiar el archivo `sshd_config` de `/etc/ssh/` al directorio creado.

```
mkdir -p files/etc
mkdir -p files/etc/ssh
cp /etc/ssh/sshd_config ./files/etc/ssh/sshd_config.canaima
```

##### 5. Modificar el archivo para que el usuario root no pueda acceder al servidor `ssh` y que no se pueda reenviar paquetes de `X11`. Las líneas son:

```
PermitRootLogin no
X11Forwarding no
```  

##### 6. Dentro del directorio debian se creó el archivo `changelog` con el siguiente contenido:

```
canaima-sshd-config (0.1) unstable; urgency=low

* Initial release.

-- Ernesto Nadir Crespo Avila <ecrespo@gmail.com>  Sun, 13 Nov 2011 10:22:48 -0430
```

##### 7. Se crea el archivo `debian/compat`  con el valor 7.

##### 8. Se crea el archivo `debian/control` y `debian/control.in` con la siguiente información:

```
Source: canaima-sshd-config
Section: config
Priority: extra
Maintainer: Ernesto Nadir Crespo Avila <ecrespo@gmail.com>
Build-Depends: cdbs (>= 0.4.23-1.1), debhelper (>= 4.2.0), config-package-dev (>= 4.5~)
Standards-Version: 3.9.2

Package: canaima-sshd-config
Architecture: all
Pre-Depends: openssh-server
Depends: cdbs, ${misc:Depends}
Provides: ${diverted-files}
Conflicts: ${diverted-files}
Description: Archivo de configuracion de ssh
Archivo de configuracion del servidor ssh.
```

En este caso se coloca el parámetro `Pre-Depends` ya que se necesita tener el servidor `openssh` instalado y bien configurado para poder agregarle cambios al archivo `/etc/ssh/sshd_config` .

##### 9. Se crea el archivo `debian/copyright`, en este caso se está usando el mismo copyright de los archivos de ejemplo de `config-package-dev`:

```
canaima-ssh-config package.

Author: Ernesto Nadir Crespo Avila <ecrespo@gmail.com>

Copyright © 2011 Ernesto Nadir Crespo Avila <ecrespo@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

##### 10. Se crea el archivo `debian/canaima-sshd-config.install` . Este archivo define donde se va a tomar los archivos de configuración y a donde se van a copiar.
 
```
files/* /
```

##### 11. Se crea el archivo `debian/rules`. En este archivo se define la extensión `.canaima`, la cual permite diferenciar de los paquetes base de Debian de la meta distribución canaima, además se define el archivo a modificar y luego los include de los `cdbs`:

```
#!/usr/bin/make -f

DEB_DIVERT_EXTENSION = .canaima
# Replace some base files with simple replacements.
DEB_DIVERT_FILES_canaima-sshd-config += \
/etc/ssh/sshd_config.canaima 
# These files are installed via dh_install from the files/ directory
# (see debian/canaima-sshd-config.install)

include /usr/share/cdbs/1/rules/debhelper.mk
include /usr/share/cdbs/1/rules/config-package.mk
```

##### 12. Crear el paquete debian y firmarlo con la llave `gpg`:

```
dpkg-buildpackage -rfakeroot -kC97E7015
```

Al ejectuar un `ls`  se pueden ver los archivos creados:
	
```
ls -l canaima-sshd*
-rw-r--r-- 1 ecrespo ecrespo 3948 nov 13 16:09 canaima-sshd-config_0.1_all.deb
-rw-r--r-- 1 ecrespo ecrespo  864 nov 13 16:09 canaima-sshd-config_0.1.dsc
-rw-r--r-- 1 ecrespo ecrespo 1521 nov 13 16:09 canaima-sshd-config_0.1_i386.changes
-rw-r--r-- 1 ecrespo ecrespo 2745 nov 13 16:09 canaima-sshd-config_0.1.tar.gz
```


##### 13. Se verifica que el paquete Debian cumple con el policy de Debian:

```
lintian -i canaima-sshd-config_0.1.dsc
```

##### 14. Verificar la instalación del paquete Debian.
```
sudo dpkg -i canaima-sshd-config_0.1_all.deb 
[sudo] password for ecrespo: 
Selecting previously unselected package canaima-sshd-config.
(Leyendo la base de datos ... 418546 ficheros o directorios instalados actualmente.)
Desempaquetando canaima-sshd-config (de canaima-sshd-config_0.1_all.deb) ...
Configurando canaima-sshd-config (0.1) ...
Añadiendo `desviación de /etc/ssh/sshd_config a /etc/ssh/sshd_config.canaima-orig por canaima-sshd-config'
```

##### 15. Al ejecutar un `ls -l` en el directorio `/etc/ssh/sshd_config*` se verá que se crea un enlace al archivo original y se muestra los archivos agregados de la extensión canaima:
```
root@jewel:/etc/ssh# ls -l sshd_config*
lrwxrwxrwx 1 root root   19 nov 13 16:16 sshd_config -> sshd_config.canaima
-rw-r--r-- 1 root root 2487 nov 13 10:15 sshd_config.canaima
-rw-r--r-- 1 root root 2489 nov 13 13:20 sshd_config.canaima-orig
```

##### 16. Al revisar el archivo se nota que el campo para permitir a root conectarse al servidor ssh se encuentra en no, igual caso para el parámetro de reenvío de `X11`. Se revisa el hash `md5` del archivo y se nota que del archivo original al actual son diferentes:

```
a358d423fa6b8bf640a7fd1e06731ea3  sshd_config
```

Al crear paquetes de configuración de esta forma (una forma limpia de modificar archivos de configuración) y al eliminar el paquete de configuración los archivos originales se vuelven a usar:
	
```
apt-get remove -f canaima-sshd-config

root@jewel:/etc/ssh# md5sum sshd_config
8caefdd9e251b7cc1baa37874149a870  sshd_config
``` 

Se tienen varios ejemplos para usar `config-package-dev` como por ejemplo paquetes binarios, configuración de cron, etc.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
