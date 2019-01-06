Title: Script en python que configura los accesos rápidos de teclado a aplicaciones en gnome con gconf
Date: 2009-12-12 19:00
Category: Tutorial Python
Tags: Linux, accesibilidad, gconf, gnome, python
lang: es
translation: true

El script lo pueden bajar de [googlecode](http://code.google.com/p/python-config-accesskey-gnome/source/browse/pyconfig-accessgnome.py).

Este programa tiene su ayuda:

```
./pyconfig-accessgnome.py --help
pyconfig-orca options
option : --help : Print this help
option : --list : List gconf for gnome-orca
option : --all : add all config access key in gconf
option : --nautilus : add gconf access key to nautilus
option : --gnome-terminal : add gconf access key to gnome-terminal
option : --oowriter : add gconf access key to oowriter
option : --pidgin : add gconf access key to pidgin
option : --gedit : add gconf access key to gedit
option : --gnome-calculator : add gconf access key to gnome-calculator
option : --ooimpress : add gconf access key to ooimpress
option : --oocalc : add gconf access key to oocalc
option : --rhythmbox : add gconf access key to rhythmbox
option : --orca : add gconf access key to orca
option : --iceweasel : add gconf access key to iceweasel
```
La opción --all permite configurar todas las opciones de una vez, también se puede configurar unas aplicaciones nada más.

```
./pyconfig-accessgnome.py --all
./pyconfig-accessgnome.py --pidgin --orca --iceweasel
```



```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Name: pyconfig-accessgnome
Description: Aplicación y módulo que permite modificar los accesos rápido de teclas a programas
Version:0.2
License: GPLv3
Copyright: Copyright (C) 2009  Libre Accesibilidad
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
Changelog:
 * Agregada multiples opciones de configuración

"""

import gconf


class Conf:
    def __init__(self):
        self.gconfClient = gconf.client_get_default()
        self.aplicaciones = ("orca", "gnome-terminal","oowriter","iceweasel","nautilus","ooimpress","pidgin","oocalc","gedit","gnome-calculator","rhythmbox")
        self.comando = "/apps/metacity/keybinding_commands/command_"
        self.asignacion_teclado = "/apps/metacity/global_keybindings/run_command_"
        self.teclas = {"orca":"o","gnome-terminal":"t","oowriter":"w","iceweasel":"n","nautilus":"h","ooimpress":"i","pidgin":"p","oocalc":"x","gedit":"e","gnome-calculator":"c","rhythmbox":"m"}
        self.colorblind = {}
        

        
    def modificar(self):
        cont = 1
        for aplicacion in self.aplicaciones:
            ruta1 =  "%s%s" %(self.comando,cont)
            ruta2 = "%s%s"  %(self.asignacion_teclado,cont)
            self.gconfClient.set_string(ruta1, "%s" %aplicacion)
            self.gconfClient.set_string(ruta2, "%s" %self.teclas[aplicacion])
            cont = cont +1
    
    def modificar_opcion(self,opciones_validas):
 cont = 1
 for aplicacion in opciones_validas:
     if aplicacion in self.aplicaciones:
  ruta1 = "%s%s" %(self.comando,cont)
  ruta2 = "%s%s" %(self.asignacion_teclado,cont)
  self.gconfClient.set_string(ruta1, "%s" %aplicacion)
  self.gconfClient.set_string(ruta2, "%s" %self.teclas[aplicacion])
  cont = cont +1
     else:
  print "please change this option: %s" %aplicacion
    
    def listar(self):
        cont = 1
        for aplicacion in self.aplicaciones:
            ruta1 =  "%s%s" %(self.comando,cont)
            ruta2 = "%s%s"  %(self.asignacion_teclado,cont)
            print self.gconfClient.get_string(ruta1),self.gconfClient.get_string(ruta2)
            cont = cont +1


if __name__ == "__main__":
    import sys
    config = Conf()
    global opciones
    opciones = config.teclas.keys()
    def mensaje():
        print "pyconfig-orca options " 
        print "option : --help    : Print this help"
        print "option : --list    : List gconf for gnome-orca"
        print "option : --all     : add all config access key in gconf"
        for opcion in opciones:
   print "option : --%s   : add gconf access key to %s" %(opcion,opcion)
    
    if len(sys.argv) == 1 :
        mensaje()
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--list" :
            config.listar()
        elif sys.argv[1] == "--all":
            config.modificar()
        elif sys.argv[1] == "--help" :
            mensaje()
        else:
     for opcion in opciones:
  if sys.argv[1] =="--%s" %opcion:
      config.modificar_opcion(opcion)
    elif len(sys.argv) > 2:
 bandera = 0
 opciones_validas = []
 for opcion in sys.argv[1:]:
     if opcion == "--list" :
  bandera = 1
  continue
     elif opcion == "--all":
  bandera = 1
  continue
     elif opcion == "--help":
  bandera == 1
  continue
     else:
  opciones_validas.append(opcion[2:])
 if bandera == 1:
     mensaje()
     print "If you have a two option or more, please don\'t use --list,--all or --help."
 else:
     config.modificar_opcion(opciones_validas)
     print "all change do it"

```

En próximo post se mostrará la interfaz gráfica para la aplicación.


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)