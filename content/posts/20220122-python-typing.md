Title: Introducción a anotación y tipos en Python
Date:  2022-01-22 12:00
Category: Tutorial Python
Tags: python,typing,pydantic,mypy
lang: es
translation: true
Slug: python_typing
Authors: Ernesto Crespo
Summary: Conozca como usar la verificación del tipado estático y las mejores prácticas


Artículos anteriores se tocó el tema de uso de dataclass, pydantic y orjson y como usar el tipado, en este artículo se explicará las mejores prácticas:

* [Dataclases en Python](https://www.seraph.to/python_dataclass.html#python_dataclass)
* [Validación de datos con Pydantic](https://www.seraph.to/python_pydantic.html#python_pydantic)
* [Introducción a orjson](https://www.seraph.to/python_orjson.html#python_orjson)

La verificación de tipos aparte de ayudar a entender mejor el código facilita la detección de errores rapidamente y automáticamente usando por ejemplo mypy. La verificación de tipos se incorporó en Python desde la versión 3.5. 


Este artículo se basa en el artículo en inglés: [Improving Your Python Projects With Type Hints](https://betterprogramming.pub/improving-your-python-projects-with-type-hints-63cbdb16d97c)

## Sintaxis de tipado

Python soporta anotaciones de tipos para variables básicas soportadas por el lenguaje str, int, float, bool y None. Viene incorporada en la librería typing.

### Anotación de variables

Se puede indicar el tipo de una variable al usar los dos puntos ":". Por ejemplo: 


```python 

from typing import List

nombre: str = 'Pedro'
edad: int = 24
altura_mts: float = 1.7
colegas: List[str] = ['Jane', 'John']

```

Se define el tipo y el valor que tendrá esa variable. 


### Anotación en las funciones

En el caso de las funciones se puede colocar anotaciones en las variables de los argumentos, así como en la salida de la función. 


```python 

from typing import Dict, List
import math 

def calc_area_circulo(radio: float) -> float:
    return math.pi*(radio**2)
  
def send_email(
    subject: str,
    body: str,
    recipients: List[str],
    cache: Dict[str, str]
) -> bool:
  
    # .... 
    # Devuelve True o False el envío de un correo

    return True 
```

En la primera función se pasa como argumento el radio de tipo flotante y devuelve el resultado del área del circulo que es flotante también. 

EN el siguiente ejemplo se define una función que recibe subject (string), body (string),recipients (lista de string), cache (diccionario que tiene llaves de string y valores de string) y la función devuelve boleano. 

### Usar tipos especiales

Existe una serie de tipos que complementan a los básicos: 

* Any: 
* Literal: 
* Union
* TypeDict
* NoReturn
* Final


#### Any 

Una variable tipo Any es compatible con todas los tipos básicos. 

```python 

from typing import Any

resultado: Any = "Procesado"
  
resultado = 10

estatus: str = "Pendiente"

estatus = resultado


```
En el primer caso se define la variable resultado tipo Any que se le asigna un string, luego se le asigna un entero, el cual no es problema por que el tipo Any lo soporta. Luego se define la variable estatus de tipo string y asignando un string, luego sin problemas se asigna resultado a la variable estatus; esto tampoco es problema por que resultado es tipo any.


#### Literal

El tipo literal se usa para indicar que tiene un valor igual a los valores indicados (tipos). 

```python 


from typing import Literal


GENERO = Literal["hombre", "mujer", "no especificado"]

def crear_usuario(
    nombre: str,
    apellido: str,
    genero: GENERO,
) -> Dict[str, str]:
    return {
        "nombre": nombre,
        "apellido": apellido,
        "genero": genero
    }

crear_usuario("John", "Doe", "hombre")

{'nombre': 'John', 'apellido': 'Doe', 'genero': 'hombre'}

```

Se define una lista para el genero de tipo literal, y el tipo es uno de los definidos (hombre, mujer, no especificado). 


#### Union

Algunas variables a veces necesitan dos tipos básicos. 

```python 

from typing import Union


def get_temperatura() -> Union[int, float]:
    return 20.8  # funciona también con 20.

```

Se define una función que devuelve  entero o flotante, esto se logra usando Union. 


#### TypedDict

TypedDict permite definir un tipo de dato diccionario. 

```python 

from typing import TypedDict, Union


class Card(TypedDict):
    rank: Union[str, int]
    suit: str

# The Card class now has behaviours of both TypedDict and dict classes

# Card can be used to annotate a variable
ace_of_spade: Card = {'rank': 'A', 'suit': '♤'}

# or can be instantiated
ace_of_spade = Card(rank='A', suit='♤')

print(ace_of_spade)

{'rank': 'A', 'suit': '♤'}

```

#### NoReturn

NoReturn es similar to void en otros lenguajes de programación, en mi caso antes usaba None cuando una función no devuelve nada. 

```python 

from typing import NoReturn

def hola1() -> None:
    print("Hola Mundo!")

def hola2() -> NoReturn:
    print("Hola Mundo!")

```

Se definen dos funciones hola, la primera como None y la segunda como NoReturn, que es como debe definirse una función que no devuelve un valor. 

#### Final


Este tipo de dato se define para no redefinir un valor. 

```python 


from typing import Final


MIN_NOMBRE_LONG: Final = 2

# mypy reporta error por que se le está asignando un nuevo valor a la
# variable
MIN_NOMBRE_LONG += 1


class Validador(object):
    MIN_NOMBRE_LONG: Final[int] = 4

class UserValidador(Validador):
    # El interprete marca una bandera en esta línea
    MIN_NOMBRE_LONG = 3

```

### Uso de verificadores de tipo

Uno de los más usados verificadores de tipos es mypy. Se puede instalar usando pip:

```bash 

pip install mypy 

```

Para usarlo simplemente se llama a mypy y se le pasa el archivo a verificar. 

El código a validar se muestra a continuación: 

```python 

#!/usr/bin/env python3

from typing import Literal, Dict


GENERO = Literal["hombre", "mujer", "no especificado"]


def crear_usuario(
    nombre: str,
    apellido: str,
    genero: GENERO,
) -> Dict[str, str]:
    return {
        "nombre": nombre,
        "apellido": apellido,
        "genero": genero
    }


crear_usuario("John", "Doe", "hombre")
crear_usuario("Jane", "Doe", "mujer")
crear_usuario("John", "Doe", "x")

```

Este código devolverá error al intentar crear un usuario con genero x.

```bash 

mypy   pruebas_typing.py
content/code/pruebas_typing.py:23: error: Argument 3 to "crear_usuario" has incompatible type "Literal['x']"; expected "Union[Literal['hombre'], Literal['mujer'], Literal['no especificado']]"
Found 1 error in 1 file (checked 1 source file)
```

Este es el mensaje de error que devuelve al intentar colocar un valor x en el genero. 


La notación de tipo y la verificación nos facilita validar que una variable tenga un tipo de datos siempre y no cambie, a mí me paso hace poco que hice una función que devolvía una lista, tiempo después un desarrollador cambio la lista por un diccionario, y la función funcionaba, pero al pasarle mypy. 



---
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
