Title: Actualización del programa Desarrollo de interfaz gráfica para la configuración de accesos rápidos del teclado
Date: 2010-08-08 09:00
Category: Tutorial Python
Tags: Linux,  accesibilidad, gconf, glade, gnome, gtk, Linux, python, tiflotecnologia
lang: es
translation: true

En el artículo anterior se explico la mejora del script que permite cambiar las configuraciones de las teclas rápidas en gnome, ahora se explicará la mejora del programa mencionado en este [artículo](https://www.seraph.to/desarrollo-de-interfaz-grafica-para-la-configuracion-de-accesos-rapidos-de-teclado-para-gconf.html).

La captura de pantalla de la imagen muestra con respecto al artículo anterior un combobox que está deshabilitado en este momento, dicho combobox permitirá elegir entre 3 distribuciones Debian, Ubuntu o Canaima.

La imagen se muestra en la siguiente figura:

![GUI](./images/gui-gconf-gnome-2010.png)

La idea es la posibilidad de configurar los accesos rápidos de todas las aplicaciones mostradas o sólo las que se quiera.

```python
def on_button2_clicked(self,*args):
                #Se crea el objeto config de la clase Conf
                Config = configGconf.Conf()
                #Se crea un ciclo con la lista de las aplicaciones.
                for aplicacion in self.__aplicaciones:
                        #Se modifica las aplicaciones una por una pasando la aplicación.
                        Config.modificar_opcion(aplicacion,1)
```

El código completo del programa lo puedes bajar [pyconfig-accessgnome-ui.py](http://python-config-accesskey-gnome.googlecode.com/hg/pyconfig-accessgnome-ui.py) la interfaz gráfica elaborada en glade se puede bajar  de [pyconfig-accessgnome.glade](http://code.google.com/p/python-config-accesskey-gnome/source/browse/pyconfig-accessgnome.glade).

En el siguiente artículo se explicará como crear el paquete python.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)