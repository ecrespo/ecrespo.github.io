Title: Copiar Xandros en pendrive para iniciar el proceso de instalación en la Asus EEEPC
Date: 2009-03-15 09:00
Category: Linux
Tags: Debian,Asus  
lang: es
translation: true

Una de las cosas simpaticas del Xandros que trae la Asus EEEPC 901 es el paradigma de escritorio que se aleja del escritorio tradicional y se acerca a la interfaz de los dispositivos moviles como celulares.
He durado un tiempo usando la EEEPC 901 con Debian y quería probar el proceso de instalación de Xandros para reinstalar Debian la versión estable Lenny.

Se necesita un Pendrive de 2GB aproximadamente ya que a veces el equipo no lee pendrive mayores a 2GB y los de 1GB no son suficientes para crear el sistema de arranque.

Lo primero que hay que hacer es buscar el DVD del Asus llamado Recuperación de Linux Rev 1.0. Se copian los archivos:

* P701L.gz
* usb.img
* user_start.dat
* 2008.04.03_20.30.bld
* blockcount.dat

Lo primero que se necesita hacer es conectar el pendrive y ejecutar el comando data dump:

```
dd if=./usb.img of=/dev/sdb
```

En mi caso el pendrive es el dispositivo sdb.

Luego es necesario montar el pendrive y copiar los archivos P701L.gz, user_start.dat, 2008.04.03_20.30.bld y blockcount.dat

```
mount /dev/sdb1 /mnt/temporal
cp -v P701L.gz 2008.04.03_20.30.bld blockcount.dat user_start.dat /media/EEEPC/
```

Con este procedimiento ya se tiene creado el pendrive de arranque y sólo queda conectar el pendrive en el Asus para iniciar el proceso de instalación.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
