Title: CRUD usando Flask para MongoDB (parte 3).  
Date: 2016-09-28 11:00
Category: Tutorial Python
Tags: Python,MongoDB,Flask,Docker,CRUD
lang: es  
translation: true  

Continuando con la serie de artículos sobre acceso a mongodb desde Flask. 

Los artículos anteriores son:

- [Consulta a MongoDB desde Flask (parte 1)](https://www.seraph.to/consulta-a-mongodb-desde-flask-parte-1.html) 
- [Consulta a MongoDB desde Flask (parte 2 - paginación)](https://www.seraph.to/consulta-a-mongodb-desde-flask-parte-2-paginacion.html)

Para revisar los artículos relacionados a este artículo pueden ver:

- [Artículos sobre Docker](https://www.seraph.to/tag/docker.html)
- [Artículos sobre MongoDB](https://www.seraph.to/tag/mongodb.html)
- [Artículos sobre Flask](https://www.seraph.to/tag/flask.html)


En la base de datos mongodb se tiene lo siguientes datos de los empleados:
```
[{"edad": 29, "nombre": "Jane Doe", "dni": 8, "sexo": "Femenino", "_id": {"$oid": "57ebbce45fd2bbeffc51330b"}}, {"edad": 39, "nombre": "John Doe", "dni": 7, "sexo": "Masculino", "_id": {"$oid": "57ebbd195fd2bbeffc51330c"}}, {"edad": 55, "nombre": "Pedro Perez", "dni": 6, "sexo": "Masculino", "_id": {"$oid": "57ebbd505fd2bbeffc51330d"}}, {"edad": 65, "nombre": "Petra", "dni": 5, "sexo": "Femenino", "_id": {"$oid": "57ebbd6b5fd2bbeffc51330e"}}, {"edad": 18, "nombre": "Luis Gonzalez", "dni": 4, "sexo": "Masculino", "_id": {"$oid": "57ebc34d5fd2bbeffc51330f"}}, {"edad": 28, "nombre": "Carolina", "dni": 3, "sexo": "Femenino", "_id": {"$oid": "57ebc3715fd2bbeffc513310"}}, {"edad": 34, "nombre": "Luissana", "dni": 2, "sexo": "Femenino", "_id": {"$oid": "57ebc3935fd2bbeffc513311"}}, {"edad": 43, "nombre": "Neg", "dni": 1, "sexo": "Masculino", "_id": {"$oid": "57ebc4b85fd2bbeffc513312"}}]
```
Para este artículo se va a desarrollar y probar un CRUD con Flask usando como base de datos mongodb.

#### Insertar un empleado en la colección

El código para insertar un empleado se muestra a continuación:
```

#Se define la funcion add con metodo get


@app.route('/add',methods=['GET'])


def add():


    #Se toma el nombre, sexo, edad y dni como argumentos del url


    nombre = str(request.args['nombre'])


    sexo = str(request.args['sexo'])


    edad = int(request.args['edad'])


    dni = int(request.args['dni'])





    #Se usa la coleccin empleados.


    empleados = mongo.db.empleados


    #Se inserta el documento a la coleccion


    empleados.insert({'nombre':nombre,'sexo':sexo,'edad':edad,'dni':dni})


    #Se retorna que el usuario fue agregado.


    return jsonify({'resultado': 'Usuario agregado' })

```

#### Buscar un empleado en la colección

El código para buscar un empleado en la colección se muestra a continuación:
```
#Se crea la funcion find con metodo get. @app.route('/find',methods=['GET']) def find():     #Se obtiene el nombre como argumento del url.     nombre = str(request.args['nombre'])     #Se conecta a la coleccion empleados.     empleados = mongo.db.empleados     #Se busca el nombre en la coleccion.     resultado = empleados.find_one({'nombre':nombre})     #Y se devuelve el resultado.     return dumps(resultado)
```

#### Actualizar un empleado en la colección

El código para actualizar un empleado se muestra a continuación:

```
#Se define la funcion update con metodo get que actualiza un documento de la

#coleccion.

@app.route('/update',methods=['GET'])

def update():

    #Se toma el nombre,edad y dni como argumentos.

    nombre = str(request.args['nombre'])

    edad = int(request.args['edad'])

    dni = int(request.args['dni'])

    #Se conecta a la coleccion.

    empleados = mongo.db.empleados

    #Se busca el nombre en los documentos.

    empleado = empleados.find_one({'nombre':nombre})

    #Se actuliza la edad, el dni.

    empleado['edad'] = edad

    empleado['dni'] = dni

    #Se salva el empleado en la coleccion.

    empleados.save(empleado)

    #Se devuelve que el usuario ha sido actualizado.

    return dumps({'resultado': 'Usuario actualizado'})

```

#### Remover un empleado de la colección


El código para remover un empleado de la colección es el siguiente:

```
#Se define la funcion delete.


#donde en el url se pasa el nombre del empleado a borrar


@app.route('/delete/<nombre>')


def delete(nombre):


    #Se conecta a la coleccion empleados.


    empleados = mongo.db.empleados


    #Se busca el documento del empleado por el nombre.


    empleado = empleados.find_one({'nombre':nombre})


    #Se remueve el empleado de la coleccion.


    empleados.remove(empleado)


    #Se devuelve el resultado.


    return dumps({'resultado': 'Usuario removido'})

```

Noten que la forma de pasar argumentos a la función delete es diferente de las demás funciones.


Construcción de la imagen Docker y ejecución de los contenedores
Los archivos Dockerfile y docker-compose.yml se explicaron en el primer artículo de esta sección ( se encuentran en el inicio de este artículo los enlaces).

Para construir la imagen docker se ejecuta:
```
docker-compose build
```
Para ejecutar los contenedores de la aplicación y de mongodb se ejecuta:
```
docker-compose up
```

Prueba del CRUD

Para crear un empleado se abre el siguiente URL en el navegador:
``` 
http://localhost:5000/add?nombre=Ernesto&dni=33&edad=11&sexo=Masculino
```
Devuelve un json:
```
{
  "resultado": "Usuario agregado"
}
```

Para buscar el empleado que se incorporó anteriormente se abre el navegador en el URL:
```
http://localhost:5000/find?nombre=Ernesto
```
Devuelve el siguiente json:
```
{"_id": {"$oid": "57ec8714b7cd2f00565e8784"}, "sexo": "Masculino", "edad": 11, "nombre": "Ernesto", "dni": 33}
```

Para actualizar al empleado Ernesto se abre el navegador en el siguiente URL:
```
http://localhost:5000/update?nombre=Ernesto&edad=45&dni=50
```
Acá se actualiza la edad y el dni.

Esto devuelve el siguiente json:
```
{"resultado": "Usuario actualizado"}
```
Por último se va a eliminar al empleado abriendo el navegador en el siguiente URL:
```
http://localhost:5000/delete/Ernesto
```
Esto devuelve el siguiente json:
```
{"resultado": "Usuario removido"}
```

Se nota que para el delete la forma de pasar el URL es distinta a las demás que se han ejecutado.



El código fuente de este artículo se encuentra en la rama [mongo3 de gitlab.com](https://gitlab.com/ecrespo/tutorial-flask/tree/mongo3/)

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)


