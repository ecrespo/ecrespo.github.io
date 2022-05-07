Title: Darle estilo material design a Django (parte 1, el admin)  
Date: 2015-04-26 9:00  
Category: Tutorial Python  
Tags: Canaima,Debian,Python,Ubuntu,Django, Material design  
lang: es  
translation: true  

Continuando con los artículos sobre [Django](https://www.seraph.to/tag/django.html).

En este caso se tocará el tema de usar en el admin y formularios un estilo llamado [Material Design](https://en.wikipedia.org/wiki/Material_design) ([desarrollado por Google para Android](https://material.io/design/introduction/)), la idea es que nuestro backend tenga ese estilo. Para ello se tiene una aplicación de Django llamada [Django-material](http://demo.viewflow.io/).

La documentación de django-material la pueden ver en el siguiente [enlace](http://docs.viewflow.io/django_material.html).

Instalación:
Para instalar django-material se ejecuta el comando `pip`:
```
pip install django-material
```
Se crea el proyecto prueba:
```python
django-admin startproject prueba
```
Se tiene los siguientes directorios y archivos:
```
prueba
├── manage.py
└── prueba
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

En `settings.py` se agregan las aplicaciones :

- material

- material.admin


Al final se tiene lo siguiente en la sección de aplicaciones:

```python
# Application definition


INSTALLED_APPS = (


    'material',
    'material.admin',

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

)


```

Nota: `material.admin` debe estar antes que admin.

```python
Se ejecuta manage.py migrate:
ecrespo@grievous:~/django/prueba$ ./manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: staticfiles, material, messages, material_admin
  Apply all migrations: admin, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
  Installing custom SQL...
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying sessions.0001_initial... OK
````
Se crea el usuario administrador del proyecto:
```python
./manage.py createsuperuser
Username (leave blank to use 'ecrespo'): ernesto
Email address: ecrespo@
Password:
Password (again):
Superuser created successfully.
```
Se ejecuta el servidor web de django:
```
ecrespo@grievous:~/django/prueba$ ./manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
April 26, 2015 - 16:22:53
Django version 1.8, using settings 'prueba.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Se muestra la imagen del inicio de sesión del admin de Django:

![](./images/darleestilomaterialdesignadjangoadmin1-1.png)


Se muestra la imagen del admin luego de iniciar sesión:

![](./images/darleestilomaterialdesignadjangoadmin1-2.png)


La siguiente imagen muestra la sección de usuarios del admin de Django:

![](./images/darleestilomaterialdesignadjangoadmin1-3.png)

En siguiente artículo se explicará como darle el estilo material design a los formularios de una aplicación.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
