Title: Conexiones remotas por ssh desde python
Date: 2010-03-30 12:00
Category: Tutorial de Python
Tags: Linux,ssh,python,paramiko
lang: es
translation: true


Con el módulo paramiko se puede crear conexiones ssh a equipos remotos, el siguiente ejemplo muestra como establecer dicha conexión con la ejecución de un comando de forma remota:


```python

#Se importa el modulo que permite establecer conexiones ssh
import paramiko

#Se crea la conexion con el cliente ssh
ssh = paramiko.SSHClient()

#Se define la politica de intercambio de llaves del ssh
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#Se establece la conexion remota pasando la direccion IP, el nombre 
#y clave del usuario
ssh.connect('192.168.33.46', username='ernesto',password="wxyz")
#Se ejecuta el comando de forma remota
stdin, stdout, stderr = ssh.exec_command("cd bin;ls -l")
#Se muestra el resultado del comando
listado =stdout.readlines()
for i in listado: print i
#Se cierra la sesion de ssh
ssh.close()

```

A continuación se muestra el resultado de la ejecución del script:

```

ernesto@canaima:~/bin/python$ python py-ssh.py 
total 4444
-rw-r--r-- 1 ernesto ernesto 39462 nov 9 14:50 a01.svg
-rwxr-xr-x 1 ernesto ernesto 16820 nov 9 14:49 a01.top
-rwxr-xr-x 1 ernesto ernesto 16820 nov 9 14:51 A01.TOP
-rw-r--r-- 1 ernesto ernesto 10440 nov 9 14:52 a02.svg
-rwxr-xr-x 1 ernesto ernesto 4382 nov 9 14:51 a02.top
-rwxr-xr-x 1 ernesto ernesto 32 nov 9 14:51 a03.top
-rw-r--r-- 1 ernesto ernesto 2379 oct 8 15:55 ej5.py
drwxr-xr-x 13 ernesto ernesto 4096 oct 28 16:43 firefox
lrwxrwxrwx 1 ernesto ernesto 15 feb 8 07:54 Firefox -> firefox/firefox
-rw-r--r-- 1 ernesto ernesto 33662 nov 27 17:17 hola.c
-rw-r--r-- 1 ernesto ernesto 37 nov 27 17:17 hola.py
drwxr-xr-x 2 ernesto ernesto 4096 dic 3 11:29 lenguajeC
drwxr-xr-x 2 ernesto ernesto 4096 dic 25 07:48 lv
-rw-r--r-- 1 ernesto ernesto 3640 oct 18 14:20 Matematica_Braille.py
-rw-r--r-- 1 ernesto ernesto 33792 oct 18 14:12 Matematica_libglade.glade
-rwxr-xr-x 1 ernesto ernesto 39 oct 5 22:35 prueba.py
drwxr-xr-x 19 ernesto ernesto 4096 feb 21 20:31 python
-rw-r--r-- 1 ernesto ernesto 4318141 nov 9 14:50 sys
-rwxr-xr-x 1 ernesto ernesto 4261 nov 9 14:53 top2sv
-rwxr-xr-x 1 ernesto ernesto 1051 nov 9 14:48 top2svg.py
drwxr-xr-x 3 ernesto ernesto 4096 nov 9 14:53 top2svg-v0.2


```



===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)