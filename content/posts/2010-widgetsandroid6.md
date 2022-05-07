Title: Widgets en Android con python. Parte 6 (Botones)
Date: 2010-07-16 11:00
Category: Tutorial Python en Android
Tags: Android, Python
lang: es
translation: true

Continuando con los [widgets del API de ASE para el lenguaje python](https://www.seraph.to/category/tutorial-python-en-android.html) se hará un script que muestra 3 botones y se mostrará el mensaje del resultado de darle clip al botón.


El código del programa es el siguiente:

```python
#Importando el módulo android.
import android

#Crear la instancia del objeto android
droid = android.Android()

#Título y mensaje del botón.
title = 'Alerta'
message = ('Esta alerta tiene 3 botones y' 'se espera que presione uno')
 
#Crear el widget de mensaje de alerta 
droid.dialogCreateAlert(title, message)
 
#Se definen los mensajes de los botones (si, no y cancelar).
droid.dialogSetPositiveButtonText('Si')
droid.dialogSetNegativeButtonText('No')
droid.dialogSetNeutralButtonText('Cancelar')

#Mostrar el mensaje
droid.dialogShow()

#Captura del resultado de darle clip a algún botón.
#el resultado es un diccionario.
response = droid.dialogGetResponse().result
 
#Se muestra un mensaje con el resultado de darle clip.
droid.makeToast('El resultado de la ejecucion del boton es: %s'    %response['which'])
```

En la siguiente figura se muestra el widget de los botones.

![Botones ](./images/botones2.png)

Luego se presentará las 3 figuras de darle clip a cada botón.
Mensaje del boton Si. 

![Boton - Si](./images/botones3.png)

Mensaje del boton Cancelar.

![Boton - Cancelar](./images/botones4.png)

Mensaje del botón No.

![Boton - No](./images/botones5.png)


Para finalizar se muestra la imPara finalizar se muestra la figura del código QR del script.


![Código](./images/botones1.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)