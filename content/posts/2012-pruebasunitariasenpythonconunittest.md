Title: Pruebas Unitarias en Python con unittest
Date: 2012-12-26 9:00
Category: Tutorial Python
Tags: General,Linux,numpy,Python,TDD,unittest
lang: es
translation: true

Continuando con las herramientas que permiten el aseguramiento de la calidad, ahora se realizará pruebas unitarias a la función que cálcula la raíz cuadrada del artículo anterior ([Probar código con doctest](https://www.seraph.to/probar-codigo-con-doctest.html#probar-codigo-con-doctest)).

El desarrollo guiado por pruebas ó [Test driven development](http://es.wikipedia.org/wiki/TDD) (TDD), es una práctica de la programación que involucra dos prácticas: Escribir las pruebas primero y refactorizar continuamente el código.

Para escribir primero las pruebas se usa generalmente las [pruebas unitarias](http://es.wikipedia.org/wiki/Prueba_unitaria). esto es una forma de probar el correcto funcionamiento de un módulo de código. Permite asegurar el correcto funcionamiento de cada módulo por separado, luego con las [pruebas de integración](https://es.wikipedia.org/wiki/Pruebas_de_integraci%C3%B3n), se podrá asegurar el correcto funcionamiento del sistema.

Ciclo de desarrollo guidado por pruebas (TDD).
En primer lugar se debe definir una lista de requisitos, después se ejecuta el siguiente ciclo:

1. Elegir un requisito: Se elige de una lista el requerimiento que se cree dará mayor conocimiento del problema y que a la vez sea facilmente implementable.  

2. Escribir una prueba.  

3. Verificar que la prueba falle: Si la prueba no falla es por que el requerimiento ya estaba implementado o por que la prueba es erronea.   

4. Ejecutar las pruebas automatizadas: Verificar que todo el conjunto de pruebas funciona correctamente.  

5. Eliminación de duplicación: Se eliminará código duplicado.   

6. Actualización de la lista de requisitos: Se actualiza la lista de requisitos tachando el requisito implementado.

Para que una prueba unitaria sea buena tiene que cumplir los siguientes requisitos:

- Automatizable: No debe ejecutarse manualmente (útil para integración continua).  

- Completas: Deben cubrir la mayor cantidad de código.  

- Reutilizables: No se deben crear pruebas que sólo puedan ser ejecutadas una vez (útil para integración continua).  

- Independientes: La ejecución de una prueba no debe afectar la ejecución de otra prueba.

- Profesionales: Las pruebas deben ser consideradas igual que el código, con la misma profesionalidad, documentación, etc. 

Las pruebas unitarias son pruebas automatizadas que prueban pequeñas piezas de código, usualmente una función o un método.

Python tiene el API de `PyUnit` para pruebas unitarias. El módulo se llama `unittest`, se basa en el framework `XUnit` diseñado por Ken Beck y Erich Gamma.

El código de ejemplo muestra por un lado la función Raiz y por el otro la clase RaizTest que hereda de `unittest.TestCase`. Esta clase tendrá 3 métodos, el primero que cálcula la raiz de 9 y devuelve 3, el segundo que cálcula la raiz de 0 y devuelve 0 y por último el que cálcula la raiz de un valor negativo y devuelve una excepción o mensaje de error.

El código se muestra  a continuación:

```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Se importa el módulo unittest y math

import unittest

import math

#Función raiz cuadrada.

def Raiz(a):

    #Si a es mayor o igual a cero se calcula la raiz cuadrada

    if a >= 0:

        return math.sqrt(a)

    #Si es menor a cero se genera una excepción donde se informa que a debe ser mayor o igual a cero.

    else:

        raise ValueError,"a debe ser >= 0"

class RaizTest(unittest.TestCase):

    def test_Raiz(self):

        #Test para la raiz de nueve que devuelve 3 que debe pasar.

        self.assertEqual(3, Raiz(9))

    def test_zero(self):

        #Test para la raiz de 0 que devuelve 0, que debe pasar.

        self.assertEqual(0, Raiz(0))    

    def test_negative(self):

        #Test para la raiz de un número negativo, que debe fallar.

        # Este debe devolver un ValueError, pero se espera un IndexError.

        self.assertRaises(IndexError, Raiz(-10))

if __name__ == '__main__':

    #Se ejecuta la prueba unitaria

    unittest.main()

```

Al ejecutar el código se tiene lo siguiente:  
```
ecrespo@jewel:~/proyectos/ernesto-ecrespo.blogspot/timeit$ python test-raiz.py 
.E.
======================================================================
ERROR: test_negative (__main__.RaizTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test-raiz.py", line 40, in test_negative
    self.assertRaises(IndexError, Raiz(-10))
  File "test-raiz.py", line 24, in Raiz
    raise ValueError,"a debe ser >= 0"
ValueError: a debe ser >= 0

----------------------------------------------------------------------
Ran 3 tests in 0.001s

FAILED (errors=1)
```

Como se puede ver, la prueba de un valor negativo falla. 
Si se comenta el método de prueba de valor negativo la ejecución devuelve que no hay errores:
```
ecrespo@jewel:~/proyectos/ernesto-ecrespo.blogspot/timeit$ python test-raiz.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Las funciones de `unittest` utilizadas son:  

- `assertEqual`: Prueba donde dos valores son iguales.
- `assertRaises`: Prueba donde una excepción es devuelta.  

Para más métodos del módulo unittest se puede revisar la [documentación](https://docs.python.org/2/library/unittest.html#unittest.TestCase).



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)