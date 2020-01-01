Title: Profiling de un script Python con la herramienta cProfile
Date: 2016-06-13 12:00 
Category: Tutorial Python
Tags: Python,Profiling,cProfile
lang: es  
translation: true  
  
Hace un tiempo toque el tema de herramientas de profiling para Python ([ver enlace](https://www.seraph.to/tag/profiling.html)).

Hay otras herramientas como cProfile que se pueden usar y son menos invasiva que las de los artículos anteriores, quiero decir, no necesitan modificar el código de la aplicación para que sea utilizada.

Como script de prueba usaré el mismo de raíz cuadrada que se encuentra en mi repo en [github](https://github.com/ecrespo/raizcuadrada), el mismo de los artículos sobre [pruebas unitarias](https://www.seraph.to/pruebas-unitarias-en-python-con-unittest.html#pruebas-unitarias-en-python-con-unittest), [pruebas unitarias con docker](https://www.seraph.to/ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker.html#ejecutar-una-prueba-de-unittest-en-python-con-un-contenedor-docker), [pruebas de documentación](https://www.seraph.to/separar-codigo-de-pruebas-de-la-documentacion-doctest-2da-parte.html), [pruebas de documentación con docker](https://www.seraph.to/ejecutar-una-prueba-de-doctest-con-un-contenedor-docker.html#ejecutar-una-prueba-de-doctest-con-un-contenedor-docker)  y el de [pylint con docker](https://www.seraph.to/analizar-codigo-python-con-pylint-desde-docker.html#analizar-codigo-python-con-pylint-desde-docker).

No se necesita instalar nada para usar `cProfile`.

El código del módulo raíz cuadrada es el siguiente:
```python
#!/usr/bin/env python3

# -*- coding: utf-8 -*-



"""

Se importa el módulo math para calcular la raiz cuadrada.

"""

import math



#Función raiz cuadrada.

def Raiz(a):

    """Si a es mayor o igual a cero se calcula la raiz cuadrada"""

    if a >= 0:

        return math.sqrt(a)

    #Si es menor a cero se genera una excepción donde se informa que a debe ser mayor o igual a cero.

    else:

        raise ValueError("a debe ser >= 0")



if __name__ == '__main__':

    #Se importa el módulo doctest

    #import doctest

    #Se realiza la prueba al archivo raizcuadra.txt

    #doctest.testfile("raizcuadrada.txt")

    Raiz(5)

    Raiz(9)

    Raiz(25)

    #Raiz(-1)

```

Para ejecutar cProfile:
```python
python -m cProfile -s cumtime raizcuadrada.py

         8 function calls in 0.000 seconds



   Ordered by: cumulative time



   ncalls  tottime  percall  cumtime  percall filename:lineno(function)

        1    0.000    0.000    0.000    0.000 raizcuadrada.py:6(<module>)

        3    0.000    0.000    0.000    0.000 raizcuadrada.py:10(Raiz)

        3    0.000    0.000    0.000    0.000 {math.sqrt}

        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

```


Esto mismo se puede ejecutar desde el contenedor que se usó en el artículo de `pyLint`:
```
docker run  -v "$PWD:/app" -ti prueba-python  python -m cProfile -s cumtime raizcuadrada.py
```

A continuación se muestra una figura de la ejecución del comando:

![](./images/profilingdeunscriptpythonconcprofile-1.png)




Para más información pueden revisar la [documentación oficial de python](https://docs.python.org/2/library/profile.html), [un artículo en inglés sobre cProfile](https://julien.danjou.info/guide-to-python-profiling-cprofile-concrete-case-carbonara/) y una [guía de análisis de rendimiento para python](https://www.huyng.com/posts/python-performance-analysis). 


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
