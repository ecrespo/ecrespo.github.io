Title: Volviendo a lo básico, POO en Python (parte 4)  
Date: 2016-10-31 09:00  
Category: Tutorial Python  
Tags: Python,POO
lang: es  
translation: true  

Los artículos anteriores sobre Programación Orientada a Objetos los pueden revisar en el [enlace](https://www.seraph.to/tag/poo.html).

En este artículo se tocará el tema de la herencia, la encapsulación, el uso de getter, setter y deleter, el uso de método estático y y classmethod.

En el artículo de la [parte 3 de POO](https://www.seraph.to/volviendo-a-lo-basico-poo-en-python-parte-3.html) se explica el uso de @property y @método.setter, falto explicar el deleter que sirve para borrar atributos del objeto.

El @staticmethod se usa cuando no se está usando el argumento self en un método.

El @classmethod define un método que se le pasa entre los argumentos a la clase (por convención se define como cls).

Se creará la clase Punto2D con los siguientes atributos y métodos:

- Se define al punto como (x,y), la clase Punto2 tiene los atributos privados (estos atributos no se pueden acceder a ellos desde la instancia de la clase, por esa razón se tiene el getter y setter):
    - self.__x
    - self.__y
- Método __init__ que le asigna los valores inciales a la instancia.
- getter, setter y deleter de punto.
- getter, setter y deleter de ValorX y ValorY.
- Método mover: Asigna nuevo valor a punto.
- Método reset: Asigna el valor (0,0) al punto. 
- Método distanciaOtroPunto: Cálcula la distancia con otro punto.

El código de `ej12.py` se muestra a continuación:

```python
#!/usr/bin/env python3

# -*- coding: utf-8 -*-


from math import sqrt


class Punto2D(object):

    """Representacion de un punto en 2 dimensiones"""

    cont_puntos = 1



    def __init__(self,punto=(0,0)):

        '''constructor del punto'''

        self.__x,self.__y = punto

        Punto2D.cont_puntos += 1



    @property

    def ValorX(self):

        '''Devuelve el valor de X'''

        return self.__x



    @ValorX.setter

    def ValorX(self,x):

        '''Se le asigna un valor  a x por medio de setter'''

        self.__x = x



    @property

    def ValorY(self):

        '''Devuelve el valor de y'''

        return self.__y



    @ValorY.setter

    def ValorY(self,y):

        '''Se le asigna un valor a y por medio del setter'''

        self.__y = y



    @property

    def punto(self):

        """el getter de punto, devuelve el punto"""

        return (self.__x,self.__y)



    @punto.setter

    def punto(self,punto):

        ''''el setter de punto'''

        self.__x,self.__y = punto



    @property

    def cantPuntos(self):

        '''Devuelve la cantidad de puntos creados'''

        return Empleado.cont_puntos



    @punto.deleter

    def punto(self):

        '''deleter de punto'''

        del self.__x

        del self.__y

        cont_puntos = 0



    def mover(self,x,y):

        '''mueve el punto a un nuevo punto'''

        self.__x, self.__y = x,y



    def reset(self):

        '''coloca en el origen al punto'''

        self.mover(0,0)



    def distanciaOtroPunto(self,oPunto):

        '''devuelve la distancia entre el punto original y un punto dado'''

        return sqrt((self.__x - oPunto.punto[0])**2 + (self.__y - oPunto.punto[1])**2 )



    @staticmethod

    def autor(autor):

        '''Se define el autor de la clase'''

        return "El autor de esta clase es: {}".format(autor)



    @classmethod

    def cantidadPuntos(cls,cantidad):

        '''Se cambia la cantidad de puntos'''

        cls.cont_puntos = cantidad



if __name__ == "__main__":

    #Se crea cordenada de la clase Punto2D donde se le pasa (4,6)

    cordenada = Punto2D((4,6))

    #Se muestra el valor del punto.

    print(cordenada.punto)

    #Se asigna por setter un nuevo valor

    cordenada.punto = (10,15)

    #Se muestra el nuevo valor de cordenada

    print(cordenada.punto)

    #Se calcula la distancia con respecto a otro punto.

    print(cordenada.distanciaOtroPunto(Punto2D((100,100))))

    #Se fija el punto en un valor (0,0)

    cordenada.reset()

    #Se muestra el nuevo valor de la cordenada.

    print (cordenada.punto)

    #Se muestra un mensaje pasando el autor de la clase.

    print (cordenada.autor("Ernesto"))

    #Muestra la cantidad de puntos que se han creado.

    print ('Cantidad de puntos : {0}'.format(cordenada.cont_puntos ))

    #Se modifica la cantidad de puntos a 1 por medio de setter.

    Punto2D.cantidadPuntos(1)

    #Se vuelve a mostrar la cantida de puntos.

    print ('Cantidad de puntos : {0}'.format(cordenada.cont_puntos ))

    #Se borra la instancia cordenada.

    del(cordenada)

    #Se intenta mostrar el punto pero va a devolver que no se puede

    try:

        print (cordenada.punto)

    except (NameError):

        print ("No existe el objeto cordenada")
``` 

Al ejecutar `ej12.py` se tiene lo siguiente:
```python
python ej12.py
(4, 6)
(10, 15)
123.794184031
(0, 0)
El autor de esta clase es: Ernesto
Cantidad de puntos : 3
Cantidad de puntos : 1
No existe el objeto cordenada

```

Ahora se va a crear `ej12_3d.py` que tendrá la clase Punto3D que hereda de Punto2D.

La clase Punto3D tiene practicamente los mismos métodos, lo único distinto es que ahora maneja un punto con 3 dimensiones, para ello hereda del punto en 2 dimensiones X y Y y maneja Z. 

Así que se sobrecarga los métodos de Punto2D en Punto3D. Para poder acceder al objeto Punto2D se usa super. 

A continuación el código de `ej12_3d.py`:

```python
#!/usr/bin/env python3


# -*- coding: utf-8 -*-





#Se importa la clase Punto2D de ej12.py


from ej12 import Punto2D


#Se importa raiz cuadrada


from math import sqrt





class Punto3D(Punto2D):


    '''Se define la clase Punto3D'''





    def __init__(self,punto3d):


        '''Método init donde se le asigna x y y a Punto2D por medio de super'''


        super(Punto3D,self).__init__(punto3d[0:-1])


        self.__z = punto3d[-1]





    @property


    def ValorZ(self):


        '''devuelve el valor de z por medio de getter'''


        return self.__z





    @ValorZ.setter


    def ValorZ(self,z):


        '''Se asigna un valor a z por medio de setter'''


        self.__z = z





    @ValorZ.deleter


    def ValorZ(self):


        '''se borra el valor de z por medio de deleter'''


        del (self.__z)





    @property


    def punto(self):


        '''el getter de punto, devuelve el punto'''


        x,y = super(Punto3D,self).punto


        return (x,y,self.ValorZ)





    @punto.setter


    def punto(self,punto3d):


        '''Se le asigna un valor al punto por medio de setter'''


        super(Punto3D,self).mover(punto3d[0],punto3d[1])


        self.__z = punto3d[-1]





    @punto.deleter


    def punto(self):


        '''Se borra el punto por medio de deleter'''


        print ("Punto borrado")


        del Punto2D


        del self.__z





    def mover(self,x,y,z):


        '''Se asigna un nuevo valor al punto''''


        super(Punto3D,self).mover(x,y)


        self.__z = z





    def reset(self):


        '''Se fija el punto como (0,0,0)'''


        super(Punto3D,self).mover(0,0)


        self.__z = 0





    def distanciaOtroPunto(self,oPunto):


        '''devuelve la distancia entre el punto original y un punto dado'''


        x,y = super(Punto3D,self).punto


        z = self.__z


        return sqrt((x - oPunto.punto[0])**2 + (y - oPunto.punto[1])**2 + (z - oPunto.ValorZ) ** 2 )


if __name__ == '__main__':


    #Se crea la instancia Punto3D con el punto.


    punto3d = Punto3D((4,6,4))


    #Se muestra el valor del punto


    print(punto3d.punto)


    #Se asigna un nuevo valor a punto.


    punto3d.punto = (3,3,3)


    #Se muestra dicho valor


    print(punto3d.punto)


    #Se muestra los valores de x,y y z.


    print(punto3d.ValorX)


    print(punto3d.ValorY)


    print(punto3d.ValorZ)


    #Se asigna el valor (0,0,0)


    punto3d.reset()


    #Se muestra su valor.


    print(punto3d.punto)


    #Se calcula la distancia con otro punto.


    print(punto3d.distanciaOtroPunto(Punto3D((15,45,55))))


    #Se borra el punto3d.


    del(punto3d)


    #Se intenta mostrar el valor o devuelve que el objeto no existe.


    try:


        print (punto3d.punto)


    except (NameError):


        print ("No existe el objeto punto3d")

```

Al ejecutar `ej12_3d.py` se obtiene lo siguiente:
```python
python ej12_3d.py
(4, 6, 4)
(3, 3, 3)
3
3
3
(0, 0, 0)
72.6291952317
No existe el objeto punto3d
```


En este artículo se muestra la encapsulación, la herencia y varios métodos.

Los códigos lo pueden encontrar en gitlab tanto para [ej12.py](https://gitlab.com/ecrespo/tutorial-poo/blob/master/ej12.py) como para [ej12_3d.py](https://gitlab.com/ecrespo/tutorial-poo/blob/master/ej12_3d.py).

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)



