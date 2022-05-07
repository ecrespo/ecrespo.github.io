Title: Instalación de open365.io en un servidor Debian Jessie local  
Date: 2016-09-16 09:00  
Category: Tutorial de Linux
Tags: Python,Linux,Open365, Debian,Ubuntu
lang: es  
translation: true  

Open365 es un SaaS que permite trabajar de manera colaborativa y en la nube la suite informática Libre Office versión 5.1, Open365 se encuentra en estado beta pero es estable en este momento.

En la [página oficial del proyecto](https://open365.io/) podrán encontrar más información, incluso tienen un vídeo demostrativo:

[https://www.youtube.com/watch?v=S2DH8bpCf1shttps://www.youtube.com/watch?v=S2DH8bpCf1s](https://www.youtube.com/watch?v=S2DH8bpCf1shttps://www.youtube.com/watch?v=S2DH8bpCf1s "https://www.youtube.com/watch?v=S2DH8bpCf1s")

La idea es instalarlo en un equipo con Debian Jessie.

Requerimientos:
Se requiere tener instalado lo siguiente:

1. Docker ([Instalación de docker en Debian Jessie](https://www.seraph.to/instalar-docker-en-debian-jessie.html)).
2. Python3.
3. Docker-compose (instalar vía pip3:  pip3 install docker-compose).


#### Procedimiento de instalación:
Vía `apt-get` se instala lo siguiente: 
```
apt-get install libmysqlclient-dev python3-dev python3-pip
```
Vía pip3 se instala pymongo, ldap3, requests y mysqlclient:
```
pip3 install mysqlclient  pymongo ldap3 requests
```

Se baja open365 de [github](https://github.com/Open365/Open365) vía git: 
```
git clone  https://github.com/Open365/Open365.git
```
Se ingresa al directorio Open365:
```
cd Open365
```
Se inicia la instalación: 
```
sudo ./open365 install
```
A continuación viene una serie de preguntas:
```
Additionally this will consume over 15gb of space.
Are you sure you want to continue? [y/n] y
Enter your domain or IP: midominio.prueba
We detected you are using a newer version of Docker. Unfortunately, Open365 isn't yet fully
compatible with docker versions newer than 1.9. A workaround involves running the virtualized
applications in privileged mode. Do you want to launch the applications in privileged mode?
This is potentially unsafe, specially if you are going to give accounts to third parties.
You won't be able to save documents edited in virtual applications. [y/n] y
```
Está ultima pregunta es que se tiene una versión de Docker muy nueva y open365 no ha sido probada en ella. 

Luego de responder las preguntas empieza el proceso de descarga de imagenes docker de open365. 

Para desintalar open365 se ejecuta:
```
sudo ./open365 destroy
```

Open365 tiene clientes para:
- Windows  
- Mac  
- Linux  
- Iphone  
- Android  

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)




