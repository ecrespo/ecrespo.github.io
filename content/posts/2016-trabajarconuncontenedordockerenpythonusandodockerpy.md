Title: Trabajar con un contenedor docker en Python usando docker-py  
Date: 2016-08-21 09:00  
Category: Tutorial de Docker
Tags: Linux,Python, docker-py
lang: es  
translation: true  


En este artículo se utilizará la librería docker-py para acceder a imágenes y contenedores Docker desde python.

La documentación de docker-py se encuentra en su sitio [oficial](https://docker-py.readthedocs.io/en/stable/).


Los artículos anteriores sobre Docker son:

1. [Instalar Docker en Debian Jessie](https://www.seraph.to/instalar-docker-en-debian-jessie.html)  

2. [Uso de Docker en Debian Jessie (parte 1)](https://www.seraph.to/uso-de-docker-en-debian-jessie-parte-1.html)  

3. [Uso de Docker en Debian Jessie (parte 2)](https://www.seraph.to/uso-de-docker-en-debian-jessie-parte-2.html)  

4. [Crear una imagen Docker a partir de un archivo Dockerfile](https://www.seraph.to/crear-una-imagen-docker-a-partir-de-un-archivo-dockerfile.html)  

5. [Iniciando Django usando Docker](https://www.seraph.to/iniciando-django-usando-docker.html)  

6. [Instalar Gitlab por medio de Docker](https://www.seraph.to/instalar-gitlab-por-medio-de-docker.html)  

7. [Ejecutando microservicios con docker usando docker-compose](https://www.seraph.to/ejecutando-micros-servicios-con-docker-usando-docker-compose.html)  

8. [Docker en Docker (DinD)](https://www.seraph.to/docker-en-docker-dind.html)

9. [Iniciando Django con docker usando docker-compose con postgresql como microservicio.](https://www.seraph.to/iniciando-django-con-docker-usando-docker-compose-con-postgresql-como-microservicio.html)

10. [Importar un contenedor Docker en Python.](https://www.seraph.to/importar-un-contenedor-docker-en-python.html#importar-un-contenedor-docker-en-python) 

11. [Compartir imagenes Docker por medio de archivos tar](https://www.seraph.to/compartir-imagenes-docker-por-medio-de-archivos-tar.html#compartir-imagenes-docker-por-medio-de-archivos-tar).

12. [Crear un registro de imagenes Docker privado.](https://www.seraph.to/crear-un-registro-de-imagenes-docker-privado.html#crear-un-registro-de-imagenes-docker-privado)

13. [Usar Anaconda desde un contenedor Docker.](https://www.seraph.to/usar-anaconda-desde-un-contenedor-docker.html#usar-anaconda-desde-un-contenedor-docker)  

14. [Crear un entorno de Integración y Despligue continue con Docker para node.js.](https://www.seraph.to/crear-un-entorno-de-integracion-y-despligue-continue-con-docker-para-nodejs.html#crear-un-entorno-de-integracion-y-despligue-continue-con-docker-para-nodejs)  

15. [Usar Jupyter Notebook desde un contenedor Docker.](https://www.seraph.to/usar-jupyter-notebook-desde-un-contenedor-de-docker.html#usar-jupyter-notebook-desde-un-contenedor-de-docker)  

16. [Ejecutar una prueba de doctest con un contenedor Docker](https://www.seraph.to/ejecutar-una-prueba-de-doctest-con-un-contenedor-docker.html#ejecutar-una-prueba-de-doctest-con-un-contenedor-docker).

17. [Ejecutar una prueba de unittest en Python con un contenedor Docker.](https://www.seraph.to/ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker.html#ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker) 

18. [Montar una Plataforma como servicio (PaaS) con Dokku (docker)](https://www.seraph.to/montar-una-plataforma-como-servicio-paas-con-dokku-docker.html#montar-una-plataforma-como-servicio-paas-con-dokku-docker).  

19. [Uso de docker-machine.  ](https://www.seraph.to/uso-de-docker-machine.html#uso-de-docker-machine)

20. [Proveer un cluster con docker swarm y docker-machine.](https://www.seraph.to/proveer-un-cluster-con-docker-swarm-y-docker-machine.html#proveer-un-cluster-con-docker-swarm-y-docker-machine)

21. [Instalar Jenkins por medio de Docker y crear una imagen Docker de Jenkins](https://www.seraph.to/instalar-jenkins-por-medio-de-docker-y-crear-una-imagen-docker-de-jenkins.html#instalar-jenkins-por-medio-de-docker-y-crear-una-imagen-docker-de-jenkins) 

22. [Automatizar la construcción de imágenes Docker con github.](https://www.seraph.to/automatizar-la-construccion-de-imagenes-docker-con-github.html#automatizar-la-construccion-de-imagenes-docker-con-github) 

23. [Crear una imagen Docker para MongoDB3.](https://www.seraph.to/crear-una-imagen-docker-para-mongodb-3.html#crear-una-imagen-docker-para-mongodb-3)

24. [Crear un contenedor Docker como entorno de desarrollo para Sails.js.](https://www.seraph.to/crear-un-contenedor-docker-como-entorno-de-desarrollo-para-sailsjs.html#crear-un-contenedor-docker-como-entorno-de-desarrollo-para-sailsjs)

25. [Correr aplicaciones de escritorio desde un contenedor Docker.](https://www.seraph.to/correr-aplicaciones-de-escritorio-desde-un-contenedor-docker.html#correr-aplicaciones-de-escritorio-desde-un-contenedor-docker)

26. [Usar dockerui para la gestión de imágenes y contenedores de Docker](https://www.seraph.to/usar-dockerui-para-la-gestion-de-imagenes-y-contenedores-de-docker.html#usar-dockerui-para-la-gestion-de-imagenes-y-contenedores-de-docker) 

27. [Crear una imagen Docker de RethinkDB](https://www.seraph.to/crear-una-imagen-docker-de-rethinkdb.html#crear-una-imagen-docker-de-rethinkdb)

28. [Analizar código python con pylint desde Docker](https://www.seraph.to/analizar-codigo-python-con-pylint-desde-docker.html#analizar-codigo-python-con-pylint-desde-docker)

29. [Instalar gitlab-runner de gitlab-ci por medio de Docker](https://www.seraph.to/ejecutar-una-prueba-de-integracion-continua-con-gitlab-ci-y-gitlab-runner.html#ejecutar-una-prueba-de-integracion-continua-con-gitlab-ci-y-gitlab-runner)

30. [Crear datos JSON a partir de un diccionario en Flask (parte 1) (actualización- Docker)](https://www.seraph.to/crear-datos-json-a-partir-de-un-diccionario-en-flask-parte-1-actualizacion-docker.html#crear-datos-json-a-partir-de-un-diccionario-en-flask-parte-1-actualizacion-docker)

31. [Correr sonarqube desde un contenedor Docker](https://www.seraph.to/correr-sonarqube-desde-un-contenedor-docker.html#correr-sonarqube-desde-un-contenedor-docker)

32. [Crear una imagen docker de Redis.](https://www.seraph.to/crear-una-imagen-docker-de-redis.html#crear-una-imagen-docker-de-redis)

33. [Introducción de Redis con Python](https://www.seraph.to/introduccion-de-redis-con-python.html#introduccion-de-redis-con-python)

El primer script contiene lo siguiente:

```python

#!/usr/bin/python


#Se importa el cliente docker.

from docker import Client


#Se asocia la instancia cliente de docker con el socket.

cli = Client(base_url='unix://var/run/docker.sock')



print ("Se muestra la imagen docker de debian")

print (cli.images(name="debian"))



#Se crea un contenedor basandose en la imagen de debian y ejecuta sleep por 30 seg

container = cli.create_container(image="debian",command='/bin/sleep 30')



print  ("se imprime la informacion del contenedor")

print(container)

print ("Se muestra la información de los contenedores que están corriendo.")

print (cli.containers())

```

Al ejecutar el script se tiene:
```
python app.py
```
Se muestra la imagen docker de debian
```
[{u'Created': 1449257280, u'Labels': None, u'VirtualSize': 125090240, u'ParentId': u'sha256:2e4b1470911604ccb99e3d2a9db8487661bb1d6db5b7aa9e4cf54a4b8bc7e33e', u'RepoTags': [u'debian:latest'], u'RepoDigests': None, u'Id': u'sha256:87b7eb6de0a6def7be27d485caf243354f8b5e19f41b0222b19f6f02b102dc61', u'Size': 125090240}]
se imprime la informacion del contenedor
{u'Id': u'766563f15d12562ff8fc6ff1a89ed76b1ebd914bfa9b8f753a4acf925778e720', u'Warnings': None}
Se muestra la informacion de los contenedores que estan corriendo.
[{u'Status': u'Up 43 minutes', u'Created': 1459285417, u'Image': u'jupyter/notebook', u'Labels': {}, u'NetworkSettings': {u'Networks': {u'bridge': {u'NetworkID': u'', u'MacAddress': u'02:42:ac:11:00:02', u'GlobalIPv6PrefixLen': 0, u'Links': None, u'GlobalIPv6Address': u'', u'IPv6Gateway': u'', u'IPAMConfig': None, u'EndpointID': u'ec791d0a8b52fee4fc46447b43304ce626629790e3a525cd4ae03e6a25bda3d5', u'IPPrefixLen': 16, u'IPAddress': u'172.17.0.2', u'Gateway': u'172.17.0.1', u'Aliases': None}}}, u'HostConfig': {u'NetworkMode': u'default'}, u'ImageID': u'sha256:1c02aa25b7b817d8b7a7557b4b62250db6c735da3e7fabb4b3a157e55256e2d4', u'State': u'running', u'Command': u'tini -- jupyter notebook', u'Names': [u'/berserk_darwin'], u'Mounts': [{u'RW': True, u'Source': u'/home/ernesto/dockers/notebook/notebook', u'Destination': u'/notebooks', u'Mode': u'', u'Propagation': u'rprivate'}], u'Id': u'dfcc1bd19dab02580cce30d1719d8514eb0af2ab1dec8b01e42b95376ce5e608', u'Ports': [{u'IP': u'0.0.0.0', u'Type': u'tcp', u'PublicPort': 8888, u'PrivatePort': 8888}]}]

```

El script `app2.py` tiene lo siguiente:

```
#!/usr/bin/python

#Se importa el cliente docker.

from docker import Client

#Se import io para el manejo del texto en la salida.

from io import BytesIO

#Se crea el archivo dockerfile

dockerfile = '''

 # Shared Volume

 FROM busybox

 MAINTAINER Ernesto Crespo, ecrespo@gmail.com

 VOLUME /data

 CMD ["/bin/sh"]

 '''

 #Se define el encode como utf-8

f = BytesIO(dockerfile.encode('utf-8'))

#Se crea la instancia del cliente docker al socket.

cli = Client(base_url='unix://var/run/docker.sock')



#Se construye la imagen y devuelve la salida de la misma.

response = [line for line in cli.build(

 fileobj=f, rm=True, tag='ecrespo/data'

 )]



print ("Se muestra la respuesta")

for i in response:

 print (i)



print ("Se muestra los contenedores que estan corriendo, en este caso uno de jupyter")

print (cli.containers())

```

EL resultado de ejecutar el script `app2.py` es el siguiente:

Se muestra la respuesta
```
{"stream":"Step 1 : FROM busybox\n"}

{"stream":" ---\u003e 8c9d515b3079\n"}

{"stream":"Step 2 : MAINTAINER Ernesto Crespo, ecrespo@gmail.com\n"}

{"stream":" ---\u003e Using cache\n"}

{"stream":" ---\u003e 5efdc0a317b7\n"}

{"stream":"Step 3 : VOLUME /data\n"}

{"stream":" ---\u003e Using cache\n"}

{"stream":" ---\u003e b0132c6c3a87\n"}

{"stream":"Step 4 : CMD /bin/sh\n"}

{"stream":" ---\u003e Using cache\n"}

{"stream":" ---\u003e a7c85281e78c\n"}

{"stream":"Successfully built a7c85281e78c\n"}
```
Se muestran los contenedores que estan corriendo, en este caso uno de jupyter
```
[{u'Status': u'Up 56 minutes', u'Created': 1459285417, u'Image': u'jupyter/notebook',
 u'Labels': {}, u'NetworkSettings': {u'Networks': {u'bridge': {u'NetworkID': u'',
 u'MacAddress': u'02:42:ac:11:00:02', u'GlobalIPv6PrefixLen': 0, u'Links': None, 
u'GlobalIPv6Address': u'', u'IPv6Gateway': u'', u'IPAMConfig': None, 
u'EndpointID': u'ec791d0a8b52fee4fc46447b43304ce626629790e3a525cd4ae03e6a25bda3d5',
 u'IPPrefixLen': 16, u'IPAddress': u'172.17.0.2', u'Gateway': u'172.17.0.1',
u'Aliases': None}}}, u'HostConfig': {u'NetworkMode': u'default'},
 u'ImageID': u'sha256:1c02aa25b7b817d8b7a7557b4b62250db6c735da3e7fabb4b3a157e55256e2d4',
 u'State': u'running', u'Command': u'tini -- jupyter notebook', 
u'Names': [u'/berserk_darwin'], u'Mounts': [{u'RW': True,
 u'Source': u'/home/ernesto/dockers/notebook/notebook',
 u'Destination': u'/notebooks', u'Mode': u'', u'Propagation': u'rprivate'}],
 u'Id': u'dfcc1bd19dab02580cce30d1719d8514eb0af2ab1dec8b01e42b95376ce5e608',
 u'Ports': [{u'IP': u'0.0.0.0', u'Type': u'tcp', u'PublicPort': 8888,
 u'PrivatePort': 8888}]}]
```
Como se puede ver en la documentación y en los scripts ejecutados, se puede crear
 una aplicación que acceda al API de docker o trabajar con las imágenes y contenedores 
desde python. 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)


