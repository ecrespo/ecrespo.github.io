Title: CRUD usando Flask y MongoDB con ORM Flask-MongoAlchemy (parte 4)  
Date: 2016-09-29 09:00  
Category: Tutorial Python  
Tags: Python,MongoDB,Flask,Docker,CRUD
lang: es  
translation: true  

Continuando con la serie de artículos sobre acceso a mongodb desde Flask. 

Los artículos anteriores son:  

- [Consulta a MongoDB desde Flask (parte 1)](https://www.seraph.to/consulta-a-mongodb-desde-flask-parte-1.html) 
- [Consulta a MongoDB desde Flask (parte 2 - paginación)](https://www.seraph.to/consulta-a-mongodb-desde-flask-parte-2-paginacion.html)
- [CRUD usando Flask para MongoDB  (parte 3)](https://www.seraph.to/crud-usando-flask-para-mongodb-parte-3.html) 

Para revisar los artículos relacionados a este artículo pueden ver:

- [Artículos sobre Docker](https://www.seraph.to/tag/docker.html)
- [Artículos sobre MongoDB](https://www.seraph.to/tag/mongodb.html)
- [Artículos sobre Flask](https://www.seraph.to/tag/flask.html)


La base de datos sigue manteniendo el formato de los artículos anteriores.

En este caso se va a ingresar el empleado "Ernesto" , luego se busca en la base de datos, se actualizará su información y se eliminará de la base de datos.

### Archivo Dockerfile ###
Este archivo tiene pequeños cambios, se eliminó pymongo y Flask-PyMongo, aunque mongoalchemy al final lo usa. 

A continuación el archivo Dockerfile:

```python

FROM python

WORKDIR /code/

RUN pip3 install --upgrade pip


RUN pip3 install Flask


RUN pip3 install Flask-MongoAlchemy


EXPOSE 5000


ADD ./app/* /code/


COPY ./app/* /code/


CMD python run.py 

```

El archivo `docker-compose.yml` se mantiene igual que en los artículos anteriores.


### Archivo app/run.py ###

En este caso el crud se hace con `mongoalchemy`. 

A continuación se muestra el código de `run.py` : 

```python
#!/usr/bin/env python



#Se importa Flask, reqest y jsonify

from flask import Flask, request,jsonify



#Se importa MongoAlchemy

from flask_mongoalchemy import MongoAlchemy



#Se importa dumps

from bson.json_util import dumps



#Se instancia la clase de Flask, se configura el acceso

#a la base de datos mongodb a empleados

app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE'] = 'empleados'

app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://mongo:27017/empleados'



#Se instancia mongoalchemy pasando la app.

db = MongoAlchemy(app)



#Se crea la clase empleados la cual manejara los documentos.

class empleados(db.Document):

    nombre = db.StringField()

    sexo = db.StringField()

    edad = db.IntField()

    dni = db.IntField()





#Se define la funcion add con metodo get

@app.route('/add',methods=['GET'])

def add():

    #Se crea la instancia empleado de la clase empleados donde se

    #logra hacer la inserción de un empleado con el metodo save.

    empleado = empleados(nombre=str(request.args['nombre']),

                            sexo = str(request.args['sexo']),

                            edad = int(request.args['edad']),

                            dni = int(request.args['dni']))

    empleado.save()



    #Se retorna que el usuario fue agregado.

    return jsonify({'resultado': 'Usuario agregado' })



#Se crea la funcion find con metodo get.

@app.route('/find',methods=['GET'])

def find():

    #Se realiza la busqueda y se devuelve el resultado, si existe un error de atributo (que el empleado no existe)

    #Se devuelve empleado no encontrado.

    try:

        resultado = empleados.query.filter(empleados.nombre == str(request.args['nombre'])).first()

        return dumps({'resultado':{'nombre':resultado.nombre,'sexo':resultado.sexo,'edad':resultado.edad,'dni':resultado.dni}})

    except (AttributeError):

        return dumps({'resultado': 'Empleado no encontrado'})





@app.route('/update',methods=['GET'])

def update():

    #Se intenta buscar al empleado, si existe se toma los argumentos para actualizar sus

    #datos y devolver que se actualizo, si no devuelve usuario no encontrado.

    try:

        resultado = empleados.query.filter(empleados.nombre == str(request.args['nombre'])).first()

        resultado.sexo = str(request.args['sexo'])

        resultado.edad = int(request.args['edad'])

        resultado.dni = int(request.args['dni'])

        resultado.save()

        return dumps({'resultado':'Empleado actualizado'})

    except (AttributeError):

        return dumps({'resultado': 'Empleado no encontrado'})





@app.route('/delete/<nombre>')

def remove(nombre):

    #Se busca el empleado, si existe se borra de la base de datos y se devuelve

    #mensaje de empleado borrado, si no, se devuelve el mensaje de empleado no

    #encontrado.

    try:

        resultado = empleados.query.filter(empleados.nombre == str(nombre)).first()

        resultado.remove()

        return dumps({'resultado':'empleado borrado'})

    except (AttributeError):

        return dumps({'resultado':'Empleado no encontrado'})







if __name__ == "__main__":

    #Se corre la aplicacion en modo debug

    app.run(host="0.0.0.0",debug=True)


```

### Construir la imagen Docker y ejecutar los contenedores ###

Para construir la imagen se ejecuta:
```
docker-compose build
```
Para ejecutar los contenedores docker se ejecuta:
```
docker-compose up
```
Probar el CRUD
#### Crear un empleado:
Al abrir el navegador en el siguiente URL se inserta el empleado:
```
http://localhost:5000/add?nombre=Ernesto&dni=33&edad=11&sexo=Masculino
```
El resultado se muestra en un JSON:
```
{
  "resultado": "Usuario agregado"
}
```
#### Buscar un empleado
Al abrir el navegador con el siguiente URL se busca el empleado:
```
http://localhost:5000/find?nombre=Ernesto
```
El resultado de la busqueda se muestra en un JSON:
```
{"resultado": {"nombre": "Ernesto", "sexo": "Masculino", "dni": 33, "edad": 11}}
```
#### Actualizar un empleado
Al abrir el navegador con el siguiente URL se actualiza la información de un usuario:
```
http://localhost:5000/update?nombre=Ernesto&edad=45&dni=50&sexo=Masculino
```

El resultado se muestra en un JSON:
```
{"resultado": "Empleado actualizado"}
```

#### Borrar un empleado
Ahora queda eliminar un documento de la base de datos, se abre el siguiente URL:
```
http://localhost:5000/delete/Ernesto
```
El resultado se muestra en un JSON:
```
{"resultado": "empleado borrado"}
```
Si se vuelve a consultar por el usuario el JSON que se devuelve dirá usuario no encontrado:
```
http://localhost:5000/find?nombre=Ernesto

{"resultado": "Empleado no encontrado"}
```
Esto indica que ha sido borrado de la base de datos el documento del empleado.

Ya con esto se probó todo el proceso del CRUD en documentos de una colección de la base de datos MongoDB.

El código fuente de la aplicación de este artículo se encuentra en el [repositorio tutorial-flask en la rama mongo4 en gitlab.](https://gitlab.com/ecrespo/tutorial-flask/tree/mongo4)

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)


