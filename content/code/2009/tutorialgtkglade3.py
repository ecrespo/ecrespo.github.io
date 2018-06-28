#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygtk
pygtk.require('2.0')
import gtk, gtk.glade, inspect, sys
class ej4:
    def __init__(self):
        #Se captura el archivo glade
        self.w_tree = gtk.glade.XML('ej4.glade')
        #Se capturan los widgets ventana, etiqueta3, combo1, combo2
        #boton1 y boton2.
        self.ventana = self.w_tree.get_widget('ventana')
        self.etiqueta3 = self.w_tree.get_widget('etiqueta3')
        self.combo1 = self.w_tree.get_widget('combo1')
        self.combo2 = self.w_tree.get_widget('combo2')
        self.b_capturar = self.w_tree.get_widget('boton1')
        self.b_salir = self.w_tree.get_widget('boton2')
        #Se asocian las señales de la interfaz con los métodos de la aplicación.
        self.w_tree.signal_autoconnect(dict(inspect.getmembers(self)))
        #Se crea el diccionario donde se manejan los países con sus ciudades
        self.listado = {'Venezuela': ['Caracas',
                                    'Valencia',
                                    'Barquisimeto',
                                    'Merida'],
                        'Argentina':['Buenos Aires',
                                    'Tucuman',
                                    'Mar del Plata'],
                        'Escocia':['Edimburgo','Glasgow']}
        #Se crea una lista vacía donde se maneja la ciudad antigua.
        self.ciudades_old = []
    #Método asociado al cambio del combo1
    def on_combo1_changed (self,*args):
        #Se captura el país para asociarlo a la ciudad
        ciudades = self.listado[self.combo1.get_active_text()]
        #Si el combo2 está activo se revisa las ciudades para ver si es de la lista de
        #países
        if self.combo2.get_active() == -1:
            self.ciudades_old = ciudades
            for ciudad in ciudades:
                self.combo2.append_text(ciudad)
        else:
            #Si no es de la lista de ciudades del país se remueve y se agrega la
            # nueva lista
            for i in range(1,len(self.ciudades_old)+1): self.combo2.remove_text(1)
            self.ciudades_old = ciudades
            for ciudad in ciudades: self.combo2.append_text(ciudad)
    #Si cambia el combo2 no se hace nada
    def on_combo2_changed (self, *args):
        pass
    #Si se le da clip al boton salir se cierra la aplicación
    def on_boton2(self,*args):
        gtk.main_quit()
    #Si se le da clip el boton aceptar, se captura los datos de los combos
    #y se presenta en la etiqueta
    def on_boton1(self,*args):
        self.etiqueta3.set_text("Pais : %s, Ciudad: %s" %(self.combo1.get_active_text(),
                                                        self.combo2.get_active_text()))
    #Si se le da clip a cerrar se sale de la aplicación
    def on_ventana_destroy(self,*args):
        gtk.main_quit()
    #Se muestra la ventana
    def main(self,*args):
        self.ventana.show()
        gtk.main()
if __name__ == "__main__":
    app = ej4()
    app.main()
