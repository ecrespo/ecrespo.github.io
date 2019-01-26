Title: Iniciar sesión de usuario autenticando vía pendrive
Date: 2011-07-26 09:00
Category: Tutorial de Linux
Tags: Linux,Debian, Ubuntu, Canaima,libpam,gnome, usb
lang: es
translation: true

Cuando no se pasa uno a modo paranoico se le ocurren ideas de como validar usuarios al ingresar en una sesión de escritorio vía GDM.

En Debian/Ubuntu/Canaima existe los paquetes libpam-usb y pamusb-tools, estos permiten crear una llave, dicha llave se guarda en el pendrive. Luego se configura pam para que se pida la llave al momento de ingresar usuario y clave en el GDM del equipo; si no se conecta el pendrive el GDM colocará un mensaje que clave invalida.

Para instalar estos paquetes se ejecuta aptitude:

```
aptitude install libpam-usb pamusb-tools
```

Luego se conecta el pendrive en el equipo y se agrega el dispositivo en /etc/pamusb.conf con el comando pamusb-conf:

```
pamusb-conf --add-device /media/F060-785C/
```

Donde /media/F060-785C/ es la ruta del pendrive.

Se agrega el usuario en /etc/pamusb.conf el cual iniciará sesión en el equipo:

```
pamusb-conf --add-user ecrespo
```

Se verifica la configuración de pamusb con el usuario agregado:

```
pamusb-check ecrespo
* Authentication request for user "ecrespo" (pamusb-check)
* Device "/media/F060-785C/" is connected (good).
* Performing one time pad verification...
* Regenerating new pads...
* Unable to update pads.
* Access granted.
```

Al devolver el programa acceso garantizado ya se tiene todo listo para usar el pendrive en el momento de inicio de sesión, sólo falta modificar pam para que permita la autenticación con el pendrive.

Se edita el archivo /etc/pam.d/common-aut y se agrega la siguiente línea:

```
auth sufficient pam_usb.so
```

Con esta línea el GDM verifica el token de la llave, si se quiere que pida tanto la contraseña como el token se cambia sufficient a required.

```
auth required pam_usb.so
```

A partir de ahora al iniciar sesión se necesita la contraseña y el token.

A continuación se muestra el mensaje que envía la consola al ejecutar sudo -s :

```
[sudo] password for ecrespo: 
* pam_usb v0.4.2
* Authentication request for user "ecrespo" (sudo)
* Device "/media/F060-785C/" is connected (good).
* Performing one time pad verification...
* Regenerating new pads...
* Unable to update pads.
* Access granted.
```



===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
