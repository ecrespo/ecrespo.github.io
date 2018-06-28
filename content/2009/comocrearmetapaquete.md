Title: Como crear un metapaquete
Date: 2009-03-29 11:00
Category: Linux
Tags: Debian,paquetes
lang: es
translation: true

Los metapaquetes nos facilitan el trabajo en la selección de programas, por
ejemplo, en Debian existe una lista de programas educativos y para instalarlos
todos seleccionando un sólo programa se usa el paquete debianedu que es un
metapaquete que tiene como dependencias todos los paquetes educativos.

Esa es la forma como trabaja ubuntu con kubuntu, xubuntu y sus otros sabores,
simplemente un metapaquete que maneja cada versión de ubuntu.

El programa en Debian para la creación de metapaquetes se llama equivs.

Para instalarlo se ejecuta aptitude install equivs.

Este paquete maneja dos programas:

* equivs-control: Crea un archivo como el archivo control de los paquetes de debian
donde se maneja la información del mantenedor, versión del paquete, dependencias entre
otras cosas.
* equivs-build: Crea el metapaquete del archivo que crea equivs-control.

Para crear la plantilla se ejecuta el comando con el nombre del paquete: equivs-control accesibilidad.
Esto crea la siguiente plantilla:

```
### Commented entries have reasonable defaults.
### Uncomment to edit them.
Section: misc
Priority: optional
Standards-Version: 3.6.2

Package:
# Version:
# Maintainer: Your Name
# Pre-Depends:
# Depends:
# Recommends:
# Suggests:
# Provides:
# Replaces:
# Architecture: all
# Copyright:
# Changelog:
# Readme:
# Extra-Files:
Description:
long description and info
.
second paragraph
```

Este archivo maneja la sección del paquete, la prioridad, la versión del Debian policy
(actualmente 3.8.0), el nombre del paquete, la versión, el nombre del mantenedor,las
dependencias (pre, dependencias, recomendaciones,provee y reemplaza), derechos, changelog,
readme, archivos adicionales y por último la descripción del paquete separado en 2 partes,
una descripción corta y una larga.

A continuación mostraré el archivo para accesibilidad, este manejará las dependencias
de los siguientes paquetes:

* brltty: Braille
* brltty-x11: Braille
* libcolorblind-dev: Daltonismo
* libcolorblind0: Daltonismo
* gnome-orca: Lector de pantalla orca

```
Section: misc
Priority: optional
Standards-Version: 3.8.0

Package: accesibilidad
Version: 1.0
Maintainer: Ernesto Nadir Crespo Avila
Depends: brltty, brltty-x11, libcolorblind-dev, libcolorblind0, gnome-orca
Architecture: all
Description: Metapaquete para la instalacion de aplicaciones de accesibilidad
Metapaquete para la instalacion de aplicaciones de accesibilidad para personas invidentes
```

Para crear el paquete se ejecuta el comando equivs-build accesibilidad:

```
ecrespo@canaima:~/canaima2/accesibilidad$ equivs-build accesibilidad
dh_testdir
dh_testroot
dh_clean -k
dh_testdir
dh_testroot
dh_install
dh_installdocs
dh_installchangelogs
dh_compress
dh_fixperms
dh_installdeb
dh_gencontrol
dh_md5sums
dh_builddeb
dpkg-deb: construyendo el paquete `accesibilidad' en `../accesibilidad_1.0_all.deb'.

The package has been created.
Attention, the package has been created in the current directory,
not in ".." as indicated by the message above!
```

Luego al ejecutar un ls se tiene el paquete accesibilidad_1.0_all.deb.

Este paquete no se puede instalar con dpkg ya que dará error por que dpkg no
maneja las dependencias, para ello es más útil usar apt-get o aptitude, pero
para lograrlo es necesario subir el paquete a un repositorio local para que se
pueda instalar por apt-get o aptitude (como crear un repositorio local en
el próximo post).

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
