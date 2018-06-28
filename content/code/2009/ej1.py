#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk, gtk.glade, inspect, sys
class ej1:
    def __init__(self):
        self.w_tree = gtk.glade.XML('ej1.glade')
        self.ventana =  self.w_tree.get_widget('ventana')
        self.etiqueta = self.w_tree.get_widget('etiqueta1')
        print self.etiqueta.get()
        self.etiqueta.set_text("Hola mundo")
        self.w_tree.signal_autoconnect(dict(inspect.getmembers(self)))
    def on_ventana_destroy(self,*args):
        gtk.main_quit()
    def main(self,*args):
        self.ventana.show()
        gtk.main()
if __name__ == "__main__":
    app = ej1()
    app.main()
