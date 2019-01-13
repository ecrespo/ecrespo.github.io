Title: Widgets en Android con python. Parte 7 (selección simple)
Date: 2010-07-19 09:00
Category: Tutorial Python en Android
Tags: Android, Python
lang: es
translation: true

En este artículo explicaré el uso del widget de selección simple.

La idea es tener una tupla con varios colores, se abre un widget con esos colores y se selecciona uno, luego aparecerá un mensaje con el color seleccionado.

A continuación se muestra el código en python de la aplicación:

```python
#Importar módulo android y time.
import android,time

#Se instancia el objeto Android 
droid = android.Android()

#Se crea el titulo del mensaje de alerta y se crea el widget. 
titulo = 'Color seleccionado'
droid.dialogCreateAlert(titulo)

#Se crea la tupla con la lista de colores. 
colores = ('amarillo', 'azul', 'rojo')

#Se agrega la tupla al widget de selección simple. 
droid.dialogSetItems(colores)

#Se muestra el widget. 
droid.dialogShow()

#Se captura el resultado de seleccionar un color 
respuesta  = droid.dialogGetResponse().result
#El resultado se guarda en un diccionario y se muestra en un mensaje.
droid.makeToast('El color seleccionado es: %s' %colores[respuesta['item']])
```
La siguiente figura muestra el widget de la lista de colores.

![Seleccion simple ](./images/seleccionsimple.png)

Luego de darle clip a un color se muestra un mensaje con el color selecionado como lo muestra la siguiente figura.

![Selección Simple - Salida](./images/seleccionsimpleresultado.png)

Para finalizar se muestra la figura del código QR del programa.

![Código](./images/seleccion_simple.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)