Title: Programa para el envío de SMS desde Linux con Celular Android (conexión wifi y USB)
Date: 2011-06-16 09:00
Category: Tutorial Python
Tags: Linux,Python,Android,Debian,
lang: es
translation: true

En el artículo de ejecución remota de script versión conectado por [USB](https://www.seraph.to/ejecucion-remota-de-scripts-python-desde-linux-a-un-celular-con-android-version-conectado-el-celular-por-usb.html) y la versión por [wifi](https://www.seraph.to/ejecucion-remota-de-scripts-python-desde-linux-a-un-celular-con-android.html), se  explica  en el primer caso como enviar mensajes de texto y en el segundo como ejecutar una aplicación remotamente en el celular.

En este caso se fusionará ambos tipos de conexiones para enviar mensajes de texto tanto por USB como por wifi.

Para ello se creo un clase AndroidSMS donde se define los datos siguientes:

* Tipo de conexión (wifi o usb)
* Puerto (Puerto del servidor de SL4A que se activa en el celular)
* Host (IP que tiene asignado el celular en la red wifi)

En los artículos mencionados anteriormente se explica como usar el comando adb del sdk de Android y la creación de variables de entorno para poder ejecutar remotamente scripts desde Linux al celular con Android. En este caso todo ese proceso se automatiza  en el script, pero es necesario para el caso USB ejecutar SL4A con la opción de privado y en el caso wifi con la opción de público. Además se tiene que verificar el número del puerto asignado en el servidor SL4A para pasarle como parámetro dichos datos al programa desde la línea de comandos.

A continuación se muestra el código del programa:

```python 
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Script que permite enviar mensaje de texto a un celular android desde Linux.
#Autor: Ernesto Crespo
#Correo:ecrespo@gmail.com
#Licencia: GPLv3
#Version:0.4

#Importando el modulo android,sys,re y getstatusoutput
import android,sys,re
from commands import getstatusoutput

class AndroidSMS:
    def __init__(self,conexion,puerto,host="192.168.0.100"):
        #Asignacion de la estructura de datos del Objeto
        self.__adb = "/home/ernesto/android-sdk-linux_x86/platform-tools/adb"
        self.__puerto = puerto
        self.__host = host
        self.__conexion = conexion
    
    def __ValidarNumero__(self,numero):
        """Valida si los numeros tienen 11 digitos y que sean
        de los proveedores movilnet, digitel y movistar
        """
        if len(numero) == 11 and ((re.search("041[2|4|6]\d\d\d\d\d\d\d",numero)) or (re.search("042[4|6]\d\d\d\d\d\d\d",numero))) :
            return 1
        else:
            return 0

    def __ConfigAndroid__(self):
        """__ConfigAndroid: Metodo que permite habilitar el funcionamiento
        del celular Android desde Linux tanto para wifi como para conexion USB
        """
        #Se apaga el servidor adb en el Linux
        getstatusoutput("%s kill-server" %self.__adb)
        #Se borra las variables de entorno AP_PORT y AP_HOST
        getstatusoutput("export AP_PORT=\"\"")
        getstatusoutput("export AP_HOST=\"\"")
        #Se inicia el servidor adb y se verifica que funciona correctamente
        r = getstatusoutput("%s devices" %self.__adb)
        if r[0] <> 0:
            print "Problemas con la configuracion del celular"
            sys.exit
        else:
            if self.__conexion == "usb":
                #Se verifica que el dispositivo aparece identificado
                if r[1].split("\n")[1] == "":
                    print "NO hay un celular conectado"
                    sys.exit
        #En este punto se tiene el dispositivo funcionando
        #Tanto por wifi como por usb.
        getstatusoutput("%s  forward tcp:9999 tcp:%s" %(self.__adb,self.__puerto))
        if self.__conexion == "wifi":
            #Se crean las variables de entorno AP_PORT y AP_HOST
            #para el caso de wifi
            getstatusoutput("export AP_PORT=%s" %self.__puerto)
            getstatusoutput("export AP_HOST=%s" %self.__host)
        elif self.__conexion == "usb":
            #Se crea la variable de entorno AP_PORT
            #para el caso conexion usb
            getstatusoutput("export AP_PORT=9999")
        print "Se configuro el celular sin problemas"


    def EnviarMensaje(self,numero,mensaje):
        """EnviarMensaje: Metodo que permite enviar un mensaje de texto
        pasando el numero y el mensaje
        Maneja ambos casos conexion USB o por red wifi.
        """
        if self.__ValidarNumero__(numero) == 0:
            print "Numero invalido"
            sys.exit
        #Creando la instancia droid del objeto Android
        self.__ConfigAndroid__()
        #Se crea la instancia del objeto Android dependiendo si es conexion
        #wifi se le pasa el host y el puerto
        #Si es conexion USB simplemente se crea la instancia
        if self.__conexion == "wifi":
            droid = android.Android((self.__host,self.__puerto))
        elif self.__conexion == "usb":
            droid = android.Android()
        #Enviando el mensaje de texto
        droid.smsSend(numero,mensaje)
        
    
if __name__ == '__main__':
    """Se capturan los valores de:
    *numero
    *mensaje
    *conexion
    *puerto
    *host
    """
    if len(sys.argv) == 6:
        numero = sys.argv[1]
        mensaje = sys.argv[2]
        conexion = sys.argv[3]
        puerto = sys.argv[4]
        host = sys.argv[5]
    elif len(sys.argv) == 5:
        numero = sys.argv[1]
        mensaje = sys.argv[2]
        conexion = sys.argv[3]
        puerto = sys.argv[4]
        host = ""
    else:
        print "Error: No se pasaron los parametros completos"
        sys.exit
    #Se crea la instancia de la clase AndroidSM pasando conexion,puerto y host
    androidsms = AndroidSMS(conexion,puerto,host)
    #Se envie el mensaje de texto
    androidsms.EnviarMensaje(numero,mensaje)
```

La ejecución del programa se muestra a continuación:
Se pasa primero el número de celular, luego el mensaje, luego el tipo de conexión (usb,wifi), luego el puerto y por último la IP si es el caso de wifi.

* wifi: python mensaje4.py 0xxyyyzzww "Prueba3" wifi  47529 "192.168.0.100"
* usb: python mensaje4.py 0xxyyyzzww "Prueba4" usb  43421

En la siguiente figura se muestra los mensajes recibidos en el celular:

![SMS](./images/smsandroidlinux.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
