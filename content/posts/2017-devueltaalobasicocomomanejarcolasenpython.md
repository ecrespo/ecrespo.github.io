Title: De vuelta a lo básico, como manejar colas en python.
Date: 2017-02-24 09:00
Category: Tutorial Python
Tags: Python
lang: es
translation: true

Las estructuras de datos tipo cola son tipo FIFO (primero que entra, primero que sale).

El artículo se basa en la [documentación oficial de Python en inglés](http://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues) .
Se pueden usar las listas como una cola.

Las listas soportan las siguientes métodos:

- `list.append(x)`: agrega un elemento al final de la lista, equivalente a a[len(a):] =[x].
- `list.extend(L)`: extiende una lista al agregar todos los elementos de una lista, equivalente a a[len(a):] = L.
- `list.insert(i,x)`: Inserta un elemento en la lista en una posición dada. 
- `list.remove(x)`: Elimina el primer item x de la lista.
- `list.pop([i])`:Elimina el item en la posición dada de la lista, y lo devuelve.
- `list.clear()`: Elimina todos los elementos de la lista.
- `list.count(x)`: Retorna el número de veces que x aparece en la lista.
- `list.sort(key=None,reverse=False)`: Ordena los elementos de la lista.
- `list.reverse()`: Invierte el orden de la lista.
- `list.index(x)`: Devuelve el indice del primer elemento de la lista que sea x.
- `list.copy()`: Devuelve una copia de la lista.


Para emular una cola con una lista se tiene el siguiente ejemplo:
```python
>>> cola = [3,5,6]

>>> cola.append(8)

>>> cola

[3, 5, 6, 8]

>>> cola.pop()

8

>>> cola.append(8)

>>> cola.pop(0)

3

>>> cola.append(9)

>>> cola.pop(0)

5

>>> cola.pop(0)

6

>>> cola = [3,5,6]

>>> cola

[3, 5, 6]

>>> cola.append(9)

>>> cola

[3, 5, 6, 9]

>>> cola.append(19)

>>> cola

[3, 5, 6, 9, 19]

>>> cola.pop(0)

3

>>> cola.pop(0)

5

>>> cola

[6, 9, 19]

>>> cola.pop(0)

6

>>> cola

[9, 19]

>>> cola.pop(0)

9

>>> cola

[19]

>>> cola.pop(0)

19

>>> cola

[]

```

Se usa el método `pop` diciendo que tome siempre el primer elemento de la lista.

Esto no es eficiente así que la mejor opción es implementar una cola con `collection.deque`:

```python

>>> from collections import deque


>>> cola = deque([1,2,3,4,5])


>>> cola


deque([1, 2, 3, 4, 5])


>>> cola.append(19) #Llega 19


>>> cola


deque([1, 2, 3, 4, 5, 19])


>>> cola.append(39) #Llega 39


>>> cola


deque([1, 2, 3, 4, 5, 19, 39])


>>> cola.popleft() #Sale 1


1


>>> cola.popleft() #Sale 2


2


>>> cola


deque([3, 4, 5, 19, 39])


>>> cola.append(51) #Llega 51


>>> cola


deque([3, 4, 5, 19, 39, 51])


>>> cola.popleft() #Sale 3


3


>>> cola


deque([4, 5, 19, 39, 51])

```

En este artículo se demostró como manejar colas sólo con listas o con `collections.deque`.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
