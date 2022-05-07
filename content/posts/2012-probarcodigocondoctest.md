Title: Probar código con doctest
Date: 2012-12-13 9:00
Category: Tutorial Python
Tags: Canaima,Debian,General,Linux,Python,Ubuntu,doctest
lang: es
translation: true

`Doctest` es un framework que viene en Python el cual permite desarrollar aplicaciones utilizando TDD ([Desarrollo guiado por pruebas](https://es.wikipedia.org/wiki/Desarrollo_guiado_por_pruebas)).

El TDD exige escribir las pruebas primero y la refactorización del código para llegar al resultado deseado.

En este caso se usará `doctest` el cual permite realizar pruebas según la documentación que se tenga escrita en el código. Significa que es necesario tener una documentación clara para cada función antes de desarrollarla, de esta forma se tiene claro los casos de funcionamiento correcto de la función y los casos en los cuales puede fallar.

El código de ejemplo es el de una función que permite calcular la raíz cuadrada de un número.

A continuación el código:
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Se importa el módulo math para calcular la raiz cuadrada.

import math

#Función raiz cuadrada.

def RaizCuadrada(a):

    """

    >>> RaizCuadrada(4)

    2.0

    >>> RaizCuadrada(9)

    3.0

    >>> RaizCuadrada(25)

    5.0

    >>> RaizCuadrada(0)

    0.0

    >>> RaizCuadrada(-1)

    Traceback (most recent call last):

        ...

    ValueError: a debe ser >= 0

    """

    #Si a es mayor o igual a cero se calcula la raiz cuadrada

    if a >= 0:

        return math.sqrt(a)

    #Si es menor a cero se genera una excepción donde se informa que a debe ser mayor o igual a cero.

    else:

        raise ValueError("a debe ser >= 0")
```

Como se muestra se genera en la documentación una serie de casos de ejecución de la función donde debe devolver un valor correcto y si se pasa un valor que no puede ser calculado devuelve la excepción.

Para realizar la prueba se ejecuta el código realizando una llamada al módulo `doctest` y modo `verbose`:
```python
python -m doctest -v prueba-raizcuadrada.py
```
El resultado es el siguiente:
```python
Trying:

    RaizCuadrada(4)

Expecting:

    2.0

ok

Trying:

    RaizCuadrada(9)

Expecting:

    3.0

ok

Trying:

    RaizCuadrada(25)

Expecting:

    5.0

ok

Trying:

    RaizCuadrada(0)

Expecting:

    0.0

ok

Trying:

    RaizCuadrada(-1)

Expecting:

    Traceback (most recent call last):

        ...

    ValueError: a debe ser >= 0

ok

1 items had no tests:

    prueba-raizcuadrada

1 items passed all tests:

   5 tests in prueba-raizcuadrada.RaizCuadrada

5 tests in 2 items.

5 passed and 0 failed.

Test passed.
```

Como se muestra todos los casos pasaron el test.
Pueden revisar la siguiente documentación y tutoriales:
La documentación oficial la puede revisar en el siguiente [enlace](https://docs.python.org/2/library/doctest.html).  

- [Como hacer pruebas 1: Doctest](http://magmax9.blogspot.com/2011/09/python-como-hacer-pruebas-1.html).
- [Introducción a doctest](http://pythontesting.net/framework/doctest/doctest-introduction/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A%20PythonTesting%20%28Python%20Testing%29).
- [Otro tutorial de Doctest](https://pymotw.com/3/doctest/)  

En otro artículo se explicará como separar los diferentes casos en un archivo de texto y el programa en un script aparte.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)