Title: Profiling de un script python con line_profiler
Date: 2012-12-04 9:00 
Category: Tutorial Python
Tags: General,Linux,numpy,Python,Profiling, line_profiler
lang: es
translation: true

Ahora se mostrará el uso de la herramienta `line_profiler` para hacer profiling de programas Python.

Lo primero que se tiene que hacer es instalar `line_profiler` con el comando `easy_install` o `pip`:
```
easy_install line_profiler
```
```
pip install line_profiler
```

El código que se va a revisar es el mismo del artículo anterior (matriz inversa). La diferencia es que se define en la función que genera la matriz inversa el uso del decorador profile.

El código es el siguiente:
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-


#Se importa numpy como np

import numpy as np

#Se define el uso del decorador profile. En la funcion que genera matrices inversas.

@profile

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
Para realizar el profiling se ejecuta el siguiente comando:

```python
ecrespo@jewel:~/proyectos/ernesto-ecrespo.blogspot/line_profiler$ kernprof.py -l -v  matrizinversa.py 

Wrote profile results to matrizinversa.py.lprof

Timer unit: 1e-06 s



File: matrizinversa.py

Function: Inversa at line 10

Total time: 6.05993 s



Line #      Hits         Time  Per Hit   % Time  Line Contents

==============================================================

    10                                           @profile

    11                                           def Inversa(n):

    12        12       260506  21708.8      4.3      a = np.matrix(np.random.rand(n, n))

    13        12      5799424 483285.3     95.7      return a.I
```

El resultado muestra el tiempo total de ejecución, Luego muestra cada línea de ejecución, y el porcentaje de tiempo que se ha ejecutado. Se nota que la generación de la matriz no tarda mucho, pero al invertirla si un 95,7% del tiempo de ejecución.
El significado de cada parámetro es:  

- `Line`: Es el número de línea en el archivo.
- `Hits`: Es el número de veces que la línea se ejecuta.
- `Time`: Tiempo que gasta al ejecutar cada línea.
- `Per Hit`: Tiempo promedio que se gasta al ejecutar cada línea.
- `% Time`: Porcentaje de tiempo que se gasta al ejecutar la línea relativo al tiempo que se gasta en ejecutar todas las líneas.

El código del script se encuentra en [bitbucket](https://bitbucket.org/ecrespo/ernesto-ecrespo.blogspot/src/dbfc744caa2138355d0be1811a1edbde5379f189/line_profiler/matrizinversa.py?at=default).

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV
  
O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)