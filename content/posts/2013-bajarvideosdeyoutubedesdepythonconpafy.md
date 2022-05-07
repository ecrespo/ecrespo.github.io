Title: Bajar vídeos de youtube desde Python con Pafy.
Date: 2013-09-01 9:00
Category: General
Tags: General
lang: es
translation: true

`Pafy` permite realizar busquedas de vídeos de youtube y descargarlos.

El sitio de `Pafy` se encuentra en [github](http://np1.github.io/pafy/), en ese sitio se puede bajar la librería en formato zip, tar.gz o visitar el repositorio git del proyecto.

Para instalar `Pafy` desde Linux se puede hacer con `easy_install` o `pip`:
```
pip install Pafy
```
Se ejecuta python:
```python
ernesto@grievous:~$ python

Python 2.7.3 (default, Jan  2 2013, 13:56:14) 

[GCC 4.7.2] on linux2

Type "help", "copyright", "credits" or "license" for more information.

>>> 
```

Se importa Pafy:
```python
>>> from pafy import Pafy
```

Se crea la variable donde se encuentra el url del vídeo:
```python
>>> url="http://www.youtube.com/watch?v=YOZjaqHioro"
```

Se crea la instancia del vídeo:
```python
>>> video = Pafy(url)
```

Se obtiene el título del vídeo:
```python
>>> video.title

u'Jimmy Fallon, Robin Thicke & The Roots Sing "Blurred Lines" (w/ Classroom Instruments)'
```
El rating y longitud del vídeo:

```python
>>> video.rating


4.9188302785




>>> video.length


214

```

Se muestra los metadatos del vídeo:
```python
>>> print video


Title: Jimmy Fallon, Robin Thicke & The Roots Sing "Blurred Lines" (w/ Classroom Instruments)


Author: latenight


ID: YOZjaqHioro


Duration: 00:03:34


Rating: 4.9188302785


Views: 10459846


Thumbnail: https://i1.ytimg.com/vi/YOZjaqHioro/default.jpg


Keywords: Jimmy Fallon, Late Night With Jimmy Fallon, Late Night, NBC, NBC TV, Television, Funny, Talk Show, comedic, humor, stand-up, snl, Fallon Stand-up, Fallon monologue, latenight, jokes, funny video, interview, variety, comedy sketches, talent, celebrities, music, musical performance, The Roots, video, clip, highlight, talking, youtube, jimmy fallon & robin thicke, robin thicke, blurred lines, classroom instruments, late night music room
```

Se muestra el título del vídeo, el autor, el ID del vídeo, la duración, el rating, la cantidad de veces que se ha visto, entre otra información.

Se muestra todos los formatos del vídeo y su resolución:
```python
>>> streams = video.streams


>>> for s in streams: print s.resolution, s.extension


... 


1080x1920 webm


1080x1920 mp4


720x1280 webm


720x1280 mp4


480x854 webm


480x854 flv


360x640 webm


360x640 flv


360x640 mp4


240x400 flv


320x240 3gp


144x176 3gp

```

Se muestran todos los formatos, su resolución y el url para descargarlo:

```python
>>> for s in streams: print s.resolution, s.extension, s.url


... 


1080x1920 webm http://r14---sn-ab5e6nll.c.youtube.com...


1080x1920 mp4 http://r14---sn-ab5e6nll.c.youtube.com...


720x1280 webm http://r14---sn-ab5e6nll.c.youtube.com...


720x1280 mp4 http://r14---sn-ab5e6nll.c.youtube.com...


480x854 webm http://r14---sn-ab5e6nll.c.youtube.com...


480x854 flv http://r14---sn-ab5e6nll.c.youtube.com...


360x640 webm http://r14---sn-ab5e6nll.c.youtube.com...


360x640 flv http://r14---sn-ab5e6nll.c.youtube.com...


360x640 mp4 http://r14---sn-ab5e6nll.c.youtube.com...


240x400 flv http://r14---sn-ab5e6nll.c.youtube.com...


320x240 3gp http://r14---sn-ab5e6nll.c.youtube.com...


144x176 3gp http://r14---sn-ab5e6nll.c.youtube.com...

```

Obtener la mejor resolución y su extensión:

```python
>>> best = video.getbest()


>>> best.resolution, best.extension


('1080x1920', 'webm')

```

Mejor resolución para un formato en específico:

```python

>>> best = video.getbest(preftype="mp4")


>>> best.resolution, best.extension


('1080x1920', 'mp4')


```

Obtener el url para descargar el vídeo:

```python
>>> best.url


'http://r14---sn-ab5e6nll.c.youtube.com/videoplayback...'

```

Se descarga el vídeo con un nombre y en una ruta predefinida:

```python
>>> myfilename = "/home/ernesto/videos/" + "JimmtFallon" + "." + best.extension


>>> best.download(progress=False, filepath=myfilename)


-Downloading 'Jimmy Fallon, Robin Thicke & The Roots Sing "Blurred Lines" (w/ Classroom Instruments).webm' [157,236,345 Bytes]



Done
```

Se sale de python:

```python
>>> exit()

```

Se verifica que el archivo bajo:

```
ernesto@grievous:~/videos$ ls -l


total 153556


-rw-r--r-- 1 ernesto ernesto 157236345 sep  1 11:03 JimmtFallon.webm

```

Ahora puede ejecutar su reproductor de vídeo preferido para ver el vídeo.  

En la siguiente figura se muestra la captura de pantalla del escritorio al momento de reproducir el vídeo con VLC:

![](./images/bajarvideosdeyoutubedesdepythonconpafy-1.png) 


Si desean ver el vídeo a continuación les dejo el enlace de youtube para verlo:

[https://youtu.be/YOZjaqHioro](https://youtu.be/YOZjaqHioro) 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)