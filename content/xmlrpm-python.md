Title: Ejemplo XML-RPC en python
Date: 2008-23-03 10:50
Category: XML-RPC,Python

XML-RPC permite crear un webservice que recibe unos parámetros 
y devuelve un resultado. Es como una función pero los datos 
viajan a través de la red.

El ejemplo es un webservice que recibe un valor y devuelve el doble 
de ese valor. Algo sencillo.

El servidor:

```
#Se importa el módulo XMLRPC
from SimpleXMLRPCServer import SimpleXMLRPCServer
#Se asocia a un puerto en este caso 4242
s = SimpleXMLRPCServer(("", 4242))
#La función que toma x y devuelve el doble de x.
def twice(x):
return x*2
#se registra la función
s.register_function(twice)
#se inicia el servidor
s.serve_forever()
```

El cliente:
```
#Se importa el módulo ServerProxy de xmlrpclib.
from xmlrpclib import ServerProxy
#Se conecta al equipo por el puerto 4242
s = ServerProxy('http://localhost:4242')
#Se llama a la función pasandole x y devuelve el doble de x
s.twice(2)
4
s.twice(3)
6
s.twice(15)
30
```


En el servidor se muestra los siguientes mensajes:
```
localhost - - [24/Mar/2008 00:13:38] "POST /RPC2 HTTP/1.0" 200 -
localhost - - [24/Mar/2008 00:14:23] "POST /RPC2 HTTP/1.0" 200 -
localhost - - [24/Mar/2008 00:14:36] "POST /RPC2 HTTP/1.0" 200 -
```

Son las respuestas a la conexiones del cliente.
Este programa se puede mejorar evaluando el tipo de datos que envia el 
cliente para así evitar errores al mandar un string en vez de un número.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC) 
usando la billetera digital de tu preferencia a la siguiente 
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
