Title: Monitorear el uso de memoria de un programa Python con memory_profiler
Date: 2013-02-02 10:00
Category: 
Tags: Canaima,Debian,General,Linux,Python,Ubuntu
lang: es
translation: true

`Memory_profiler` es un módulo Python desarrollado para monitorear el consumo de memoria de un programa Python línea por línea de cada instrucción del programa.

Para instalar el módulo se usa `easy_install` o `pip`:
```
easy_install -U memory_profiler
```
```
pip install -U memory_profiler
```
Se muestra el código del artículo sobre profiling publicado [antes](http://blog.crespo.org.ve/2012/12/profiling-de-un-script-python-con.html):
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

if __name__ == '__main__':
    #Se define una lista de  tamaños de la matriz
    tamagno = 2 ** np.arange(0, 12)
    #Se recorre la lista  y se invierte cada matriz con la
    #funcion Inversa
    for n in tamagno:
        Inversa(n)
```
Para iniciar el monitoreo se ejecuta el siguiente comando:
```python
python -m memory_profiler matrizinversa.py
```

El resultado se muestra a continuación:
```python
Filename: matrizinversa.py

Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     11.89 MB      0.00 MB   def Inversa(n):
    10     11.91 MB      0.02 MB       a = np.matrix(np.random.rand(n, n))
    11     12.10 MB      0.19 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.11 MB      0.00 MB   def Inversa(n):
    10     12.11 MB      0.00 MB       a = np.matrix(np.random.rand(n, n))
    11     12.16 MB      0.05 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.16 MB      0.00 MB   def Inversa(n):
    10     12.16 MB      0.00 MB       a = np.matrix(np.random.rand(n, n))
    11     12.16 MB      0.00 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.16 MB      0.00 MB   def Inversa(n):
    10     12.16 MB      0.00 MB       a = np.matrix(np.random.rand(n, n))
    11     12.16 MB      0.00 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.16 MB      0.00 MB   def Inversa(n):
    10     12.16 MB      0.00 MB       a = np.matrix(np.random.rand(n, n))
    11     12.16 MB      0.00 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.16 MB      0.00 MB   def Inversa(n):
    10     12.16 MB      0.00 MB       a = np.matrix(np.random.rand(n, n))
    11     12.17 MB      0.00 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.17 MB      0.00 MB   def Inversa(n):
    10     12.22 MB      0.05 MB       a = np.matrix(np.random.rand(n, n))
    11     12.35 MB      0.13 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.35 MB      0.00 MB   def Inversa(n):
    10     12.45 MB      0.09 MB       a = np.matrix(np.random.rand(n, n))
    11     12.95 MB      0.50 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.45 MB      0.00 MB   def Inversa(n):
    10     12.95 MB      0.50 MB       a = np.matrix(np.random.rand(n, n))
    11     13.54 MB      0.59 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.53 MB      0.00 MB   def Inversa(n):
    10     14.54 MB      2.00 MB       a = np.matrix(np.random.rand(n, n))
    11     16.79 MB      2.26 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.79 MB      0.00 MB   def Inversa(n):
    10     20.79 MB      8.00 MB       a = np.matrix(np.random.rand(n, n))
    11     28.88 MB      8.09 MB       return a.I

Filename: matrizinversa.py
Line #    Mem usage    Increment   Line Contents
================================================
     8                             @profile
     9     12.87 MB      0.00 MB   def Inversa(n):
    10     44.87 MB     32.00 MB       a = np.matrix(np.random.rand(n, n))
    11     77.38 MB     32.50 MB       return a.I
```

Se muestran los ciclos de ejecución de la generación de la matriz inversa del archivo `matrizinversa.py`, se representa en columna la información de la línea que se está ejecutando del programa, la cantidad de memoria utilizada, el incremento de memoria y el código que se está ejecutando.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)