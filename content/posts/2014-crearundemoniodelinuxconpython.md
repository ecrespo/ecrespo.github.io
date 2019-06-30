Title: Crear un demonio de Linux con Python  
Date: 2014-02-02 9:00  
Category: Tutorial Python  
Tags: Canaima,Debian,Fedora,General,Linux,Python,Ubuntu,Python-daemon,Python-lockfile  
lang: es  
translation: true  
 
Este artículo se basa en el [siguiente artículo en inglés](http://www.gavinj.net/2012/06/building-python-daemon-process.html).  
La idea es crear un proceso demonio de Linux con Python.  
Para ello se requerirá los 2 siguientes librerías de python:

- `Python-daemon`
- `Python-lockfile`

A lo debian se usa el comando `apt-get`:
```
#apt-get install python-daemon python-lockfile
```
A lo python se ejecuta el comando pip:
```python
#pip install python-daemon lockfile
```
A continuación se muestra el archivo `demonioprueba.py` que se colocará en el directorio `/usr/share/demonioprueba/`.

```python
#!/usr/bin/env python


# -*- coding: utf-8 -*-





#libreria estándar loggin y time


import logging


import time





#de python-daemon import runner


from daemon import runner





class App():


    def __init__(self):


        #Se define unos path estándar en linux.


        self.stdin_path = '/dev/null'


        self.stdout_path = '/dev/tty'


        self.stderr_path = '/dev/tty'


        #Se define la ruta del archivo pid del demonio.


        self.pidfile_path =  '/var/run/demonioprueba/demonioprueba.pid'


        self.pidfile_timeout = 5





    def run(self):


        i = 0


        while True:


            #El código principal va acá


            i += 1


            #Diferentes niveles de registro de bitacora


            logger.debug("Debug message %s" %i)


            logger.info("Info message %s" %i)


            logger.warn("Warning message %s" %i)


            logger.error("Error message %s" %i)


            time.sleep(1)





#Se crea la instancia de la clase


app = App()


#define la instancia de la clase logging para generar la bitacora


logger = logging.getLogger("demonioprueba log")


logger.setLevel(logging.INFO)


#Se define el forma del log


formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")


handler = logging.FileHandler("/var/log/demonioprueba/demoniopruebas.log")


handler.setFormatter(formatter)


logger.addHandler(handler)





#Se ejecuta el demonio llamando al objeto app


daemon_runner = runner.DaemonRunner(app)


#Esto evita que el archivo log no se cierre durante la ejecución del demonio


daemon_runner.daemon_context.files_preserve=[handler.stream]


#Ejecuta el método run del objeto app


daemon_runner.do_action()

```

El archivo se salva en la ruta `/usr/share/demonioprueba/demonioprueba.py`.
Se crean los directorios `/var/log/demonioprueba` y `/var/run/demonioprueba/`:
```
#mkdir -p /var/log/demonioprueba
#mkdir -p /var/run/demonioprueba
```
Se puede probar el demonio al ejecutar el siguiente comando:
```python
python/usr/share/demonioprueba/demonioprueba.py start
root@heimdal:~# started with pid 5915
```
Se muestra que el demonio se inicio con el pid 5915.
Al ejecutar `ps aux  | grep demonioprueba.py` se verá el proceso en ejecución:  
```
root@heimdal:~# ps aux | grep demonioprueba.py
root      5915  0.0  0.1  38088  6656 ?        S    17:00   0:00 python /usr/share/demonioprueba/demonioprueba.py start
```
Como se ve el proceso se inicio con el pid 5915. 

Se puede ver la bitacora al ejecutar:
```
tail -f /var/log/demonioprueba/demonioprueba.log
```
A continuación se muestra una parte del log:
```
2014-02-02 17:01:25,516 - demonioprueba log - WARNING - Warning message 80
2014-02-02 17:01:25,516 - demonioprueba log - ERROR - Error message 80
2014-02-02 17:01:26,517 - demonioprueba log - INFO - Info message 81
2014-02-02 17:01:26,517 - demonioprueba log - WARNING - Warning message 81
2014-02-02 17:01:26,518 - demonioprueba log - ERROR - Error message 81
2014-02-02 17:01:27,519 - demonioprueba log - INFO - Info message 82
2014-02-02 17:01:27,519 - demonioprueba log - WARNING - Warning message 82
2014-02-02 17:01:27,519 - demonioprueba log - ERROR - Error message 82
2014-02-02 17:01:28,520 - demonioprueba log - INFO - Info message 83
2014-02-02 17:01:28,521 - demonioprueba log - WARNING - Warning message 83
2014-02-02 17:01:28,521 - demonioprueba log - ERROR - Error message 83
2014-02-02 17:01:29,522 - demonioprueba log - INFO - Info message 84
2014-02-02 17:01:29,523 - demonioprueba log - WARNING - Warning message 84
2014-02-02 17:01:29,523 - demonioprueba log - ERROR - Error message 84
2014-02-02 17:01:30,523 - demonioprueba log - INFO - Info message 85
2014-02-02 17:01:30,524 - demonioprueba log - WARNING - Warning message 85
2014-02-02 17:01:30,524 - demonioprueba log - ERROR - Error message 85
```
Se puede detener el demonio ejecutando:
```
root@heimdal:~# python /usr/share/demonioprueba/demonioprueba.py stop
Terminating on signal 15
```

Ahora se creará el archivo init de demonio prueba ( salvar el archivo en `/etc/init.d/demonioprueba` ):

A continuación se muestra el script bash que se usa de plantilla como demonio init:
```python
#!/bin/bash

# Copyright (c) 1996-2012 My Company.

# All rights reserved.

#

# Author: Bob Bobson, 2012

#

# Please send feedback to bob@bob.com

#

# /etc/init.d/demonioprueba

#

### BEGIN INIT INFO

# Provides: demonioprueba

# Required-Start:

# Should-Start:

# Required-Stop:

# Should-Stop:

# Default-Start:  3 5

# Default-Stop:   0 1 2 6

# Short-Description: Test daemon process

# Description:    Runs up the test daemon process

### END INIT INFO



# Activate the python virtual environment

#    . /path_to_virtualenv/activate



case "$1" in

  start)

    echo "Starting server"

    # Start the daemon

    python /usr/share/demonioprueba/demonioprueba.py start

    ;;

  stop)

    echo "Stopping server"

    # Stop the daemon

    python /usr/share/demonioprueba/demonioprueba.py stop

    ;;

  restart)

    echo "Restarting server"

    python /usr/share/demonioprueba/demonioprueba.py restart

    ;;

  *)



    # Refuse to do other stuff


    echo "Usage: /etc/init.d/demonioprueba.sh {start|stop|restart}"


    exit 1


    ;;


esac





exit 0

```


Se le cambia el permiso al script:
```
chmod u+x demonioprueba.sh
```
Se habilita el script para la ejecución automática:
```
root@heimdal:/etc/init.d# insserv demonioprueba.sh
```
Acá les dejo [un ejemplo parecido](https://nanvel.name/weblog/python-unix-daemon/).


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)