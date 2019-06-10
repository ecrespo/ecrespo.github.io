Title: Separar código de pruebas de la documentación (doctest, 2da parte)
Date: 2012-12-14 9:00
Category: 
Tags: Canaima,Linux,Python,Ubuntu
lang: es
translation: true

En el [artículo anterior](https://www.seraph.to/probar-codigo-con-doctest.html#probar-codigo-con-doctest) se explicó como utilizar `doctest` dentro de un código para realizar pruebas sobre la documentación de cada función.

Ahora se explicará como realizar dichas pruebas de la documentación en un archivo aparte del código del programa. Se usará el mismo ejemplo del artículo anterior pero adaptandolo a tener la documentación aparte en un archivo de texto.

El código se muestra a continuación:
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Se importa el módulo math para calcular la raiz cuadrada.

import math

#Función raiz cuadrada.

def Raiz(a):

    #Si a es mayor o igual a cero se calcula la raiz cuadrada

    if a >= 0:

        return math.sqrt(a)

    #Si es menor a cero se genera una excepción donde se informa que a debe ser mayor o igual a cero.

    else:

        raise ValueError("a debe ser >= 0")

if __name__ == '__main__':

    #Se importa el módulo doctest

    import doctest

    #Se realiza la prueba al archivo raizcuadra.txt

    doctest.testfile("raizcuadrada.txt")
```

Como se ve se realiza la prueba al archivo raizcuadrada.txt. El archivo contiene lo siguiente:

```python
Modulo raiz cuadrada

=====================

Usando  'raizcuadrada'

------------------------------

Primero se importa la función:

>>> from raizcuadrada import Raiz
```

Ejemplos de calculo de raiz cuadrada:

```python
>>> Raiz(4)

2.0

>>> Raiz(9)

3.0

>>> Raiz(25)

5.0

>>> Raiz(0)

0.0

>>> Raiz(-1)

Traceback (most recent call last):

...

ValueError: a debe ser >= 0
```
Ahora lo que viene es ejecutar el comando que devuelve el resultado de las pruebas:
```
python -m doctest -v raizcuadrada.txt

Trying:

    from raizcuadrada import Raiz

Expecting nothing

ok

Trying:

    Raiz(4)

Expecting:

    2.0

ok

Trying:

    Raiz(9)

Expecting:

    3.0

ok

Trying:

    Raiz(25)

Expecting:

    5.0

ok

Trying:

    Raiz(0)

Expecting:

    0.0

ok

Trying:

    Raiz(-1)

Expecting:

    Traceback (most recent call last):

    ...

    ValueError: a debe ser >= 0

ok

1 items passed all tests:

   6 tests in raizcuadrada.txt

6 tests in 1 items.

6 passed and 0 failed.


Test passed.
```

Como se puede observar en este caso se realiza la importación del programa y luego se empieza las pruebas.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)