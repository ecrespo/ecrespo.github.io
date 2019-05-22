Title: Creación de paquete Debian que contiene un archivo cron con config-package-dev
Date: 2011-11-14 09:00
Category: Linux,Empaquetado
Tags: Canaima,Debian,Empaquetado,General,Ubuntu
lang: es
translation: true

El paquete `config-package-dev` facilita la creación de un paquete Debian que contenga un archivo de configuración de cron.

Para este caso se creará un archivo cron para el programa `logcheck`. Este programa estará como Pre-Depends para que esté instalado y configurado antes de instalar el paquete con la configuración de `logcheck` en el cron.

Instalar `logcheck`:  

```
apt-get install logcheck
```

El archivo cron para `logcheck` contendrá lo siguiente:

```
# /etc/cron.d/logcheck: crontab entries for the logcheck package

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

@reboot logcheckif [ -x /usr/sbin/logcheck ]; then nice -n10 /usr/sbin/logcheck -R; fi
* * * * *   logcheckif [ -x /usr/sbin/logcheck ]; then nice -n10 /usr/sbin/logcheck; fi

# EOF
```

##Procedimiento para la creación del paquete:  

 
#### 1. Creación del directorio de trabajo y del directorio Debian

``` 
mkdir -p canaima-cron-logcheck-0.1

mkdir -p canaima-cron-logcheck-0.1/debian
```

#### 2. Se crea el archivo `debian/changelog`.  

```
canaima-cron-logcheck (0.1) unstable; urgency=low

* Initial release.

-- Ernesto Nadir Crespo Avila <ecrespo@gmail.com>  Mon, 14 Nov 2011 21:48:20 -0430
```

#### 3. Se crea el archivo `compat` con el valor de 7.

#### 4. Se crea el archivo `control` y `control.in` con lo siguiente:

Se coloca `logcheck` como predependencia, se define el `standar version` con valor `3.9.2`.  

```
Source: canaima-cron-logcheck
Section: config
Priority: extra
Maintainer: Ernesto Nadir Crespo Avila <ecrespo@gmail.com>
Build-Depends: cdbs (>= 0.4.23-1.1), debhelper (>= 4.2.0), config-package-dev (>= 4.5~)
Standards-Version: 3.9.2

Package: canaima-cron-logcheck
Architecture: all
Depends: cdbs, ${misc:Depends}
Pre-Depends: logcheck
Provides: ${diverted-files}
Conflicts: ${diverted-files}
Description: Configuracion de cron para logcheck
Configuracion de cron para logcheck.
```

#### 5. Se crea el archivo `debian/copyright`:
Se mantiene el autor del paquete ya que se está usando tal cual el ejemplo de cron para logcheck de `config-package-dev`.  

```
canaima-cron-logcheck.
Example config-package-dev package.

Author: Tim Abbott <tabbott@mit.edu>

Copyright © 2008 Tim Abbott <tabbott@mit.edu>

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

#### 6. Se crea el archivo `debian/canaima-cron-logcheck.cron.d` con el contenido del cron para `logcheck`:  
```
# /etc/cron.d/logcheck: crontab entries for the logcheck package

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
MAILTO=root

@reboot logcheckif [ -x /usr/sbin/logcheck ]; then nice -n10 /usr/sbin/logcheck -R; fi
* * * * *   logcheckif [ -x /usr/sbin/logcheck ]; then nice -n10 /usr/sbin/logcheck; fi

# EOF
```

#### 7. Se crea el archivo `debian/rules` con el siguiente contenido:
```
#!/usr/bin/make -f

DEB_DIVERT_EXTENSION = .canaima

 # This will remove /etc/cron.d/logcheck
  DEB_REMOVE_FILES_canaima-cron-logcheck += \
/etc/cron.d/logcheck

 # We will install (using dh_installcron, by placing the new cron job
 # at debian/canaima-cron-logcheck.cron.d) a new version that runs
 # every minute, rather than every 30 minutes.  This will generate a
 # lot of mail.  Note that we cannot install a new file to the path
 # /etc/cron.d/logcheck from which a file was removed using
 # DEB_REMOVE_FILES.

include /usr/share/cdbs/1/rules/debhelper.mk
include /usr/share/cdbs/1/rules/config-package.mk
```

#### 8. Se le agrega permiso de ejecución al archivo `debian/rules`:
	
```
chmod a+x debian/rules
```

#### 9. Al final se tienen los siguientes archivos:
```
ecrespo@jewel:~/canaima/canaima-cron-logcheck-0.1$ ls -l debian/
total 28
-rw-r--r-- 1 ecrespo ecrespo  347 nov 14 22:02 canaima-cron-logcheck.cron.d
-rw-r--r-- 1 ecrespo ecrespo  157 nov 14 21:50 changelog
-rw-r--r-- 1 ecrespo ecrespo2 nov 14 21:50 compat
-rw-r--r-- 1 ecrespo ecrespo  481 nov 14 21:55 control
-rw-r--r-- 1 ecrespo ecrespo  481 nov 14 21:55 control.in
-rw-r--r-- 1 ecrespo ecrespo 1169 nov 14 22:01 copyright
-rwxr-xr-x 1 ecrespo ecrespo  612 nov 14 22:06 rules
```

#### 10. Se crea y se firma el paquete `canaima-cron-logcheck-0.1`:

```
dpkg-buildpackage -rfakeroot -kC97E7015
```

#### 11. Al final se creán los siguientes archivos:  
```
ls -l canaima-cron-logcheck*
-rw-r--r-- 1 ecrespo ecrespo 2902 nov 14 22:08 canaima-cron-logcheck_0.1_all.deb
-rw-r--r-- 1 ecrespo ecrespo  876 nov 14 22:08 canaima-cron-logcheck_0.1.dsc
-rw-r--r-- 1 ecrespo ecrespo 1551 nov 14 22:09 canaima-cron-logcheck_0.1_i386.changes
-rw-r--r-- 1 ecrespo ecrespo 1807 nov 14 22:08 canaima-cron-logcheck_0.1.tar.gz
```

#### 12. Se verifica si el paquete cumple con las políticas de Debian con `lintian`:

```
lintian -i canaima-cron-logcheck_0.1.dsc
```

#### 13. Se instala el paquete:

```
dpkg -i canaima-cron-logcheck_0.1_all.deb
```

#### 14. El archivo del cron se encuentra ya instalado:  
```
ls -l /etc/cron.d
total 12
-rw-r--r-- 1 root root 244 nov  1  2009 anacron
-rw-r--r-- 1 root root 347 nov 14 22:08 canaima-cron-logcheck
-rw-r--r-- 1 root root 544 sep 13 05:59 php5
```

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)