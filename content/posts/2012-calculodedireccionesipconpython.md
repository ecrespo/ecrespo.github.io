Title: Cálculo de direcciones IP con python
Date: 2012-03-04 09:00
Category: Tutorial de Python
Tags: Canaima,Debian,General,Python,Seguridad,Ubuntu
lang: es
translation: true

Recuerdo cuando vi la materia de redes de computadoras que a uno le tocaba calcular los segmentos de redes, hacer `subnetting`, `supernetting`, `NAT`, etc y  todos los cáculos se tenían que hacer con lápiz y papel  convirtiendo las direcciones IP en 4  bytes separados por punto, incluso en las clases del postgrado no se permitía el uso de calculadoras IP.

Para python existe una librería que permite realizar los cálculos para definir una red, un segmento de red, o reconocer cuando una IP es de un segmento de red dado.

La librería se llama `ipcalc`, se puede ver la descripción y un ejemplo en el siguiente [enlace](pypi.python.org/pypi/ipcalc/).

Para instalarlo desde la paqueteria de python se puede usar `pip` o `easy_install`:  

```python 
#pip install ipcalc
```  

Ó  

```python 
#easy_install ipcalc
```

Para el caso de Debian se ejecuta `apt-get`:  

```
#apt-get install python-ipcalc
```

Desde la consola se ejecuta python:  
```
ecrespo@jewel:~$ python
Python 2.7.2+ (default, Dec  1 2011, 01:55:02)
[GCC 4.6.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```	
Se importa de `ipcalc` a IP y Network:  

```python 
>>> from ipcalc import IP, Network
```

Se presenta el segmento de IPs de la red 192.168.10.0 con bits en 1 de la mascara 30 (mascara 255.255.255.252):  

```python 
>>> for x in Network('192.168.10.0/30'): print str(x)
...
192.168.10.0
192.168.10.1
192.168.10.2
192.168.10.3
```
	
Como se nota se tiene 4 direcciones IP las cuales la primera (192.168.10.0) es la dirección de sub red y la última (192.168.10.3) es la dirección de broadcast de esa sub red.

Si se cambia los bits de la mascara a 29 aumenta el rango de IPs de dicha sub red de 4 a 8 IPs:  

```python 
>>> for x in Network('192.168.10.0/29'): print str(x)
...
192.168.10.0
192.168.10.1
192.168.10.2
192.168.10.3
192.168.10.4
192.168.10.5
192.168.10.6
192.168.10.7
```
	
También se puede consultar si una IP dada se encuentra en un segmento de red o sub red, como ejemplo se consultará si la IP 192.168.10.8 se encuentra en la sub red 192.168.10.0/29 (obvio que no):  

```python 
>>> '192.168.10.8' in Network('192.168.10.0/29')
False
```
	
Si se prueba con la IP 192.168.10.1 devuelve True la consulta:  

```python 
>>> '192.168.10.1' in Network('192.168.10.0/29')
True
```

El último ejemplo es el caso de una red 192.68.10.0/22 ó 192.168.10.0/255.255.252.0, se quiere averiguar la IP inicial y la IP final de dicho segmento de red:  

```python 
>>> '192.168.9.1' in Network('192.168.10.0/22')
False
>>> '192.168.9.255' in Network('192.168.10.0/22')
False
>>> '192.168.10.0' in Network('192.168.10.0/22')
True
>>> '192.168.10.1' in Network('192.168.10.0/22')
True
>>> '192.168.11.1' in Network('192.168.10.0/22')
True
>>> '192.168.12.1' in Network('192.168.10.0/22')
True
>>> '192.168.13.1' in Network('192.168.10.0/22')
True
>>> '192.168.14.1' in Network('192.168.10.0/22')
False
>>> '192.168.13.255' in Network('192.168.10.0/22')
True
```
	
Con este resultado se tiene que la IP inicial es la 192.168.10.0 hasta la IP 192.168.13.255.

Se puede usar también para calcular IPs de IPv6.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)