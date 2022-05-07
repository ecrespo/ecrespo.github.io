Title: Conectarse al repositorio de bitbucket desde python
Date: 2012-02-19 09:00
Category: Tutorial de Python
Tags: Canaima,Control de versiones,Debian,General,Linux,Mercurial,Python,Ubuntu
lang: es
translation: true


Para tener un proyecto con control de versiones mercurial sólo veo 2 opciones usar [Google Code ](https://code.google.com/) o [Bitbucket](https://bitbucket.org/product/).  Para el caso de Google Code se puede acceder vía el api para usar mercurial con python como se explico en artículo [anterior](https://ecrespo.github.io/api-de-mercurial-para-python.html#api-de-mercurial-para-python).

Para Bitbucket se tiene un API para acceder a la información del repositorio que en python se llama [python-bitbucket.](https://bitbucket.org/jmoiron/python-bitbucket/).  

Para instalarlo se sigue los siguientes pasos:  

A lo Debian/Canaima/Ubuntu/LinuxMint:  

```
#apt-get install python-bitbucket
```

Con la herramienta `easy_install`:  

```
#easy_install bitbucket
```

Con la herramienta `pip`:  

```
#pip install bitbucket
```

Usar el API de bitbucket:  

Desde la consola de python, se importa el módulo `bitbucket`  

```python 
$python
	
>>> import bitbucket
```
	
Se crea la instancia de bitbucket.
	
```python 
>>> bb = bitbucket.BitBucket()
```
	
Se establece conexión a la cuenta de `bitbucket` :  

```python 
>>> bb = bitbucket.BitBucket('ecrespo', 'clave')
```

Se verifica que se autenticó en el servicio:  
```python 
>>> bb
<BitBucket API (auth: ecrespo)>
```

Se asocia la cuenta:  
```python 
>>> ecrespo = bb.user('ecrespo')
>>> ecrespo
<User: ecrespo>
```

Se lista los repositorios del usuario (se devuelve una lista con los repositorios del usuario, cada elemento de la lista es un diccionario con la información del repositorio):  
```python 
>>> ecrespo.repositories()
[{u'scm': u'hg', u'has_wiki': True, u'last_updated': u'2011-09-12 	03:56:37', u'created_on': u'2009-04-09 22:42:58', u'owner': u'ecrespo', 	u'logo': None, u'email_mailinglist': u'', u'is_mq': False, u'size': 747499, u'read_only': False, u'fork_of': None, u'mq_of': None, u'state': u'available', u'utc_created_on': u'2009-04-09 20:42:58+00:00', u'website': u'', u'description': u'Script que automatiza el proceso de conversi\xf3n de un sistema Debian/Ubuntu para que sea accesible para las personas con discapacidad visual', u'has_issues': True, u'is_fork': False, u'slug': u'automatizar-accesibilidad', u'is_private': False, u'name': u'automatizar-accesibilidad', u'language': u'', u'utc_last_updated': u'2011-09-12 01:56:37+00:00', u'email_writers': True, u'main_branch': u'default', u'no_public_forks': False, u'resource_uri': u'/api/1.0/repositories/ecrespo/automatizar-accesibilidad'}, {u'scm': u'hg', u'has_wiki': True, u'last_updated': u'2011-09-08 13:09:06', u'created_on': u'2011-08-04 05:02:06', u'owner': u'ecrespo', u'logo': None, u'email_mailinglist': u'', u'is_mq': False, u'size': 545, u'read_only': False, u'fork_of': None, u'mq_of': None, u'state': u'available', u'utc_created_on': u'2011-08-04 03:02:06+00:00', u'website': u'', u'description': u'Lista de paquetes para la accesibilidad con una descripci\xf3n y pruebas de los mismos', u'has_issues': False, u'is_fork': False, u'slug': u'accesibilidad', u'is_private': True, u'name': u'accesibilidad', u'language': u'', u'utc_last_updated': u'2011-09-08 11:09:06+00:00', u'email_writers': True, u'main_branch': None, u'no_public_forks': False, u'resource_uri': u'/api/1.0/repositories/ecrespo/accesibilidad'}]
```

Se captura la descripción del repositorio y la ruta del mismo:  
```python 
>>> ecrespo.repositories()[0]['description']
u'Script que automatiza el proceso de conversi\xf3n de un sistema Debian/Ubuntu para que sea accesible para las personas con discapacidad visual'

>>> ecrespo.repositories()[0]['resource_uri']
u'/api/1.0/repositories/ecrespo/automatizar-accesibilidad'
```
Se asocia a uno de los repositorios, en este caso el de accesibilidad.  
```python 
>>> pyaccesibilidad=ecrespo.repository('accesibilidad')

>>> pyaccesibilidad
<Repository: ecrespo's accesibilidad>
```
Se lista los tags o branches (para el caso del repositorio accesibilidad devuelve diccionarios vacíos):  
```python 
>>> pyaccesibilidad.tags()
{}

>>> pyaccesibilidad.branches()
{}
```

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
