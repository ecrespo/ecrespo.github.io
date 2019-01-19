Title: Configurando un agente snmp en linux, haciendo consultas y scripts en python para manejar información snmp
Date: 2011-03-05 09:00
Category: Tutorial Debian BSD y Python
Tags: FreeBSD, Debian, snmp, Python, Redes
lang: es
translation: true


En este artículo explicaré como configurar un agente snmp. El equipo es un BSD  Debian squeeze instalado en una máquina virtual  en mi Debian con Virtual Box.

Ejecuta el comando uname -a para ver que kernel tiene el equipo:

```
GNU/kFreeBSD bsd 8.1-1-686 #0 Tue Jan  4 17:59:05 UTC 2011 i686 i386 Intel(R) Atom(TM) CPU N270   @ 1.60GHz GNU/kFreeBSD
```

Tiene un Kernel FreeBSD 8.1 para 686.

La IP del equipo con la interfaz se toma del comando ifconfig em0:

```
em0: flags=8843 metric 0 mtu 1500
 options=9b
 ether 8:0:27:d0:71:7e
 inet6 fe80::a00:27ff:fed0:717e%em0 prefixlen 64 scopeid 0x1
 inet 192.168.0.103 netmask 0xffffff00 broadcast 192.168.0.255
 nd6 options=3
 media: Ethernet autoselect (1000baseT )
 status: active
```

La IP es la 192.168.0.103, acá se nota claramente que la información de la interfaz la maneja de forma diferente a como la maneja Linux.

Se instalará  varias aplicaciones de snmp y python con snmp:

```
aptitude install snmptrapfmt snmptt python-twisted-snmp python-pysnmp4 python-pysnmp4-doc python-pysnmp-common python-pysnmp4-mibs python-pysnmp4-apps python-pysnmp2 python-pysnmp-se python-pynetsnmp python-pyasn1 scli snimpy snmpd snmp libsnmp-python
```

Se edita el archivo /etc/snmp/snmpd.conf . Para agregar la información de contacto.


SNMP escucha localhost nada más:

```
agentAddress  udp:127.0.0.1:161
```

Acceso solamente a la información del sistema para el community public.

```
rocommunity public  default    -V systemonly
```

Información del sistema:

```
sysLocation    Servidor BSD en maquina virtual de pruebas
sysContact     Ernesto Crespo
```

Monitoreo de la partición raíz si sólo queda 10MB levanta un alarma.


```
disk       /     10000
```

Carga del sistema:

```
load   12 10 5
```

Se reinicia el servicio del agente snmp.

```
root@bsd:/home/ernesto# /etc/init.d/snmpd restart
Restarting network management services: snmpd.
```

Para verificar el funcionamiento de snmp se realiza una consulta con snmpwalk.

```
snmpwalk -v 2c -c public  localhost
iso.3.6.1.2.1.1.1.0 = STRING: "GNU/kFreeBSD bsd 8.1-1-686 #0 Tue Jan  4 17:59:05 UTC 2011 i686"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.255
iso.3.6.1.2.1.1.3.0 = Timeticks: (178) 0:00:01.78
iso.3.6.1.2.1.1.4.0 = STRING: "Ernesto Crespo "
iso.3.6.1.2.1.1.5.0 = STRING: "bsd"
iso.3.6.1.2.1.1.6.0 = STRING: "Servidor BSD en maquina virtual de pruebas"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (25) 0:00:00.25
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "The MIB module for managing TCP implementations"
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing IP and ICMP implementations"
iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing UDP implementations"
iso.3.6.1.2.1.1.9.1.3.8 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (9) 0:00:00.09
iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (9) 0:00:00.09
iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (9) 0:00:00.09
iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (18) 0:00:00.18
iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (18) 0:00:00.18
iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (20) 0:00:00.20
iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (22) 0:00:00.22
iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (24) 0:00:00.24
iso.3.6.1.2.1.25.1.1.0 = Timeticks: (653703) 1:48:57.03
iso.3.6.1.2.1.25.1.2.0 = Hex-STRING: 07 DB 03 05 0A 11 37 00 2D 04 1E
iso.3.6.1.2.1.25.1.3.0 = INTEGER: 1536
iso.3.6.1.2.1.25.1.5.0 = Gauge32: 11
```

Ahora se le da full acceso al community public para revisar toda la información que maneja el agente:

```
rocommunity public  localhost
```

Al consultar con snmpwalk ahora devuelve más información como la interfaz de red por ejemplo.

```
iso.3.6.1.2.1.1.1.0 = STRING: "GNU/kFreeBSD bsd 8.1-1-686 #0 Tue Jan  4 17:59:05 UTC 2011 i686"
iso.3.6.1.2.1.1.2.0 = OID: iso.3.6.1.4.1.8072.3.2.255
iso.3.6.1.2.1.1.3.0 = Timeticks: (632) 0:00:06.32
iso.3.6.1.2.1.1.4.0 = STRING: "Ernesto Crespo "
iso.3.6.1.2.1.1.5.0 = STRING: "bsd"
iso.3.6.1.2.1.1.6.0 = STRING: "Servidor BSD en maquina virtual de pruebas"
iso.3.6.1.2.1.1.7.0 = INTEGER: 72
iso.3.6.1.2.1.1.8.0 = Timeticks: (10) 0:00:00.10
iso.3.6.1.2.1.1.9.1.2.1 = OID: iso.3.6.1.6.3.10.3.1.1
iso.3.6.1.2.1.1.9.1.2.2 = OID: iso.3.6.1.6.3.11.3.1.1
iso.3.6.1.2.1.1.9.1.2.3 = OID: iso.3.6.1.6.3.15.2.1.1
iso.3.6.1.2.1.1.9.1.2.4 = OID: iso.3.6.1.6.3.1
iso.3.6.1.2.1.1.9.1.2.5 = OID: iso.3.6.1.2.1.49
iso.3.6.1.2.1.1.9.1.2.6 = OID: iso.3.6.1.2.1.4
iso.3.6.1.2.1.1.9.1.2.7 = OID: iso.3.6.1.2.1.50
iso.3.6.1.2.1.1.9.1.2.8 = OID: iso.3.6.1.6.3.16.2.2.1
iso.3.6.1.2.1.1.9.1.3.1 = STRING: "The SNMP Management Architecture MIB."
iso.3.6.1.2.1.1.9.1.3.2 = STRING: "The MIB for Message Processing and Dispatching."
iso.3.6.1.2.1.1.9.1.3.3 = STRING: "The management information definitions for the SNMP User-based Security Model."
iso.3.6.1.2.1.1.9.1.3.4 = STRING: "The MIB module for SNMPv2 entities"
iso.3.6.1.2.1.1.9.1.3.5 = STRING: "The MIB module for managing TCP implementations"
iso.3.6.1.2.1.1.9.1.3.6 = STRING: "The MIB module for managing IP and ICMP implementations"
iso.3.6.1.2.1.1.9.1.3.7 = STRING: "The MIB module for managing UDP implementations"
iso.3.6.1.2.1.1.9.1.3.8 = STRING: "View-based Access Control Model for SNMP."
iso.3.6.1.2.1.1.9.1.4.1 = Timeticks: (5) 0:00:00.05
iso.3.6.1.2.1.1.9.1.4.2 = Timeticks: (5) 0:00:00.05
iso.3.6.1.2.1.1.9.1.4.3 = Timeticks: (5) 0:00:00.05
iso.3.6.1.2.1.1.9.1.4.4 = Timeticks: (7) 0:00:00.07
iso.3.6.1.2.1.1.9.1.4.5 = Timeticks: (7) 0:00:00.07
iso.3.6.1.2.1.1.9.1.4.6 = Timeticks: (8) 0:00:00.08
iso.3.6.1.2.1.1.9.1.4.7 = Timeticks: (9) 0:00:00.09
iso.3.6.1.2.1.1.9.1.4.8 = Timeticks: (10) 0:00:00.10
iso.3.6.1.2.1.2.1.0 = INTEGER: 2
iso.3.6.1.2.1.2.2.1.1.1 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.1.2 = INTEGER: 2
iso.3.6.1.2.1.2.2.1.2.1 = STRING: "em0"
iso.3.6.1.2.1.2.2.1.2.2 = STRING: "lo0"
iso.3.6.1.2.1.2.2.1.3.1 = INTEGER: 6
iso.3.6.1.2.1.2.2.1.3.2 = INTEGER: 24
iso.3.6.1.2.1.2.2.1.4.1 = INTEGER: 1500
iso.3.6.1.2.1.2.2.1.4.2 = INTEGER: 16384
iso.3.6.1.2.1.2.2.1.5.1 = Gauge32: 1000000000
iso.3.6.1.2.1.2.2.1.5.2 = Gauge32: 0
iso.3.6.1.2.1.2.2.1.6.1 = Hex-STRING: 00 00 27 D0 71 7E
iso.3.6.1.2.1.2.2.1.6.2 = ""
iso.3.6.1.2.1.2.2.1.7.1 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.7.2 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.8.1 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.8.2 = INTEGER: 1
iso.3.6.1.2.1.2.2.1.9.1 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.2.2.1.9.2 = Timeticks: (0) 0:00:00.00
iso.3.6.1.2.1.2.2.1.10.1 = Counter32: 17335697
iso.3.6.1.2.1.2.2.1.10.2 = Counter32: 67940
iso.3.6.1.2.1.2.2.1.11.1 = Counter32: 18045
iso.3.6.1.2.1.2.2.1.11.2 = Counter32: 905
iso.3.6.1.2.1.2.2.1.12.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.12.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.13.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.13.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.14.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.14.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.15.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.15.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.16.1 = Counter32: 1328839
iso.3.6.1.2.1.2.2.1.16.2 = Counter32: 67940
iso.3.6.1.2.1.2.2.1.17.1 = Counter32: 12837
iso.3.6.1.2.1.2.2.1.17.2 = Counter32: 905
iso.3.6.1.2.1.2.2.1.18.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.18.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.19.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.19.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.20.1 = Counter32: 0
iso.3.6.1.2.1.2.2.1.20.2 = Counter32: 0
iso.3.6.1.2.1.2.2.1.21.1 = Gauge32: 0
iso.3.6.1.2.1.2.2.1.21.2 = Gauge32: 0
iso.3.6.1.2.1.2.2.1.22.1 = OID: ccitt.0
iso.3.6.1.2.1.2.2.1.22.2 = OID: ccitt.0
iso.3.6.1.2.1.3.1.1.1.1.1.192.168.0.1 = INTEGER: 1
iso.3.6.1.2.1.3.1.1.1.1.1.192.168.0.101 = INTEGER: 1
iso.3.6.1.2.1.3.1.1.1.1.1.192.168.0.103 = INTEGER: 1
iso.3.6.1.2.1.3.1.1.2.1.1.192.168.0.1 = Hex-STRING: F0 7D 68 52 BB 8E
iso.3.6.1.2.1.3.1.1.2.1.1.192.168.0.101 = Hex-STRING: 00 26 82 54 FE 89
iso.3.6.1.2.1.3.1.1.2.1.1.192.168.0.103 = Hex-STRING: 08 00 27 D0 71 7E
iso.3.6.1.2.1.3.1.1.3.1.1.192.168.0.1 = IpAddress: 192.168.0.1
iso.3.6.1.2.1.3.1.1.3.1.1.192.168.0.101 = IpAddress: 192.168.0.101
iso.3.6.1.2.1.3.1.1.3.1.1.192.168.0.103 = IpAddress: 192.168.0.103
iso.3.6.1.2.1.4.1.0 = INTEGER: 2
iso.3.6.1.2.1.4.2.0 = INTEGER: 64
iso.3.6.1.2.1.4.3.0 = Counter32: 18972
iso.3.6.1.2.1.4.4.0 = Counter32: 0
iso.3.6.1.2.1.4.5.0 = Counter32: 36
iso.3.6.1.2.1.4.6.0 = Counter32: 0
iso.3.6.1.2.1.4.7.0 = Counter32: 179
iso.3.6.1.2.1.4.8.0 = Counter32: 0
iso.3.6.1.2.1.4.9.0 = Counter32: 18757
iso.3.6.1.2.1.4.10.0 = Counter32: 13866
iso.3.6.1.2.1.4.11.0 = Counter32: 0
iso.3.6.1.2.1.4.13.0 = INTEGER: 60
iso.3.6.1.2.1.4.14.0 = Counter32: 0
iso.3.6.1.2.1.4.15.0 = Counter32: 0
iso.3.6.1.2.1.4.16.0 = Counter32: 0
iso.3.6.1.2.1.4.17.0 = Counter32: 0
iso.3.6.1.2.1.4.18.0 = Counter32: 0
iso.3.6.1.2.1.4.19.0 = Counter32: 0
iso.3.6.1.2.1.4.20.1.1.127.0.0.1 = IpAddress: 127.0.0.1
iso.3.6.1.2.1.4.20.1.1.192.168.0.103 = IpAddress: 192.168.0.103
iso.3.6.1.2.1.4.20.1.2.127.0.0.1 = INTEGER: 2
iso.3.6.1.2.1.4.20.1.2.192.168.0.103 = INTEGER: 1
iso.3.6.1.2.1.4.20.1.3.127.0.0.1 = IpAddress: 255.0.0.0
iso.3.6.1.2.1.4.20.1.3.192.168.0.103 = IpAddress: 255.255.255.0
iso.3.6.1.2.1.4.20.1.4.127.0.0.1 = INTEGER: 1
iso.3.6.1.2.1.4.20.1.4.192.168.0.103 = INTEGER: 1
iso.3.6.1.2.1.4.21.1.1.0.0.0.0 = IpAddress: 0.0.0.0
iso.3.6.1.2.1.4.21.1.1.127.0.0.1 = IpAddress: 127.0.0.1
iso.3.6.1.2.1.4.21.1.1.192.168.0.0 = IpAddress: 192.168.0.0
iso.3.6.1.2.1.4.21.1.1.192.168.0.103 = IpAddress: 192.168.0.103
iso.3.6.1.2.1.4.21.1.2.0.0.0.0 = INTEGER: 1
iso.3.6.1.2.1.4.21.1.2.127.0.0.1 = INTEGER: 2
iso.3.6.1.2.1.4.21.1.2.192.168.0.0 = INTEGER: 1
iso.3.6.1.2.1.4.21.1.2.192.168.0.103 = INTEGER: 2
iso.3.6.1.2.1.4.21.1.3.0.0.0.0 = INTEGER: 1
iso.3.6.1.2.1.4.21.1.3.127.0.0.1 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.3.192.168.0.0 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.3.192.168.0.103 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.4.0.0.0.0 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.4.127.0.0.1 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.4.192.168.0.0 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.4.192.168.0.103 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.5.0.0.0.0 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.5.127.0.0.1 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.5.192.168.0.0 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.5.192.168.0.103 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.6.0.0.0.0 = INTEGER: 0
iso.3.6.1.2.1.4.21.1.6.127.0.0.1 = INTEGER: 0
```

Ahora se hará una consulta snmp desde el interprete de comandos de python.

```python
#Se importa el módulo de pysnmp que genera el comando.
from pysnmp.entity.rfc3413.oneliner import cmdgen
#Se crea la instancia del generador de comandos snmp
cg = cmdgen.CommandGenerator()
#Se captura los datos del community public.
comm_data = cmdgen.CommunityData('my-manager', 'public')
#Se conecta al agente snmp desde localhost puerto 161.
transport = cmdgen.UdpTransportTarget(('127.0.0.1', 161))
#Se asocia la variable que tiene la información del sistema operativo
variables = (1, 3, 6, 1, 2, 1, 1, 1, 0)
#Se ejecuta el comando capturando el resultado y los mensajes de error.
errIndication, errStatus, errIndex, result = cg.getCmd(comm_data, transport,variables)
#Se presenta en pantalla los mensajes de error.
print errIndication,errStatus,errIndex
#Como no hay mensaje de error se presenta en pantalla el resultado del comando.
print result

```

El resultado es el siguiente:

```
None 0 0
[(ObjectName('1.3.6.1.2.1.1.1.0'), OctetString('GNU/kFreeBSD bsd 8.1-1-686 #0 Tue Jan  4 17:59:05 UTC 2011 i686'))]
```



===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
