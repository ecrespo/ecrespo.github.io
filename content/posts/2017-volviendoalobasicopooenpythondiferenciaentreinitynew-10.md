Title: Volviendo a lo básico, POO en Python ( diferencia entre `__init__` y `__new__`) (parte 10)
Date: 2017-02-05 09:00
Category: Tutorial Python
Tags: Python,POO
lang: es
translation: true

Continuando con la serie de [artículos volviendo a lo básico POO](https://www.seraph.to/tag/poo.html), en este artículo se toca el tema de las diferencias entre `__init__` y `__new__`.

Este artículo se baja en un artículo en [inglés entendiendo new e init](http://spyhce.com/blog/understanding-new-and-init) .

Muchos de los que han programado orientado a objetos en Python nunca han usado el método `__new__`, el que usan como constructor es el `__init__`.

La realidad es que el método `__init__` crea el objeto y luego lo inicializa, no es el constructor como tal, en cambio el método `__new__` sólo construye el objeto.

Para este artículo se trabajará con Python 3.

Se tiene la siguiente clase:

```python
class A(object):

    pass
```

Así que la Clase A hereda de object en Python 3.


Ahora se crea una clase que use `__new__` e `__init__`:

```python


class A(object):


    def __new__(cls):


        print "A.__new__ es llamado"


        return super(A, cls).__new__(cls)





    def __init__(self):


        print "A.__init__ es llamado"





A()

```


La salida es la siguiente:
```
A.__new__ es llamado
A.__init__ es llamado
```

Ahora vamos con un ejemplo donde `__init__`no será llamado:

```
class A(object):
    def __new__(cls):
        print "A.__new__ es llamado"

    def __init__(self):
        print "A.__init__ es llamado"

print ("Solo llamando el objeto A() o instanciandolo")

A()
a = A()
print ("*"*40)
print ("Ejecutando un print con el objeto A()")
print (A())

```

Como se puede ver, en el método `__init__` se está ejecutando un print y en el método `__new__` también.

La salida es la siguiente:
```
Solo llamando el objeto A() o instanciandolo
A.__new__ es llamado
A.__new__ es llamado
****************************************
Ejecutando un print con el objeto A()
A.__new__ es llamado
None
```

Como se puede ver, al llamar a A() o al instanciarlo, sólo se muestra la salida del  método `__new__` , y el de `__init__` no, sólo cuando se ejecuta el print(A()) es que devuelve la salida del método `__new__` y devuelve `None` el método `__init__`.

Ahora se mostrará la clase con sólo el método `__new__` donde se ejecuta un print y retorna un número:

```python
class A(object):

    def __new__(cls):


        print "A.__new__ es llamado"


        return 29


print ("Solo llamando al objeto")


A()


print ("*"*30)


print ("Llamando al objeto desde un print")


print A()
```

La salida es la siguiente:

Solo llamando al objeto
A.__new__ es llamado
******************************
Llamando al objeto desde un print
A.__new__ es llamado
29


Al sólo llamar al objeto sólo muestra el print, pero al ejecutar el print muestra el print del método y el entero que retorna.

Ahora se hará lo mismo pero con el método __init__:



class A(object):



    def __init__(self):

        print "A.__init__ es llamado"

        return 33





try:

    print ("Solo llamando al objeto")

    A()

except (TypeError):

    print ("Error de tipo")



La salida es la siguiente:
```
Solo llamando al objeto
A.__init__ es llamado
Error de tipo
```

En este caso el `return` devuelve `error de tipo`. La única forma que en el método `__init__` devuelva algo es que sea del tipo `None`.

Ahora se muestra el uso de una clase alternativa llamada `Ejemplo`:

```python
class Ejemplo(object):


    def __str__(self):


        return "Ejemplo"


class A(object):


    def __new__(cls):


        return Ejemplo()


class B(object):


    def __new__(cls):


        return super(B, cls).__new__(Ejemplo)


print ("Prueba con A")


print A()


print ("Prueba con B")


print B()
``` 


La salida devuelve lo siguiente:
```
Prueba con A
Ejemplo
Prueba con B
Ejemplo
```

Como puede verse, hay casos donde es útil utilizar `__new__` y otros donde se pueden seguir usando `__init__`.

El método `__new__` es usado en patrones de diseño con python, que será la siguiente serie de artículos que vendrán en este blog.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
