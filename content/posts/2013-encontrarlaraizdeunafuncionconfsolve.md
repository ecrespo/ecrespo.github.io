Title: Encontrar la raíz de una función con fsolve
Date: 2013-02-14 10:00
Category: Tutorial Python
Tags: Canaima,Debian, General,Linux,matplotlib,numpy,Python,Ubuntu
lang: es
translation: true

Este artículo explica como calcular la raíz de una función utilizando la función `fsolve`.

El artículo se basa en un artículo en Inglés "[How to find the rooots of a function with fsolve](https://glowingpython.blogspot.com/2011/05/how-to-find-roots-of-function-with.html)".

La función fsolve retorna la raíces de una ecuación no lineal definida por `f(x) = 0`.
Para este caso se calculará la raíz de la función `f(x) = x^3`.

A continuación se muestra el código:

```python
#Import fsolve para calcular la raiz de la funcion x^3

from scipy.optimize import fsolve

#Importar pylab

import pylab

#importar numpy

import numpy

#se calcula la potencia 3 de x con la funcion lambda

potencia3 = lambda x : x**3

#Se calcula la raiz de x^3 iniciando con x = 10

resultado = fsolve(potencia3,10) # starting from x = 10

print resultado

#Se define 400 valores de x entre -4 a 4

x = numpy.linspace(-4,4,400)

#Se genera la grafica, pasando el valor de x

#la potencia 3era de x, el valor de resultado, la potencia 3era de resultado

pylab.plot(x,potencia3(x),resultado,potencia3(resultado),'ro')

#Se define el grid

pylab.grid(b=1)

#Se muestra la grafica

pylab.show()
```
La gráfica muestra el punto donde se encuentra la raíz de la función:

![](./images/encontrarlaraizdeunafuncionconfsolve.png) 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)