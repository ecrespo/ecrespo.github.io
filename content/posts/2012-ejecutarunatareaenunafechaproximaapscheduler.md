Title: Ejecutar una tarea en una fecha próxima (APScheduler) 
Date: 2012-07-19 9:00 
Category: Tutorial Python
Tags: Canaima,Debian,General,Linux,Python,Ubuntu,Tareas
lang: es
translation: true

En el artículo [anterior](https://www.seraph.to/agendar-tareas-con-python.html#agendar-tareas-con-python) se explican 2 formas de definir tareas de forma periódica y al estilo `crond`. En este caso se explicará como ejecutar una función en una fecha próxima.

```python
#!/usr/bin/env python
#Se importa date
from datetime import date
#Se importa Scheduler
from apscheduler.scheduler import Scheduler
#Se importa sleep
from time import sleep

# Se instancia la clase scheduler
sched = Scheduler()
#Se inicia el scheduler
sched.start()

# Se define la función a ser ejecutada.
#La función toma un texto y lo presenta en pantalla.
def Tarea(texto):
    print texto

# La tarea será ejecutada el 19 de Julio de 2012.
fecha_ejecucion = date(2012, 07, 19)

# se alamacena la tarea en la variable tarea en caso que se quiera suspender
#Se le pasa la función Tarea, la fecha a ejecutar y los argumentos solicitados de la función
tarea = sched.add_date_job(Tarea, fecha_ejecucion, ['texto a escribir'])

#Se muestra las tareas definidas.
print sched.print_jobs()
#Se crea un ciclo de 10 iteraciones
#Donde se espera 60 minutos por cada iteracion
#Se muestra en pantalla las veces que se ejecuta.
for i in range(10):
    print "---- %s" %i
    sleep(3600)
#Se detiene el scheduler
sched.shutdown(wait=False)
```

Al ejecutar el programa se muestra lo siguiente:

```
ernesto@clara:~/bin/python/procesos$ sudo ./procesos3.py

Jobstore default:

    Tarea (trigger: date[2012-07-19 00:00:00], next run at: 2012-07-19 00:00:00)

None

---- 0

---- 1

text

---- 2

---- 3

---- 4

---- 5

---- 6

---- 7

---- 8

---- 9
```

Con este artículo se muestran las tres formas de ejecutar procesos con `APScheduler` (ejecución periódica, estilo crond y ejecución en una fecha próxima).

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)