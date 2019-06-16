Title: Descubrir equipos en una Red Local con Python (ipcalc y scapy).
Date: 2013-04-22 9:00
Category: Tutorial Python
Tags: Canaima,Debian,General,Linux,Python,scapy,ipcalc
lang: es
translation: true


Si se tiene una red con asignación abierta de IPs, la administración se hace algo complicada, así que se necesita tener un registro de la asignación de IPs a los equipos de la red local.

Una amiga administradora hizo un registro con una herramienta propietaria en Windows. Recordé la librería de python ipcalc que facilita el cálculo de direcciones IP y redes (un artículo de su uso [acá](https://scapy.readthedocs.io/en/latest/#about-scapy)).

Además existe la librería o herramienta scapy, el cual permite capturar y modificar paquetes de red (la documentación se puede revisar en el siguiente [enlace](https://scapy.readthedocs.io/en/latest/#about-scapy)).

Una alternativa es usar los comandos ping y arp por medio de python con el módulo commands; es preferible usar scapy que permite descubrir la dirección MAC de los equipos que tienen asignado las IPs.

Así que por un lado se usa ipcalc para definir el rango de la red según la mascara y luego con scapy se descubre las direcciones MAC.

A continuación el código que devuelve la dirección MAC de cada IP utilizada en la red:

```python

#!/usr/bin/env python

#Se importa los modulos necesarios.

from ipcalc import IP, Network

from scapy.all import srp,Ether,ARP,conf

#Se desactiva el verbose de la captura y envio de paquetes.

conf.verb=0

#Se genera un ciclo con el rango de IPs dando la RED y la mascara

for ip in Network('192.168.12.128/25'):

    #Se realiza un broadcast de MAC pasando cada IP el cual devuelve la 

    #direccion MAC de la IP consultada.

    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=str(ip)),timeout=2)

    for snd,rcv in ans:

        #Se muestra en pantalla la direccion MAC y la direccion IP

        print rcv.sprintf(r"%Ether.src% y %ARP.psrc%")
```

Al ejecutar el programa se tiene lo siguiente:

```python

ernesto@jewel:~/bin/python$ sudo ./descubrir.py

WARNING: No route found for IPv6 destination :: (no default route?)

00:26:35:c6:93:0d y 192.168.12.130

00:2e:0b:c5:70:3c y 192.168.12.132

00:2e:90:c2:ec:51 y 192.168.12.134

00:50:ca:c1:71:8a y 192.168.12.136

00:32:57:ce:81:e7 y 192.168.12.138

00:2e:90:c4:58:7c y 192.168.12.139

00:2c:25:ce:ae:be y 192.168.12.140

d0:37:88:c4:11:ed y 192.168.12.141

00:2e:90:cc:f5:16 y 192.168.12.142

00:2c:c4:c4:26:28 y 192.168.12.148

40:7a:ab:ce:11:c0 y 192.168.12.150

3c:53:8e:cc:4d:89 y 192.168.12.161

1c:5b:d6:c9:6d:a9 y 192.168.12.169

00:2e:7f:c4:8d:d7 y 192.168.12.170

00:24:c2:c8:23:8d y 192.168.12.172

68:19:ed:c75:44:31 y 192.168.12.174

74:3f:68:c2:91:d6 y 192.168.12.196

00:30:aa:c2:6d:3c y 192.168.12.201

c8:3c:dc:c8:a9:53 y 192.168.12.208

00:34:f2:c5:2f:21 y 192.168.12.211

00:34:f2:cc:2e:d0 y 192.168.12.212

00:34:f2:c5:35:70 y 192.168.12.214

00:34:f2:c3:1a:ee y 192.168.12.215

00:34:f2:c3:1b:4c y 192.168.12.216

00:34:f2:c5:33:49 y 192.168.12.224

00:3c:02:c6:b5:3f y 192.168.12.225

00:3e:90:c8:bb:d6 y 192.168.12.251
```


Así pues desde Linux y con Python se puede capturar la información de las direcciones MAC de las IPs asignadas con pocas líneas de código.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)