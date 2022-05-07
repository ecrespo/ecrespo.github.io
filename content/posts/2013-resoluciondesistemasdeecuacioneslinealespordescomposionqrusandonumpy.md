Title: Resolución de sistemas de ecuaciones lineales por descomposión QR usando Numpy
Date: 2013-02-21 9:00
Category: Tutorial Python
Tags: General,numpy,Python
lang: es
translation: true

En Diciembre se  publicó un [artículo](https://www.seraph.to/resolucion-de-sistemas-de-ecuaciones-con-numpy.html) donde se explica como resolver sistemas de ecuaciones.

Este artículo se basa de un artículo en Inglés [QR descomposition with numpy ](glowingpython.blogspot.com/2011/05/qr-decomposition-with-numpy.html).

Si se desea averiguar más sobre la descomposición QR se puede consultar a la página de [wikipedia](es.wikipedia.org/wiki/Descomposici%C3%B3n_QR) ó de la siguiente [página](rkb.home.cern.ch/rkb/AN16pp/node224.html#SECTION0002240000000000000000).

Las ecuaciones que se usaron son:
```
3x+9y-10z  =   24
x-6y+4z      =   -4
10x-2y+8z  =  20
```
Donde `Ax = b.`
```
A = [[3 9 -10][1 -6 4][10 -2 8]] y
B  = [[24][-4[[20]]
```

El código se muestra a continuación:
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

from numpy import *


#Se define los valores de la matriz A
A = array([[3,9,-10],[1,-6,4],[10,-2,8]])

Q,R = linalg.qr(A) # qr decomposition of A

#Se definen los valores de la matriz B
b = array([[24],[-4],[20]])


#resolver Ax=b usando la funcion estandar numpy
x = linalg.solve(A,b)


#resolver Ax = b usando Q y R.
y = dot(Q.T,b)
xQR = linalg.solve(R,y) 

print "\nComparacion de Soluciones:"
print x.T,'Ax=b'
print xQR.T,'Rx=y'
```
Al ejecutar el script se tiene lo siguiente:

```python
python qr.py 
``` 


Comparacion de Soluciones:
```python
[[ 2.99029126  0.40776699 -1.13592233]] Ax=b

[[ 2.99029126  0.40776699 -1.13592233]] Rx=y
```

Como se puede ver, la solución usando la función estándar de numpy y por la descomposición QR generan el mismo resultado.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)