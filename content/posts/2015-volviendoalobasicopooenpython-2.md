Title: Volviendo a lo básico, POO en Python (parte 2)
Date: 2015-12-25 9:00
Category: Tutorial Python  
Tags: Python
lang: es
translation: true

Continuando con la serie de artículos sobre programación orientada objetos con python, les dejo el enlace del [primer artículo](https://www.seraph.to/volviendo-a-lo-basico-poo-en-python-parte-1.html#volviendo-a-lo-basico-poo-en-python-parte-1).

El siguiente artículo se basa en un artículo de un blog publicado en [www.toptal.com](https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide).

En el artículo anterior se muestra las variables id_ciudad y cont_ciudad como atributos de la clase. Se mostrará con el siguiente ejemplo que no siempre es bueno usar atributos de una clase, que se rompe la norma de encapsulación de la POO.

```python

#!/usr/bin/env python3


# -*- coding: utf-8 -*-



class Servicio(object):


 dato = []



 def __init__(self,otro_dato):


  self.otro_dato = otro_dato



if __name__ == "__main__":


 s1 = Servicio(["a","b"])


 s2 = Servicio(["c","d"])


 s1.dato.append(1)


 print "dato de S1: ",s1.dato


 print "dato de S2: ",s2.dato


 s2.dato.append(2)


 print "dato de s1: ",s1.dato


 print "dato de s2: ",s2.dato


 print "otro dato de s1: ", s1.otro_dato


 print "otro dato de s2: ", s2.otro_dato

```


Al ejecutar el código se tiene:

```python
dato de S1:  [1]


dato de S2:  [1]


dato de s1:  [1, 2]


dato de s2:  [1, 2]


otro dato de s1:  ['a', 'b']


otro dato de s2:  ['c', 'd']
```


En las 4 primeras líneas de la ejecución muestrán que la instancia s1 y la instancia s2 practicamente tienen el mismo valor a pesar de que se agrega el dato en s1 y se refleja en s2, luego se agrega el dato en s2 y se refleja en s1.

En el artículo en inglés mencionan que la solución sería no tener una lista vacía como instancia de la clase si no colocar None.

A continuación el código:

```python
#!/usr/bin/env python3


# -*- coding: utf-8 -*-


class Servicio(object):


 dato = None





 def __init__(self,otro_dato):


  self.otro_dato = otro_dato





if __name__ == "__main__":


 s1 = Servicio(["a","b"])


 s2 = Servicio(["c","d"])


 s1.dato = 1


 print "dato de S1: ",s1.dato


 print "dato de S2: ",s2.dato


 s2.dato = 2


 print "dato de s1: ",s1.dato


 print "dato de s2: ",s2.dato

```



El resultado de la ejecución es el siguiente:

```python
dato de S1:  1


dato de S2:  None


dato de s1:  1


dato de s2:  2

```

Como se ve ya no muestra valores iguales entre las dos instancias de la clase.

Ahora muestro el código sin la instancia de la clase, creando dato como una variable privada y unos métodos que acceden a dato:

```python

#!/usr/bin/env python3


# -*- coding: utf-8 -*-


class Servicio(object):


 def __init__(self,otro_dato):


  self.__dato = []


  self.otro_dato = otro_dato





 def mostrar_dato(self):


  return self.__dato





 def agregar_dato(self,dato):


  self.__dato.append(dato)





 def inicializar_dato(self,):


  self.__dato = []





if __name__ == "__main__":


 s1 = Servicio(["a","b"])


 s2 = Servicio(["c","d"])


 try:


  s1.dato.append(1)


 except AttributeError:


  print "No se pudo agregar a dato de s1"


 finally:


  print s1.mostrar_dato()


  print s2.mostrar_dato()


  s1.agregar_dato(1)


  s1.agregar_dato(3)


  s2.agregar_dato(2)


  s2.agregar_dato(4)


  print s1.mostrar_dato()


  print s2.mostrar_dato()


```

Al ejecutar el script se tiene lo siguiente:

```python

No se pudo agregar a dato de s1


[]


[]


[1, 3]


[2, 4]


```

No es un error crear atributos de una instancia lo que se tiene que saber es exactamente que lo que se necesita en la clase para evitar estos errores, y lo mejor es seguir el paradigma de programación orientada a objetos.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
