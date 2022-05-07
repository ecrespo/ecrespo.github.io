Title: Instalación de Debian en un mac Book. Tercera parte (configuración)
Date: 2008-06-08 10:30
Category: Debian, Linux, Mac Book

Continuación de la configuración de la Mac Book.

Configuración de Blacklight+volumen+y eject del CDROM:
Blacklight (teclas de Fn+F1 y Fn+F2)trabaja fino usando el programa [pommed](http://packages.debian.org/pommed), 
pommed también habilita el boton de eject del cdrom. [gpomme](http://packages.debian.org/gpomme) 
es una aplicación gráfica para la configuración vía gráfica pommed.

Por defecto en Debian las teclas F1,F2,F3, ..F12 están deshabilitadas y actuán 
igual a las teclas Fn+F1 y Fn+F2, .... Fn+F12. 

Para habilitar el uso el uso de las teclas se debe modificar el archivo /etc/pommed.conf, 
cambiar init=-1 a init=80,cambiar volume="PCM" a volume="Front" y reiniciar 
pommed (/etc/init.d/pommed restart).


1. Alta resolución de la reproducción de video:

Modificar /etc/X11/xorg.conf en la sección Device agregar:

```
Option "LinearAlloc" "6144"
Option "CacheLines" "1080"
```

2. Configuración del teclado:
2.1.Configuración de X11:

Agregar está opción en la parte del teclado:

```
Option          "XkbOptions"    "lv3:rwin_switch,apple:badmap"
```

Tambièn se puede configurar en el escritorio de gnome desde:
Sistema-> 'Preferencias' -> 'Teclado'.

Y seleccionar el teclado macbook/macbook pro (int)

Para el caso de la consola se agrega la siguiente línea en /etc/console-tools/remap:

```
s/keycode 126 =/keycode 126 = AltGr/;
```

Para la emulación del mouse en el teclado se puede hacer la siguiente asignación de teclas:


```
xmodmap -e "keycode 115 = Alt_L"           # left-apple
xmodmap -e "keycode 116 = Zenkaku_Hankaku" # right-apple
xmodmap -e "keycode 108 = Pointer_Button3" # KP-ENTER
xmodmap -e "keycode 204 = Pointer_Button2" # eject
xkbset m
```

Configuración del Touchpad:

Instalar gsynaptics:

```
aptitude install gsynaptics
```

Modificar /etc/X11/xorg.conf agregando lo siguiente:

```
Section "InputDevice"
      Identifier      "Synaptics Touchpad"
      Driver          "synaptics"
      Option          "SendCoreEvents"        "true"
      Option          "Device"                "/dev/psaux"
      Option          "Protocol"              "auto-dev"
      Option          "HorizScrollDelta"      "0"
EndSection
```

Agregar las siguientes líneas en /etc/modprobe.d/:

```
install usbhid /sbin/modprobe appletouch; /sbin/modprobe --ignore-install usbhid $CMDLINE_OPTS
```

Luego agregar appletouch a /etc/initramfs-tools/modules, ejecutar update-initramfs.

Una posible configuración en el xorg.conf es la siguiente:

```
Section "InputDevice"
       Identifier      "Configured Mouse"
       Driver          "synaptics"
       Option          "SendCoreEvents"        "true"
       Option          "Device"                "/dev/input/mice"
       Option          "Protocol"              "auto-dev"
       Option          "LeftEdge"              "0"
       Option          "RightEdge"             "850"
       Option          "TopEdge"               "0"
       Option          "BottomEdge"            "645"
       Option          "MinSpeed"              "0.4"
       Option          "MaxSpeed"              "1"
       Option          "AccelFactor"           "0.02"
       Option          "FingerLow"             "55"
       Option          "FingerHigh"            "60"
       Option          "MaxTapMove"            "20"
       Option          "MaxTapTime"            "100"
       Option          "HorizScrollDelta"      "0"
       Option          "VertScrollDelta"       "30"
       Option          "SHMConfig"             "on"
   EndSection
```


Configuraciones respeto al Procesador.
Escalando la frencuencia del CPU.
Ejecutar lo siguiente:

```
echo acpi_cpufreq >> /etc/modules
```

Escalando la frencuencia en el espacio de usuario:

Instalar powertop, este permite reducir el consumo de la bateria en el momento de trabajar con ella.

```
aptitude install powertop
```

Instalar powernowd

```
aptitude install powernowd
```

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC) 
usando la billetera digital de tu preferencia a la siguiente 
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)