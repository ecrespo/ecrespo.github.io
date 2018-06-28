#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk, gtk.glade, inspect, sys

class ej3:
    def __init__(self):
        #Se captura el archivo glade
        self.w_tree = gtk.glade.XML('ej3.glade')
       #Se asocian los widgets ventana, etiqueta1, etiqueta2, entrada, boton1 y     #boton2 a unas variables del objeto
        self.ventana = self.w_tree.get_widget('ventana')
        self.etiqueta1 = self.w_tree.get_widget('etiqueta1')
        self.etiqueta2 = self.w_tree.get_widget('etiqueta2')
        self.entrada = self.w_tree.get_widget('entrada')
        self.b_capturar = self.w_tree.get_widget('boton1')
        self.b_salir = self.w_tree.get_widget('boton2')
        #Se asocia las señales de los widgets con funciones.
        self.w_tree.signal_autoconnect(dict(inspect.getmembers(self)))
        self.texto = ""

    #Se define la función salir del boton2
    def on_boton2(self,*args):
        gtk.main_quit()
    #Se define capturar el texto y presentarlo en la etiqueta2 al presionar el boton2
    def on_boton1(self,*args):
        print self.entrada.get_text()
        self.etiqueta2.set_text("Hola Sr. %s" %self.entrada.get_text())
    #Se finaliza la aplicación al darle clip en cerrar ventana.
    def on_ventana_destroy(self,*args):
        gtk.main_quit()

     #Se muestra la ventana
    def main(self,*args):
        self.ventana.show()
        gtk.main()


if __name__ == "__main__":
    app = ej3()
    app.main()
    
