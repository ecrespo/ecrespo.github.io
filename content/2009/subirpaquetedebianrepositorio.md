Title: Subir un paquete Debian (pyching) al repositorio
Date: 2000-04-09 10:00
Category: Linux,Empaquetado
Tags: Debian,Paquetes
lang: es
translation: true

Como la intención es utilizar el comando hg-buildpackage para construir un paquete
Debian, pero como en Debian muy pocos usan mercurial como repositorio. Tuve que crear
un repositorio en bitbucket.org para mis paquetes.

Para ello es necesario crear el repositorio en bitbucket.org.

Luego su equipo crear el directorio del paquete:

```
mkdir pyching
cd pyching
```

Bajarse las fuentes de pyching:
```
apt-get source pyching
Leyendo lista de paquetes... Hecho
Creando árbol de dependencias
Leyendo la información de estado... Hecho
Necesito descargar 139kB de archivos fuente.
Des:1 http://debian.velug.org.ve sid/main pyching 1.2.2-5 (dsc) [1092B]
Des:2 http://debian.velug.org.ve sid/main pyching 1.2.2-5 (tar) [134kB]
Des:3 http://debian.velug.org.ve sid/main pyching 1.2.2-5 (diff) [3931B]
Descargados 139kB en 5s (27,8kB/s)
dpkg-source: extracting pyching in pyching-1.2.2
dpkg-source: info: unpacking pyching_1.2.2.orig.tar.gz
dpkg-source: info: applying pyching_1.2.2-5.diff.gz

```

Cambiarse al directorio pyching-1.2.2:

```
cd pyching-1.2.2
```

Crear el repositorio:

```
ecrespo@canaima:~/paquetes/pyching/pyching-1.2.2$ hg init
```

Agregar las fuentes al repositorio:

```
ecrespo@canaima:~/paquetes/pyching/pyching-1.2.2$ hg add
adding #smgHtmlView.py#
adding BUGS
adding CHANGES
adding COPYING
adding COPYRIGHT
adding CREDITS
adding INSTALL
adding NEWS
adding README
adding debian/changelog
adding debian/compat
adding debian/control
adding debian/copyright
adding debian/dirs
adding debian/docs
adding debian/menu
adding debian/pyching-small.xpm
adding debian/pycompat
adding debian/rules
adding debian/watch
adding icon.xbm
adding pyching.1
adding pyching.png
adding pyching.py
adding pyching.pyw
adding pyching.sh
adding pyching_cimages.py
adding pyching_engine.py
adding pyching_hlhtx_data.py
adding pyching_idimage_data.py
adding pyching_int_data.py
adding pyching_interface_tkinter.py
adding smgAbout.py
adding smgAnimate.py
adding smgDialog.py
adding smgHtmlView.py

```

Se hace el commit:

```
ecrespo@canaima:~/paquetes/pyching/pyching-1.2.2$ hg commit -m"Subir el paquete pyching al repositorio"
```

Subir al repositorio:

```
ecrespo@canaima:~/paquetes/pyching/pyching-1.2.2$ hg push http://bitbucket.org/ecrespo/pyching/
pushing to http://bitbucket.org/ecrespo/pyching/
searching for changes
http authorization required
realm: Bitbucket.org HTTP
user: ecrespo
password:
bb/acl: ecrespo is allowed. accepted payload.
quota: 340.8 KB in use, 150.0 MB available (0.22% used)
```

Ya en este punto el paquete se encuentra en el servidor de repositorios mercurial.


![pyching](./imagenes/pyching.png)

Ahora se crea un directorio temporal para trabajar con los fuentes para empaquetarlo:

```
ecrespo@canaima:~/paquetes/pyching/temporal$ hg clone http://bitbucket.org/ecrespo/pyching/
destination directory: pyching
requesting all changes
adding changesets
adding manifests
adding file changes
added 1 changesets with 36 changes to 36 files
updating working directory
36 files updated, 0 files merged, 0 files removed, 0 files unresolved

```

Para finalizar se ejecuta el comando para empaquetar:

```
ecrespo@canaima:~/paquetes/pyching/temporal/pyching-1.2.2$ hg-buildpackage -us -uc -rfakeroot
Upstream file/directory already exists; not building
dpkg-buildpackage -rfakeroot -D -us -uc -i.hg -I.hg
dpkg-buildpackage: set CFLAGS to default value: -g -O2
dpkg-buildpackage: set CPPFLAGS to default value:
dpkg-buildpackage: set LDFLAGS to default value:
dpkg-buildpackage: set FFLAGS to default value: -g -O2
dpkg-buildpackage: set CXXFLAGS to default value: -g -O2
dpkg-buildpackage: source package pyching
dpkg-buildpackage: source version 1.2.2-5
dpkg-buildpackage: source changed by Ernesto Nadir Crespo Avila
dpkg-buildpackage: host architecture i386
fakeroot debian/rules clean
dh_testdir
dh_testroot
dh_clean
dpkg-source -i.hg -I.hg -b pyching-1.2.2
dpkg-source: info: using source format `1.0'
dpkg-source: info: building pyching using existing pyching_1.2.2.orig.tar.gz
dpkg-source: info: building pyching in pyching_1.2.2-5.diff.gz
dpkg-source: warning: ignoring deletion of file #smgHtmlView.py#
dpkg-source: info: building pyching in pyching_1.2.2-5.dsc
debian/rules build
make: No se hace nada para `build'.
fakeroot debian/rules binary
dh_testdir
dh_testroot
dh_prep
dh_installdirs
install -m 644 pyching_cimages.py pyching_engine.py \
pyching_hlhtx_data.py pyching_idimage_data.py \
pyching_int_data.py pyching_interface_tkinter.py \
smgAbout.py smgAnimate.py smgDialog.py smgHtmlView.py \
debian/pyching/usr/share/pyching/
install -m 755 pyching.py debian/pyching/usr/share/pyching/
install -m 644 pyching.png debian/pyching-small.xpm debian/pyching/usr/share/pixmaps/
install pyching.sh debian/pyching/usr/games/pyching
ln -s ../doc/pyching/CREDITS debian/pyching/usr/share/pyching/CREDITS
dh_testdir
dh_testroot
dh_installchangelogs CHANGES
dh_installdocs
dh_installmenu
dh_installman pyching.1
dh_link
dh_compress
dh_fixperms
dh_pycentral
dh_python /usr/share/pyching
dh_python: Doing nothing since dh_pycompat exists; dh_pysupport or dh_pycentral should do the work. You can remove dh_python from your rules file.
dh_installdeb
dh_gencontrol
dh_md5sums
dh_builddeb
atención, `debian/pyching/DEBIAN/control' contiene un campo `Python-Version' definido por el usuario
dpkg-deb: no se tendrán en cuenta 1 avisos sobre los ficheros de control
dpkg-deb: construyendo el paquete `pyching' en `../pyching_1.2.2-5_all.deb'.
dpkg-genchanges >../pyching_1.2.2-5_i386.changes
dpkg-genchanges: not including original source code in upload
dpkg-buildpackage: binary and diff upload (original source NOT included)
Now running lintian...
Finished running lintian.

```

Luego se revisa el directorio donde se creo el paquete:

```
ecrespo@canaima:~/paquetes/pyching/temporal/pyching-1.2.2$ cd ..
ecrespo@canaima:~/paquetes/pyching/temporal$ ls
pyching-1.2.2 pyching_1.2.2-5.diff.gz pyching_1.2.2-5_i386.build pyching_1.2.2.orig.tar.gz
pyching_1.2.2-5_all.deb pyching_1.2.2-5.dsc pyching_1.2.2-5_i386.changes
```



===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
