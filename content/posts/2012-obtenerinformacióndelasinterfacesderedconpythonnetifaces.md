Title: Obtener información de las interfaces de red con python(netifaces)
Date: 2012-02-07 09:00
Category: Tutorial de Python  
Tags: Canaima,Debian,General,Python,Redes,Ubuntu
lang: es
translation: true

Existe un módulo en python que permite obtener la información de las interfaces de red.

Dicho módulo se llama `netifaces`, con él se puede obtener la lista de interfaces de su equipo, obtener la información de Enlace de Red de cada interfaz, su dirección IPv4 y su Dirección IPv6.

Para instalar el módulo se ejecuta `apt-get` para el caso de Debian/Canaima/Ubuntu.  

```
#apt-get install python-netifaces
```

La idea es crear un script que capture la lista de interfaces del equipo y muestre la información de cada una de dichas interfaces.

El código del programa se muestra a continuación:  

```python 
#!/usr/bin/env python

#Se importa el modulo netifaces
import netifaces

#Se captura la lista de interfaces en el equipo
interfaces = netifaces.interfaces()
#Se muestra las interfaces
print "interfaces: ", interfaces

#Se recorre la lista de interfaces
for interface in interfaces:
#Se captura la informacion de cada interfaz
datos = netifaces.ifaddresses(interface)
print "--------------------------"
#Se muestra el nombre de la interface
print "Interface: %s" %interface
#Se captura la lista de parametros que tiene la interface
variables = datos.keys()
#Se muestra la direccion de la capa de enlace de red de la interface
print "Capa de enlace de red: ", datos[netifaces.AF_LINK][0]['addr']
#Si esta presente la informacion de IPV4 se muestra
if netifaces.AF_INET in variables:
print "IPv4: IP: %s, Mascara: %s" %(datos[netifaces.AF_INET][0]['addr'], datos[netifaces.AF_INET][0]['netmask'])
#Si esta presente la informacion de IPv6 se muestra
if netifaces.AF_INET in variables:
print "IPv6: IP: %s, Mascara: %s " %(datos[netifaces.AF_INET6][0]	['addr'], datos[netifaces.AF_INET6][0]['netmask'])
```
El resultado del programa se muestra a continuación:
```python 
interfaces: ['lo', 'eth0', 'wlan0']
--------------------------
Interface: lo
Capa de enlace de red: 00:00:00:00:00:00
IPv4: IP: 127.0.0.1, Mascara: 255.0.0.0
IPv6: IP: ::1, Mascara: ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff
--------------------------
Interface: eth0
Capa de enlace de red: 71:6a:b7:77:46:5f
--------------------------
Interface: wlan0
Capa de enlace de red: 00:26:85:74:fe:89
IPv4: IP: 192.168.10.108, Mascara: 255.255.255.0
IPv6: IP: fe80::236:92ff:fa54:fe89%wlan0, Mascara: ffff:ffff:ffff:ffff::
```
Para más información sobre el módulo pueden visitar la información en la página de [Python](https://pypi.org/project/netifaces/) o el sitio de la [aplicación](https://alastairs-place.net/projects/netifaces/). 


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)