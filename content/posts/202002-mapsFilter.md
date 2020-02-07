Title: Sustituir ciclos con map, filter y reduce.
Date:  2020-02-07 15:33
Category: Tutorial de Python
Tags: Python,Maps,Filter,Reduce
lang: es
translation: true
Slug: python-loops-maps-filter-reduce-2020
Authors: Ernesto Crespo
Summary: Uso de Map,Filter y Reduce


Este artículo se basa en el artículo en medium, [How To Replace Your Python For Loops with Map, Filter, and Reduce](https://medium.com/better-programming/how-to-replace-your-python-for-loops-with-map-filter-and-reduce-c1b5fa96f43a). 


El artículo tendrá 3 faces, la primera será la de mostrar la lógica de los ejemplos usando ciclos, luego se usará list comprehension y por último map, filter y reduce. 


## Ciclos 

En esta primera parte se generará una lista con 100 números (se que no es necesario un ciclo para generar está primera lista), luego a esa lista se calculará los números pares, luego se generará una lista con el cuadrado de los números generados al inicio y por último se calculará la suma total de los números de la última lista.

### Generación de números en una lista

In [1]:
```python
numeros = [] 
for i in range(0,100): 
    numeros.append(i)
print(numeros)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

Otra forma de hacerlo: 
In [2]:
```python
numeros = list(range(100))
print(numeros)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


### Filtrar números pares de la lista


In[3]: 
```python 
numeros_pares = [] 
for numero in numeros:
    if numero % 2 == 0: 
        numeros_pares.append(numero) 
print(numeros_pares)
```

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


### Calcular el cuadrado de los números pares

In[4]:
```python
numeros_pares_cuadrados = []
for numero in numeros_pares:
    numeros_pares_cuadrados.append(numero ** 2)
print(numeros_pares_cuadrados)
```

[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]

### Calcular la suma total de los números pares pares

In[5]:
```python 
# calculate total
total = 0
for numero in numeros_pares_cuadrados:
   total += numero
print(total)
```
161700


## Usando list comprehension

Ahora se repitirán los cáculos usando list comprehension en vez de ciclos. 

### Filtrar números pares de la lista


In[6]: 
```python 
numeros_pares = [numero for numero in numeros if numero % 2 == 0] 
print(numeros_pares)
```

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]


### Calcular el cuadrado de los números pares

In[7]:
```python
numeros_pares_cuadrados = [numero ** 2 for numero in numeros_pares]
print(numeros_pares_cuadrados)
```

[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]


### Calcular la suma total de los números pares pares

In[8]:
```python 
# calculate total
total = sum([numero for numero in numeros_pares_cuadrados])
print(total)
```
161700

## Usando map, filter y reduce 

### Definiciones

* map: Aplicar el mismo conjunto de pasos a cada elemento, almacenando el resultado.
map(función,lista)
* filter: aplicar criterio de validación y almacene elementos que evalúen True ese criterio.
filter(función,lista)
* reduce: devuelve un valor que se pasa de un elemento a otro.
reduce(función,lista)

Para el caso de la función que se le pasa es necesario mencionar que se usará a lambda.

Acá coloco un ejemplo sencillo de lambda que calcula la suma de dos números:
In[9]: 
```python 
suma = lambda x,y: x+y 
print(suma(1,2))
```
3

### Filtrar números pares de la lista

Se tiene un lambda que se le pasa de argumento x, y se evalua si es un número par, a filter se le pasa el lambda y la lista de números a filtrar. 

In[10]: 
```python 
numeros_pares = list(filter(lambda x: (x % 2 == 0), numeros))
print(numeros_pares)
```

[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

### Calcular el cuadrado de los números pares

En este caso se usa map, el cual se tiene un lambda que tiene de argumento x, y se calcula el cuadrado de x, a map se le pasa la lista de números pares.

In[11]:
```python
numeros_pares_cuadrados = list(map(lambda x: (x ** 2), numeros_pares))
print(numeros_pares_cuadrados)
```

[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724, 7056, 7396, 7744, 8100, 8464, 8836, 9216, 9604]

### Calcular la suma total de los números pares pares

Para este caso se tiene que importar reduce de la biblioteca functools. 

El lambda requiere un acumulador y un valor n, la cual se suman. A reduce se le pasa el lambda y la lista de números pares cuadrados.

In[12]:
```python 
from functools import reduce

total = reduce(lambda acc, n: acc + n, numeros_pares_cuadrados)
print(total)
```

161700

Como se muestra en la serie de ejemplos, puede ser innecesario, dependiendo del caso que se necesite usar for o while para crear una lista o tener un resultado de una lista, se puede usar list comprehension o filter, map  y reduce. Esto hace que pueda ser más rápido el código que se esté desarrollando.


####
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
