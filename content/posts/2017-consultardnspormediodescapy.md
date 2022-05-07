Title: Consultar DNS por medio de Scapy
Date: 2017-07-16 09:00
Category: Tutorial Python
Tags: General,Debian,Python,DNS
lang: es
translation: true
 
Hace unos años escribí un artículo sobre [descubrir equipos de una red local con python usando ipcalc y scapy](https://www.seraph.to/descubrir-equipos-en-una-red-local-con-python-ipcalc-y-scapy.html), ahora muestro el uso de scapy para consultar DNS a un servidor de DNS determinado.



El programa es muy sencillo, es una función que se le pasa el servidor y el url a consultary devuelve la IP del url. A continuación se muestra el código:

```python

#!/usr/bin/env python3


from scapy.all import *


def consulta(dns="8.8.8.8",dominio="www.google.com"):
    dnsServer = dns
    domconsulta= dominio
    #Se define la estructura del paquete de consulta de DNS, que es un paquete UDP
    #Que va por el puerto 53, se le pasa el servidor y el url.
    paquete_dns= IP(dst=dnsServer)/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname=domconsulta))
    #Se hace la consulta y se devuelve el resultado
    request_pqt = sr1(paquete_dns,verbose=0)
    return request_pqt[DNS].summary()
    
if __name__ == "__main__":
    print (consulta("8.8.8.8","www.debian.org"))
```

Al ejecutar el script se tiene el siguiente resultado:
```python
sudo python3 pydns1.py
WARNING: No route found for IPv6 destination :: (no default route?). This affects only IPv6
DNS Ans "'128.31.0.62'"
```

Como se puede notar, la IP de www.debian.org es la 128.31.0.62.




##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
