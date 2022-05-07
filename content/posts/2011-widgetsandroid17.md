Title: Manejando contactos y realizando una llamada con python en Android
Date: 2011-08-15 09:10
Category: Tutorial Python en Android
Tags: Android, Python, Reproductor Música
lang: es
translation: true

Retornando a los artículos sobre Android.

Este artículo toca el tema de como capturar la información del telefono y contacto del celular. Se crea una lista de contactos y telefonos, se despliega la información en un widget de selección simple, luego de seleccionar al contacto se captura la selección, se despliega la información del contacto y al final se realiza la llamada a dicho contacto.

Las clases nuevas utilizadas en el programa son:

* queryContent:Realiza una busqueda dentro de un contenido. En este caso se busca los contactos.
* phoneCallNumber: Permite realizar una llamada pasando el número de telefono como un string.

El código del programa se muestra a continuación:

```python 
#Importar el modulo android
import android
#importar la funcion sleep del modulo time
from time import sleep
#Crea la instancia droid del objeto Android.
droid = android.Android()
#Se captura los contactos
contactos = droid.queryContent('content://com.android.contacts/data/phones',\

        ['display_name','data1'],None,None,None).result


#Se crean la lista nombres y telefonos
nombres = []
telefonos = []

#Se agrega la informacion de los contactos a las listas.
for i in range(len(contacts)):
    nombres.append(contacts[i][u'display_name'])
    telefonos.append(contacts[i][u'data1'])

#Se despliega la lista de contactos
droid.dialogCreateAlert("Contactos")
droid.dialogSetItems(nombres)
droid.dialogShow()
#Se captura el resultado de la seleccion simple
respuesta  = droid.dialogGetResponse().result
#Se muestra la informacion del contacto seleccionado
droid.makeToast('El contacto seleccionado es: %s, su numero es: %s'
                %(nombres[respuesta['item']],telefonos[respuesta['item']]))
sleep(5)
droid.makeToast("Realizando la llamada")
sleep(2)
#Se realiza la llamada al contacto seleccioando.
droid.phoneCallNumber("%s" %telefonos[respuesta['item']])
```

A continuación se muestra la figura de la lista de contactos:

![Contactos](./images/contactos.png)

La siguiente figura muestra el contacto seleccionado:

![Contactos](./images/contactos2.png)

La última figura muestra la realización de la llamada del contacto seleccionado:

![Llamada](./images/llamada.png)

El código QR del programa se muestra en la siguiente figura:

![Código QR](./images/contactos1.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
