Title: Mejorado el script en python que configura los accesos rápidos de teclado a aplicaciones en Gnome con gconf.
Date: 2010-08-07 11:10
Category: Tutorial de Python y Linux
Tags: Python,Gnome, Gconf, Accesibilidad
lang: es
translation: true


Para cambiar un poco la temática sobre Android volveré a tocar un programa que explique en el [siguiente artículo](https://www.seraph.to/script-en-python-que-configura-los-accesos-rapidos-de-teclado-a-aplicaciones-en-gnome-con-gconf.html).


El programa lo pueden bajar desde google code y tiene el nombre de [configGconf.py](http://python-config-accesskey-gnome.googlecode.com/hg/configGconf.py).

Las mejoras que tiene el programa son las siguientes:

* Se puede seleccionar entre las distribuciones Debian, Ubuntu y Canaima ya que dependiendo del caso se usa iceweasel como navegador o firefox.
* Se despliega más información a la hora de ejecutar el programa.
* Se usa el módulo python-argparse para capturar los argumentos del programa.
* Se pueden modificar todas las opciones de los accesos rápidos del teclado o una sola opción.


Se tiene que tener instalado la librería para python argparse; en el caso de Debian, Ubuntu y Canaima se ejecuta:

```
aptitude install python-argparse
```

Bajar el programa del enlace ya publicado.

Es necesario darle permisos de ejecución:

```
chmod a+x configGconf.py
```

A continuación se explica el uso del programa con la mejora de la captura de los argumentos:

1. Si se ejecuta configGconf.py sin argumentos o con la opción -h devuelve la ayuda.
2. Si se ejecuta con -v devuelve el número de versión del programa.
3. Para listar la configuración que maneja las teclas rápidas con agregar la opción de acción (-a o --accion) y se pasa como argumento listar.
4. Para cambiar todas las configuraciones de los accesos rápidos de teclado se agrega la acción cambiar, la opción (-d o --distribucion) con argumentos debian, ubuntu o canaima.
5. Para cambiar una sola opción se agrega en la acción el argumento modificarOpción, la distribución que se está usando (explicado en 4) y que opción se quiere cambiar (orca,gnome-terminal,oowriter,iceweasel,nautilus,ooimpress,pidgin,oocalc,gedit,gnome-calculator,rhythmbox).


A continuación se muestra los resultados de cada procedimiento anterior:

```
./configGconf.py 
usage: configGconf [-h] [-a {cambiar,listar,modificarOpcion}]
                   [-d {debian,canaima,ubuntu}]
                   [-o {orca,gnome-terminal,oowriter,iceweasel,nautilus,ooimpress,pidgin,oocalc,gedit,gnome-calculator,rhythmbox}]
                   [-v]

```

Cambiar accesos rapidos en teclado a Gnome
```
optional arguments:

 -h, --help            show this help message and exit
  -a {cambiar,listar,modificarOpcion}, --accion {cambiar,listar,modificarOpcion}
                        lista gconf
  -d {debian,canaima,ubuntu}, --distribucion {debian,canaima,ubuntu}
                        seleccione entre Canaima,Debian y ubuntu
  -o {orca,gnome-terminal,oowriter,iceweasel,nautilus,ooimpress,pidgin,oocalc,gedit,gnome-calculator,rhythmbox}, --opcion {orca,gnome-terminal,oowriter,iceweasel,nautilus,ooimpress,pidgin,oocalc,gedit,gnome-calculator,rhythmbox}
                        Cambia la configuración de una opción
  -v, --version
```

```
./configGconf.py -v
configGconf 0.4

./configGconf.py -a listar
Listar accesos rapidos del teclado a gconf
________________________________________________
Aplicación:  orca o
Aplicación:  gnome-terminal t
Aplicación:  oowriter w
Aplicación:  iceweasel n
Aplicación:  nautilus h
Aplicación:  ooimpress i
Aplicación:  pidgin p
Aplicación:  oocalc x
Aplicación:  gedit e
Aplicación:  gnome-calculator c
Aplicación:  rhythmbox m

./configGconf.py  -a cambiar -d debian
Listar accesos rapidos del teclado de gconf
________________________________________________
Configurando aplicacion: orca, acceso teclado: o
Configurando aplicacion: gnome-terminal, acceso teclado: t
Configurando aplicacion: oowriter, acceso teclado: w
Configurando aplicacion: iceweasel, acceso teclado: n
Configurando aplicacion: nautilus, acceso teclado: h
Configurando aplicacion: ooimpress, acceso teclado: i
Configurando aplicacion: pidgin, acceso teclado: p
Configurando aplicacion: oocalc, acceso teclado: x
Configurando aplicacion: gedit, acceso teclado: e
Configurando aplicacion: gnome-calculator, acceso teclado: c
Configurando aplicacion: rhythmbox, acceso teclado: m


./configGconf.py  -a modificarOpcion -d debian -o oowriter
Listar accesos rapidos del teclado de gconf
________________________________________________
Configurando aplicacion: oowriter, acceso teclado: w

```

Para finalizar el artículo se colocará el código del programa:


```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Name: configGconf
Description: Aplicación y módulo que permite modificar los accesos rápido de teclas a programas
Version:0.4
License: GPLv3
Copyright: Copyright (C) 2009  Distrito Socialista Tecnologico AIT PDVSA Mérida
Author: Ernesto Nadir Crespo Avila
Email: ecrespo@gmail.com
Changelog:
 0.1: * Agregada multiples opciones de configuración.
 0.2: * Agregada opción de selección de distribución debian, ubuntu o canaima.
      * Agregada información adicional a la hora de desplegar en pantalla.
 0.3: * Agregado el uso del módulo argparse para simplificar la captura de argumentos del comando.
 0.4: * Agregada la posibilidad de modificar una sóla opción de las teclas rápidas de gconf.
"""
version = "0.4"
autor = "Ernesto Nadir Crespo Avila"
email = "ecrespo@gmail.com"
copyright = "GPLv3"


#Importar módulo gconf
import gconf




class Conf:
    def __init__(self):
        #Se crea la instancia de la clase de gconf
        self.__gconfClient = gconf.client_get_default()
        #Se crea la tupĺa aplicaciones        
        self.__aplicaciones = ("orca", "gnome-terminal","oowriter","iceweasel","nautilus","ooimpress","pidgin","oocalc","gedit","gnome-calculator","rhythmbox")
        #Se crea la ruta del comando del teclado y la ruta del modificador de teclado
        self.__comando = "/apps/metacity/keybinding_commands/command_"
        self.__asignacion_teclado = "/apps/metacity/global_keybindings/run_command_"
        #Se crea un diccionario teclas con la asociación entre la aplicación y su acceso rápido de teclado
        self.__teclas = {"orca":"o","gnome-terminal":"t","oowriter":"w","iceweasel":"n","nautilus":"h","ooimpress":"i","pidgin":"p","oocalc":"x","gedit":"e","gnome-calculator":"c","rhythmbox":"m"}


    def modificar_opcion(self,opciones,distribucion,interfaz=0):
        if distribucion <> "debian":
            self.__aplicaciones = ("orca", "gnome-terminal","oowriter","firefox","nautilus","ooimpress","pidgin","oocalc","gedit","gnome-calculator","rhythmbox")
            self.__teclas = {"orca":"o","gnome-terminal":"t","oowriter":"w","firefox":"n","nautilus":"h","ooimpress":"i","pidgin":"p","oocalc":"x","gedit":"e","gnome-calculator":"c","rhythmbox":"m"}
            if opciones == "iceweasel":
                opcion = "firefox"
            elif opciones == "firefox":
                opcion = opciones
            else:
                opcion = opciones
        else:
            if opciones == "firefox":
                opcion = "iceweasel"
            else:
                opcion = opciones
                
        if interfaz == 0:
            print "Listar accesos rapidos del teclado de gconf"
            print "________________________________________________"
        cont = 1
        #se genera un ciclo con las aplicaciones existentes
        for aplicacion in self.__aplicaciones:
            #Si la opción existe como aplicación se modifica el gconf, si no se sale sin resultado
            if aplicacion == opcion:
                ruta1 = "%s%s" %(self.__comando,cont)
                ruta2 = "%s%s" %(self.__asignacion_teclado,cont)
                self.__gconfClient.set_string(ruta1, "%s" %aplicacion)
                self.__gconfClient.set_string(ruta2, "%s" %self.__teclas[aplicacion])
                if interfaz == 0:
                    #Se imprime en pantalla los cambios logrados.
                    print "Configurando aplicacion: %s, acceso teclado: %s" %(aplicacion,self.__teclas[aplicacion])
                break
            cont = cont+1
    
    def modificar(self,distribucion):
        """
        modificar: Permite modificar los accesos rápidos del teclado
        Argumentos:
         * distribucion: se le pasa una distribución a utilizar entre debian,ubuntu y canaima.
        """
        cont = 1
        print "Listar accesos rapidos del teclado de gconf"
        print "________________________________________________"
        #Se la distribución no es debian se cambia iceweasel por firefox en las variables aplicaciones y teclas.
        if distribucion <> "debian":
            self.__aplicaciones = ("orca", "gnome-terminal","oowriter","firefox","nautilus","ooimpress","pidgin","oocalc","gedit","gnome-calculator","rhythmbox")
            self.__teclas = {"orca":"o","gnome-terminal":"t","oowriter":"w","firefox":"n","nautilus":"h","ooimpress":"i","pidgin":"p","oocalc":"x","gedit":"e","gnome-calculator":"c","rhythmbox":"m"}
        #Se genera un ciclo según las aplicaciones
        for aplicacion in self.__aplicaciones:
            #Definición de las rutas del gconf del comando y del modificador del teclado
            ruta1 =  "%s%s" %(self.__comando,cont)
            ruta2 = "%s%s"  %(self.__asignacion_teclado,cont)
            #Se modifica gconf
            self.__gconfClient.set_string(ruta1, "%s" %aplicacion)
            self.__gconfClient.set_string(ruta2, "%s" %self.__teclas[aplicacion])
            #Se imprime en pantalla los cambios logrados.
            print "Configurando aplicacion: %s, acceso teclado: %s" %(aplicacion,self.__teclas[aplicacion])
            cont = cont +1
    
    
    def listar(self):
        """
        listar: Permite listar los accesos rápidos de teclado de gconf
        """
        cont = 1
        print "Listar accesos rapidos del teclado a gconf"
        print "________________________________________________"
        #Se crea un ciclo según la lista de aplicaciones
        for aplicacion in self.__aplicaciones:
            #Se define la ruta del comando del teclado según gconf
            ruta1 =  "%s%s" %(self.__comando,cont)
            #Se define la ruta del modificador del teclado
            ruta2 = "%s%s"  %(self.__asignacion_teclado,cont)
            #Se desplega en pantalla 
            print "Aplicación: " ,self.__gconfClient.get_string(ruta1),self.__gconfClient.get_string(ruta2)
            cont = cont +1




if __name__ == "__main__":
    #Importar módulo argparse para capturar los argumentos del comando    
    import argparse
    #Se instancia la clase Conf en el objeto config
    config = Conf()
    #Creación del parse 
    parser = argparse.ArgumentParser(prog='configGconf',description="Cambiar accesos rapidos en teclado a Gnome")
    acciones = ["cambiar","listar","modificarOpcion"]
    distribuciones = ["debian","canaima","ubuntu"]
    aplicaciones = ["orca", "gnome-terminal","oowriter","iceweasel","nautilus","ooimpress","pidgin","oocalc","gedit","gnome-calculator","rhythmbox"]
    #Se agrega las opciones accion, distribucion y version.    
    parser.add_argument('-a','--accion',type=str,choices=acciones,default=acciones,help='lista gconf')
    parser.add_argument('-d','--distribucion',choices=distribuciones,type=str,default=distribuciones,help='seleccione entre Canaima,Debian y ubuntu')
    parser.add_argument('-o','--opcion',choices=aplicaciones,type=str,default=aplicaciones,help='Cambia la configuración de una opción')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.4') 
    #Se captura los argumentos del comando ejecutado.
    args = parser.parse_args()
    # ejecución de las opciones según la acción y la distribución
    if args.accion == "listar":
        #Se lista las configuraciones de los accesos del teclado
        config.listar()
    elif args.distribucion in ('debian','ubuntu','canaima') and args.accion == "cambiar":
        #Se modifican las opciones de los accesos del teclado
        config.modificar(args.distribucion)
    elif args.accion == "modificarOpcion":
        #Permite modificar una opcion
        config.modificar_opcion(args.opcion,args.distribucion)
    else:
        #Si no se pasa ningún argumento se despliega la ayuda
        parser.print_help()
```


En el siguiente artículo se explicará los cambios que se hicieron en la interfaz gráfica del artículo [Desarrollo de interfaz gráfica para la configuración de accesos rápidos del teclado](https://www.seraph.to/desarrollo-de-interfaz-grafica-para-la-configuracion-de-accesos-rapidos-de-teclado-para-gconf.html).
Luego se explicará como se crea un paquete python y como se crea un paquete para Debian a partir del paquete python.


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)