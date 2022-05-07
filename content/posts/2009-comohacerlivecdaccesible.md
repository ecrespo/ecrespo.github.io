Title: Como hacer un live-usb o live-cd
Date: 2009-03-29 10:00
Category: Linux
Tags: Live-CD,Debian,Instalación
lang: es
translation: true

Basandome en las guías de los siguientes enlaces  [live-usb](http://www.debian-administration.org/articles/630) y el tutorial en español de [Debian Live](http://el-directorio.org/DebianLive#head-9df2b36e5793bbfb9353ffbf472fb3e38608935e), es un tutorial de la antigua versión de live-helper llamada live-package
o este otro [tutorial](http://wiki.freenetproject.org/deDebianLiveCD) que explica como remasterizar el live-cd.

Live-helper es un framework que permite la creación de un live-cd o live-usb basandose
en un sistema Debian.

Se necesita un equipo con suficiente espacio en disco para poder construir el sistema
live con 3GB de espacio es suficiente.

1. Instalar live-helper:

```
aptitude install live-helper
```

2. Crear un directorio para trabajar en el ambiente:  

```
mkdir live-usb
```

3. Cambiarse al directorio de trabajo.

```
cd live-usb
```

4. Crear la configuración para la creación del live-usb.

```
lh_config -b usb-hdd -d lenny --mirror-bootstrap http://debian.velug.org.ve/debian/ --mirror-chroot http://debian.velug.org.ve/debian/ --mirror-binary http://debian.velug.org.ve/debian --username Usuario --iso-publisher "Ernesto Crespo" -l es --security disabled --hostname live-usb --bootappend-live "locale=es_VE.UTF-8 keyb=es" --packages-lists "gnome gdm iceweasell-i10n-es-es iceweasel pidgin openoffice openoffice.org-writer openoffice.org-l10n-es myspell-es evince less mc module-assistant wireless-tools printconf hpijs foomatic-db-gutenprint cupsys-bsd foomatic-filters-ppds hplip foomatic-db-hpijs cupsys cupsys-client cupsys-driver-gutenprint foomatic-db-engine vim-full "
```

5. Crear la imagen.

```
lh_build
```

6. Copiar la imagen binary.img al pendrive. Si el dispositivo se identifica como /dev/sda se ejecuta el siguiente comando.

```
dd if=./binary.img of=/dev/sda bs=1M
```

7.1. Probar el iso. Si es un live-cd se ejecuta:

```
qemu -cdrom binary.img -boot d
```

7.2. Si es un live-usb se ejecuta:

```
qemu -hda binary.img -boot c
```

En este proceso se creará una imagen llamada binary.img para dispositivos USB, se definió
el repositorio a utilizar, el nombre de usuario del live, una descripción de la persona
quien está publicando el live, se definió los locales a utilizar y el mapa del teclado al
momento del arranque del live; por último se define la lista de paquetes a utilizar en el live-usb.

Si se desea crear un live-cd se tiene que considerar que el espacio máximo que puede tener el live-cd
es de 700MB, para ello la configuración del ambiente es la siguiente:

```
lh_config -b iso -d lenny --mirror-bootstrap http://debian.velug.org.ve/debian/ --mirror-chroot http://debian.velug.org.ve/debian/ --mirror-binary http://debian.velug.org.ve/debian --username usuario --iso-publisher "Ernesto Crespo" -l es --security disabled --hostname live-cd --bootappend-live "locale=es_VE.UTF-8 keyb=es" --bootstrap-flavour minimal --apt apt --linux-flavours 486 --binary-indices disabled --memtest disabled --apt-recommends disabled --packages-lists "gnome gdm iceweasell-i10n-es-es iceweasel pidgin openoffice openoffice.org-writer openoffice.org-l10n-es myspell-es evince less mc module-assistant wireless-tools printconf hpijs foomatic-db-gutenprint cupsys-bsd foomatic-filters-ppds hplip foomatic-db-hpijs cupsys cupsys-client cupsys-driver-gutenprint foomatic-db-engine"
```


Las opciones en color distinto permitirán reducir el tamaño del live-cd ya que se hará una imagen mínima,
se usará apt-get en vez de aptitude, se usará el kernel para arquitectura 486, se deshabilita los
indices de los binarios, la instalación de mentest y las recomendaciones de apt.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)