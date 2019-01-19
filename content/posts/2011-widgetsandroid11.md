Title: Control remoto del reproductor de música en Debian desde Android
Date: 2011-04-03 09:00
Category: Demostración Aplicación para Android
Tags: Android, Linux, Debian, gnome
lang: es
translation: true

Buscando aplicaciones para control remoto de reproductores de música en Linux desde Android me encontre con [tesla](http://sourceforge.net/apps/trac/android-tesla/).

Para instalar tesla en el celular se pueden bajar  el archivo apk desde [andAppStore](http://andappstore.com/AndroidApplications/apps/186356).
En su equipo con Debian es necesario instalar openssh y libpam-ck-connector.
aptitude install libpam-ck-connector openssh-server openssh-client openssh-blacklist-extra openssh-blacklist

Es necesario reiniciar ssh.
```
/etc/init.d/ssh restart.
```

Se tiene que conectar el celular a una red wifi igual que su computador.

Al iniciar tesla en el celular le pedirá la dirección IP de su computador, el usuario con el cual se inicia sesión y su clave como lo muestra la figura.

![App tesla - setup](./images/tesla1.png)

Se puede seleccionar otros reproductores que funcionan en Linux antes de darle conectar a la aplicación.

La siguiente imagen muestra a tesla funcionando en el celular y luego el productor Rhythmbox.

![App tesla - control](./images/reproductormusica.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
