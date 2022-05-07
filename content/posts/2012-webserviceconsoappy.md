Title: WebService con Soappy
Date:  2012-02-06 09:30
Category: Tutorial de Python 
Tags: Debian,General,Linux,Python,Ubuntu
lang: es
translation: true

Hace ya mucho tiempo escribí un ejemplo de como usar [xml-rpc ](https://ecrespo.github.io/ejemplo-xml-rpc-en-python.html) desde python como webservice.
En este caso se explicará el uso de otro protocolo que deriva de `xml-rpc` que se llama `SOAP` (Simple Object Access Protocol).

`SOAP` es un protocolo estándar que define cómo dos objetos en diferentes procesos pueden comunicarse por medio del intercambio de datos `XML`. Pueden conseguir más información en la página de [wikipedia](https://es.wikipedia.org/wiki/SOAP).


En python existe un módulo para trabajar con SOAP que se llama [soappy](https://pypi.org/project/SOAPpy/). Lo primero que se hará es instalarlo.  

```
#apt-get install python-soappy
```

La idea es crear 4 funciones, de suma, resta, multiplicación y división, registrarlas en el servicio `SOAP`, levantar el servidor y realizar las llamadas desde el cliente.

El programa servidor de `SOAP` es el siguiente:  
```
#!/usr/bin/env python

import SOAPpy
	
#Funciones que devuelven la suma, resta, multiplicacion y division de 2 numeros
	
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b
	
def multiplicacion(a,b):
    return a*b
	
def division(a,b):
    return a/b
	
#Se crea la instancia del servicio SOAP en el equipo por el puerto 8080.
server = SOAPpy.SOAPServer(("localhost", 8080))
	
#Registro de las funciones suma,resta, multiplicacion y division
#en el servicio SOAP.
server.registerFunction(suma)
server.registerFunction(resta)
server.registerFunction(multiplicacion)
server.registerFunction(division)
	
#Levantar el servicio SOAP.
server.serve_forever()
```
El programa cliente de `SOAP` es el siguiente:  
```
#!/usr/bin/env python

#Se importa el modulo SOAPpy
import SOAPpy
	
#Se crea la instancia del proxy SOAP
#a el servidor SOAP
server = SOAPpy.SOAPProxy("http://localhost:8080/")

#Se llama las funciones registradas en el servidor SOAP
print "El resultado de la suma es: ", server.suma(5,10)
print "El resultado de la resta es: ",server.resta(20,5)
print "El resultado de la multiplicacion es: ", server.multiplicacion(10,5)
print "El resultado de la division es: ", server.division(10,3)
```
	
Se le da permisos de ejecución a ambos archivos, se ejecuta primero el servidor y luego el cliente que devuelve el siguiente resultado:

Se ejecuta cada programa en una consola distinta.  

```ecrespo@jewel:~/bin$ ./soapservidor.py```
	
```
ecrespo@jewel:~/bin$ ./soapcliente.py
El resultado de la suma es:  15
El resultado de la resta es:  15
El resultado de la multiplicacion es:  50
El resultado de la division es:  3
```	

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
