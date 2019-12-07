Title: API rest Full para Python con Eve (parte 1).  
Date: 2015-04-07 9:00  
Category: Tutorial Python  
Tags: Canaima,Debian,Python,Ubuntu,Eve, API restfull 
lang: es  
translation: true  

`Eve` es un framework API rest diseñado "para humanos", en enlace para ver el proyecto es el [siguiente](https://docs.python-eve.org/en/stable/).

Soporta mongodb y backends de SQL. Sus características las pueden revisar [acá](https://docs.python-eve.org/en/stable/features.html).

Este artículo se basa en el [quickstart de la aplicación](https://docs.python-eve.org/en/stable/quickstart.html).

Para instalar a Eve se usa el comando `pip` o `easy_install`:
```python
#pip install Eve
```
ó
```python
#easy_install Eve
```
Luego se creará un archivo con nombre `run.py`. Su código es el siguiente:
```python
#Se importa eve de Eve
from eve import Eve

#Se crea la instancia de Eve
app = Eve()

#Se ejecuta run.
if __name__ == '__main__':
        app.run()
```

Ahora se crea un archivo `settings.py` con el siguiente contenido:
```python
DOMAIN = {'persona': {}}
```
Los dos archivos deben estar guardados en el mismo directorio.

Ahora se ejecuta `run.py`:
```python
ernesto@grievous:~/bin/apirest$ python run.py
 * Running on http://127.0.0.1:5000/
```
Ahora se consulta el API con curl:
```
ernesto@grievous:~$ curl -i http://127.0.0.1:5000
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 64
Server: Eve/0.5.3 Werkzeug/0.9.6 Python/2.7.8
Date: Wed, 08 Apr 2015 00:09:14 GMT

{"_links": {"child": [{"href": "persona", "title": "persona"}]}}
```

Ahora se consulta a persona:
```
ernesto@grievous:~$ curl http://127.0.0.1:5000/persona
{"_items": [], "_links": {"self": {"href": "persona", "title": "persona"}, "parent": {"href": "/", "title": "home"}}, "_meta": {"max_results": 25, "total": 0, "page": 1}}
```
Lo que muestra la ejecución de `run.py` es lo siguiente:
```
ernesto@grievous:~/bin/apirest$ python run.py
 * Running on http://127.0.0.1:5000/
127.0.0.1 - - [07/Apr/2015 19:39:14] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [07/Apr/2015 19:41:35] "GET /persona HTTP/1.1" 200 -
```
Se muestran las 2 peticiones en el log.

En próximo artículo se explicará el uso de `Eve` con `mongodb`.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
