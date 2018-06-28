Title: Instalar Debian en la Asus EEE PC 901
Date: 2009-03-15 11:00
Category: Linux,Debian
Tags: Linux,Debian, Asus
lang: es
translation: true

Luego de instalar Xandros instalaré Debian Lenny, los pasos son los siguientes:

1. Bajar Imagen del instalador de aquí junto con el archivo md5.

2. Verificar que la imagen bajara correctamente con el comando md5sum debian-eeepc.img.

3. Copiar la imagen en el pendrive (preferiblemente de 1GB mínimo o máximo 2 GB ya que algunos
  pendrive de mayor capacidad no funcionan en la Asus). Con el Comando data dump y el nombre del
  dispositivo se tiene para ejecutar el comando dd if=./debian-eeepc.img of=/dev/sdb, donde sdb
  es el caso de mi dispositivo en el computador que estoy utilizando.

4. Se reinicia el equipo se selecciona F2 para configurar el arranque por pendrive USB y se inicia el proceso de arranque del instalador.

5. El proceso de instalación es el mismo del instalador de Lenny, la diferencia es que esta
versión soporta en el arranque la tarjeta inalámbrica atheros.

El siguiente post se explicará todo el proceso de configuración de Debian en la Asus para luego probar instalar Android.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
