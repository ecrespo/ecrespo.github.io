Title: Ejecutar comandos de forma remota y transferencia de archivos con python
Date: 2011-02-09 09:00
Category: Tutorial Linux y Python
Tags: Linux, Debian, Paramiko, Python, ssh
lang: es
translation: true

Este artículo explicará como realizar conexiones ssh de forma automática  y realizar transferencias de archivos por medio de python.

Lo primero que se tiene que hacer es crear la clave pública y privada para ssh y así poder ejecutar comandos remotos sin necesidad de clave, una guía de como hacerlo la tiene [Rafael Bonifaz en su blog](http://rafael.bonifaz.ec/blog/2011/01/ssh-con-claves-publicas-y-privadas/).

El primer ejemplo permite establecer una conexión remota ssh y ejecutar un comando en el equipo remoto.

```python
!/usr/bin/env python
#Programa que ejecuta un comando de forma remota


#Se importa el módulo paramiko
import paramiko


#Se crea la función ssh donde se le pasa el usuario, la IP del equipo remoto, el comando a ejecutar, la clave
#del usuario en el equipo remoto (en este caso se autentica por llaves), puerto de la conexión ssh y se guarda
#un log de la conexión.


def ssh(usuario,hostname,comando,puerto=22,log="paramiko.log"):
        #Se guarda el log
        paramiko.util.log_to_file(log)
        #Se define la ruta donde se encuentra la llave RSA
        llave = "/home/ernesto/.ssh/id_rsa"
        #Se carga la llave RSA
        key = paramiko.RSAKey.from_private_key_file(llave)
        #Se crea la instancia del cliente ssh
        conexion = paramiko.SSHClient()
        #Se carga las llaves del host para validar la autenticación por llaves.
        conexion.load_system_host_keys()
        #Se establece la conexión pasando la IP, puerto del equipo, el usuario y su clave.
        conexion.connect(hostname,puerto,usuario,pkey=key)
        #Se crea una tupla con la entrada estándar, salida estándar y los mensajes de error al ejecutar el comando.
        stdin,stdout,stderr = conexion.exec_command(comando)
        #Se lee la salida estándar y se presenta la información en pantalla.
        print stdout.read()
        #Se cierra la conexión ssh.
        conexion.close()


if __name__ == "__main__":
        #Se ejecuta la función
        ssh("admin","80.13.11.25","ls -l")


```

El resultado del comando es el siguiente:

```
total 93960


drwxr-xr-x  2 admin admin     4096 feb  3 01:00 prueba
drwxr-xr-x  2 admin admin     4096 may  4  2010 public_html
-rw-r--r--  1 admin admin  3180604 ene 30 16:17 web2py-manual.pdf
```

Para la transferencia de archivos se usará las claves RSA para que no se tenga que pasar la clave del usuario por el script en python. La idea es conectarse al equipo remoto y transferir los archivos que se encuentran en un directorio.


A continuación el código del programa:

```python
#!/usr/bin/env python
#Programa que permite transferir archivos de un equipo remoto al local
#Se importa los módulos paramiko y os.
import paramiko,os


#Se crea la función recuperar archivo con los argumentos equipo, puerto, usuario y ruta del directorio donde
#se encuentran los archivos.


def recuperar_archivos(equipo,puerto,usuario,dir_path):
    #Se define la ruta donde se encuentra la llave RSA
    llave = "/home/ernesto/.ssh/id_rsa"
    #Se carga las llaves en la variable key
    key = paramiko.RSAKey.from_private_key_file(llave)
    #Se le pasa el equipo y puerto como parámetro de transporte
    c = paramiko.Transport((equipo,puerto))
    #Se crea la conexión pasando el usuario y la llave RSA.
    c.connect(username=usuario,pkey=key)
    #Se crea la conexión sftp donde se le pasa la conexión definida anteriormente.
    sftp = paramiko.SFTPClient.from_transport(c)
    #Se captura la lista de archivos de la ruta que se le pasa a la función.
    archivos = sftp.listdir(dir_path)
    #Se presenta un mensaje de recibiendo los archivos y se realiza la transferencia.
    for f in archivos:
        print "Recibiendo ",f
        sftp.get(os.path.join(dir_path,f),f)
    #Al finalizar se cierra la conexión.
    c.close()


if __name__ == "__main__":
    #Se ejecuta la función donde se le pasa la IP del equipo remoto con el puerto, luego el usuario y la ruta de
    #los archivos a transferir.
    recuperar_archivos("80.13.11.25",22,"admin","/home/admin/prueba/")

```

El resultado es el siguiente:

```
Recibiendo  control-python.pdf
Recibiendo  web2py-manual.pdf
```




===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
