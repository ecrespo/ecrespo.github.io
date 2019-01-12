Title: Conectarse a internet por medio de un celular con android (AziLink)
Date: 2010-05-29 13:00
Category: Tutorial Linux
Tags: Linux, Android, Debian
lang: es
translation: true


A diferencia de las aplicaciones que usan http proxy AziLink permite conectarse por celular usando openvpn.

La página del proyecto AziLink lo puedes conseguir en este e[nlace](http://code.google.com/p/azilink/).

El enlace para bajar openvpn es openvpn.net. En Debian y Ubuntu con ejecutar un aptitude es suficiente:

```
aptitude install openvpn-blacklist openvpn

```

Los pasos son los siguientes:
1. Habilitar el modo depuración del USB en el teléfono. En el home de las apliaciones del celular ir a Configuración->Aplicaciones->Desarrollo->USB debugging.

2. Instale el SDK de Android, el procedimiento lo consigue en este [enlace](http://ernesto-ecrespo.blogspot.com/2010/05/instalacion-del-sdk-de-android-en-linux.html).
3. Instalar AziLink desde el market del celular.
4. En el computador hacer el redireccionamiento de puertos:

```
adb forward tcp:41927 tcp:41927
```

5. En el celular ejecutar AziLink y verificar que su servicio esté activo.
6. Bajar y descomprimir azilink.zip donde se encuentra el archivo de configuración.

La configuración de openvpn es la siguiente:

```
#Define tun como dispositivo
dev tun
#Define la IP y puerto remoto, el que se configuro en la redirección con adb
remote 127.0.0.1 41927 tcp-client
#Define la IP punto a punto de la conexión openvpn
ifconfig 192.168.56.2 192.168.56.1
#Define rutas
route 0.0.0.0 128.0.0.0
route 128.0.0.0 128.0.0.0
#Define flags del socket.
socket-flags TCP_NODELAY
#keepalive 10 30
ping 10
#Define el DNS por medio de las opciones de dhcp
dhcp-option DNS 192.168.56.1
```

7. Agregar en /etc/resolv.conf el siguiente DNS:

```
nameserver 192.168.56.1
```

8. Iniciar openvpn con el archivo de configuración:

```
sudo openvpn --config azilink.ovpn 
```

```
Sat May 29 23:28:18 2010 OpenVPN 2.1.0 i486-pc-linux-gnu [SSL] [LZO2] [EPOLL] [PKCS11] [MH] [PF_INET6] [eurephia] built on Apr 10 2010
Sat May 29 23:28:18 2010 WARNING: --ping should normally be used with --ping-restart or --ping-exit
Sat May 29 23:28:18 2010 NOTE: OpenVPN 2.1 requires '--script-security 2' or higher to call user-defined scripts or executables
Sat May 29 23:28:18 2010 ******* WARNING *******: all encryption and authentication features disabled -- all data will be tunnelled as cleartext
Sat May 29 23:28:18 2010 TUN/TAP device tun0 opened
Sat May 29 23:28:18 2010 /sbin/ifconfig tun0 192.168.56.2 pointopoint 192.168.56.1 mtu 1500
Sat May 29 23:28:18 2010 Attempting to establish TCP connection with [AF_INET]127.0.0.1:41927 [nonblock]
Sat May 29 23:28:18 2010 TCP connection established with [AF_INET]127.0.0.1:41927
Sat May 29 23:28:18 2010 TCPv4_CLIENT link local: [undef]
Sat May 29 23:28:18 2010 TCPv4_CLIENT link remote: [AF_INET]127.0.0.1:41927
Sat May 29 23:28:21 2010 Peer Connection Initiated with [AF_INET]127.0.0.1:41927
Sat May 29 23:28:22 2010 Initialization Sequence Completed
```

Al revisar en whatismyip.com la IP que se está usando es la siguiente 201.239.27.224.

Personalmente prefiero está opción que usar http proxy, el archivo de configuración de openvpn se puede mejorar como permitir que copie el archivo de resolv.conf al momento de levantar el vpn y colocar el archivo anterior al detener el vpn.


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)