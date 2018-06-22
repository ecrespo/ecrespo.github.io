Title: Instalando asterisk 
Date: 2008-04-13 10:00
Category: Asterisk Debian Linux
Tags: Debian, Asterisk 
lang: es
translation: true

Desde hace un año me ha tocado trabajar con asterisk y es ahora que 
he logrado comprar una tarjeta Motorola X100P, podre crear un 
gateway a la telefonía Pública.

### Instalación de asterisk.

Para realizar la instalación de asterisk desde las fuentes es necesario 
instalar algunos paquetes:
```
aptitude install libnewt0.52 libnewt-pic libnewt-dev zlib1g zlib1g-dev dcmtk libdcmtk1 libdcmtk1-dev libssl-dev libssl0.9.8 libssl0.9.8-dbg initramfs-tools libnewt0.52 libnewt-pic libnewt-dev
```
Procedimiento:
1. Instalación de zaptel: Al ejecutar lspci se ve que se tiene instalado 
la tarjeta motorola:
```
01:00.0 Communication controller: Motorola Wildcard X100P
```
1.1. Desempaquetar zaptel
```
tar ­-zxvf zaptel­1.4.9.2.tar.gz
```

1.2. Cambiarse al directorio de zaptel
```
cd zaptel-1.4.9.2/
```
1.3. Configurar zaptel
```
./configure
```

1.4.Ejecutar make menuselect
1.5. Ejecutar make
1.6. Ejecutar make install
1.7. Ejecutar make config
1.8. Crear el archivo udev para zaptel
```
make install-udev
```

Esto creará un demonio para levantar automáticamente la tarjeta X100P.

1.9. Revisar que zaptel detecta la tarjeta.
```
zaptel_hardware
pci:0000:01:00.0 wcfxo- 1057:5608 Wildcard X100P
```

1.10. Editar /etc/zaptel.conf y agregar fxsks=1
1.11. Cargar el módulo /etc/init.d/zaptel restart

2. Instalación de libpri.
2.1. Desempaquetar libpri
```
tar -xvzf libpri-1.4.3.tar.gz
```
2.2. Cambiar al directorio
```
cd libpri-1.4.3/
```
2.3. Ejecutar make
2.4. Ejecutar make install
3. Instalar asterisk
3.1. Desempaquetar asterisk
```tar -xvzf asterisk-1.4.19.tar.gz
```
3.2. Cambiar al directorio
```
cd asterisk-1.4.19/
```
3.3. Configurar
```
./configure
```
3.4. Seleccionar módulos
```
make menuselect
```
3.5. Compilar
```
make
```

3.6. Instalar
```
make install
```

3.7. Instalar ejemplos
```
make samples
```

3.8. Instalar documentación
```
make progdocs
```

3.9. Instalar script para arranque automatico de asterisk
```
make config
```

4. Instalar asterisk-addons

4.1 Desempaquetar asterisk-addons
```
tar -xvzf asterisk-addons-1.4.6.tar.gz
```

4.2. Cambiar de directorio
```
cd asterisk-addons-1.4.6/
```

4.3. Configurar
```
./configure
```

4.4. Seleccionar módulos
```
make menuselect
```

4.5. Compilar
```
make
```
4.6. Instalar
```
make install
```

4.7. Instalar ejemplos
```
make samples
```

5. Instalación de voces en español adicionales de la página de VoIPnovatos.
5.1. Cambiar al directorio donde se encuentran los sonidos
```
cd /var/lib/asterisk/sounds/
```

5.2 Instalar el core de gsm
```
tar -xvzf /usr/local/src/voipnovatos-core-sounds-es-gsm-1.4.tar.gz
```

5.3. Instalar el core de g729
```
tar -xvzf /usr/local/src/voipnovatos-core-sounds-es-g729-1.4.tar.gz
```

5.4. Instalar las extras de gsm
```
tar -xvzf /usr/local/src/voipnovatos-extra-sounds-es-gsm-1.4.tar.gz
```

5.5. Instalar las extras de g729
```
tar -xvzf /usr/local/src/voipnovatos-extra-sounds-es-g729-1.4.tar.gz
```

5.6. Instalar Music on Hold en español
```
tar -xvzf /usr/local/src/asterisk-voces-es-v1_2-moh-voipnovatos.tar.gz
```

Luego de esto se tiene el asterisk totalmente instalado.
En próximo post publicare la configuración de la tarjeta X100P y configuración 
base de asterisk.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC) 
usando la billetera digital de tu preferencia a la siguiente 
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)