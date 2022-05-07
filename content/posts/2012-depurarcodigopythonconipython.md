Title: Depurar código python con ipython.
Date: 2012-12-06 9:00
Category: Tutorial Python
Tags: General,Linux,numpy,python,ipython
lang: es
translation: true

En los 3 artículos anteriores se explicó como realizar profiling con 3 herramientas (timeit, line_profiler y cProfile). Ahora se explicará como depurar código python.

En este caso se explicará la depuración de código utilizando `ipython`.
`ipython` aparte de permitir hacer profiling también permite realizar depuración de código.

Se mostrará el código de la generación de un arreglo, luego se muestra en pantalla el arreglo, el valor de un elemento de ese arreglo y el recorrido de los elementos del arreglo:

```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

#Se importa numpy como np

import numpy as np

a = np.arange(10)

print a

print a[8]

print a[9]

for i in a:

    print i

print a[10]
```

El resultado de ejecutar el script es el siguiente:

```
ecrespo@jewel:~/proyectos/ernesto-ecrespo.blogspot/debugipython$ python arreglo.py 

[0 1 2 3 4 5 6 7 8 9]

8

9

0

1

2

3

4

5

6

7

8

9

Traceback (most recent call last):

  File "arreglo.py", line 17, in <module>

    print a[10]

IndexError: index out of bounds
```


Se muestra el mensaje de error de tratar de presentar en pantalla el valor del elemento 10 del arreglo a (que no existe).

Se ejecuta a continuación `ipython` desde la consola Linux, ipython entra en un interprete interactivo, ahí se ejecuta el comando `%run script.py`. Esto hace que se inicie el modo depuración con el script que se pasa como argumento:

```python
ecrespo@jewel:~/proyectos/ernesto-ecrespo.blogspot/debugipython$ ipython

Python 2.7.3rc2 (default, Apr 22 2012, 22:35:38) 

Type "copyright", "credits" or "license" for more information.



IPython 0.13.1 -- An enhanced Interactive Python.

?         -> Introduction and overview of IPython's features.

%quickref -> Quick reference.

help      -> Python's own help system.

object?   -> Details about 'object', use 'object??' for extra details.



In [1]: %run arreglo.py

[0 1 2 3 4 5 6 7 8 9]

8

9

0

1

2

3

4

5

6

7

8

9



---------------------------------------------------------------------------


IndexError                                Traceback (most recent call last)


/usr/lib/python2.7/dist-packages/IPython/utils/py3compat.pyc in execfile(fname, *where)


    176             else:


    177                 filename = fname


--> 178             __builtin__.execfile(filename, *where)





/home/ecrespo/proyectos/ernesto-ecrespo.blogspot/debugipython/arreglo.py in <module>()


     15     print i


     16 


---> 17 print a[10]





IndexError: index out of bounds

```

El resultado es la ejecución del script y señala la sección donde se tiene el error.

Ahora se ejecuta el comando `%debug`:
```python
In [2]: %debug
> /home/ecrespo/proyectos/ernesto-ecrespo.blogspot/debugipython/arreglo.py(17)<module>()
     15     print i
     16 
---> 17 print a[10]
```
Se ve claramente que el error se encuentra en la línea 17 del script, donde se trata de mostrar en pantalla el elemento 10 del arreglo el cual no existe.

Se puede listar el código al ejecutar el comando `list`:
```python
ipdb> list
     12 print a[9]
     13 
     14 for i in a:
     15     print i
     16 
---> 17 print a[10]
```
Evaluar código. Se puede ejecutar una instrucción python para evaluar el tamaño del arreglo.
```python
ipdb> len(a)
10
```
Se muestra en pantalla el valor de a:
```python
ipdb> print a
[0 1 2 3 4 5 6 7 8 9]
```
Ver las llamadas del stack:Es un stack que contiene información acerca de las funciones activas de un programa en ejecución. El comando para ver el stack es bt:

```python
ipdb> bt

  /usr/lib/python2.7/dist-packages/IPython/utils/py3compat.py(178)execfile()


    174             if isinstance(fname, unicode):


    175                 filename = fname.encode(sys.getfilesystemencoding())


    176             else:


    177                 filename = fname


--> 178             __builtin__.execfile(filename, *where)





> /home/ecrespo/proyectos/ernesto-ecrespo.blogspot/debugipython/arreglo.py(17)<module>()


     13 


     14 for i in a:


     15     print i


     16 


---> 17 print a[10]



Moverse hacia arriba en el stack se logra al ejecutar el comando `u`:
```python
ipdb> u
> /usr/lib/python2.7/dist-packages/IPython/utils/py3compat.py(178)execfile()
    176             else:
    177                 filename = fname
--> 178             __builtin__.execfile(filename, *where)

Para moverse hacia abajo en el stack se logra al ejecutar el comando d:
ipdb> d
> /home/ecrespo/proyectos/ernesto-ecrespo.blogspot/debugipython/arreglo.py(17)<module>()
     15     print i
     16 
---> 17 print a[10]
```


Para salirse del modo depuración se ejecuta el comando `exit`, para salirse del interprete de comandos `ipython` se vuelve a ejectuar `exit`.

Se tiene claro que el error en el script se encuentra en la línea 17, donde se trata de imprimir en pantalla un elemento del arreglo que no existe.

De esta forma se puede realizar depuración de código python con `ipython`. 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)