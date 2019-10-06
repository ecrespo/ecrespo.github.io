Title: Volviendo a lo básico, POO en Python (parte 3)
Date: 2015-12-31 9:00  
Category: Tutorial Python  
Tags: Python,POO  
lang: es  
translation: true  

Continuando con algunos conceptos de POO en Python, se tienen los artículos anteriores:

1. [Volviendo a lo básico, POO en Python (parte 1)](https://www.seraph.to/volviendo-a-lo-basico-poo-en-python-parte-1.html#volviendo-a-lo-basico-poo-en-python-parte-1)
2. [Volviendo a lo básico, POO en Python (parte 2)](https://www.seraph.to/volviendo-a-lo-basico-poo-en-python-parte-2.html#volviendo-a-lo-basico-poo-en-python-parte-2)

En esté artículo se muestra el uso de  __ `getattr`__  (se ejecuta al acceder a un atributo que no existe), como obtener valores y modificar valores, y como se simplifica con el uso del decorador `@property`.

Se creará la clase Punto donde se mostrará el uso de __`getattr` __ :
```python
class Punto(object):

 def __init__(self,x=3,y=5):

  self._x = x

  self._y = y


 def __getattr__(self,attr):

  print "No se puede acceder a un atributo invalido"


if __name__ == "__main__":

 punto = Punto(5,5)

 punto.var

```

Al ejecutar el programa se tiene:
```python
$ python ej6.py
```
No se puede acceder a un atributo inválido

Al intentar acceder a un atributo no existente se ejecuta el método __ `getattr`__ donde se muestra en pantalla el mensaje no se puede acceder a un atributo inválido.

El siguiente código vuelve a mostrar la clase punto pero está vez se tienen dos métodos, uno que muestra el valor del punto y otro que modifica el valor del punto y se usará la función interna `property`.
La sintaxis de la función `property` es:  

```python
property(getter,setter,delete,doc).
```  

El código a continuación:

```python
class Punto(object):

 def __init__(self,x,y):

  self._x = x

  self._y = y



 def get_punto(self):

  return (self._x, self._y)



 def set_punto(self,punto):



  self._x, self._y = punto



 punto = property(get_punto,set_punto)





if __name__ == "__main__":

 punto = Punto(4,6)

 print(punto.punto)

 punto.punto = (10,15)

 print(punto.punto)


```


Al ejecutar el programa se tiene:
```python
$ python ej7.py
(4, 6)
(10, 15)
```

Como último ejemplo de uso de `getter` y `setter` se muestra el uso del decorador `@property`, y como simplifica el uso de `property` con respecto al código anterior:

```python

#!/usr/bin/env python3


# -*- coding: utf-8 -*-





class Punto(object):





 def __init__(self,punto):


  self._x,self._y = punto





 @property


 def punto(self):


  return (self._x,self._y)





 @punto.setter


 def punto(self,punto):


  self._x,self._y = punto








if __name__ == "__main__":


 cordenada = Punto((4,6))


 print(cordenada.punto)


 cordenada.punto = (10,15)


 print(cordenada.punto)

```



Al ejecutar el programa se tiene:
```python
$ python ej8.py
(4, 6)
(10, 15)
```
Lo primero que se hace es definir un método punto donde se retorna una tupla con el valor de x y de y, a este método se le coloca el decorador property. Luego se crea otro método llamado punto donde se toma un punto y se le asigna a x y a y pero definiendo un decorador @punto.setter el primer método hace el trabajo del getter y el segundo del setter.

Referencia:

1. [Python Avanzado](https://magmax.org/blog/2013/9/30/python-avanzado/)
2. [Ejemplos de referencia (módulos y tareas)](http://www.sromero.org/wiki/programacion/tutoriales/python/ref_ejemplos)

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
