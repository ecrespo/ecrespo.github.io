Title: Geolocalización de direcciones IP y dominios de Internet con GeoIP en python
Date: 2012-02-26 09:00
Category: Tutorial de Python  
Tags: Canaima,Debian,Linux,Python,Redes,Ubuntu
lang: es
translation: true

A nivel mundial se crearon varios grupos de direcciones IP de IPv4 (Clases A,B o C) la cual permiten definir redes y rango de equipos para dichas redes.

Claro actualmente se está migrando a IPv6 ya que las direcciones IPv4 se agotaron hace un par de años aproximadamente (aunque existan soluciones como NAT, Subnetting o Supernetting que permiten utilizar más eficientemente las IPs).

Con GeoIP para python se puede averiguar de cual País proviene una IP, también se puede conocer un dominio o sitio en específico donde se encuentra alojado, conocer el rango de IPs de una clase de IPv4.

Para instalar `python-geoip` a lo Debian (Debian, Canaima, Ubuntu, LinuxMint), se convierte el usuario en superusuario y ejecuta:  

```
#apt-get install python-geoip
```

Se ejecuta el interprete de comandos de python:  
```
ecrespo@jewel:~$ python
Python 2.7.2+ (default, Dec  1 2011, 01:55:02)
[GCC 4.6.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```	
Se importa el módulo `geoip`:  
```python 
>>> import GeoIP
```
Se crea el objeto de la Instancia de GeoIP, asociandole la información de GeoIP de la memoria Cache:  
```python 
>>> gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
```
Se busca en cual País se encuentra alojado yahoo.com:  
```python 
>>> print gi.country_code_by_name("yahoo.com")
US
>>> print gi.country_name_by_name("yahoo.com")
United States
```
En el primer caso se devuelve el código del País, en el segundo se devuelve el nombre del País.

Ahora se probará con yahoo.es:  
```python 
>>> print gi.country_code_by_name("www.yahoo.es")
IE
>>> print gi.country_name_by_name("www.yahoo.es")
Ireland
```
Se nota que yahoo.com está alojado en Estados Unidos y yahoo.es se encuentra alojado en Irlanda.

Ahora se buscará en cual País se encuentra alojado www.cantv.net (es obvio):  
```python 
>>> print gi.country_code_by_name("www.cantv.net")
VE
>>> print gi.country_name_by_name("www.cantv.net")
Venezuela
```
Aunque es posible que dominios de Venezuela se encuentren alojados en otros Países, un ejemplo sería www.crespo.org.ve:  
```python 
>>> print gi.country_name_by_name("www.crespo.org.ve")
Sweden
```
Para terminar se probará averiguar el País según la IP que se le pase:  
```python 
>>> print gi.country_name_by_addr("24.24.24.24")
United States
>>> print gi.country_name_by_addr("150.186.32.0")
Venezuela
```
La primera IP se encuentra en Estados Unidos y la segunda en Venezuela.

Para averiguar el rango de IPs de la IP de Venezuela se ejecuta `geoip` solicitando que devuelva el rango de IPs:  
```python 
>>> print gi.range_by_ip("150.186.32.0")
('150.185.0.0', '150.189.255.255'
```
Está Ip por el rango de direcciones que maneja es una clase B.

Con esta herramienta se puede usar para aplicaciones Web con Django por ejemplo y dicha aplicaciones puede mostrar información del País donde se conectan los usuarios.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)

