Title: Agendar tareas con python
Date: 2012-07-18 9:00 
Category: Tutorial Python
Tags: Canaima,Debian,Linux,Python,Ubuntu,Tareas periodicas
lang: es
translation: true

En Linux se pueden ejecutar procesos de forma periodica gracias a `cron` o en un momento determinado gracias a `at`.

En python se tiene una librería que permite ejecutar de forma periodica o en una fecha determinada al estilo de `cron` o `at`, la librería se llama [APScheduler](https://pypi.org/project/APScheduler/) (Advanced Python Scheduler). La documentación de `SPScheduler` lo pueden revisar en este [enlace](https://apscheduler.readthedocs.io/en/latest/).

El ejemplo a mostrar a continuación permite ejecutar 2 tareas, la primera tarea se ejecuta a intervalos de 1 minuto, la segunda tarea se ejecuta de lunes a viernes en una hora específica.

El código del ejemplo se muestra a continuación:
```python
#!/usr/bin/env python

#Se importa Scheduler

from apscheduler.scheduler import Scheduler

#Se importa ctime y sleep

from time import ctime,sleep

#Se crea la instancia de la clase Scheduler

sched = Scheduler()

#Se crea una funcion con la tarea1, pero se dfine

#un decorador para la tarea para que sea periodica

#Cada minuto se ejecutara la tarea.

@sched.interval_schedule(minutes=1)

def Tarea1():

    #Muestra en pantalla la fecha y hora

    print "Se ejecuta cada minuto: %s" %ctime()

#Se crea la tarea2 al estilo cron por medio de un decorador cron

#que se ejecuta de lunes a viernes a las 9:40pm.

@sched.cron_schedule(day_of_week='mon-fri', hour=21,minute=30)

def Tarea2():

    #Se muestra en pantalla la hora del momento que se ejecuta la aplicacion.

    print "Se ejecuto a las : %s" %ctime()

#Se pasa la configuracion al scheduler

sched.configure()

#Se inicia el scheduler

sched.start()

#Se muestra las tareas definidas.

print sched.print_jobs()

#Se crea un ciclo de 10 iteraciones

#Donde se espera un minuto por cada iteracion

#Se muestra en pantalla las veces que se ejecuta.

for i in range(10):

    print "---- %s" %i

    sleep(60)

#Se detiene las tareas del scheduler al finalizar

#las iteraciones

sched.shutdown(wait=False)
```
La salida de la ejecución del programa se muestra a continuación:

```
ernesto@clara:~/bin/python/procesos$ sudo ./procesos2.py 

Jobstore default:

    Tarea1 (trigger: interval[0:01:00], next run at: 2012-07-18 21:27:59.911483)

    Tarea2 (trigger: cron[day_of_week='mon-fri', hour='21', minute='30'], next run at: 2012-07-18 21:30:00)

None

---- 0

Se ejecuta cada minuto: Wed Jul 18 21:27:59 2012

---- 1

Se ejecuta cada minuto: Wed Jul 18 21:28:59 2012

---- 2

Se ejecuta cada minuto: Wed Jul 18 21:29:59 2012

Se ejecuto a las : Wed Jul 18 21:30:00 2012

---- 3

Se ejecuta cada minuto: Wed Jul 18 21:30:59 2012

---- 4

Se ejecuta cada minuto: Wed Jul 18 21:31:59 2012

---- 5

Se ejecuta cada minuto: Wed Jul 18 21:32:59 2012

---- 6

Se ejecuta cada minuto: Wed Jul 18 21:33:59 2012

---- 7

Se ejecuta cada minuto: Wed Jul 18 21:34:59 2012

---- 8

Se ejecuta cada minuto: Wed Jul 18 21:35:59 2012

---- 9

Se ejecuta cada minuto: Wed Jul 18 21:36:59 2012
```
Con está librería se puede definir la ejecución de procesos a ciertos días y horas, o de forma periódica.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)