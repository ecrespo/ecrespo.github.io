Title: Importar un contenedor Docker en Python.
Date: 2016-02-24 09:00  
Category: Tutorial de Docker 
Tags: Linux,Python, Docker  
lang: es  
translation: true  

![](./images/importaruncontenedordockerenpython-1.png)

En los artículos anteriores sobre Docker se ha tocado el manejo de imágenes, ahora se explicará como importar un contenedor desde Python, este artículo se basa en el [siguiente artículo en inglés](https://blog.deepgram.com/import-a-docker-container-in-python/).

1. [Instalar Docker en Debian Jessie](https://www.seraph.to/instalar-docker-en-debian-jessie.html)  
2. [Uso de Docker en Debian Jessie (parte 1)](https://www.seraph.to/uso-de-docker-en-debian-jessie-parte-1.html)  
3. [Uso de Docker en Debian Jessie (parte 2)](https://www.seraph.to/uso-de-docker-en-debian-jessie-parte-2.html)  
4. [Crear una imagen Docker a partir de un archivo Dockerfile](https://www.seraph.to/crear-una-imagen-docker-a-partir-de-un-archivo-dockerfile.html)  
5. [Iniciando Django usando Docker](https://www.seraph.to/iniciando-django-usando-docker.html)  
6. [Instalar Gitlab por medio de Docker](https://www.seraph.to/instalar-gitlab-por-medio-de-docker.html)  
7. [Ejecutando microservicios con docker usando docker-compose](https://www.seraph.to/ejecutando-micros-servicios-con-docker-usando-docker-compose.html)  
8. [Docker en Docker (DinD)](https://www.seraph.to/docker-en-docker-dind.html)
9. [Iniciando Django con docker usando docker-compose con postgresql como microservicio.](https://www.seraph.to/iniciando-django-con-docker-usando-docker-compose-con-postgresql-como-microservicio.html)

Se tiene el módulo [Sidomo](https://github.com/deepgram/sidomo) que permite manejar contenedores.

Para instalar `sidomo` se ejecuta el comando `pip`:
```
pip install -e git+https://github.com/deepgram/sidomo.git#egg=sidomo
```
Se baja la imagen Docker de Ubuntu:
```
docker pull ubuntu
```
El código de ejemplo del sitio de `sidomo` se encuentra en el siguiente [enlace](https://github.com/deepgram/sidomo/blob/master/examples/hello_world.py).


La modificación del código es el siguiente:

```python
#!/usr/bin/env python

from sidomo import Container

def say_hello(to):


    """Just say it."""


    with Container(


        'ubuntu',


        stderr=False


    ) as c:


        for line in c.run(


            'echo Hola Mundo  %s' % to


        ):


            yield line



if __name__ == '__main__':


    for line in say_hello("desde un contenedor Docker"):


        print line

```


Al ejecutar el código se tiene:
```python
python ejemplo.py 
Hola Mundo desde un contenedor Docker
```

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
