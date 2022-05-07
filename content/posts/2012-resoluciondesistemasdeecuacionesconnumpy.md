Title: Resolución de sistemas de ecuaciones con NumPy
Date: 2012-12-02 9:00
Category: Tutorial Python
Tags: Canaima,Debian,General,Linux,numpy,Python,Ubuntu
lang: es
translation: true

Recordando un poco de resolución de sistemas de ecuaciones con Algebra Lineal.

Se puede usar python por medio de NumPy para resolver estos sistemas de ecuaciones por medio de matrices.

Las ecuaciones que se quieren resolver son:
```
3x+9y-10z = 24
x-6y+4z = -4
10x-2y+8z = 20
```
Estas ecuaciones se pueden representar como un sistema de Matrices como `A*x=B`, donde si se desea resolver la matríz x se aplica la inversa de A, `x = inv(A)*B`. Donde A para nuestro caso es `[[3 9 -10][1 -6 4][10 -2 8]` y B es `[[24][-4[[20]]`.

El código para resolver el sistema de ecuaciones es el siguiente:
```python
#!/usr/bin/env python

#Se importa numpy como np
import numpy as np


#Se define los valores de la matriz A
A = np.matrix([[3,9,-10],[1,-6,4],[10,-2,8]])

#Se definen los valores de la matriz B
B = np.matrix([[24],[-4],[20]])

#Se calcula el valor de X con X=inv(A)*B
X = A**(-1)*B


#Se muestra el resultado
print("El resultado de X es:",X)

#Para verificar el resultado se calcula X*A y debe dar B
print("El resultado de A*X es B-> ",A*X)
```

El resultado de ejecutar el script se muestra a continuación:
```python
('El resultado de X es:', matrix([[ 2.99029126],
        [ 0.40776699],
        [-1.13592233]]))
('El resultado de A*X es B-> ', matrix([[ 24.],
        [ -4.],
        [ 20.]]))
```
Hay un problema a la hora de calcular la matriz inversa y es que no todas las matrices pueden ser invertidas, así que está solución no funciona para todos los casos. La solución es usar la función [numpy.linalg.svd](docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html).

El código siguiente en vez de usar la clase matrix usará la clase array y usar la función `numpy.linalg.svd`.
```python
#!/usr/bin/env python

#Se importa numpy como np
import numpy as np

#Se define los valores de la matriz A
A = np.array([[3,9,-10],[1,-6,4],[10,-2,8]])

#Se definen los valores de la matriz B
B = np.array([[24],[-4],[20]])

#Se calcula el valor de X con X=inv(A)*B
X = np.linalg.inv(A).dot(B)


#Se muestra el resultado
print("El resultado de X es:",X)
```
El resultado es el siguiente:
```
('El resultado de X es:', array([[ 2.99029126],
       [ 0.40776699],
       [-1.13592233]]))
```
Así pues el valor de x es 2.99, el de y es 0.407 y el de z es -1.1359, mostrado con 2 procedimientos distintos.

El código de estos 2 ejemplos lo pueden encontrar en el [repositorio de bitbucket de códigos de este blog](https://bitbucket.org/ecrespo/ernesto-ecrespo.blogspot/src/71eb8e1fcbaf472997dbcd4d179f2423b7ee4ae6/numpy1?at=default).

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)