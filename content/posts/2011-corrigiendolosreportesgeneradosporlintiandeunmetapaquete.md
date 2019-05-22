Title: Corrigiendo los reportes generados por lintian de un metapaquete
Date: 2011-09-22 09:00
Category: Linux,Empaquetado
Tags: Canaima,Debian,Empaquetado,General,Linux,Ubuntu
lang: es
translation: true


Este artículo explicará como corregir los mensajes generados por `lintian`, estos mensajes son debido a que el programa empaquetado o metapaquete no cumple con el [policy de Debian](http://www.debian.org/doc/debian-policy/) y para subir dicho programa es necesario que esté sin errores ni warning.

El archivo que se va a verificar es el [.dsc del metapaquete creado al empaquetar canaima-caribay-radio](https://gitorious.org/sierra-nevada/canaima-caribay-radio/blobs/master/canaima-caribay-radio_1.0.dsc).

Al ejecutar `lintian` con el archivo `dsc` devuelve el siguiente mensaje:

```
lintian -i canaima-caribay-radio_1.0.dsc
```

```
W: canaima-caribay-radio source: debhelper-but-no-misc-depends canaima-caribay-radio
N: 
N:The source package uses debhelper, but it does not include
N:${misc:Depends} in the given binary package's debian/control entry. Any
N:debhelper command may add dependencies to ${misc:Depends} that are
N:required for the work that it does, so recommended best practice is to
N:always add ${misc:Depends} to the dependencies of each binary package if
N:debhelper is in use.
N:
N:Refer to the debhelper(7) manual page for details.
N:
N:Severity: normal, Certainty: possible
N: 
W: canaima-caribay-radio source: package-uses-deprecated-debhelper-compat-version 4
N: 
N:The debhelper compatibility version used by this package is marked as
N:deprecated by the debhelper developer. You should really consider using
N:a newer compatibility version.
N:
N:The compatibility version can be set in (preferred) debian/compat or by
N:setting and exporting DH_COMPAT in debian/rules. If it is not set in
N:either place, debhelper defaults to the deprecated compatibility version
N:1.
N:
N:Refer to the debhelper(7) manual page for details.
N:
N:Severity: normal, Certainty: certain
N: 
W: canaima-caribay-radio source: binary-arch-rules-but-pkg-is-arch-indep
N: 
N:It looks like you try to run code in the binary-arch target of
N:debian/rules, even though your package is architecture- independent.
N:
N:Severity: normal, Certainty: certain
N: 
```

El primer warning es que hace falta agregar `${misc:Depends]` en las dependencias.  Adicionalmente se tiene que cambiar el parámetro `Standards-Version` a la versión `3.9.1`.

```
Section: misc
Priority: optional
Homepage: http://canaima.softwarelibre.gob.ve
Standards-Version: 3.9.1

Package: canaima-caribay-radio
Version: 1.0
Maintainer: Ernesto Nadir Crespo Avila <ecrespo@cenditel.gob.ve>
Depends: ${misc:Depends},jackd2, libjack-jackd2-0, libjack-jackd2-dev, pulseaudio-module-jack, qjackctl,  
libjack-jackd2-0, libjack-jackd2-dev, vorbis-tools, libvorbis-dev, libogg-dev, libmad0-dev, libsamplerate0-dev,  
libflac-dev, libsndfile1-dev, libavcodec-dev, libavformat-dev, libspeex-dev, python-gtk2-dev,  
python-mutagen, libdbus-1-dev, ffmpeg, libshout3-dev, libtwolame-dev, twolame,
idjc, audacity, audacity-data, audacity-dbg, icecast2, easytag
Architecture: all
Copyright: copyright
Changelog: changelog 
Description: Metapaquete para la instalacion de radio streaming
Metapaquete para la instalacion de radio streaming con icecast2 e idjc.
```


El segundo warning menciona que el archivo `debian/compat` tiene dentro el número 4 y es necesario que se actualice a la versión de `debhelper` que se está usando para empaquetar, en este caso debe cambiar a 8. Esto se tiene que cambiar en la plantilla de `equivs`.  

```
vim /usr/share/equivs/template/debian/compat
```  

Cambiar 4 por 8.

El siguiente warning menciona un problema en la definición de la arquitectura, que es necesario quitar `binary-arch` y nuestro paquete es independiente de la plataforma. Esto se resuelve modificando `canaima-caribay-radio` cambian el parámetro `Architecture: all` por `any`.

Luego de realizar esos cambios se vuelve a crear el metapaquete y a ejecutar `lintian`:

```
lintian -i canaima-caribay-radio_1.0.dsc
```

```
W: canaima-caribay-radio source: dh-clean-k-is-deprecated
N: 
N:This package calls dh_clean -k in its debian/rules file and declares a
N:debhelper compatibility version of at least 7.
N:
N:debhelper 7 deprecated dh_clean -k in favour of dh_prep.
N:
N:Refer to the dh_clean(1) manual page for details.
N:
N:Severity: normal, Certainty: certain
N: 
W: canaima-caribay-radio source: package-lacks-versioned-build-depends-on-debhelper 8
N: 
N:The package either doesn't declare a versioned build dependency on
N:debhelper or does not declare a versioned build dependency on a new
N:enough version of debhelper to satisfy the declared compatibility level.
N:
N:Recommended practice is to always declare an explicit versioned
N:dependency on debhelper equal to or greater than the compatibility level
N:used by the package, even if the versioned dependency isn't strictly
N:necessary. Having a versioned dependency also helps with backports to
N:older releases and correct builds on partially updated systems.
N:
N:Refer to the debhelper(7) manual page for details.
N:
N:Severity: minor, Certainty: certain
N: 
```

Luego de cambiar el archivo `compat` y la versión del `standards-version` aparece un warning sobre el comando `dh_clean -k` que se tiene que sustituir por `dh_prep` en el archivo `debian/rules` de la plantilla:

```
vim /usr/share/equivs/template/debian/rules
```

```
install: build
dh_testdir
dh_testroot
dh_prep
```

El otro warning menciona que `debhelper` tiene un número de versión viejo. Para cambiarlo se busca el archivo `control.in` en las plantillas y se modifica la `dep`

```
vim /usr/share/equivs/template/debian/control.in
```

Se modifica la siguiente línea:

```
Build-Depends: debhelper (>= 8)
```

Se vuelve a empaquetar y a ejecutar `lintian`:  

```
lintian -i canaima-caribay-radio_1.0.dsc
```

Listo, no más mensajes de error o warnings.  

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
