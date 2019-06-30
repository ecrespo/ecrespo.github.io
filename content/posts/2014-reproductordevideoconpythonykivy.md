Title: Reproductor de vídeo con python y kivy  
Date: 2014-04-19 10:00  
Category: Tutorial Python  
Tags: Android,Canaima,Debian,General,gnome,Python,Ubuntu,kivy
lang: es  
translation: true  


De los dos artículos anteriores, el [introductorio con manejo de etiquetas](https://www.seraph.to/desarrollo-de-aplicaciones-multiplataforma-con-python-y-kivy.html#desarrollo-de-aplicaciones-multiplataforma-con-python-y-kivy); y 
[el de botón y scatter](https://www.seraph.to/widget-button-y-scatter-widget-de-comportamiento-en-kivy.html#widget-button-y-scatter-widget-de-comportamiento-en-kivy) ahora explicaré algo más completo, la reproducción de un vídeo.

Este artículo se basa en [inglés sobre un reproductor de vídeo y scatter con kivy](http://karanbalkar.com/2012/10/learning-kivy-video-player-and-scatter-widgets/).

Ahora se mostrará como asociar un evento (una función) al botón al darle click.

A continuación el código del reproductor:
```python
#Se importa kivy y se valida que es la versión 1.8.0

import kivy

kivy.require('1.8.0')



#Se importa la clase App

from kivy.app import App

#Se importa Button, Widget y VideoPlayer

from kivy.uix.button import Button

from kivy.uix.widget import Widget

from kivy.uix.videoplayer import VideoPlayer



#Se instancia Widget y Button.

parent= Widget()

button= Button()



#Se crea la clase MyApp que hereda de App

class MyApp(App):

    #Se define el método build.

    def build(self):

         #Se instancia Button con su texto y tamaño del  mismo.

         button = Button(text='Reproductor Video', font_size=14)

         #Se asocia al boton la función on_button_press al argumento on_press

         button.bind(on_press=on_button_press)  

         #Se agrega button a la instancia de parent

         parent.add_widget(button) #agrega el boton

         #Retorna parent 

         return parent



#Se define la función on_button_press

def on_button_press(self):

        #Se crea la instancia de VideoPlayer donde se le pasa como argumento la fuente de vídeo,

        #el estado y la opción allow_stretch True.

        video= VideoPlayer(source='Tribus-SethGodin.webm', state='play',options={'allow_stretch': True})

        #Se agrega el vídeo a la instancia parent

        parent.add_widget(video) #add videoplayer

        #Se retorna parent

        return parent

     

if __name__ == '__main__':

    MyApp().run()

```



El resultado de reproducir el script se muestra en el siguiente vídeo:

[https://youtu.be/todhoMD1jBY](https://youtu.be/todhoMD1jBY "https://youtu.be/todhoMD1jBY")

<iframe width="560" height="315" src="https://www.youtube.com/embed/todhoMD1jBY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



Nota: El vídeo del reproductor no tiene problemas con el audio, el problema generador de screencast no he logrado hacer que grabe audio :-/ ...


Si desea conocer más sobre el widget VideoPlayer puede ver el siguiente [enlace](https://kivy.org/doc/stable/api-kivy.uix.videoplayer.html#kivy.uix.videoplayer.VideoPlayer.allow_fullscreen).

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)