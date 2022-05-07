Title: Analizando código Python con Pylint
Date: 2012-12-11 9:00
Category: Tutorial Python
Tags: General,Linux,numpy,python,PyLint
lang: es
translation: true

`Pylint` es una herramienta de análisis de código creada por LogiLab.  Es más complejo que `Pyflakes` y permite más personalización. Para más información de pylint puede revisar el [manual](https://www.logilab.org/card/pylint_manual).

Se puede instalar `pylint` por medio de `easy_install` o `pip` y si es una distribución de Linux basada en Debian se puede instalar vía `apt-get`:

```python
easy_install  pylint
```
```python
pip install pylint
```
```
apt-get install pylint
```
La salida de `pylint` puede ser texto crudo o puede ser en formato html. Los mensajes tienen el siguiente formato:
TIPO_MENSAJE: LINEA:[OBJECTO:] MENSAJE

El tipo de mensaje puede ser de la siguiente forma:

- [R]: Significa que se recomienda la refactorización del código.
- [C]: Significa que en el código hubo violación de estilos.
- [W]: Es una alarma por un problema menor.
- [E]: Significa mensaje de error o un potencial bug.
- [F]: Indica un error grave, bloqueo para análisis futuros.
- Se usará el mismo código del artículo anterior:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Se importa numpy como np
import numpy as np
from pudb import set_trace; set_trace()
import string
a = np.arange(10)
print a
print a[8]
print a[9]
for i in a:
    if i == plataforma:
        print i
```

Este script se salva con el nombre de `arreglo.py`.

Ahora se ejecutará `pylint` y se le pasa como argumento el archivo `arreglo.py`:

La salida de la ejecución de `pylint` se muestra a continuación:

```python
************* Module arreglo


C:  1,0: Missing docstring


C:  7,28: More than one statement on a single line


W:  8,0: Uses of a deprecated module 'string'


C: 12,0: Invalid name "a" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)


E: 18,12: Undefined variable 'plataforma'


W:  8,0: Unused import string








Report


======


12 statements analysed.





Duplication


-----------





+-------------------------+------+---------+-----------+


|                         |now   |previous |difference |


+=========================+======+=========+===========+


|nb duplicated lines      |0     |0        |=          |


+-------------------------+------+---------+-----------+


|percent duplicated lines |0.000 |0.000    |=          |


+-------------------------+------+---------+-----------+











Statistics by type


------------------




+---------+-------+-----------+-----------+------------+---------+


|type     |number |old number |difference |%documented |%badname |


+=========+=======+===========+===========+============+=========+


|module   |1      |1          |=          |0.00        |0.00     |


+---------+-------+-----------+-----------+------------+---------+


|class    |0      |0          |=          |0           |0        |


+---------+-------+-----------+-----------+------------+---------+


|method   |0      |0          |=          |0           |0        |


+---------+-------+-----------+-----------+------------+---------+


|function |0      |0          |=          |0           |0        |


+---------+-------+-----------+-----------+------------+---------+











External dependencies


---------------------


::





    numpy (arreglo)


    pudb 


      \-set_trace (arreglo)




Raw metrics


-----------





+----------+-------+------+---------+-----------+


|type      |number |%     |previous |difference |


+==========+=======+======+=========+===========+


|code      |11     |64.71 |11       |=          |


+----------+-------+------+---------+-----------+


|docstring |0      |0.00  |0        |=          |


+----------+-------+------+---------+-----------+


|comment   |3      |17.65 |3        |=          |


+----------+-------+------+---------+-----------+


|empty     |3      |17.65 |3        |=          |


+----------+-------+------+---------+-----------+











Messages by category


--------------------




+-----------+-------+---------+-----------+


|type       |number |previous |difference |


+===========+=======+=========+===========+


|convention |3      |3        |=          |


+-----------+-------+---------+-----------+


|refactor   |0      |0        |=          |


+-----------+-------+---------+-----------+


|warning    |2      |2        |=          |


+-----------+-------+---------+-----------+


|error      |1      |1        |=          |


+-----------+-------+---------+-----------+











Messages


--------




+-----------+------------+


|message id |occurrences |


+===========+============+


|W0611      |1           |


+-----------+------------+


|W0402      |1           |


+-----------+------------+


|E0602      |1           |


+-----------+------------+


|C0321      |1           |


+-----------+------------+


|C0111      |1           |


+-----------+------------+


|C0103      |1           |


+-----------+------------+











Global evaluation


-----------------


Your code has been rated at 1.67/10 (previous run: 1.67/10)
```


Si se desea más información de la información generada en el reporte de pylint se puede revisar la documentación antes [mencionada](https://www.logilab.org/card/pylint_manual).

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)