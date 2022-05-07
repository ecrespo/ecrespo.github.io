Title: API de Mercurial para Python
Date: 2012-01-24 09:00
Category: Tutorial de Python 
Tags: Canaima,Control de versiones,Debian,General,Linux,Mercurial,Python,Ubuntu
lang: es
translation: true

Mercurial, como ya se ha explicado es un sistema de control de versiones distribuído desarrollado en python, otros sistemas de control de versiones tienen API o módulos para python, pero para el caso de mercurial no había visto una API para usarlo desde python.

Revisando los artículos que publican en los sparks de python  en Google+ me encuentro con que existe un API que se llama [hgapi](https://bitbucket.org/haard/hgapi).

El API soporta lo siguiente:
```
hg init
hg id
hg add <file>
hg commit [files] [-u name] [--close-branch]
hg update <rev>
hg heads
hg log
hg remove
hg status
hg merge (fails on conflict)
hg revert
```

El procedimiento para instalarlo es el siguiente:  
```python 
# pip install hgapi
Downloading/unpacking hgapi
Downloading hgapi-1.1.0.tar.gz
Running setup.py egg_info for package hgapi
	  
Installing collected packages: hgapi
Running setup.py install for hgapi
	  
Successfully installed hgapi
Cleaning up...
```
Se crea el directorio pruebas:

```
$mkdir pruebas
```

Dentro del directorio pruebas se crea el archivo `hora.txt`:  

```
cd pruebas
touch hora.txt
```

Ya está todo listo para probar el API.

###### 1.  Se importa el módulo `hgapi`:  
```python 
import hgapi
```  

###### 2. Fuera del directorio `pruebas` se crea la instancia del repositorio:
```python 
repo = hgapi.Repo("pruebas")
```  

######3. Se inicializa el repositorio:
```python 
repo.hg_init()
```  

###### 4. Se agrega el archivo hora.txt:
```python 
repo.hg_add("hora.txt")
```  

###### 5. Se realiza el commit colocando la descripción y el usuario quien realiza el commit:
```python 
repo.hg_commit("Agregando archivo hora.txt",user="ernesto")
```  

###### 6. Se captura la descripción:
```python 
str(repo['tip'].desc)
'Agregando archivo hora.txt'
```

Esto es lo básico que explica el sitio de hgapi. Lo interesante es que ya se puede automatizar procesos de mercurial desde python.

La documentación de hgapi la pueden revisar [aquí](https://pythonhosted.org/hgapi/).


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)