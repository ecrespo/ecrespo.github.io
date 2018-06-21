Title: Instalación de Debian en un mac Book. Segunda parte
Date: 2008-08-06 10:10
Category: Debian, Linux, Mac Book

Continuando con el proceso de instalación.

Al reiniciar el equipo se selecciona arranque desde Linux en el 
refit. Al iniciar sesión se entra con la cuenta creada y se procede 
a abrir una consola o a ejecutar synaptic para la selección de los repositorios.

En mi caso prefiero usar los de velug:
```
deb http://debian.velug.org.ve/debian lenny main contrib non-free
deb http://debian.velug.org.ve/debian-multimedia lenny main
```

Se ejecuta aptitude update.

Lo primero que se va a configurar es la tarjeta de red inalámbrica la cual 
su shipset es madwifi.

El kernel que trae lenny en sus repositorios es el 2.6.24-1y actualmente el equipo 
tiene el 2.6.22-3, se procede a instalar un kernel más actualizado. Adicionalmente 
se instalará subversion para poder instalar madwifi desde el repositorio de su página oficial.

```
aptitude install linux-image-2.6.24-1-amd64 linux-headers-2.6.24-1-amd64 svn subversion
```

Al terminar de instalar se ejectura lilo para actualizar el gestor de arranque y se 
reinicia el equipo.

Ya se tiene el kernel más reciente para verificar se ejecuta:

```
debian:~# uname -a
Linux debian 2.6.24-1-amd64 #1 SMP Sat May 10 09:28:10 UTC 2008 x86_64 GNU/Linux
```

A continuación se procede a configurar la tarjeta de red inalámbrica:

1. Se descarga del trink de svn de madwifi:

```
# svn co http://svn.madwifi.org/madwifi/trunk madwifi
```

2. Se descarga hal de people.freebsd.org:

```
# wget http://people.freebsd.org/~sam/ath_hal-20080528.tgz
```

3. Cambiarse al directorio de madwifi y renombrar el directorio hal:

```
# cd madwifi
# mv hal hal.old
```

4. Extraer el contenido de hal de freebsd y se renombra:

```
# tar -xvzf ../ath_hal-20080528.tgz

# mv ath_hal-20080528 hal
```

5. Se compila e instala madwifi en los directorios respectivos:

```
#make install BINDIR=/usr/bin MANDIR=/usr/share/man
```

6. Se recrea la lista de dependencias de los módulos:

```
#depmod -ae
```

7. Levantar el módulo madwifi:

```
#modprobe ath_pci
```

8. Verificar que se levanta el módulo con la salida del comando dmesg:

```
ath_hal: module license 'Proprietary' taints kernel.
ath_hal: 0.10.5.6 (AR5210, AR5211, AR5212, AR5416, RF5111, RF5112, RF2413, RF5413, RF2133, RF2425, RF2417)
wlan: svn r3711
ath_pci: svn r3711
ACPI: PCI Interrupt 0000:02:00.0[A] -> GSI 17 (level, low) -> IRQ 17
PCI: Setting latency timer of device 0000:02:00.0 to 64
MadWifi: ath_attach: HAL managed transmit power control (TPC) disabled.
MadWifi: ath_attach: Interference mitigation is supported. Currently disabled.
MadWifi: ath_attach: Switching rfkill capability off.
ath_rate_sample: 1.2 (svn r3711)
wifi0: 11a rates: 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: 11b rates: 1Mbps 2Mbps 5.5Mbps 11Mbps
wifi0: 11g rates: 1Mbps 2Mbps 5.5Mbps 11Mbps 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: turboA rates: 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: turboG rates: 6Mbps 9Mbps 12Mbps 18Mbps 24Mbps 36Mbps 48Mbps 54Mbps
wifi0: H/W encryption support: WEP AES AES_CCM TKIP
wifi0: Atheros AR5418 chip found (MAC 12.10, PHY SChip 8.1, Radio 12.0)
wifi0: Use hw queue 1 for WME_AC_BE traffic
wifi0: Use hw queue 0 for WME_AC_BK traffic
wifi0: Use hw queue 2 for WME_AC_VI traffic
wifi0: Use hw queue 3 for WME_AC_VO traffic
wifi0: Use hw queue 4 for XR traffic
wifi0: Use hw queue 7 for UAPSD traffic
wifi0: Use hw queue 8 for CAB traffic
wifi0: Use hw queue 9 for beacons
ath_pci: wifi0: Atheros 5418: mem=0x50100000, irq=17
```

9. Sólo queda seleccionar la red inalambrica
10. A continuación se muestra la interfaz configurada:

```
debian:~# iwconfig ath0
ath0 IEEE 802.11g ESSID:"ROOMSERVER" Nickname:""
Mode:Managed Frequency:2.432 GHz Access Point: 00:14:78:C5:87:0E 
Bit Rate:54 Mb/s Tx-Power:14 dBm Sensitivity=1/1 
Retry:off RTS thr:off Fragment thr:off
Encryption key:off
Power Management:off
Link Quality=73/70 Signal level=-23 dBm Noise level=-96 dBm
Rx invalid nwid:835 Rx invalid crypt:0 Rx invalid frag:0
Tx excessive retries:0 Invalid misc:0 Missed beacon:0
```

Ya se puede liberar del cable de red y utilizar la laptop con su conexión inalámbrica.

En el siguiente post se continuará con la configuración del laptop.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC) 
usando la billetera digital de tu preferencia a la siguiente 
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
