Title: Crear llave gpg desde Python
Date: 2012-03-03 09:00
Category: Tutorial de Python
Tags: Canaima,Debian,General,Python,Seguridad,Ubuntu
lang: es
translation: true

Existen varias herramientas para crear, manipular llaves `gpg`.

Quienes no conozcan de `GPG` pueden leer el siguiente [tutorial](http://personales.upv.es/%7Ealalbiol/pages/Mini_Tutorial_GPG.html).

El paquete para python que permite manejar  las llaves `gpg` es `python-pyme`.  

```
#apt-get install python-pyme python-pyme-doc
```

La documentación de la librería pyme la encuentran en el siguiente [enlace](http://pyme.sourceforge.net/doc/pyme/index.html).

En la documentación se tiene una lista de ejemplos, se copia el archivo de `genkey.py` al home del usuario:  

```
cp /usr/share/doc/python-pyme-doc/examples/genkey.py ~/
```

Se edita el archivo `genkey.py`, se modifica el tipo de llave a RSA, se define la longitud de la llave (1024,2048 o 4096), longitud de la subllave (el mismo valor de la lñongitud de la llave), el nombre real, comentario del nombre, correo, frase de la llave, fecha de expiración de la llave.  
```python 
#!/usr/bin/env python
# $Id: genkey.py,v 1.6 2008/03/08 18:21:08 belyi Exp $
# Copyright (C) 2004 Igor Belyi <belyi@users.sourceforge.net>
# Copyright (C) 2002 John Goerzen <jgoerzen@complete.org>
#
#    This program is free software; you can redistribute it and/or #modify
#    it under the terms of the GNU General Public License as #published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty #of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  #See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public #License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  #02111-1307  #USA
	 
	
#Importar pyme
from pyme import core, callbacks
	
# Initialize our context.
#Inicializa el contexto.
core.check_version(None)
c = core.Context()
#Se define algunas configuraciones
c.set_armor(1)
c.set_progress_cb(callbacks.progress_stdout, None)
	
# This example from the GPGME manual
#Este es un ejemplo desde el manual gpgme.
	
parms = """<GnupgKeyParms format="internal">
Key-Type: RSA
Key-Length: 2048
Subkey-Type: ELG-E
Subkey-Length: 2048
Name-Real: Ernesto Nadir Crespo Avila
Name-Comment: seraph1
Name-Email: ecrespo@gmail.com
Passphrase: frasedelallave
Expire-Date: 2020-08-15
</GnupgKeyParms>
"""
#Se genera la llave pasandole los parámetros.
c.op_genkey(parms, None, None)
#Se imprime en patanalla el resultado de la generación.
print c.op_genkey_result().fpr
```	

Para crear la llave se ejecuta el archivo `genkey.py`:  
```python 
$python genkey.py
......
PROGRESS UPDATE: what = primegen, type = 46, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 46, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 43, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 43, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 43, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 43, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 43, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 94, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 94, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 94, current = 0, total = 0
PROGRESS UPDATE: what = primegen, type = 94, current = 0, total = 0
FFF598686F3ADE35C52BF65E4478C8341643F0EB
```
	
Al desplegar la lista de llaves se tiene lo siguiente:  
```python 
$gpg --list-keys
...
pub   2048R/1643F0EB 2012-03-04 [caduca: 2020-08-15]
uid                  Ernesto Nadir Crespo Avila (seraph1) <ecrespo@gmail.com>
sub   2048g/9F8E9C20 2012-03-04 [caduca: 2020-08-15]
```
Los últimos 8 números hexagecimales es el identificador de la llave `gpg`. Luego se exporta a un servidor de llaves y se puede compartir la llave pública para firmar o cifrar correos.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)