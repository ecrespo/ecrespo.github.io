Title: Crear URL recortadas con Python (bit.ly)  
Date: 2014-01-25 9:00  
Category: Tutorial Python  
Tags:  Canaima,Debian,General,Python,Ubuntu,bit.ly
lang: es  
translation: true  

Todos conocemos lo famoso que se han hecho los sitios para recortar URL debido al problema de microblogin a 144 caracteres (donde tenemos que ahorrar en la escritura).

Los recortadores reducen la cantidad de caracteres que puede llegar a tener una url que queramos compartir.

Existen varios sitios que facilitan el recortar URL:

- Bit.ly
- Goo.gl
- TinyURL  

En este caso se va a probar con `bit.ly`, el sitio tiene un API para poder acceder desde un programa, su documentación se encuentra [acá](https://dev.bitly.com/api.html).

[Es necesario registrar la aplicación](https://bitly.com/a/sign_in?rd=/a/oauth_apps) y luego buscar el [apikey](https://bitly.com/a/your_api_key).

El script que se va a hacer tiene de requerimiento los siguientes módulos de python:

- `urllib`
- `urllib2`
- `re`
- `simplejson`  

El script es sencillo, se pasa la serie de módulos a utilizar, se pasa el usuario y el apikey que se obtuvo de ' `bit.ly` y se llama a la función que recorta la url.

A continuación se muestra el código:
```python
#!/usr/bin/python


# Script que convierte un url a un url recortado por medio de bit.ly


# requiere urllib, urllib2, re, simplejson





#Se intenta importar los modulos que se necesito si no devuelve mensaje de error


#donde se menciona que se requiere los los modulos.


try:


  from re import match


  from urllib2 import urlopen, Request, HTTPError


  from urllib import urlencode


  from simplejson import loads


except ImportError, e:


  raise Exception('Required module missing: %s' % e.args[0])





#Definicion de usuario y clave bit.ly


user = "o_5j8ri77vv6aa"


apikey  = "R_172fe1dcf183470c85ce345aaa784cf9395"





#Funcion que recorta el url, se le pasa un url y devuelve el mismo recortado


def shorten(url):


    #Se maneja la excepcion de error http





    try:


        #Se le pasa los parametros url, user, apikey y formato de serializacion en


        #este caso json


        params = urlencode({'longUrl': url, 'login': user, 'apiKey': apikey, 'format': 'json'})


        #Se hace la solicitud al api de bit.ly pasandole los parametros


        req = Request("http://api.bit.ly/v3/shorten?%s" % params)


        #Se abre la respuesta.


        response = urlopen(req)


        #Se lee y se carga


        j = loads(response.read())


        #Si el codigo de estatus de la peticion http es 200


        #se retona el url recortada


        if j['status_code'] == 200:


            return j['data']['url']


        #Si no es 200 se genera una excepcion pasando el mensaje de estatus


        raise Exception('%s'%j['status_txt'])


    #Si no se logra la conexion http se devuelve un mensaje de error.


    except HTTPError, e:


        raise('HTTP error%s'%e.read())

if __name__ == '__main__':


    #Se importa argv del modulo sys


    from sys import argv


    #Si no inicia el argumento con http se devuelve un mensaje de error 


    #solicitando que se coloque el http al url.


    if not match('http://',argv[1]):


        raise Exception('Debe iniciar con "http://"')


    #Se muestra en la consola el url recortado

    print shorten(argv[1])

```

Al ejecutar el script se tiene lo siguiente:  
```
ernesto@grievous:~/bin/python$ ./acortarurl.py http://blog.crespo.org.ve

http://bit.ly/LXP0QB

```

Con el script ya se puede ir recortando url de por ejemplo el artículo anterior donde se [obtiene la lista de artículos de un blog por medio de rss](http://blog.crespo.org.ve/2014/01/jugando-con-rss-del-blog-desde-python.html).

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)