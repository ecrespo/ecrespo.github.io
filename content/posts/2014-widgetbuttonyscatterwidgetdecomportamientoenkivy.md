Title: Widget button y Scatter (widget de comportamiento) en kivy.  
Date: 2014-04-19 08:00  
Category: Tutorial Python  
Tags: Canaima,Debian,General,gnome,Python,Ubuntu,kivy  
lang: es  
translation: true  


El [artículo anterior](https://www.seraph.to/desarrollo-de-aplicaciones-multiplataforma-con-python-y-kivy.html#desarrollo-de-aplicaciones-multiplataforma-con-python-y-kivy) se mostró una pequeña introducción de kivy y como tener una ventana con una etiqueta.

También se mostró como separar el layaout de la programación.
A continuación se mostrará dos ejemplos, uno utilizando el widget button y otro con una etiqueta dentro de un Scatter (widget de comportamiento que permite drag, rotar y escalar un widget).
El artículo se basa del [vídeo tutorial No.1](https://www.youtube.com/watch?v=F7UKmK9eQLY) del equipo de kivy:

El código python del ejemplo del botón se muestra a continuación:
```python
#!/usr/bin/env python

#Se importa kivy

import kivy

#Se valida que se tiene la versión 1.8.0 de kivy

kivy.require('1.8.0')



#Se importa la clase App y el widget Button

from kivy.app import App

from kivy.uix.button import Button



#Se crea la clase Hola3App que hereda de App

class Hola3App(App):

    #Se define el método build que devuelve el widget Button sin argumentos.

    def build(self):

        return Button()





if __name__ == "__main__":

    #Se crea la instancia de la clase y se ejecuta.

    Hola3App().run()
```
El archivo `hola3.kv` con el layout de `hola3.py` se muestra a continuación:
Se define el texto del botón, el color será azul y su tamaño.
```python
# File name: hello2.kv

#:kivy 1.8.0

<Button>: 

  text: 'Hola mundo v3!'

  font_size:100

  background_color:(0,0,1,1)

```

El siguiente vídeo muestra la ejecución del script:

[https://youtu.be/gFk4w-p4qhc](https://youtu.be/gFk4w-p4qhc "https://youtu.be/gFk4w-p4qhc")


El siguiente ejemplo es del uso del widget de comportamiento Scatter, este widget permite realizar drag, cambiar de escala de lo que contenga el widget y rotar, aparte es un wiget que soporta multitouch.

El código de ´hola4.py´ se muestra a continuación:
```python
#!/usr/bin/env python

#se importa kivy

import kivy

#Se válida que la versión de kivy sea la 1.8.0

kivy.require('1.8.0')



#Se importa la clase App

from kivy.app import App

#Se importa Scatter, Label y FloatLayout

from kivy.uix.scatter import Scatter

from kivy.uix.label import Label

from kivy.uix.floatlayout import FloatLayout





#Se crea la clase Hola4App que hereda de App

class Hola4App(App):

    #Se define el método build

    def build(self):

        #Se instancia al objeto FloatLayout

        f = FloatLayout()

        #Se instancia al objeto Scatter

        s = Scatter()

        #Se instancia al objeto Label con el texto y el tamaño.

        l = Label(text="Hola v4",font_size=100)

        #Se agrega a FloatLayout la instancia del widget scatter

        f.add_widget(s)

        #Se agrega el widget Label a Scatter

        s.add_widget(l)

        #Se retorna la instancia de FloatLayout

        return f





if __name__ == "__main__":

    #Se ejecuta run de la instancia del objeto Hola4App 

    Hola4App().run()

```

El siguiente vídeo muestra el resultado de la ejecución del script:

[https://youtu.be/_AeT3LkVwkk](https://youtu.be/_AeT3LkVwkk "https://youtu.be/_AeT3LkVwkk")

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)