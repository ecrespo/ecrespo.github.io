#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk, gtk.glade, inspect, sys

class ej5:
    def __init__(self):
        #Se captura el archivo de la interfaz glade
        self.w_tree = gtk.glade.XML('ej5.glade')
        #Se asocian los widgets ventana1, etiqueta2, entrada, boton1, boton2
        #ventana1, boton3 y boton4
        self.ventana1 = self.w_tree.get_widget('ventana1')
        self.etiqueta2 = self.w_tree.get_widget('etiqueta2')
        self.entrada = self.w_tree.get_widget("entrada")
        self.b_capturar = self.w_tree.get_widget('boton1')
        self.b_salir = self.w_tree.get_widget('boton2')
        self.ventana2 =self.w_tree.get_widget("ventana2")
        self.baceptar = self.w_tree.get_widget("boton3")
        self.bsalir = self.w_tree.get_widget("boton4")
        #Se asocian las señales con los métodos
        self.w_tree.signal_autoconnect(dict(inspect.getmembers(self)))
        #Se define la variable texto en blanco.
        self.texto = ""
    #El método del boton2 salir, al darle clip se cierra la aplicación
    def on_boton2_clicked(self,*args):
        gtk.main_quit()
    #El boton1 es para capturar el texto y luego se muestra la ventana2
    def on_boton1_clicked(self,*args):
        self.texto = self.entrada.get_text()
        self.ventana2.show()

    #El boton3 es el boton que acepta la captura de texto, se hace esto y se le
    #pasa el texto a la etiqueta2, se cierra la ventan2.
    def on_boton3_clicked(self,*args):
        self.etiqueta2.set_text(self.texto)
        self.ventana2.hide()
    #Se cierra la ventana2
    def on_boton4_clicked(self,*args):
        self.ventana2.hide()
    #Al presionar cerrar la ventana1 se cierra la aplicación
    def on_ventana1_destroy(self,*args):
        gtk.main_quit()
    #Al presionar cerrar la ventana2 se oculta la misma
    def on_ventana2_destroy(self,*args):
        self.ventana2.hide()
    #Se muestra la ventana1 y se oculta la ventana 2 al iniciar el programa.
    def main(self,*args):
        self.ventana2.hide()
        self.ventana1.show()
        gtk.main()

if __name__ == "__main__":
    app = ej5()
    app.main()
