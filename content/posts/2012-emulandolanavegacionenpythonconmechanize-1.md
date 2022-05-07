Title: Emulando la navegación en python con mechanize (parte 1)
Date: 2012-03-10  09:00
Category: Tutorial de Python
Tags: 
lang: es
translation: true

En estos días me ha tocado programar una aplicación que permita interactuar de manera automática con otra, para ello utilicé la librería `python-mechanize`.

Está librería permite la interacción con aplicaciones web para automatizar dicha interacción o cuando se quiere realizar pruebas de estrés a una aplicación se usa `multi-mechanize`.

La página de mechanize la pueden revisar en el siguiente [enlace](http://wwwsearch.sourceforge.net/mechanize/). Hay una guía en [Inglés](http://stockrt.github.io/p/emulating-a-browser-in-python-with-mechanize/).

En estos día he estado practicando con django (framework de desarrollo web en python) donde espero pronto poder publicar artículos al respecto.

La aplicación en Django es la de manejo de bookmarks, se tiene un inicio de sesión, una página de bienvenida al usuario registrado, luego se puede listar los bookmarks y cerrar la sesión (aplicación en desarrollo).

Pues todo esos pasos se van a automatizar con `python-mechanize`.

Para instalar mechanize se puede hacer a lo Debian:  

```
#apt-get install python-mechanize
```

La siguiente figura muestra la aplicación en django sin mucho adorno.  

![](./images/emulandolanavegacionenpythonconmechanizeparte1-1.png) 

Al darle click en sesión o Inicio de Sesión aparece la solicitud de usuario y clave como lo muestra la figura:  

![](./images/emulandolanavegacionenpythonconmechanizeparte1-2.png) 


Al darle botón derecho sobre la entrada de Usuario selecciona Inspeccionar elemento (esto en google chrome o chromium) y aparece una sección donde se muestra el código del formulario.  

![](./images/emulandolanavegacionenpythonconmechanizeparte1-3.png) 

De esa forma se puede averiguar los nombres de los elementos del formulario para luego utilizarlo en el código python con `mechanize`.

Se inicia el interprete de comandos de python:  
```
ecrespo@jewel:~$ python
Python 2.7.2+ (default, Dec  1 2011, 01:55:02)
[GCC 4.6.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```	
Se importa mechanize y el manejo de cookies:  
```python 
>>> import mechanize
>>> import cookielib
```
Se crea la instancia browser de `mechanize`:  
```python 
>>>br = mechanize.Browser()
```
Se crea la instancia del cookie:  
```python 
>>>cj = cookielib.LWPCookieJar()
```
Se asocia la instancia del cookie con el navegador:  
```python 
>>>br.set_cookiejar(cj)
```
Se define que no se maneja robots:  
```python 
>>>br.set_handle_robots(False)
```
Se define el tiempo de refrescamiento:  
```python 
>>>br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
```
Se define las cabeceras del navegador, en este caso se le está diciendo que el navegador es un firefox desde Linux Debian:  
```python 
>>>br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; es-VE; rv:1.9.0.1)Gecko/2008071615 Debian/6.0 Firefox/9')]
```
Se abre la aplicación web que se encuentra en localhost y puerto 8050:  
```python 
>>>r = br.open('http://localhost:8050/')
```
Se muestra el resultado de la página:  
```python 
>>>print r.read()
```
En la siguiente figura se muestra el resultado (el código html de la página) del comando anterior:  

![](./images/emulandolanavegacionenpythonconmechanizeparte1-4.png) 

Ahora se revisarán los links que maneja la página para darle click a sesión o Inicio de sesión para ingresar el usuario y clave:

Se crea un ciclo con los enlaces existentes en la página, luego se consulta el texto de cada enlace, si es sesión se abre el enlace pasado el url del mismo, luego finaliza el ciclo.  
```python 
>>> for link in br.links():
...     if link.text == "sesion":
...         r= br.open("%s" %link.absolute_url)
...         break
...     else:
...         continue
```
Ya en este momento se encuentra en la página de ingreso de usuario y clave:  
```python 
>>> print br.geturl()
http://localhost:8050/sesion/
```
Se puede mostrar el código html de la página de Inicio de sesión con el comando `br.response().read()`:  
```python 
>>>print br.response().read()
```
En la figura se muestra el resultado del comando:  

![](./images/emulandolanavegacionenpythonconmechanizeparte1-5.png) 

Se puede mostrar los campos del formulario con el comando `br.forms()`:  
```python 
>>> for form in br.forms():
...     print form
...
<POST http://localhost:8050/sesion/ application/x-www-form-urlencoded
  <HiddenControl(csrfmiddlewaretoken=d3c9e6c2e06f5014647a1711ee3d4908) (readonly)>
  <TextControl(username=)>
  <PasswordControl(password=)>
  <SubmitControl(<None>=login) (readonly)>
  <HiddenControl(next=/) (readonly)>>
```
Se nota que se tienen dos campos de entrada de datos username y password y el botón de login para enviar los datos.

Como se tiene un sólo formulario se usa el parámetro `nr=0`, en el caso que existan varios formularios en dicha página sigue con los números consecutivos o se le pasa el nombre del formulario si existe `name="nombre"`:  
```python 
>>>br.select_form(nr=0)
```
Ahora se le pasa los datos de usuario y clave, luego se le da click al botón de envío:  
```python 
>>> br.form['username'] = 'usuario'
>>> br.form['password'] = 'clave'
>>> br.submit()
<response_seek_wrapper at 0xb6f0a06cL whose wrapped object = <closeable_response at 0xb6f0d4ccL whose fp = <socket._fileobject object at 0xb6eff5ac>>>
```
Al ejecutar `response().read()` se mostrará la página de bienvenida del usuario que ingreso a la aplicación:  
```python 
>>>print br.response().read()
```
En la siguiente figura se muestra el resultado del comando:  

![](./images/emulandolanavegacionenpythonconmechanizeparte1-6.png) 

Se muestran los enlaces disponibles y se selecciona el de publicar:  
```python 
>>> for enlace in br.links():
...     if enlace.text == "Publicar":
...         s = br.open("%s" %enlace.absolute_url)
...         break
...     else:
...         continue
```	
Se muestra el url de la página:  
```python 
>>> print br.geturl()
http://localhost:8050/salvar/
```	
Ahora se ingresará un URL de un sitio, por ejemplo www.python.org:

Primero se despliega el formulario:  
```python 
>>> for form in br.forms():
...     print form
...
<POST http://localhost:8050/salvar/ application/x-www-form-urlencoded
  <HiddenControl(csrfmiddlewaretoken=d3c9e6c2e06f5014647a1711ee3d4908) (readonly)>
  <TextControl(url=)>
  <TextControl(title=)>
  <TextControl(tags=)>
  <SubmitControl(<None>=save) (readonly)>>
```	
Se tiene que pasar el url, luego el título del url y etiquetas:  
```python 
>>> br.select_form(nr=0)
>>> br.form['url'] = "www.python.org"
>>> br.form['title'] = "Python"
>>> br.form['tags'] = "Python Programacion"
>>> br.submit()
<response_seek_wrapper at 0xb6efee0cL whose wrapped object = <closeable_response at 0xb6f12aacL whose fp = <socket._fileobject object at 0xb6eff86c>>>
```	
Se muestra el contenido de la página luego de ingresar los datos:  
```python 
>>> print br.response().read()
```
En la siguiente figura se muestra el resultado:  

![](./images/emulandolanavegacionenpythonconmechanizeparte1-7.png) 

Para finalizar se presenta los enlaces disponibles para luego cerrar la sesión del usuario:  
```python 
>>> for link in br.links():
...     if  link.text == "Cerrar Sesion":
...         r = br.open("%s" %link.absolute_url)
...         break
...     else:
...         continue
```
Se muestra el código html de la página resultante luego de dar click en cerrar sesión y la figura donde aparece dicho código:  
```python 
>>>print br.response().read()
```	
![](./images/emulandolanavegacionenpythonconmechanizeparte1-8.png) 

En el siguiente artículo sobre `mechanize` se explicará el uso de formularios más complejos que sólo entrar datos.  


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)