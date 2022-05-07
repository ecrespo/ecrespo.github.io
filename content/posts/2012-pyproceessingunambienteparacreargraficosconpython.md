Title: Pyproceessing: Un ambiente para crear gráficos con Python
Date: 2012-12-24 9:00
Category: Tutorial Python
Tags: General,Linux,Pyprocessing,Python
lang: es
translation: true

Pyprocessing es un paquete python que permite crear gráficos que se basa en las librerías  [OpenGL](https://www.opengl.org/) y [Pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home). El proyecto se aloja en [google code](https://code.google.com/archive/p/pyprocessing/).

En la documentación encontrarán la guía de referencia rápida, un tutorial [básico](https://code.google.com/archive/p/pyprocessing/wikis/BasicTutorial.wiki), [un tutorial más completo](https://code.google.com/archive/p/pyprocessing/wikis/Tutorials.wiki) y las [instrucciones de uso](https://code.google.com/archive/p/pyprocessing/wikis/UsageInstructions.wiki).

Para instalarlo en linux se usa `easy_install` o `pip`:
```
easy_install pyprocessing
```
```
pip install pyprocessing
```

El ejemplo que se hará es el de crear con rectangulo, líneas y elipses una especie de muñeco sin brazos junto a una pequeña esfera. Este ejemplo se basa en el pequeño ejemplo que tiene el proyecto en la página de entrada.

El código se muestra a continuación:

```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Se importa pyprocessing

from pyprocessing import *

#define el tamaño de la ventana.

size(200,200)

#Define un rectangulo en el centro de la ventana

rectMode(CENTER)

#Se crea el rectangulo(x,y,ancho,alto)

rect(100,100,20,100)

#Se crean 3 elipses(x,y,ancho,alto)

ellipse(100,70,60,60)

ellipse(81,70,16,32) 

ellipse(119,70,16,32)

#Se crean 2 lineas(x1,y1,x2,y2)

line(90,150,80,160)

line(110,150,120,160)

#No se crea bordes en la figura

noStroke();

#Define que tendrá luz la esfera

lights();

#Define la cantidad de desplazamiento con respecto a la ventana.

#(derecha/izquierda,arriba/abajo,delante/detrás)

translate(28, 48, 0);

#Se crea una esfera con radio 15

sphere(15)

#Se muestra en la ventana.

run()
```
La siguiente figura muestra el resultado del código al ser ejecutado:

![](./images/pyproceessingunambienteparacreargraficosconpython.png) 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)