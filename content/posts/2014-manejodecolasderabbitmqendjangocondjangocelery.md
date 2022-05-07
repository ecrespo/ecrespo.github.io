Title: Manejo de colas de RabbitMQ en Django con Django-Celery  
Date: 2014-04-29 9:00  
Category: Tutorial Python  
Tags: Canaima,Debian,Python,Ubuntu,Django,Django-Celery
lang: es    
translation: true  
 
[Hace un tiempo escribí unos 3 artículos sobre Django](https://www.seraph.to/tag/django.html), ahora se tocará un tema algo más complejo pero útil cuando se requiere rendimiento en procesos.

A continuación paso a explicar un proceso sencillo de manejo de colas de `RabbitMQ` por medio de `Django-Celery`.

La idea es realizar una instalación y configuración básica, nada de tener `RabbitMQ` en varias máquinas virtuales y que se maneje la autenticación de las diferentes colas de las diferentes máquinas.

La documentación la pueden encontrar en el siguiente [enlace](https://celery.readthedocs.io/en/latest/getting-started/first-steps-with-celery.html).

Lo primero que se necesita es tener `rabbitMQ` instalado en Debian Wheezy.
```
#aptitude install rabbitmq-server
```
Luego de la instalación se verifica que se inicie el servicio:
```
root@pruebas:~# invoke-rc.d rabbitmq-server status 
Status of node rabbit@pruebas ...
[{pid,3595},
 {running_applications,[{rabbit,"RabbitMQ","2.8.4"},
                        {mnesia,"MNESIA  CXC 138 12","4.7"},
                        {os_mon,"CPO  CXC 138 46","2.2.9"},
                        {sasl,"SASL  CXC 138 11","2.2.1"},
                        {stdlib,"ERTS  CXC 138 10","1.18.1"},
                        {kernel,"ERTS  CXC 138 10","2.15.1"}]},
 {os,{unix,linux}},
 {erlang_version,"Erlang R15B01 (erts-5.9.1) [source] [64-bit] [async-threads:30] [kernel-poll:true]\n"},
 {memory,[{total,26213352},
          {processes,10386936},
          {processes_used,10386922},
          {system,15826416},
          {atom,504409},
          {atom_used,473948},
          {binary,263704},
          {code,11874771},
          {ets,771120}]},
 {vm_memory_high_watermark,0.39999999862767177},
 {vm_memory_limit,233180364},
 {disk_free_limit,1000000000},
 {disk_free,6221991936},
 {file_descriptors,[{total_limit,924},
                    {total_used,8},
                    {sockets_limit,829},
                    {sockets_used,5}]},
 {processes,[{limit,1048576},{used,167}]},
 {run_queue,0},
 {uptime,5808}]
...done.
```

También se puede verificar desde el comando `rabbitctl`:
``` 
root@pruebas:~# rabbitmqctl status 
Status of node rabbit@pruebas ...
[{pid,3595},
 {running_applications,[{rabbit,"RabbitMQ","2.8.4"},
                        {mnesia,"MNESIA  CXC 138 12","4.7"},
                        {os_mon,"CPO  CXC 138 46","2.2.9"},
                        {sasl,"SASL  CXC 138 11","2.2.1"},
                        {stdlib,"ERTS  CXC 138 10","1.18.1"},
                        {kernel,"ERTS  CXC 138 10","2.15.1"}]},
 {os,{unix,linux}},
 {erlang_version,"Erlang R15B01 (erts-5.9.1) [source] [64-bit] [async-threads:30] [kernel-poll:true]\n"},
 {memory,[{total,26211600},
          {processes,10386952},
          {processes_used,10386938},
          {system,15824648},
          {atom,504409},
          {atom_used,473972},
          {binary,262176},
          {code,11874771},
          {ets,771120}]},
 {vm_memory_high_watermark,0.39999999862767177},
 {vm_memory_limit,233180364},
 {disk_free_limit,1000000000},
 {disk_free,6221991936},
 {file_descriptors,[{total_limit,924},
                    {total_used,8},
                    {sockets_limit,829},
                    {sockets_used,5}]},
 {processes,[{limit,1048576},{used,167}]},
 {run_queue,0},
 {uptime,5848}]
...done.
```
Como la conexión de Django es con una sóla máquina no se requiere autenticación del `rabbitMQ` así que ese paso lo pueden ver en el siguiente [enlace](https://celery.readthedocs.io/en/latest/getting-started/brokers/rabbitmq.html).

Ahora se instalará `python`, `celery` y `django-celery`:
``` 
#aptitude install python2.7 python2.7-dev python-django python-django-celery python-celery
```

Al terminar de instalar la aplicación ahora se va a crear un proyecto django:
Se crea el directorio django en `/srv/`
```
#mkdir -p /srv/django 
```
Luego se crea el proyecto pasarela con el comando `django-admin`:
```
root@pruebas:/srv/django# django-admin startproject pasarela
```
Dentro del directorio pasarela se encontrará la estructura de archivos que maneja django:
```
-rwxr-xr-x 1 pasarela pasarela   251 abr 29 15:32 manage.py
drwxr-xr-x 3 pasarela pasarela  4096 abr 29 16:49 pasarela
-rw-rw-rw- 1 pasarela pasarela 69632 abr 29 16:59 pasarela.db
```  

Luego dentro del directorio pasarela se tiene lo siguiente:
```  
root@pruebas:/srv/django/pasarela/pasarela# ls -l
total 32
-rw-r--r-- 1 pasarela pasarela    0 abr 29 15:32 __init__.py
-rw-r--r-- 1 pasarela pasarela 5464 abr 29 16:46 settings.py
-rw-r--r-- 1 pasarela pasarela  562 abr 29 15:32 urls.py
-rw-r--r-- 1 pasarela pasarela 1138 abr 29 15:32 wsgi.py
```
Se crea el directorio `apps`:
```
root@pruebas:/srv/django/pasarela/pasarela#mkdir -p apps
```
Dentro del directorio se crea el archivo `__init__.py`:
```
root@pruebas:/srv/django/pasarela/pasarela/apps# touch __init__,py
```
Ahora se crea la aplicación `sms`:
``` 
root@pruebas:/srv/django/pasarela/pasarela/apps# django-admin startapp sms
```
El directorio `sms` contiene lo siguiente:
``` 
root@pruebas:/srv/django/pasarela/pasarela/apps/sms# ls -l
total 24
-rw-r--r-- 1 pasarela pasarela   0 abr 29 15:46 __init__.py
-rw-r--r-- 1 pasarela pasarela  57 abr 29 15:46 models.py
-rw-r--r-- 1 pasarela pasarela 383 abr 29 15:46 tests.py
-rw-r--r-- 1 pasarela pasarela  26 abr 29 15:46 views.py
```
En este directorio se crea el archivo `tasks.py` con el siguiente contenido: 
```
#Se importa Celery
from celery import Celery
#Se instancia Celery importando tasks, se define el broker (quien recibe los procesos en este 
#caso rabbitMQ con el protocolo amgp) y se define el backend (quien recibe los resultado
#del proceso encolado en este caso con rabbitMQ y el protocolo amgp) 
app = Celery('tasks', broker='amqp://',backend='amqp')

#Se usa el decorador task de app y se define la suma.
@app.task
def add(x, y):
    return x + y
```
Lo que se va a hacer es manejar la suma por medio de la cola de `rabbitMQ`.

Ahora se revisa el contenido del archivo `settings.py` (lo más relevante): 

Se va a trabajar por los momentos con la base de datos `sqlite`:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pasarela.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
```
Se define el uso horario de la aplicación: 
```
TIME_ZONE = 'America/Caracas'
```
Se define el idioma:
``` 
LANGUAGE_CODE = 'es-ve'
```
Se agrega la aplicación `djcelery` y `sms`:
``` 
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'djcelery',
    'pasarela.apps.sms',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)
```
Ahora queda sincronizar la base de datos (acá se crea la base de datos para django, lo necesario para django celery y la cuenta del administrador de la aplicación):
``` 
root@pruebas:/srv/django/pasarela# python manage.py syncdb
```

Ahora lo que queda es iniciar `celery`: 
Se inicia `manage.py` de django diciéndole que va a iniciar celery en nivel de información y con dos procesos concurrentes.
```
ernesto@pruebas:/srv/django/pasarela$ python manage.py celeryd -E -l info -c 2
/usr/lib/python2.7/dist-packages/djcelery/loaders.py:108: UserWarning: Using settings.DEBUG leads to a memory leak, never use this setting in production environments!
  warnings.warn("Using settings.DEBUG leads to a memory leak, never "
[2014-04-29 17:22:37,272: WARNING/MainProcess]  

 -------------- celery@pruebas v2.5.3
---- **** -----
--- * ***  * -- [Configuration]
-- * - **** ---   . broker:      amqp://guest@localhost:5672//
- ** ----------   . loader:      djcelery.loaders.DjangoLoader
- ** ----------   . logfile:     [stderr]@INFO
- ** ----------   . concurrency: 2
- ** ----------   . events:      ON
- *** --- * ---   . beat:        OFF
-- ******* ----
--- ***** ----- [Queues]
 --------------   . celery:      exchange:celery (direct) binding:celery
                  

[Tasks]
  . pasarela.apps.sms.tasks.add

[2014-04-29 17:22:37,293: INFO/PoolWorker-1] child process calling self.run()
[2014-04-29 17:22:37,297: INFO/PoolWorker-2] child process calling self.run()
[2014-04-29 17:22:37,307: WARNING/MainProcess] celery@pruebas has started.
```

En otra consola se inicia el shell del `manage.py` de django: 
Se importa la función add que se definió en el archivo `tasks.py`.
```
ernesto@pruebas:/srv/django/pasarela$ python manage.py shell
Python 2.7.3 (default, Mar 13 2014, 11:03:55) 
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)

>>> from pasarela.apps.sms.tasks import add
#Se realiza la suma de 11+19
>>> result = add.delay(11, 19)
#Se obtiene el resultado:
>>> result.get()
30
#Se verifica si ya celery está listo para recibir más procesos:
>>> result.ready()
True
#Se verifica si ya el proceso termino.
>>> result.successful()
True
```
En la salida de celery se tiene lo siguiente:
``` 
[2014-04-29 17:25:36,200: INFO/MainProcess] Got task from broker: pasarela.apps.sms.tasks.add[64275874-545b-4ab9-bfc8-ea38904d2320]
[2014-04-29 17:25:36,228: INFO/MainProcess] Task pasarela.apps.sms.tasks.add[64275874-545b-4ab9-bfc8-ea38904d2320] succeeded in 0.0155239105225s: 30
```

Como se muestra el `celery` recibe y devuelve el resultado de la suma con su tiempo de ejecución, si se tienen varios equipos con `rabbitMQ` se puede mejorar significativamente los procesos de ejecución de funciones en django.

Pueden revisar la siguiente [presentación](https://es.scribd.com/document/57279486/Celery-An-A-Synchronous-Task-Queue-Not-Only-for-Django).


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)