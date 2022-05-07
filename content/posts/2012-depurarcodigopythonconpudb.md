Title: Depurar código python con pudb
Date: 2012-12-07 9:00
Category: Tutorial de Python
Tags: General,Linux,numpy,python,pudb
lang: es
translation: true

`Pudb` es una herramienta de depuración full pantalla para la consola. Soporta teclas de cursor y comandos del editor vi. Se puede integrar con `ipython` si se requiere.

Para instalarlo en distribuciones basadas en Debian se ejecuta el siguiente comando:
```
apt-get install python-pudb
```
Para instalarlo con `easy_install` o `pip` se ejecuta lo siguiente:
```
easy_install pudb
```
```
pip install pudb
```

Se depurará el mismo código del [artículo anterior](http://blog.crespo.org.ve/2012/12/depurar-codigo-python-con-ipython.html). Se agregará al código para la depuración:
from pudb import set_trace; set_trace()

El código completo se muestra a continuación:
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Se importa numpy como np
import numpy as np

from pudb import set_trace; set_trace()


a = np.arange(10)
print a
print a[8]
print a[9]

for i in a:
    print i
    
print a[10]
```
Para iniciar la depuración se ejecuta python haciendo una llamada al módulo de `pudb.run` y luego se pasa el script a depurar:
```
python -m pudb.run arreglo.py
```
En la siguiente figura se muestra la interfaz de `pudb`.

![](./images/depurarcodigopythonconpudb-1.png) 

En la ventana principal se muestra el código del script, en la primera ventana lateral superior se muestra las variables, la siguiente ventana inferior se muestra el stack y por último los breakpoints. 

Para ver las opciones existentes de la interfaz se presiona a la tecla "?". En la siguiente figura se muestra las opciones.

![](./images/depurarcodigopythonconpudb-2.png) 


Opciones:  

- Control+p: Permite editar las preferencias de la interfaz.
- n (next): Permite saltar a la siguiente instrucción del código.
- c (continue):  Continua a la siguiente instrucción.
- s (step into): Salta a la siguiente instrucción.
- r/f:: Finaliza la función actual.
- t: Corre al cursor.
- e: Muestra el traceback (postmorten o en el estado de una excepción).
- H: Mueve a la línea actual (al final del stack). 
- u: Mueve hacia arriba en el stack
- d: Mueve hacia abajo en el stack
- !: Invoca un interprete de comandos python en el actual ambiente.
- o: Muestra la consola o la salida de la pantalla.
- b: Conmuta los breakpoints.
- q: Salir/reiniciar el script.

En la siguiente figura se muestra las preferencias:

![](./images/depurarcodigopythonconpudb-3.png) 

La siguiente figura muestra a el depurador en funcionamiento.

![](./images/depurarcodigopythonconpudb-4.png) 


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)