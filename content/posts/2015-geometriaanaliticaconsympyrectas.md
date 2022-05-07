Title: Geometría Analítica con Sympy (rectas)  
Date: 2015-02-23 11:20  
Category: Tutorial Python  
Tags: Canaima,Debian,General,Python,Ubuntu,Sympy
lang: es  
translation: true  

Continuando con el manejo de geometría analítica de Sympy ahora se explicará el manejo de rectas.

Un resumen de los artículos anteriores:

* [Cálculo de límites con Sympy](https://www.seraph.to/calculo-de-limites-con-la-libreria-sympy.html#calculo-de-limites-con-la-libreria-sympy)

* [Cálculo de derivadas con Sympy](https://www.seraph.to/calculo-de-derivadas-con-sympy.html#calculo-de-derivadas-con-sympy)

* [Cálculo de integrales con Sympy](https://www.seraph.to/calculo-de-integrales-con-sympy.html#calculo-de-integrales-con-sympy)

* [Resolución de sistemas de ecuaciones lineales con Sympy](https://www.seraph.to/resolucion-de-sistemas-de-ecuaciones-con-sympy.html#resolucion-de-sistemas-de-ecuaciones-con-sympy)

* [Geometría analítica con Sympy (segmentos)](https://www.seraph.to/geometria-analitica-con-sympy-segmentos.html#geometria-analitica-con-sympy-segmentos)

En el siguiente [enlace](https://bitbucket.org/ecrespo/ernesto-ecrespo.blogspot/src/c645a908ed04a4cf0178f41df93fe1d9c871eee8/geometriaanalitica/geometria-lineas.ipynb?at=default) encontrarán el archivo notebook del código que se explicará a continuación.

A continuación se muestra el código del script de manejo de rectas.
```python
#!/usr/bin/env python

from sympy.geometry import *



#Creacion de 4 puntos

P1 = Point(0, 0)

P2 = Point(3, 4)

P3 = Point(2, -1)

P4 = Point(-1, 5)



#Creacion de 2 segmentos

S1 = Segment(P1, P2);#segmento 1 a partir de los puntos 1 y 2

S2 = Segment(P3, P4);#Segmento 2 a partir de los puntos 3 y 4



#Se crea 2 rectas

#A partir de los puntos 1 y 2

L1 = Line(P1, P2)

#Se crea la recta 2 que ser perpendicular a la recta 1 y contenga al punto 3

L2 = L1.perpendicular_line(P3)





#Manejo de rectas



print L2.arbitrary_point();#Punto arbitrario de la recta 2 (ecuacion parametrica)

print L2.equation() ;#ecuacion de la recta 2

print L2.contains(P4);#Linea 2 contiene al punto 4?

print L2.distance(P4);#distancia del punto 4 a la recta 2?

print L1.is_parallel(S2);#La recta 1 es paralela al segmento 2?
```
A continuación el resultado de la ejecución del script:  
```
Point(4*t + 2, -3*t - 1)

3*x + 4*y - 2

False

3

False
```

A continuación se muestra una imagen de la ejecución del notebook para este artículo:

![](./images/geometriaanaliticaconsympyrectas-1.png)

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
