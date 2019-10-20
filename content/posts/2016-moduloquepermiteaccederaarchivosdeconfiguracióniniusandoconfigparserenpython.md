Title: Módulo que permite acceder a archivos de configuración .ini usando ConfigParser en Python
Date: 2016-01-04 09:00
Category: Tutorial Python
Tags: Python
lang: es
translation: true

Hace años tenía un módulo en python que permitía acceder a archivos de configuración del tipo .ini (secciones, clave-valor) por medio del módulo [ConfigParser](https://docs.python.org/2/library/configparser.html) (un ejemplo de como usar ConfigParser lo pueden ver [acá](https://pymotw.com/2/ConfigParser/)).

Ese script o módulo lo han utilizado en varios proyectos y últimamente lo estaba actualizando e incorporando en un desarrollo de envío de SMS.

Este módulo es de propósito general y no debería estar incorporado en una aplicación en específico o en cada aplicación que lo necesite, así que [he creado un proyecto en github donde alojaré dicho módulo](https://github.com/Mangoosta/pywrapper-config), en un futuro cercano espero subirlo a los [repositorios de Python](https://pypi.org/).

La segunda versión de dicho módulo toma conceptos de los artículos de programación orientada a objetos de artículos anteriores:

1. [Volviendo a lo básico, POO en Python (parte 1)](https://www.seraph.to/volviendo-a-lo-basico-poo-en-python-parte-1.html#volviendo-a-lo-basico-poo-en-python-parte-1)  
2. [Volviendo a lo básico, POO en Python (parte 2)](https://www.seraph.to/volviendo-a-lo-basico-poo-en-python-parte-2.html#volviendo-a-lo-basico-poo-en-python-parte-2)  
3. [Volviendo a lo básico, POO en Python (parte 3)](https://www.seraph.to/volviendo-a-lo-basico-poo-en-python-parte-3.html#volviendo-a-lo-basico-poo-en-python-parte-3)

La primera versión del código la pueden ver a continuación:
```
#!/usr/bin/env python
import ConfigParser,os
"""
Descripcion: Modulo que permite manipular archivos de configuracion.
Autor: Ernesto Crespo
Correo: ecrespo@gmail.com
Licencia: GPL Version 3
Copyright: Copyright (C) 2011 Ernesto Nadir Crespo Avila
Version: 0.2

"""

class config:
    """Modulo que permite manejar archivo de configuracion"""    
    def __init__(self,cnffile):
        self.__cnffile = cnffile
        self.__config = ConfigParser.ConfigParser()
        self.__config.read(self.__cnffile)
        
        
    def ShowItemSection(self,section):
        return self.__config.items(section)
    
    def ShowValueItem(self,section,option):
        return self.__config.get(section,option)
    
    def change(self,section,option,value):
        self.__config.set(section,option,value)

    
    def write(self):
        self.__config.write(open(self.__cnffile,'w'))
```

La nueva versión cambia la declaración del objeto, usa el decorador @property para definit el getter y el setter, define el método getattr y agrega el método que muestra las secciones:

El código de la nueva versión se muestra a continuación:
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import ConfigParser
from ConfigParser import ConfigParser

"""
Nombre: pywrapper_config
Descripcion: Modulo que permite manipular archivos de configuracion.
Autor: Ernesto Crespo
Correo: ecrespo@gmail.com
Licencia: GPL Version 3
Copyright: Copyright (C) 2016 Ernesto Nadir Crespo Avila <ecrespo@gmail.com> 
Version: 0.3

"""

#Clase config
class Config(object):
    """Clase Config: facilita el uso del modulo ConfigParser"""

    def __init__(self, cnffile):
        """Constructor toma el archivo de configuracion e inicializa ConfigParser"""
        self._cnffile = cnffile
        self._config = ConfigParser()
        self._config.read(self._cnffile)

    @property
    def cnffile(self):
        """Se consulta el valor del archivo de configuracion"""
        return self._cnffile
    
    @cnffile.setter
    def cnffile(self,cnffile):
        """Se modifica el valor del archivo de configuración y se vuelve a leer el mismo"""
        self._cnffile = cnffile
        self._config.read(self._cnffile)

    def __getattr__(self):
        """__getattr__ devuelve None si se trata de acceder a un atributo que no existe"""
        return None 

    def show_sections(self):
        """Muestra las secciones del archivo de configuracion"""
        return self._config.sections()

    def show_item_section(self, section):
        """Se define la funcion que muestra los item de una seccion"""
        return self._config.items(section)

#
    def show_value_item(self, section, option):
        """Se muestra el valor de los item"""
        return self._config.get(section, option)

#
    def change(self, section, option, value):
        """Se cambia el valor de la opcion"""
        self._config.set(section, option, value)

#
    def write(self):
        """Se escribe al archivo de configuracion"""
        self._config.write(open(self._cnffile,'w'))



if __name__ == '__main__':
    #Se crea la instancia de Config pasando el archivo de configuracion ini
    configuracion = Config("./conf/androidsms.conf")
    #Se muestra las secciones
    print("Secciones: {0} ".format(configuracion.show_sections()))
    #Se muestra los items de la seccion server
    print("Items de la seccion server: {0} ".format(configuracion.show_item_section("server")))
    #Se muestra la ip de la seccion server
    print("IP: {0}".format(configuracion.show_value_item("server","ip")))
    #Se muestra el archivo de configuracion
    print("Archivo de configuracion: {0}".format(configuracion.cnffile))
    #Se cambia en caliente de archivo de configuracion
    configuracion.cnffile = "./conf/python_android_sms.conf"
    print("Archivo de configuracion: {0}".format(configuracion.cnffile))
    #Se muestra las secciones del nuevo archivo de configuracion
    print("Secciones: {0}".format(configuracion.show_sections()))
```
A continuación se muestra el resultado de ejecutar el código anterior:
```
$ python pywrapper_config.py 
Secciones: ['sqlite', 'time', 'server'] 
Items de la seccion server: [('ip', '"127.0.0.1"'), ('port', '"8080"')] 
IP: "127.0.0.1"
Archivo de configuracion: ./conf/androidsms.conf
Archivo de configuracion: ./conf/python_android_sms.conf
Secciones: ['sqlite', 'time', 'server', 'tiempo', 'usb', 'paths']
```

El truco de cambiar de archivo de configuración se tiene en el setter, a continuación el código: 
```
    @cnffile.setter
    def cnffile(self,cnffile):
        """Se modifica el valor del archivo de configuración y se vuelve a leer el mismo"""
        self._cnffile = cnffile
        self._config.read(self._cnffile)
```
Aparte de agregar el archivo de configuración a la variable privada cnffile se vuelve a leer el archivo de configuración, esto facilita el cambio de archivos de configuración en caliente sin tener que volver a instanciar la clase Config.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)