Title: Comandos básicos de adb (Android Debug Bridge) para acceder al motorola milestone A853
Date: 2010-05-29 10:00
Category: Tutorial Linux
Tags: Linux, Android, Debian
lang: es
translation: true

En el [artículo anterior](https://www.seraph.to/instalacion-del-sdk-de-android-en-linux.html#instalacion-del-sdk-de-android-en-linux) se explico como instalar el SDK de Android en Debian, a continuación se explicará el comando que permite dar acceso al celular como ver la microsd, instalar aplicaciones en el celular desde el computador entre otras cosas. 

Cambiarse al directorio tools del SDK de Android. 

```
cd android-sdk_r06-linux_86/tools 
```

Crear un enlace de la aplicación adb a /usr/bin . 

```
sudo ln -s /home/ernesto/android-sdk-linux_86/tools/adb /usr/bin/adb 

ls -l /usr/bin/adb 
lrwxrwxrwx 1 root root 44 may 27 20:12 /usr/bin/adb -> /home/ernesto/android-sdk-linux_86/tools/adb 
```

Crear el archivo 50-android.rules en el directorio /etc/udev/rules.d 

```
vim /etc/udev/rules.d/50-android.rules 

```

Agregar el siguiente contenido al archivo: 

```
SUBSYSTEMS=="usb", ATTRS{idVendor}=="0bb4", ATTRS{idProduct}=="0c02", GROUP="androiddev", SYMLINK+="android%n" 
```

Se crea el grupo androiddev. 

```
sudo addgroup --system androiddev 

```

Se cambia los permisos del archivo y se recarga las reglas udev. 

```
sudo chmod a+rx /etc/udev/rules.d/50-android.rules 
sudo /etc/init.d/udev reload 
```

En el celular asegurarse que está en modo depuración de la conexión USB. Esto es: 
Ajustes->Aplicaciones->Desarrollo. 

Iniciar adb como servidor: 

```
sudo ./adb start-server 

```

Luego se verifica que se tiene acceso al celular con el comando adb devices. 

```
adb devices 
* daemon not running. starting it now * 
* daemon started successfully * 
List of devices attached 
0403725B09015010 device 
```

Cuando aparece está información y no caracteres raros o ??? o no aparece nada es que ya se tiene conectado el celular al computador. 


El comando adb shell nos crea un shell desde el celular y se ejecuta el comando ls -l: 

```
$ ls -l 
drwxrwxrwt root root 2010-05-29 08:01 tmp 
drwxrwxr-x system system 2010-02-23 07:41 pds 
drwxrwxrwt root root 2010-05-29 13:21 sqlite_stmt_journals 
dr-x------ root root 2010-05-29 08:00 config 
drwxrwx--- system cache 2010-05-27 11:00 cache 
d---rwxr-x system sdcard_rw 2010-05-29 08:01 sdcard 
lrwxrwxrwx root root 2010-05-29 08:00 d -> /sys/kernel/debug 
lrwxrwxrwx root root 2010-05-29 08:00 etc -> /system/etc 
drwxr-xr-x root root 2010-01-06 09:29 system 
drwxr-xr-x root root 1969-12-31 20:00 sys 
drwxr-x--- root root 1969-12-31 20:00 sbin 
dr-xr-xr-x root root 1969-12-31 20:00 proc 
-rwxr-x--- root root 453 1969-12-31 20:00 init_prep_keypad.sh 
-rwxr-x--- root root 13218 1969-12-31 20:00 init.rc 
-rwxr-x--- root root 14824 1969-12-31 20:00 init.mapphone_umts.rc 
-rwxr-x--- root root 6840 1969-12-31 20:00 init.mapphone_cdma.rc 
-rwxr-x--- root root 1677 1969-12-31 20:00 init.goldfish.rc 
-rwxr-x--- root root 104324 1969-12-31 20:00 init 
-rw-r--r-- root root 118 1969-12-31 20:00 default.prop 
drwxrwx--x system system 2010-05-29 08:01 data 
drwx------ root root 2009-11-19 15:42 root 
drwxr-xr-x root root 2010-05-29 08:01 dev 
```

Este comando muestra los archivos y directorios que se tienen en el celular. Noten que son comandos unix/Linux así que si se cambian de directorio al system y luego app en el encontrarán los paquetes apk que se encuentran instalados en el celular. 


```
$cd /system/app 
pwd 
$pwd 
/system/app 
$ls -l 
-rw-r--r-- root root 1500786 2010-01-06 09:28 MotoID.apk 
-rw-r--r-- root root 433280 2010-01-06 09:28 MovilnetContainer.apk 
-rw-r--r-- root root 2624470 2010-01-06 09:28 Maps.apk 
-rw-r--r-- root root 677433 2010-01-06 09:28 Talk.apk 
-rw-r--r-- root root 50410 2010-01-06 09:28 GoogleContactsSyncAdapter.apk 
-rw-r--r-- root root 327750 2010-01-06 09:28 MediaUploader.apk 
-rw-r--r-- root root 1310501 2010-01-06 09:28 Vending.apk 
-rw-r--r-- root root 735409 2010-01-06 09:28 Gmail.apk 
-rw-r--r-- root root 380550 2010-01-06 09:28 GoogleApps.apk 
-rw-r--r-- root root 778098 2010-01-06 09:28 SetupWizard.apk 
-rw-r--r-- root root 53777 2010-01-06 09:28 TalkProvider.apk 
```

Estos son algunos programas que se tienen instalados en el celular. 

Los comandos que se pueden utilizar en el shell son los siguientes: 

* ls Lista los directorios y carpetas existentes en la ruta que estemos.
* reboot Reinicia el terminal
* rm Borra un archivo
* rmdir Borra un directorio
* cd Cambia de directorio
* mkdir Crea un directorio
* mkswapp Crea un sistema de intercambio
* mount Monta una unidad o partición
* umount Desmonta una unidad
* mv Mueve o renombra un archivo 

Se puede ejecutar un ls dentro del sdcard/Videos y se muestra lo siguiente: 

```
$adb shell ls /sdcard/Videos/ 
How.I.Met.Your.Mother.S05E21.HDTV.XviD-LOL.[VTV].avi 
The.Big.Bang.Theory.S03E20.The.Spaghetti.Catalyst.HDTV.XviD-FQM.avi 
```

Para Borrar los archivos se ejecuta adb shell rm y luego se vuelve a ejecutar el ls para demostrar que se han borrado los archivos de la tarjeta sd del celular: 

```
ernesto@jewel:~$ adb shell rm sdcard/Videos/*.avi 
ernesto@jewel:~$ adb shell ls sdcard/Videos 
ernesto@jewel:~$ 
```

También se puede instalar aplicaciones en el celular desde el computador con el comando adb install rutapaquete.apk: 


A continuación se instala una aplicación de Sudoku desde el computador al celular. 


```
ernesto@jewel:~$ adb install /home/ernesto/Descargas/OpenSudoku-1.1.1-02.apk 
603 KB/s (223640 bytes in 0.361s) 
pkg: /data/local/tmp/OpenSudoku-1.1.1-02.apk 
Success 
```

También se puede copiar archivos del celular al computador y del computador al celular: 

```
ernesto@jewel:~$ adb push /home/ernesto/varios.mp3 /sdcard/mp3z/ 
1944 KB/s (7768607 bytes in 3.901s) 
```

En este ejemplo se coloca un archivo mp3 del computador al celular. 

```
ernesto@jewel:~$ adb pull /sdcard/python_scripts_r0.zip ./ 
52 KB/s (4280 bytes in 0.078s)
```

Este comando se trae un archivo de la memoria sdcard del celular al computador. 

EL próximo artículo explicará como conectarse a internet desde un celular con android. 


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)