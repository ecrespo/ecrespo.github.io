Title: Configuración de una tarjeta Motorola X100P
Date: 2008-04-13 10:10
Category: Asterisk, Debian, Linux
Tags: Asterisk 
lang: es
translation: true

Ya se tiene asterisk instalado y ahora viene la configuración 
de la tarjeta Motorola X100P.

### Procedimiento de configuración: 

1. Editar el archivo /etc/default/zaptel para que solo maneje 
el módulo que se debe utilizar ( wcfxo). Esto se logra comentando 
todos los módulos que no se van a utilizar.

2. Visualizar el dispositivo

```
zaptel_hardware -v
pci:0000:01:00.0 wcfxo- 1057:5608 Wildcard X100P
```

3. Verificar funcionamiento de la tarjeta

```
ztcfg -vvvvvvvvvvvvvv
Zaptel Version: 1.4.9.2
Echo Canceller: MG2
Configuration
======================


Channel map:

Channel 01: FXS Kewlstart (Default) (Slaves: 01)

1 channels to configure.
```

4. Editar el archivo /etc/asterisk/zapata.conf. Colocar las siguientes líneas:

```
[channels]
language=es
context=entrantes
signalling=fxs_ks
usecallerid=yes
hidecallerid=no
callwaiting=yes
callwaitingcallerid=yes
threewaycalling=yes
transfer=yes
cancallforward=yes
callreturn=yes
echocancel=yes
echocancelwhenbridged=yes
rxgain=0.0
txgain=0.0
group=1
pickupgroup=1
immediate=yes
musiconhold=default channel => 1
```

5. Recargar módulos

```
asterisk -rx "module reload"
```

6. Añadir extensión que permita a llamar por la tarjeta. Editar /etc/asterisk/extension.conf

```
[entrantes]
exten => s,1,Dial(SIP/1000,60,tr)
exten => s,2,Voicemail,u1000
exten => s,102,Voicemail,b1000 
```

Esta lineas le dice al Asterisk que todas las llamadas que recibe la tarjeta 
las dirija al telefono "1000", y despues de 60 segundos salta el buzon de voz.

Para realizar llamadas añadiremos las siguientes lineas:

```
[salientes]
exten => _[9]XXXXXXXX,1,Dial,Zap/1/${EXTEN}
```

Todas las numeros que comienzan con 9 se hacen usando la tarjeta.


Ahora falta configurar las extenxiones, llamada en espera, llamada en conferencia 
entre otras cosas.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC) 
usando la billetera digital de tu preferencia a la siguiente 
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
