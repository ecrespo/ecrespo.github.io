Title: Estructura de datos en Python (Lista Enlazada)
Date: 2017-03-11 09:00
Category: Tutorial Python
Tags: General,Python
lang: es
translation: true

Continuando con la serie de estructuras de datos, en el artículo anterior se trato de la [estructura de datos Nodo](https://www.seraph.to/estructura-de-datos-en-python-nodo.html), en este artículo se usará el Nodo por medio de composición en la lista enlazada.

Este artículo se basa del tutorial en youtube llamado [Python:Linked Lists](http://www.youtube.com/watch?v=Ast5sKQXxEU) donde pasan el enlace al [código en github](http://github.com/joeyajames/Python/blob/master/LinkedLists.py).

<iframe width="560" height="315" src="https://www.youtube.com/embed/Ast5sKQXxEU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

La lista enlazada se basa en el `Nodo`, como recordarán el Nodo tiene el dato y lo que apunta al próximo nodo.  En el caso de la lista enlazada contendrá lo siguiente:

- Argumentos:
    - Nodo: Al crear la lista enlazada se crea un Nodo sin datos y que apunte a None.
     - primero: variable privada que apunta al primer nodo.
     -  ultimo: variable privada que apunta al último nodo.
     -  tamagno: variable privada que lleva la cantidad de nodos que maneja la lista.
- Métodos:
    - obtenerTamagno: Devuelve el tamaño de la lista.
    - add: Agrega un nodo a la lista enlazada.
    - remove: Remueve un nodo de la lista enlazada.
    - find:Busca un dato en la lista, devuelve el dato o False.



El código de la lista enlazada se muestra a continuación:

```python
#!/usr/bin/env python3

#Se importa Nodo de nodos.

from nodos import Nodo


class ListaEnlazada(object):

    def __init__(self,primero = Nodo(None,None)):

        """Se asigna como Nodo inicial a primero y ultimo por que apuntan al mismo nodo

        y se define el tamagno de la lista en cero"""

        self.__primero = primero 

        self.__ultimo = self.__primero

        self.__tamagno = 0





    def obtenerTamagno(self):

        """Devuelve el tamagno de la lista"""

        return self.__tamagno



    def add(self,d):

        """Agrega un nodo a la lista enlazada"""

        #Se crea una instancia de nodo donde se le pasa el dato d y se coloca

        #como proximo nodo el primer nodo.

        nodoNuevo = Nodo(d,self.__primero)

        #El primer nodo apunta al nodo nuevo y se incrementa el tamagno.

        self.__primero = nodoNuevo

        self.__tamagno += 1





    def remove(self,d):

        """Se elimina el nodo que tenga el dato d"""

        #Al nodo actual se le asigna el primer nodo

        nodoActual = self.__primero

        #Y al nodo anterior se le asigna None.

        nodoAnterior = None



        #Mientras exista el nodo actual-

        while nodoActual:

            #Si el dato de nodo actual es igual al dato que se esta buscando.

            if nodoActual.dato == d:

                #Si existe nodo anterior

                if nodoAnterior:

                    #Se asigna  al apuntador proximo del nodo anterior el proximo de nodo actual

                    nodoAnterior.proximo = nodoActual.proximo

                else: 

                    #A primero se le asigna el apuntador al proximo nodo del nodo actual

                    self.__primero = nodoActual.proximo

                #En cualquiera de los dos casos se decrementa el tamagno de la lista.

                self.__tamagno -= 1

                #Devuelve True por que se elimino.

                return True

            else:

                #Se asigna al nodo anterior el nodo actual

                nodoAnterior = nodoActual

                #Se asigna al nodo actual, el nodo proximo del nodo actual

                nodoActual = nodoActual.proximo





    def find(self,d):

        """Se busca d en la lista enlazada, si existe devuelve d, si no devuelve None"""

        #a nodo actual se le asigna el primer nodo.

        nodoActual = self.__primero

        #Mientras exista el nodo actual.

        while nodoActual:

            #Si el dato de nodo actual es igual a d, devuelve d

            if nodoActual.dato == d:

                return d

            else:

                #Si no, el nodo actual apunta al proximo nodo.

                nodoActual = nodoActual.proximo

        #Si no se encuentra devuelve None.

        return None 







if __name__ == '__main__':

    miLista = ListaEnlazada()

    miLista.add(1)

    miLista.add(8)

    miLista.add(12)

    print("size: {0}".format(miLista.obtenerTamagno()))

    print (miLista.find(8))

    miLista.remove(8)

    print("size: {0}".format(miLista.obtenerTamagno()))

    print(miLista.remove(12))

    print("size:{0} ".format(miLista.obtenerTamagno()))

    print(miLista.find(5))

```

Al ejecutar el script se tiene lo siguiente:
```
python listas.py 
size: 3
8
size: 2
True
size: 1
None
```

Como se puede ver se agregan 3 elementos a la lista, luego se muestra el tamaño de la lista, se va eliminando cada elemento de la lista, donde se muestra el `tamagno` de la lista mientras se van eliminando elementos, y por último se busca el valor de 5 en la lista donde devuelve `None`. 



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
