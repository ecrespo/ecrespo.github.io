Title: Escaneado de redes inalámbricas con python desde Android
Date: 2010-06-27 13:00
Category: Tutorial Python
Tags: Android, Linux, Python
lang: es
translation: true

Revisando el API de ASE encuentro que hay una forma de escanear redes inalámbricas con python en Android.
La idea es escanear las redes inalámbricas existentes y luego guardar la información en un archivo y presentarla en pantalla del celular.

A continuación se presenta el código:

```python

#Importar los módulos android y time
import  android,time

#Creando el objeto droid de la clase Android
droid =  android.Android()

#Escanear las redes inalámbricas existentes y  guardar en la variable redeswifi
redeswifi = droid.wifiGetScanResults()

#Se crea un  archivo de texto donde se almacenará la información de las redes
archivo =  open('/sdcard/redes.txt','w')

#Se crea una lista vacía
lista = []

#La información  de las redes inalámbricas se encuentra en el indice 1
# de una lista,  este indice contiene otra lista y dentro hay un diccionario
for i in  range(len(redeswifi[1])):
    #Se espera 1 segundo por cada iteración
    time.sleep(1)
    
    #Se toma los  valores del diccionario(ssid,frequency,capabilities,level)
    essid =  redeswifi[1][i]['ssid']
    frecuencia = redeswifi[1][i]['frequency']
    capacidad =  redeswifi[1][i]['capabilities']
    level = redeswifi[1][i]['level']
    
    #Se prepara  la información para ser presentada en pantalla y en archivo
    infored =  "Red inalambrica : %s, frecuencia: %s, señal: %s, cifrado:%s" \
                                                                 %(essid,frecuencia,level,capacidad)
    
    #Se presenta  la información en la pantalla del celular y se guarda también
    #en una lista
     droid.makeToast(infored)
    lista.append("%s\n" %infored)

#Se escribe en el  archivo y se cierra el mismo
archivo.writelines(lista)
archivo.close()
```

A continuación se muestra el contenido del archivo generado en el script:

```
Red inalambrica : prueba, frecuencia: 2442, señal: -91, cifrado:
Red inalambrica : pasillo, frecuencia: 2422, señal: -93, cifrado:[WPA2-PSK-TKIP+CCMP]

```



===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)