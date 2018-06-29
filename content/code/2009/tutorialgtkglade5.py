#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importación de módulos
import pygtk
pygtk.require('2.0')
import gtk, gtk.glade, inspect, sys
#Creación de la clase ej8
class ej8:
    #Creación del método constructor de la clase.
    def __init__(self):
        #Se captura el archivo xml de la interfaz
        self.w_tree = gtk.glade.XML('ej8.glade')
        #Se asocia la ventana1
        self.ventana1 = self.w_tree.get_widget('ventana1')
        #Se asocia el widget textview1
        self.textview1 = self.w_tree.get_widget('textview1')
        #Se asocia el widget de la selección de archivo
        self.seleccionararchivo = self.w_tree.get_widget('seleccionararchivo')
        #Se asocia el boton salir
        self.botonsalir = self.w_tree.get_widget('botonsalir')
        #Se asocia los eventos con las señales
        self.w_tree.signal_autoconnect(dict(inspect.getmembers(self)))
        #Se asocia el objeto buffer de texto
        self.buffertexto = gtk.TextBuffer()
        #Se crea una lista vacía
        self.lista = []
        #Se crea la variable que contendrá el nombre del archivo seleccionado
        self.archivo_name = ""
    #Se crea el método de selección de archivo
    def on_seleccionararchivo_file_set(self,*args):
        #Se captura el nombre del archivo en la variable
        self.archivo_name = self.seleccionararchivo.get_filename()
        #Se abre el archivo colocando su contenido en una lista
        self.lista = open(self.archivo_name,"r").readlines()
        #Se recorre la lista y se coloca el contenido en el buffer de texto
        for i in range(len(self.lista)):
            self.buffertexto.insert_at_cursor(self.lista[i])
        #Se coloca el contenido del buffer en el textview
        self.textview1.set_buffer(self.buffertexto)
        #Se oculta la ventana de selección de archivo
        self.seleccionararchivo.hide()

    #Se crea el método para el boton salir
    def on_botonsalir_clicked(self,*args):
        gtk.main_quit()

    #Se crea el método para cerrar la aplicación
    def on_ventana1_destroy(self,*args):
        gtk.main_quit()

    #Se crea el método main que muestra la ventana
    def main(self,*args):
        self.ventana1.show()
        gtk.main()

if __name__ == "__main__":
    app = ej8()
    app.main()
