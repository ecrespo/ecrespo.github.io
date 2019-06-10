Title: Profiling de un script python con timeit
Date: 2012-12-03 9:00
Category: Tutorial Python
Tags: General,numpy,Python,Profiling, timeit
lang: es
translation: true

El profiling permite conocer el tiempo que consume un programa en ejecutarse e incluso conocer cuanto tarda cada llamada de funciones de distintos módulos utilizados.

El ejemplo que se hará es un script que tiene una función donde se le pasa el tamaño de la matriz NxN  generada de forma aleatoria y devuelve la matriz inversa. Luego se genera una lista de tamaños de forma aletoria. Se crea un ciclo recorriendo la lista donde dentro del ciclo se crea la matriz inversa.

El script se guarda con nombre `ej4.py`.
El código del script se muestra a continuación:
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-



#Se importa numpy como np

import numpy as np





#Se crea la función que invierte una matriz de valores aleatorios

def Inversa(n):

    a = np.matrix(np.random.rand(n, n))

    return a.I



#Se define una lista de  tamaños de la matriz

tamagno = 2 ** np.arange(0, 12)





#Se recorre la lista de tamaños y se invierte cada matriz con la

#funcion.

for n in tamagno:

    Inversa(n)
```

Desde la consola se ejecuta  `ipython --pylab`. Luego se ejecuta el comando `%run -t ej4.py` el cual devuelve el tiempo de ejecución en la capa de usuario, capa de sistema. Luego se ejecuta `%run -p ej4.py` el cual devuelve los tiempos de ejecución de cada función.
```python
ecrespo@jewel:~/bin/python/matplotlib$ ipython --pylab

Python 2.7.3rc2 (default, Apr 22 2012, 22:35:38) 

Type "copyright", "credits" or "license" for more information.



IPython 0.13.1 -- An enhanced Interactive Python.

?         -> Introduction and overview of IPython's features.

%quickref -> Quick reference.

help      -> Python's own help system.

object?   -> Details about 'object', use 'object??' for extra details.



Welcome to pylab, a matplotlib-based Python environment [backend: TkAgg].

For more information, type 'help(pylab)'.



In [1]:  %run -t ej4.py



IPython CPU timings (estimated):

  User   :       8.79 s.

  System :       0.13 s.

Wall time:       6.17 s.





In [2]:  850 function calls in 6.201 seconds





   Ordered by: internal time





   ncalls  tottime  percall  cumtime  percall filename:lineno(function)


       12    5.556    0.463    5.556    0.463 {numpy.linalg.lapack_lite.dgesv}


       24    0.236    0.010    0.236    0.010 {numpy.core.multiarray._fastCopyAndTranspose}


       12    0.229    0.019    0.229    0.019 {method 'rand' of 'mtrand.RandomState' objects}


       12    0.058    0.005    0.058    0.005 {method 'astype' of 'numpy.ndarray' objects}


       12    0.042    0.004    0.042    0.004 {method 'copy' of 'numpy.ndarray' objects}


       24    0.036    0.001    0.036    0.001 {numpy.core.multiarray.zeros}


       12    0.022    0.002    5.909    0.492 linalg.py:404(inv)


        1    0.012    0.012    6.200    6.200 ej4.py:5(<module>)


       12    0.006    0.001    6.188    0.516 ej4.py:9(Inversa)


        1    0.001    0.001    6.201    6.201 {execfile}


       12    0.000    0.000    5.851    0.488 linalg.py:244(solve)


        1    0.000    0.000    6.201    6.201 interactiveshell.py:2390(safe_execfile)


       12    0.000    0.000    0.036    0.003 numeric.py:1830(identity)


       12    0.000    0.000    5.909    0.492 defmatrix.py:808(getI)


       12    0.000    0.000    0.000    0.000 linalg.py:99(_commonType)


        1    0.000    0.000    0.000    0.000 {open}


       24    0.000    0.000    0.043    0.002 defmatrix.py:233(__new__)


       36    0.000    0.000    0.000    0.000 defmatrix.py:279(__array_finalize__)


       36    0.000    0.000    0.000    0.000 linalg.py:66(_makearray)


       36    0.000    0.000    0.000    0.000 {numpy.core.multiarray.array}


       12    0.000    0.000    0.236    0.020 linalg.py:139(_fastCopyAndTranspose)


       24    0.000    0.000    0.000    0.000 {method '__array_prepare__' of 'numpy.ndarray' objects}


       12    0.000    0.000    0.000    0.000 {method 'view' of 'numpy.ndarray' objects}


       12    0.000    0.000    0.000    0.000 linalg.py:127(_to_native_byte_order)


       75    0.000    0.000    0.000    0.000 {isinstance}


       36    0.000    0.000    0.000    0.000 numeric.py:167(asarray)


       12    0.000    0.000    0.000    0.000 defmatrix.py:55(asmatrix)


       12    0.000    0.000    0.000    0.000 {method 'transpose' of 'numpy.ndarray' objects}



 60    0.000    0.000    0.000    0.000 {issubclass}


       12    0.000    0.000    0.000    0.000 linalg.py:151(_assertRank2)


       36    0.000    0.000    0.000    0.000 linalg.py:71(isComplexType)


       12    0.000    0.000    0.000    0.000 linalg.py:157(_assertSquareness)


       24    0.000    0.000    0.000    0.000 linalg.py:84(_realType)


       36    0.000    0.000    0.000    0.000 {getattr}


       61    0.000    0.000    0.000    0.000 {len}


        1    0.000    0.000    0.000    0.000 posixpath.py:312(normpath)


        1    0.000    0.000    0.000    0.000 posixpath.py:118(dirname)


       30    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}


        1    0.000    0.000    0.000    0.000 syspathcontext.py:55(__enter__)


        1    0.000    0.000    0.000    0.000 {posix.getcwdu}


       12    0.000    0.000    0.000    0.000 {max}


       24    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}


        1    0.000    0.000    0.000    0.000 {numpy.core.multiarray.arange}


        1    0.000    0.000    6.201    6.201 py3compat.py:173(execfile)


        1    0.000    0.000    0.000    0.000 posixpath.py:341(abspath)


        1    0.000    0.000    0.000    0.000 syspathcontext.py:62(__exit__)


       12    0.000    0.000    0.000    0.000 {min}


        1    0.000    0.000    0.000    0.000 posixpath.py:60(join)


        5    0.000    0.000    0.000    0.000 {method 'startswith' of 'unicode' objects}


        1    0.000    0.000    0.000    0.000 {_codecs.utf_8_decode}


        1    0.000    0.000    6.201    6.201 <string>:1(<module>)


        1    0.000    0.000    0.000    0.000 {method 'encode' of 'unicode' objects}


        1    0.000    0.000    0.000    0.000 {method 'split' of 'unicode' objects}


        1    0.000    0.000    0.000    0.000 {method 'rfind' of 'unicode' objects}


        1    0.000    0.000    0.000    0.000 posixpath.py:249(expanduser)


        1    0.000    0.000    0.000    0.000 utf_8.py:15(decode)


        1    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}


        1    0.000    0.000    0.000    0.000 posixpath.py:51(isabs)


        1    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}


        1    0.000    0.000    0.000    0.000 {method 'rstrip' of 'unicode' objects}




        2    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}


        1    0.000    0.000    0.000    0.000 syspathcontext.py:52(__init__)


        1    0.000    0.000    0.000    0.000 {method 'join' of 'unicode' objects}


        1    0.000    0.000    0.000    0.000 {method 'endswith' of 'unicode' objects}


        1    0.000    0.000    0.000    0.000 {sys.getfilesystemencoding}


        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

```

El código lo pueden encontrar en [bitbucket](https://bitbucket.org/ecrespo/ernesto-ecrespo.blogspot/src/dbfc744caa2138355d0be1811a1edbde5379f189/line_profiler/matrizinversa.py?at=default).

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)