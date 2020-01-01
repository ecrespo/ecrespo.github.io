Title: API Rest Ful con Flask y MongoDB (Flask-MongoAlchemy y Flask-restful)
Date: 2016-10-12 09:00
Category: Tutorial de Python
Tags: Python,API restful,Flask,MongoDB,Flask-restful,Flask-MongoAlchemy,Docker,Docker-compose
lang: es
translation: true

En el artículo [anterior](https://www.seraph.to/crud-usando-flask-y-mongodb-con-orm-flask-mongoalchemy-parte-4.html) se explicó como hacer el API Rest Ful usando HTTP con los métodos GET, POST, PUT y DELETE, sin usar una librería para el Rest Ful. 

En este artículo se usará la librería Flask-RestFul, su documentación la pueden revisar [acá](https://flask-restful-cn.readthedocs.io/en/0.3.5/index.html). 

### Estructura de archivos y directorios del proyecto

La estructura de archivos y directorios sigue siendo la misma que en el artículo anterior:
```
tutorial-flask/
├── app
│   └── run.py
├── docker-compose.yml
├── Dockerfile
└── README.md

```

Archivo `Dockerfile` y `docker-compose.yml`

Al archivo Dockerfile se le agrega que se instale `flask-restful`, a continuación el archivo:

```python
FROM python


WORKDIR /code/

RUN pip3 install --upgrade pip


RUN pip3 install  pymongo


RUN pip3 install Flask


RUN pip3 install Flask-PyMongo


RUN pip3 install Flask-MongoAlchemy


RUN pip3 install Flask-restful


EXPOSE 5000


ADD ./app/* /code/


COPY ./app/* /code/


CMD python run.py


```

El archivo `docker-compose.yml` si es el mismo del artículo anterior:

```
flask-rest1:

  build: .

  ports:

    - "5000:5000"

  volumes:

    - "./app/:/code"

  links:

    - mongo

mongo:

  image: mongo

  ports:

    - "27017:27017"

  volumes:

    - "/srv/data/db:/data/db:rw"

```

### Código de la aplicación

Se usarán los mismos métodos HTTP del artículo anterior (GET,POST,PUT y DELETE), el url para las consultas será /empleados y la forma de pasar argumentos por el url es pasando el nombre del empleado /empleados/<string:nombre>  . 

Se crean dos clases:

- EmpleadoList: Esta clase no se le pasa argumentos por URL, tiene dos métdos GET y POST:
    - GET: Permite listar los empleados que existen en la base de datos.
    - POST: Permite insertar un empleado a la base de datos pasando un json con los datos.
- Empleado: que a los métodos se le pasa el nombre de un empleado. Se define los métodos GET, PUT y DELETE:
    - GET: Permite buscar un empleado pasando su nombre, se devuelve un json con sus datos.
    - PUT: Permite actualizar la información de un empleado, pasando su nombre y el json con los datos a modificar, devuelve un jso con todos los empleados.
    - DELETE: Permite borrar un empleado de la base de datos, se le pasa el nombre del empleado, devuelve un json con todos los empleados.



El código de `app/run.py` se muestra a continuación:

```python


#!/usr/bin/env python


#Se importa Flask, reqest y jsonify


from flask import Flask, request,jsonify, Response



#Se importa MongoAlchemy


from flask_mongoalchemy import MongoAlchemy


#Se importa dumps


from bson.json_util import dumps


#rom flask_restful import Resource, Api


from flask_restful import reqparse, abort, Api, Resource




#Se instancia la clase de Flask, se configura el acceso


#a la base de datos mongodb a empleados


app = Flask(__name__)


app.config['MONGOALCHEMY_DATABASE'] = 'empleados'


app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://mongo:27017/empleados'



#Se instancia mongoalchemy pasando la app.


db = MongoAlchemy(app)



#Se asocia el API a la aplicacion


api = Api(app)



#Se crea la clase empleados la cual manejara los documentos.


class empleados(db.Document):


    nombre = db.StringField()


    sexo = db.StringField()


    edad = db.IntField()


    dni = db.IntField()


#Se define la funcion de pagina no encontrada.


@app.errorhandler(404)


def not_found(error=None):


    mensaje = {


            'status': 404,


            'message': 'Not Found: ' + request.url,


    }


    resp = Response(jsonify(mensaje),status=404,mimetype='application/json')





    return resp





#Clase EmpleadosList que permite listar los empleados o insertar un empledo.


#Se definen los metdos get y post


class EmpleadosList(Resource):


    #Se define el metodo get el cual devuelve un json con todos los empleados.


    def get(self):


        #Se realiza la busqueda y se devuelve el resultado, si existe un error de atributo (que el empleado no existe)


        #Se devuelve empleado no encontrado.


        try:


            consulta = empleados.query.all()


            resultado = []


            for i in consulta:


                resultado.append(i.wrap())


            resp =  Response(dumps(resultado),status=200,mimetype='application/json')


            resp.headers['Link'] = 'http://blog.crespo.org.ve'


            return resp


        except (AttributeError):


            return not_found



    #Se define el metodo post para agregar un empleado por medio de un json a la


    #base de datos mongoDB.


    def post(self):


        #args = parser.parse_args()


        #Se crea la instancia empleado de la clase empleados donde se


        #logra hacer la inserción de un empleado con el metodo save.


        nombre = str(request.json['nombre'])


        sexo = str(request.json['sexo'])


        edad = int(request.json['edad'])


        dni = int(request.json['dni'])


        empleado = empleados(nombre=nombre,sexo=sexo,edad=edad,dni=dni)


        empleado.save()


        #Se retorna que el usuario fue agregado.


        ###


        consulta = empleados.query.all()


        listado = []


        for i in consulta:


            listado.append(i.wrap())


        resp =  Response(dumps(listado),status=201,mimetype='application/json')


        resp.headers['Link'] = 'http://blog.crespo.org.ve'


        return resp


#Se crea la Clase Empleado que hereda de Resource


#Tiene los metodos get, put y delete


class Empleado(Resource):


    #Se define el metodo get, permite buscar un empleado por su nombre


    def get(self,nombre):


        #Se realiza la busqueda y se devuelve el resultado, si existe un error de atributo (que el empleado no existe)


        #Se devuelve empleado no encontrado.


        try:


            resultado = empleados.query.filter(empleados.nombre == nombre).first()


            return dumps({'nombre':resultado.nombre,'sexo':resultado.sexo,'edad':resultado.edad,'dni':resultado.dni}),200,{'Content-Type':'application/json'}


        except (AttributeError):


            return not_found

    #Se define el metodo put que permite actualizar la informacion de un empleado


    #pasando su nombre, los datos a modificar se pasan en un json.


    def put(self,nombre):


        #Se intenta buscar al empleado en la base de datos, si no esta devuelve error


        try:


            #Se consulta en la base de datos, donde devuelve el primer elemento encontrado


            resultado = empleados.query.filter(empleados.nombre == nombre).first()


            #Se toma los datos de un json y se guardan en sus variables, salvando luego


            #en la base de datos.


            resultado.sexo = str(request.json['sexo'])


            resultado.edad = int(request.json['edad'])


            resultado.dni = int(request.json['dni'])


            resultado.save()


            #Se realiza la consulta desplegando los empleados


            consulta = empleados.query.all()


            listado = []


            for i in consulta:


                listado.append(i.wrap())


            #Se devuelve la nueva lista de empleados en un json.


            resp =  Response(dumps(listado),status=201,mimetype='application/json')


            resp.headers['Link'] = 'http://blog.crespo.org.ve'


            return resp


        except (AttributeError):


            return not_found


    #Se define el metodo delete que permite borrar un empleado de la base de datos


    #pasando el nombre del empleado.


    def delete(self,nombre):


        #Se busca el empleado, si existe se borra de la base de datos y se devuelve


        #mensaje de empleado borrado, si no, se devuelve el mensaje de empleado no


        #encontrado.


        try:


            resultado = empleados.query.filter(empleados.nombre == nombre).first()


            resultado.remove()


            ###


            consulta = empleados.query.all()


            listado = []


            for i in consulta:


                listado.append(i.wrap())


            resp =  Response(dumps(listado),status=200,mimetype='application/json')


            resp.headers['Link'] = 'http://blog.crespo.org.ve'


            return resp


        except (AttributeError):


            return not_found


#Se define las rutas para los recursos con las clases asociadas:


#/empleado


#/empleado/<string:nombre>


api.add_resource(EmpleadosList,'/empleado')


api.add_resource(Empleado,'/empleado/<string:nombre>')


if __name__ == "__main__":


    #Se corre la aplicacion en modo debug


    app.run(host="0.0.0.0",debug=True)

```

### Construcción de la imagen y ejecución del contenedor

Construcción de la imagen Docker:
```
docker-compose build
```

Ejecución del contenedor Docker:
```
docker-compose up
```

### Prueba del API Rest Full
Se usará postman para consultar al API.
#### Listar todos los empleados
Se abre postman en el url http://localhost:5000/empleado con método GET, a continuación se muestra una captura de pantalla:

![](./images/apirestfulconflaskymongodb-1.png)

El JSON que se devuelve es el siguiente:
```
[{"edad": 29, "sexo": "Femenino", "nombre": "Jane Doe", "dni": 8, "_id": {"$oid": "57ebbce45fd2bbeffc51330b"}}, {"edad": 39, "sexo": "Masculino", "nombre": "John Doe", "dni": 7, "_id": {"$oid": "57ebbd195fd2bbeffc51330c"}}, {"edad": 55, "sexo": "Masculino", "nombre": "Pedro Perez", "dni": 6, "_id": {"$oid": "57ebbd505fd2bbeffc51330d"}}, {"edad": 65, "sexo": "Femenino", "nombre": "Petra", "dni": 5, "_id": {"$oid": "57ebbd6b5fd2bbeffc51330e"}}, {"edad": 18, "sexo": "Masculino", "nombre": "Luis Gonzalez", "dni": 4, "_id": {"$oid": "57ebc34d5fd2bbeffc51330f"}}, {"edad": 34, "sexo": "Femenino", "nombre": "Luissana", "dni": 2, "_id": {"$oid": "57ebc3935fd2bbeffc513311"}}, {"edad": 42, "sexo": "Masculino", "nombre": "Neg", "dni": 1, "_id": {"$oid": "57ebc4b85fd2bbeffc513312"}}, {"edad": 29, "sexo": "Femenino", "nombre": "Dayana", "dni": 1050, "_id": {"$oid": "57f64d7d557e3f00086651e8"}}]
```
Agregar un empleado

Se abre postman en el URL http://localhost:5000/empleado con método POST y se pasa el siguiente JSON:
```
{
 "nombre": "Nadir",
 "sexo": "Masculino",
 "edad": 45,
 "dni": 11059
}
```

A continuación se muestra la captura de pantalla de la colocación de los datos:

![](./images/apirestfulconflaskymongodb-2.png)

Al ejecutar la acción se tiene el siguiente resueltado (como lo muestra la siguiente captura de pantalla):

![](./images/apirestfulconflaskymongodb-3.png)

El JSON que se devuelve es el siguiente:
```
[{"edad": 29, "sexo": "Femenino", "nombre": "Jane Doe", "dni": 8, "_id": {"$oid": "57ebbce45fd2bbeffc51330b"}}, {"edad": 39, "sexo": "Masculino", "nombre": "John Doe", "dni": 7, "_id": {"$oid": "57ebbd195fd2bbeffc51330c"}}, {"edad": 55, "sexo": "Masculino", "nombre": "Pedro Perez", "dni": 6, "_id": {"$oid": "57ebbd505fd2bbeffc51330d"}}, {"edad": 65, "sexo": "Femenino", "nombre": "Petra", "dni": 5, "_id": {"$oid": "57ebbd6b5fd2bbeffc51330e"}}, {"edad": 18, "sexo": "Masculino", "nombre": "Luis Gonzalez", "dni": 4, "_id": {"$oid": "57ebc34d5fd2bbeffc51330f"}}, {"edad": 34, "sexo": "Femenino", "nombre": "Luissana", "dni": 2, "_id": {"$oid": "57ebc3935fd2bbeffc513311"}}, {"edad": 42, "sexo": "Masculino", "nombre": "Neg", "dni": 1, "_id": {"$oid": "57ebc4b85fd2bbeffc513312"}}, {"edad": 29, "sexo": "Femenino", "nombre": "Dayana", "dni": 1050, "_id": {"$oid": "57f64d7d557e3f00086651e8"}}, {"edad": 45, "sexo": "Masculino", "nombre": "Nadir", "dni": 11059, "_id": {"$oid": "57fe2800d76747000b2ef40f"}}]
```

### Buscar un empleado  
Para buscar un empleado se pasa el siguiente URL http://localhost:5000/empleado/Nadir con método GET al postman, a continuación se muestra una captura de pantalla del resultado:

![](./images/apirestfulconflaskymongodb-3.png)

El JSON que devuelve es el siguiente:
```
"{\"edad\": 45, \"sexo\": \"Masculino\", \"nombre\": \"Nadir\", \"dni\": 11059}"
```

#### Actualizar empleado

Para actualizar al empleado Nadir se pasará el siguiente url a postman http://localhost:5000/empleado/Nadir con método PUT, y se pasará el siguiente json:
```
{
 "sexo": "Masculino",
 "edad": 35,
 "dni": 11059
}
```
La captura de pantalla muestra los datos que se cargaron a postman:

![](./images/apirestfulconflaskymongodb-4.png)

Al ejecutar la acción se tiene la siguiente captura de pantalla:

![](./images/apirestfulconflaskymongodb-5.png)

El JSON que devuelve es el siguiente:
```
[{"edad": 29, "sexo": "Femenino", "nombre": "Jane Doe", "dni": 8, "_id": {"$oid": "57ebbce45fd2bbeffc51330b"}}, {"edad": 39, "sexo": "Masculino", "nombre": "John Doe", "dni": 7, "_id": {"$oid": "57ebbd195fd2bbeffc51330c"}}, {"edad": 55, "sexo": "Masculino", "nombre": "Pedro Perez", "dni": 6, "_id": {"$oid": "57ebbd505fd2bbeffc51330d"}}, {"edad": 65, "sexo": "Femenino", "nombre": "Petra", "dni": 5, "_id": {"$oid": "57ebbd6b5fd2bbeffc51330e"}}, {"edad": 18, "sexo": "Masculino", "nombre": "Luis Gonzalez", "dni": 4, "_id": {"$oid": "57ebc34d5fd2bbeffc51330f"}}, {"edad": 34, "sexo": "Femenino", "nombre": "Luissana", "dni": 2, "_id": {"$oid": "57ebc3935fd2bbeffc513311"}}, {"edad": 42, "sexo": "Masculino", "nombre": "Neg", "dni": 1, "_id": {"$oid": "57ebc4b85fd2bbeffc513312"}}, {"edad": 29, "sexo": "Femenino", "nombre": "Dayana", "dni": 1050, "_id": {"$oid": "57f64d7d557e3f00086651e8"}}, {"edad": 35, "sexo": "Masculino", "nombre": "Nadir", "dni": 11059, "_id": {"$oid": "57fe2800d76747000b2ef40f"}}]
```

Como se puede notar los datos del empleado Nadir en lo que respecta a su edad ha cambiado.

#### Borrar empleado
Para terminar se borrará el empleado Nadir de la base de datos, se pasa el url http://localhost/empleado/Nadir con método DELETE, a continuación se muestra el resultado en el postman:

![](./images/apirestfulconflaskymongodb-6.png)

El JSON que devuelve es el siguiente:
```
[{"edad": 29, "sexo": "Femenino", "nombre": "Jane Doe", "dni": 8, "_id": {"$oid": "57ebbce45fd2bbeffc51330b"}}, {"edad": 39, "sexo": "Masculino", "nombre": "John Doe", "dni": 7, "_id": {"$oid": "57ebbd195fd2bbeffc51330c"}}, {"edad": 55, "sexo": "Masculino", "nombre": "Pedro Perez", "dni": 6, "_id": {"$oid": "57ebbd505fd2bbeffc51330d"}}, {"edad": 65, "sexo": "Femenino", "nombre": "Petra", "dni": 5, "_id": {"$oid": "57ebbd6b5fd2bbeffc51330e"}}, {"edad": 18, "sexo": "Masculino", "nombre": "Luis Gonzalez", "dni": 4, "_id": {"$oid": "57ebc34d5fd2bbeffc51330f"}}, {"edad": 34, "sexo": "Femenino", "nombre": "Luissana", "dni": 2, "_id": {"$oid": "57ebc3935fd2bbeffc513311"}}, {"edad": 42, "sexo": "Masculino", "nombre": "Neg", "dni": 1, "_id": {"$oid": "57ebc4b85fd2bbeffc513312"}}, {"edad": 29, "sexo": "Femenino", "nombre": "Dayana", "dni": 1050, "_id": {"$oid": "57f64d7d557e3f00086651e8"}}]
```
Como se puede ver el empleado Nadir ya no existe en la base de datos.

Para terminar se muestra la captura de pantalla del contenedor ejecutándose:

![](./images/apirestfulconflaskymongodb-7.png)

Se mantiene resaltado la salida de la ejecución de Flask ( a continuación se muestra el texto):
```
flask-rest1_1 | 172.17.0.1 - - [12/Oct/2016 12:02:56] "GET /empleado HTTP/1.1" 200 -
mongo_1       | 2016-10-12T12:09:37.175+0000 I COMMAND  [conn2] update empleados.empleados query: { _id: ObjectId('57fe2800d76747000b2ef40f') } update: { _id: ObjectId('57fe2800d76747000b2ef40f'), edad: 45, sexo: "Masculino", nombre: "Nadir", dni: 11059 } keysExamined:0 docsExamined:0 nMatched:1 nModified:1 upsert:1 keyUpdates:0 writeConflicts:0 numYields:1 locks:{ Global: { acquireCount: { r: 2, w: 2 } }, Database: { acquireCount: { w: 2 } }, Collection: { acquireCount: { w: 2 } } } 326ms
flask-rest1_1 | 172.17.0.1 - - [12/Oct/2016 12:09:37] "POST /empleado HTTP/1.1" 201 -
flask-rest1_1 | 172.17.0.1 - - [12/Oct/2016 12:12:40] "GET /empleado/Nadir HTTP/1.1" 200 -
flask-rest1_1 | 172.17.0.1 - - [12/Oct/2016 12:18:23] "POST /empleado/Nadir HTTP/1.1" 405 -
mongo_1       | 2016-10-12T12:20:00.777+0000 I COMMAND  [conn2] update empleados.empleados query: { _id: ObjectId('57fe2800d76747000b2ef40f') } update: { _id: ObjectId('57fe2800d76747000b2ef40f'), edad: 35, sexo: "Masculino", nombre: "Nadir", dni: 11059 } keysExamined:1 docsExamined:1 nMatched:1 nModified:1 keyUpdates:0 writeConflicts:0 numYields:2 locks:{ Global: { acquireCount: { r: 3, w: 3 } }, Database: { acquireCount: { w: 3 } }, Collection: { acquireCount: { w: 3 } } } 124ms
flask-rest1_1 | 172.17.0.1 - - [12/Oct/2016 12:20:00] "PUT /empleado/Nadir HTTP/1.1" 201 -
flask-rest1_1 | 172.17.0.1 - - [12/Oct/2016 12:23:19] "DELETE /empleado/Nadir HTTP/1.1" 200 -
```

Con esto se ha mejorado la forma de como crear un API Rest, en este caso usando flask-restful. 

El repositorio del proyecto se encuentra en el repositorio gitlab tutorial-flask en la rama [mongo-flask-restful](https://gitlab.com/ecrespo/tutorial-flask/tree/mongo-flask-restful).


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)



