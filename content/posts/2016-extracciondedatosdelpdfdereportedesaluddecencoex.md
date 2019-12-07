Title: Extracción de Datos del PDF de reporte de salud de Cencoex  
Date: 2016-02-08 09:00    
Category: Tutorial Python  
Tags: Python,Mongodb,Api restfull,Eve
lang: es  
translation: true 


Este artículo es la continuación de los artículos de extracción de datos de un PDF, enfocado al reporte de Cencoex del área de [salud](http://www.cencoex.gob.ve/images/stories/pdfs/estadisticas/Salud.pdf).

La siguiente figura muestra el pdf antes mencionado:

![](./images/extracciondedatosdelpdfdereportedesaluddecencoex-1.png)

Los artículos anteriores de extracción de pdf son:  
1. [Extracción de información de PDFs con Python (parte 1).](https://www.seraph.to/extraccion-de-informacion-de-pdfs-con-python-parte-1.html)  
2. [Extracción de información de PDFs con Python (parte 2).](https://www.seraph.to/extraccion-de-informacion-de-pdfs-con-python-parte-2.html)  
3. [Extracción de Información de PDFs con Python (parte 3).](https://www.seraph.to/extraccion-de-informacion-de-pdfs-con-python-parte-3.html)  

En el caso del Pdf del reporte de Cencoex se tiene el script ya explicado anteriormente que guarda la información en una base de datos mongodb llamada `cencoex` en una colección llamada salud. 

La siguiente figura muestra los documentos de la colección:

![](./images/extracciondedatosdelpdfdereportedesaluddecencoex-2.png)

Con está información almacenada en mongodb se creará un API Restful con Eve como se explico en los [artículos anteriores](http://blog.crespo.org.ve/search/label/Eve).

La imagen anterior muestra que los documentos tienen los siguientes campos:  

- `_id`: En el identificador del objeto  
- `rif`: Es el RIF de la empresa a la cual se le asignaron los dolares, el campo es un string.  
- `monto`: Monto en Dolares de la asignación de divisas a dicha empresa, el campo es un string.  
- `empresa`: Es el nombre de la empresa a la cual se le asignaron los dolares, el campo es un string.   
- `numero`: es el número asignado que aparece en el pdf, es un entero.   

Con esta información es que se construirá el esquema para acceder por medio de Eve.

A continuación el archivo `settings.py`:
```python
#Configuracion de mongodb
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
#MONGO_USERNAME = 'user'
#MONGO_PASSWORD = 'user'
MONGO_DBNAME = 'cencoex'



RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
#Esquema
schema = {
    'numero': {
        'type': 'integer',
    },
    'rif': {
        'type': 'string',
        'maxlength': 11,
    },
    'empresa': {
        'type': 'string',
    },
    'monto': {
        'type': 'string',
    },
}



empresa = {
    'titulo': 'numero',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'numero'
    },

    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

DOMAIN = {
    'salud': empresa,
}

```
Como se ve, el dominio es salud que toma la información de la empresa donde el campo a manejar es el número. Se definió el esquema que maneja los mismos campos de la colección. 


El archivo `run.py` es el cual permite iniciar el API RestFul:
```python
#!/usr/bin/env python

from eve import Eve
app = Eve()

if __name__ == '__main__':
    app.run()

```
Para iniciar el API RestFul se ejecuta el `run.py`:
```
python run.py
```

Al acceder a http://127.0.0.1:5000/ por medio del cliente restclient se tiene lo siguiente:

![](./images/extracciondedatosdelpdfdereportedesaluddecencoex-3.png)

Para acceder a la lista de elementos del API RestFul se coloca en el cliente http://127.0.0.1:5000/salud/, la siguientes figuras muestran el resultado:

![](./images/extracciondedatosdelpdfdereportedesaluddecencoex-4.png)

![](./images/extracciondedatosdelpdfdereportedesaluddecencoex-5.png)

Como se ve en la figura se trae un JSON con los documentos de la base de datos mongodb.

Ahora se quiere acceder al primer número del reporte de la siguiente forma:
``` 
http://127.0.0.1:5000/salud/1
```
El resultado se muestra en las siguientes dos figuras:

![](./images/extracciondedatosdelpdfdereportedesaluddecencoex-6.png)

![](./images/extracciondedatosdelpdfdereportedesaluddecencoex-7.png)


Claro, esto es una demostración, pero se puede buscar realizar busquedas con otros campos. 

Se puede usar Django con el framework de API RestFul a fin  de mejorar la forma de consultar dichos documentos de la base de datos mongodb.

La idea era mostrar lo fácil que es publicar los datos de un Reporte de Cencoex, en realidad lo más complicado es extraer los datos de un PDF, incluso se pierde información dependiendo del formato de documento utilizado, como se mostró en artículo anterior el documento es una hoja de cálculo en Excel y si se perdió información en la extracción. 

Las instituciones que tienen dicha información en base de datos pueden hacer públicos los campos que se requieran de sólo lectura en un API RestFul, así se elimina el proceso de buscar información de PDFs. 


A continuación dejo la propuesta que está trabajando la comunidad de software libre en [github por parte de la comunidad de Software Libre de Venezuela](https://github.com/cslve/gobiernoabierto).


A continuación unos  vídeos de youtube:
Gobierno Abierto:

[https://youtu.be/wcao6i1yDQ4](https://youtu.be/wcao6i1yDQ4 "https://youtu.be/wcao6i1yDQ4")

<iframe width="560" height="315" src="https://www.youtube.com/embed/wcao6i1yDQ4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



Alianza para el Gobierno Abierto:

[https://youtu.be/QbGDoV_HoFY](https://youtu.be/QbGDoV_HoFY "https://youtu.be/QbGDoV_HoFY")  

<iframe width="560" height="315" src="https://www.youtube.com/embed/QbGDoV_HoFY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


[https://youtu.be/Mj7NvmFr5i0](https://youtu.be/Mj7NvmFr5i0 "https://youtu.be/Mj7NvmFr5i0")

<iframe width="560" height="315" src="https://www.youtube.com/embed/Mj7NvmFr5i0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
