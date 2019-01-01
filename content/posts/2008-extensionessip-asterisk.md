Title: Crear extensiones SIP
Date: 2008-14-04 10:00
Category: Asterisk, Debian, Linux

Para crear las extensiones sip es necesario modificar el 
archivo /etc/asterisk/sip.conf. Se crearan 10 extensiones. 

Estas extensiones comienzan desde 1000 hasta 1010.

Antes de empezar a crear las extensiones se explicará la estructura 
del archivo sip.conf.

### Archivo sip.conf

El archivo sip.conf se lee de arriba hacía abajo.

1. La sección [general] contiene las opciones globales, estas opciones son :

* allow: Habilita que un determinado codec sea usado. Puede usarse la opción all.
* bindaddr: Dirección IP donde el asterisj usará para escuchar.
* disallow: Prohíbe un determinado codec. Puede usarse la opción all.
* bindport: Puerto donde asterisk espera por las conexiones.
* maxexpirey: Tiempo máximo para registros en segundos.
* defaultexpirey: Tiempo por defecto para registrarse en segundos.
* register: Registra Asterisk con otro host. El formato es una dirección SIP opcionalmente seguido por una barra / y una extensión.

* language: Define el idioma a usar.

A continuación se muestra un ejemplo:
```
[general]
bindport = 5060
bindaddr = 10.1.30.45
context = default
disallow = all
allow = ulaw
maxexpirey = 120
defaultexpirey = 80
```

2. Opciones de cada teléfono.

Las opciones para cada teléfono son:

* [name]: Es la parte del nombre del usuario de SIP.
* peer: Entidad para la cual asterisk envia llamadas.
* user: Entidad que realiza llamadas a través de asterisk.
* type: Configurar la clase de conexión; las opciones son peer(recibe llamadas del asterisk), user(hace llamadas para el asterisk) y friend(recibe y hace llamadas).

* host: Dirección IP o el nombre del host del equipo a conectarse a asterisk. Se puede usar también la opción dinamic donde se espera que el teléfono se registre.

* secret: Es una clave compartida entre el teléfono y el servidor asterisk para autenticar los peers y los users al hacer una llamada.

A continuación se muestra un ejemplo:
```
[polycom]
type=friend
secret=1234
host=10.58.254.15
context=trusted
[ekiga]
type=friend
secret=1234
host=dynamic
```

3. Plan de discado.

El plan de discado permite definir como asterisk gestionará las 
llamadas. El plan de discado se configura en el archivo 
/etc/asterisk/extensions.conf, está estructurado en 4 partes:

* Aplicaciones. Las aplicaciones son parte importante de asterisk. 
Estas tratan al canal de voz, tocando sonidos, aceptando dígitos o 
cortando una llamada.

* Contextos: Permiten organizar y mejorar la seguridad del plan de discado. Los contextos están ligados con los canales.
* Extensiones: Es un string que dispara un evento.tiene 3 tipos: literal, estándar o especial.
* Prioridad: Son pasos numerados de ejecución de cada extensión. Cada prioridad llama a una aplicación en específico. Comienzan en 1 y aumenta de 1 en 1.

A continuación se muestra un ejemplo:
```
exten=>8580,1,Dial(SIP/8580,20)
exten=>8580,2,voicemail(u8580)
exten=>8580,101,voicemail(b8580)
exten=> número (nombre), prioridad, aplicación
```

### Archivos de configuración

1. Archivo /etc/asterisk/sip.conf

```
[1000] 
type=friend
username=1000
secret=1234
host=dynamic
context=sip
mailbox=100

[1001] 
type=friend
username=1001
secret=1234
host=dynamic
context=sip
mailbox=101

[1002] 
type=friend
username=1002
secret=1234
host=dynamic
context=sip
mailbox=102

[1003] 
type=friend
username=1003
secret=1234
host=dynamic
context=sip
mailbox=103

[1004] 
type=friend
username=1004
secret=1234
host=dynamic
context=sip
mailbox=104

[1005] 
type=friend
username=1005
secret=1234
host=dynamic
context=sip
mailbox=105

[1006] 
type=friend
username=1006
secret=1234
host=dynamic
context=sip
mailbox=106

[1007] 
type=friend
username=1007
secret=1234
host=dynamic
context=sip
mailbox=107

[1008] 
type=friend
username=1008
secret=1234
host=dynamic
context=sip
mailbox=108

[1009] 
type=friend
username=1009
secret=1234
host=dynamic
context=sip
mailbox=109

[1010] 
type=friend
username=1010
secret=1234
host=dynamic
context=sip
mailbox=110
```

2. Archivo extensions.conf

```
[sip] #; aqui defino la seccion sip
exten => 1000,1,Dial(SIP/1000,20); Si el número a llamar es 1000, se llama al usuario 1000, mediante canal sip, dejar que suene por 20 segundos, si no hay respuesta se procede a la prioridad 2.
exten => 1000,2,Voicemail(u1000); La prioridad 2 llama al buzon de voz. y se da el mensaje que el usuario 1000 no está disponible. La única forma de salir de acá es colgando la llamada.
exten => 1000,102,Voicemail(b1000); Si el número de marcado en la prioridad 1 devuelve un estado "busy" entonces el dial saltará a la prioridad 101+ prioridad actual, resultando 102.
exten => 1000,103,Hangup

exten => 1001,1,Dial(SIP/1001,20)
exten => 1001,2,Voicemail(u1001)
exten => 1001,102,Voicemail(b1001)
exten => 1001,103,Hangup

exten => 1002,1,Dial(SIP/1002,20)
exten => 1002,2,Voicemail(u1002)
exten => 1002,102,Voicemail(b1002)
exten => 1002,103,Hangup

exten => 1003,1,Dial(SIP/1003,20)
exten => 1003,2,Voicemail(u1003)
exten => 1003,102,Voicemail(b1003)
exten => 1003,103,Hangup

exten => 1004,1,Dial(SIP/1004,20)
exten => 1004,2,Voicemail(u1004)
exten => 1004,102,Voicemail(b1004)
exten => 1004,103,Hangup

exten => 1005,1,Dial(SIP/1005,20)
exten => 1005,2,Voicemail(u1005)
exten => 1005,102,Voicemail(b1005)
exten => 1005,103,Hangup

exten => 1006,1,Dial(SIP/1006,20)
exten => 1006,2,Voicemail(u1006)
exten => 1006,102,Voicemail(b1006)
exten => 1006,103,Hangup

exten => 1007,1,Dial(SIP/1007,20)
exten => 1007,2,Voicemail(u1007)
exten => 1007,102,Voicemail(b1007)
exten => 1007,103,Hangup

exten => 1008,1,Dial(SIP/1008,20)
exten => 1008,2,Voicemail(u1008)
exten => 1008,102,Voicemail(b1008)
exten => 1008,103,Hangup

exten => 1009,1,Dial(SIP/1009,20)
exten => 1009,2,Voicemail(u1009)
exten => 1009,102,Voicemail(b1009)
exten => 1009,103,Hangup

exten => 1010,1,Dial(SIP/1010,20)
exten => 1010,2,Voicemail(u1010)
exten => 1010,102,Voicemail(b1010)
exten => 1010,103,Hangup
```


Imaginense tener que crear 100 extensiones!!!!!

Para solucionar esto se puede definir un conjunto de extensiones usando estándares.

Un nombre de extensión es un estándar, si este se inicia con un carácter 
subrayado "_".

Los siguientes carácteres tienen un significado especial:

* X: Corresponde a cualquier dígito de 0-9.
* Z: Corresponde a cualquier dígito de 1-9.
* N: Corresponde a cualquier dígito de 2-9.
* 1237-9]: Corresponde a cualquier dígito entre el rango.
* . : Corresponde a uno o más caracteres.

Asterisk también usa algunos nombres de extensión para propósitos especiales:

* ¡ : Invalido.
* s: Inicio.
* h: Colgó.
* t: Tiempo de espera.
* T: Tiempo de espera absoluto.
* o: Operador.
* a: Llamado cuando el usuario presiona "*" durante un mensaje inicial del buzón de voz.
* fax: Usado para la detección de fax en los canales zap.

Adicionalmente se usará variables para simplificar las extensiones.

Este ejemplo es para las extensiones 1000 hasta 1019. Se está usando la variable 
EXTEND el cual guarda el número de extensión.

```
exten => _10[0-1]X,1,Dial(SIP/${EXTEND},20)
exten => _10[0-1]X,2,Voicemail(u${EXTEN})
exten => _10[0-1]X,102,Voicemail(b${EXTEN})
exten => _10[0-1]X,103,Hangup
```

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC) 
usando la billetera digital de tu preferencia a la siguiente 
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)