Title: Compartir repositorios Mercurial por ssh
Date: 2011-12-08 09:00
Category: Linux,Desarrollo
Tags: Canaima,Control de versiones,Debian,Linux,mercurial,ssh,Ubuntu
lang: es
translation: true

[En artículo anterior](https://www.seraph.to/compartir-repositorios-de-mercurial-con-mercurial-server.html) se explica como compartir un repositorio mercurial con `mercurial-server`, ahora se explicará como hacerlo usando `ssh` con claves públicas.

Lo que primero se va a hacer es crear la clave pública para `ssh` y distribuirlo al equipo o los equipos, luego se verifica el funcionamiento del `ssh` con la clave pública.

La idea es mantener respaldado la configuración de un equipo que está con control de versiones con mercurial usando [etckeeper](https://www.seraph.to/gestionar-los-archivos-de-configuracion-en-etc-con-etckeeper-y-mercurial.html).

En el servidor es necesario instalar `etckeeper`, `mercurial` y `ssh`.

```
apt-get install etckeeper mercurial openssh-server
```

Configurar `etckeeper` y `mercurial`.

```
vim /etc/etckeeper/etckeeper.conf
```

Se descomenta y agrega lo siguiente en el archivo:

```
# The VCS to use.
VCS="hg"
#VCS="git"
#VCS="bzr"
#VCS="darcs"

# Options passed to git commit when run by etckeeper.
#GIT_COMMIT_OPTIONS=""

# Options passed to hg commit when run by etckeeper.
HG_COMMIT_OPTIONS="-u ecrespo@gmail.com"

# Options passed to bzr commit when run by etckeeper.
#BZR_COMMIT_OPTIONS=""

# Options passed to darcs record when run by etckeeper.
#DARCS_COMMIT_OPTIONS="-a"

# Uncomment to avoid etckeeper committing existing changes
# to /etc automatically once per day.
AVOID_DAILY_AUTOCOMMITS=1

# Uncomment to avoid etckeeper committing existing changes to
# /etc before installation. It will cancel the installation,
# so you can commit the changes by hand.
#AVOID_COMMIT_BEFORE_INSTALL=1

# The high-level package manager that's being used.
# (apt, pacman-g2, yum etc)
HIGHLEVEL_PACKAGE_MANAGER=apt

# The low-level package manager that's being used.
# (dpkg, rpm, pacman-g2, etc)
LOWLEVEL_PACKAGE_MANAGER=dpkg  
```

Luego:

```
vim /etc/mercurial/hgrc
```

```
[ui]
username = "Ernesto Nadir Crespo Avila <ecrespo@gmail.com>"
editor = vim
# pedir indicación de archivos cambiados:
verbose=True
```

Inicializar `etckeeper`.

```
etckeeper init
...
adding ssl/certs/f950ccc2.0
adding ssl/certs/facacbc6.0
adding ssl/certs/ff783690.0
adding ssl/certs/signet_ca1_pem.pem
adding ssl/certs/signet_ca2_pem.pem
adding ssl/certs/signet_ca3_pem.pem
adding ssl/certs/signet_ocspklasa2_pem.pem
adding ssl/certs/signet_ocspklasa3_pem.pem
adding ssl/certs/signet_pca2_pem.pem
adding ssl/certs/signet_pca3_pem.pem
adding ssl/certs/signet_rootca_pem.pem
adding ssl/certs/signet_tsa1_pem.pem
adding ssl/certs/spi-ca-2003.pem
adding ssl/certs/spi-cacert-2008.pem
adding ssl/certs/ssl-cert-snakeoil.pem
adding ssl/certs/thawte_Primary_Root_CA.pem
adding ssl/openssl.cnf
adding ssl/private/ssl-cert-snakeoil.key
adding subversion/config
adding subversion/servers
adding sudoers
adding sudoers.d/README
adding sysctl.conf
adding sysctl.d/README.sysctl
adding sysctl.d/bindv6only.conf
adding terminfo/README
adding timezone
adding ts.conf
adding ucf.conf
adding ufw/applications.d/bind9
adding ufw/applications.d/openssh-server
adding ufw/applications.d/postfix
adding vga/dvorak-us.keymap
adding vga/libvga.config
adding vga/libvga.et4000
adding vga/null.keymap
adding vim/vimrc
adding vim/vimrc.tiny
adding w3m/config
adding w3m/mailcap
adding wgetrc
adding xml/catalog
adding xml/xml-core.xml
```

Este comando agregará todos los archivos de configuración dentro del directorio `/etc` a un control de versiones, en este caso `mercurial`.

Al ejecutar el comando de mercurial para ver el estatus muestra los archivos que fueron agregados:

```
hg status /etc/
...
A sudoers
A sudoers.d/README
A sysctl.conf
A sysctl.d/README.sysctl
A sysctl.d/bindv6only.conf
A terminfo/README
A timezone
A ts.conf
A ucf.conf
A ufw/applications.d/bind9
A ufw/applications.d/openssh-server
A ufw/applications.d/postfix
A vga/dvorak-us.keymap
A vga/libvga.config
A vga/libvga.et4000
A vga/null.keymap
A vim/vimrc
A vim/vimrc.tiny
A w3m/config
A w3m/mailcap
A wgetrc
A xml/catalog
A xml/xml-core.xml
```

Ahora se hace el primer commit.

```
etckeeper commit "Inicializacion del control de versiones"
...
sysctl.conf
sysctl.d/README.sysctl
sysctl.d/bindv6only.conf
terminfo/README
timezone
ts.conf
ucf.conf
ufw/applications.d/bind9
ufw/applications.d/openssh-server
ufw/applications.d/postfix
vga/dvorak-us.keymap
vga/libvga.config
vga/libvga.et4000
vga/null.keymap
vim/vimrc
vim/vimrc.tiny
w3m/config
w3m/mailcap
wgetrc
xml/catalog
xml/xml-core.xml
committed changeset 0:10c12e9f2889
```

Ahora se creará la clave ssh y se copiará en el servidor.

```
ssh-keygen -t rsa -C "ecrespo@gmail.com" -f hgernesto-identity
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in hgernesto-identity.
Your public key has been saved in hgernesto-identity.pub.
The key fingerprint is:
ca:7a:09:57:77:85:9c:05:d8:73:ca:d0:b1:41:5c:11 ecrespo@gmail.com
The key's randomart image is:
+--[ RSA 2048]----+
|           B=BEo |
|          o Ooo  |
|           o.=   |
|        . . +    |
|       .S. .     |
|    ....         |
|     oo.         |
|     .o          |
|    ..           |
+-----------------+
```

Se copia la clave pública al servidor.

```
scp hgernesto-identity.pub ernesto@www.crespo.org.ve:.ssh/
ernesto@www.crespo.org.ve's password:
hgernesto-identity.pub           100%  399     0.4KB/s   00:00
```    

Se accede al servidor:

```
ssh ernesto@www.crespo.org.ve
ernesto@www.crespo.org.ve's password:
Linux crespo.org.ve 2.6.26-2-vserver-amd64 #1 SMP Fri Aug 14 09:21:21 UTC 2009 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Dec  8 18:58:20 2011 from 190.75.37.237

ernesto@crespo:~$
```

Se agrega la llave publica al archivo `authorized_keys`.

```
cd .ssh
cat hgernesto-identity.pub &gt;&gt;  authorized_keys
```

Se regresa al equipo que se conectará al servidor.

Se crea el archivo `~/.ssh/config` Se agrega el host, el usuario y la clave privada que se va a usar para la conexión ssh.

```
Host www.crespo.org.ve
   	user ernesto
   	IdentityFile ~/.ssh/hgernesto-identity
```
Se verifica que se conecte al servidor usando la llave pública.

```
ssh www.crespo.org.ve -i ~/.ssh/hgernesto-identity -l ernesto
Linux crespo.org.ve 2.6.26-2-vserver-amd64 #1 SMP Fri Aug 14 09:21:21 UTC 2009 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Dec  8 19:20:08 2011 from 190.75.37.237

ernesto@crespo:~$
```

Esta vez el servidor no pidió clave para el usuario.

Ahora se va a clonar el directorio etc para tener la configuración en el home del usuario.

```
sudo hg clone /etc conf-www.respo.org.ve
...
getting subversion/servers
getting sudoers
getting sudoers.d/README
getting sysctl.conf
getting sysctl.d/README.sysctl
getting sysctl.d/bindv6only.conf
getting terminfo/README
getting timezone
getting ts.conf
getting ucf.conf
getting ufw/applications.d/bind9
getting ufw/applications.d/openssh-server
getting ufw/applications.d/postfix
getting vga/dvorak-us.keymap
getting vga/libvga.config
getting vga/libvga.et4000
getting vga/null.keymap
getting vim/vimrc
getting vim/vimrc.tiny
getting w3m/config
getting w3m/mailcap
getting wgetrc
getting xml/catalog
getting xml/xml-core.xml
1775 files updated, 0 files merged, 0 files removed, 0 files unresolved
```

Se cambia el dueño y el grupo del repositorio ya que pertenece a root y no se va  a poder clonar con ese dueño.

```
sudo chown -R ernesto.ecrespo conf-www.respo.org.ve/
```

Ahora se prueba realizar la clonación del repositorio del servidor en la máquina local.

```
ernesto@zeath:~$ hg clone ssh://ernesto@www.crespo.org.ve/repo/conf-www.respo.org.ve
destination directory: conf-www.respo.org.ve
requesting all changes
adding changesets
adding manifests
adding file changes
added 1 changesets with 1775 changes to 1775 files
updating to branch default
1775 files updated, 0 files merged, 0 files removed, 0 files unresolved
remote: 1 changesets found
```

Se verifica el repositorio local.

```
ernesto@zeath:~$ hg log conf-www.respo.org.ve/
changeset:   0:10c12e9f2889
tag:         tip
user:        ecrespo@gmail.com
date:        Thu Dec 08 19:11:24 2011 +0000
summary:     Inicializacion del control de versiones
```

Ya se tiene respaldada la configuración del servidor por medio de control de versiones, si se desea tener automatizado el proceso se puede crear scripts que se coloquen en el cron de manera que diariamente se tenga actualizado el respaldo de la configuración del servidor por medio de control de versiones distribuido (mercurial).

Es recomendable sacar del control de versiones los archivos `shadow`, `passwd` y `group`.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
