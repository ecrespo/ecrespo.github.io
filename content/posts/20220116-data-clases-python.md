Title: Dataclases en Python
Date:  2022-01-16 15:45
Category: Tutorial Python
Tags: dataclass
lang: es
translation: true
Slug: python_dataclass
Authors: Ernesto Crespo
Summary: Este artículo como crear dataclases y su utilidad

Los artículos en que se basa este artículo son: 

* [Data Classes in Python](https://justgiveacar.medium.com/data-classes-in-python-991a3f68ddf9)
* [9 Reasons Why You Should Start Using Python Dataclasses](https://towardsdatascience.com/9-reasons-why-you-should-start-using-python-dataclasses-98271adadc66)


Data clases en python permiten escribir menos código, y está soportado en python a partir de la versión 3.7. 


## Clases regulares

Se comenzará con una clase simple en Python llamada perro, con un método init donde se toma los argumentos de la clase como atributos:

* Nombre: Tipo string.
* Raza: Tipo string.
* Edad: Tipo entero.


```python 

class Perro:
    nombre: str
    raza: str
    edad: int
      
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad

```

Se instancia tres mascotas con la clase Perro: 

```python 

mascota1 = Perro('RUDY', 'Terrier Australiano', 2)
mascota2 = Perro('TEDDY', 'bichón frisé', 2)
mascota3 = Perro('TEDDY', 'bichón frisé', 2)

```

Se compara la mascota 2 con al 3:

```python
mascota2 == mascota3

False
```

A pesar que ambas mascotas tienen los mismos datos en sus atributos, si se hace una comparación devuelve falso. 

Una opción es usar un método para la comparación atributo por atributo. 



Se imprime el contenido de la mascota2: 
```python

print(mascota2)


<__main__.Perro object at 0x7f9c104e7640>

```

Lo que se muestra es el id en memoria de la instancia de Perro.

Para mostrar el contenido se toma cada atributo: 
```python
print(mascota2.nombre,mascota2.raza,mascota2.edad)

TEDDY bichón frisé 2


```

## Data clases

Para poder usar dataclass se tiene que instalar vía pip: 

```bash 
pip install dataclasses
```

Se tomara la misma clase de Perro, esta vez usando un decorador de dataclass. 

Importar dataclass: 

```python

from dataclasses import dataclass

```

Se define la clase Perro con los mismos atributos de la clase anterior: 

```python 

@dataclass
class Perro:
    nombre: str
    raza: str
    edad: int

```

Se define la clase y cada atributo se le define el tipo y nada más. 

Ahora se crean las mascotas: 

```python 

mascota1 = Perro('RUDY', 'Terrier Australiano', 2)
mascota2 = Perro('TEDDY', 'bichón frisé', 2)
mascota3 = Perro('TEDDY', 'bichón frisé', 2)

```

Ahora al comparar la mascota 2 y 3, no devolverá falso: 

```python 

print(mascota2 == mascota3)

True

```

A continuación se imprime el contenido de la mascota2: 

```python 

print(mascota2)

Perro(nombre='TEDDY', raza='bichón frisé', edad=2)

```

Ahora no devuelve el Id, devuelve la clase perro con los valores del atributo que se le asignaron a la mascota2.

También se puede acceder a los datos de los atributos: 

```python 
print(mascota2.nombre,mascota2.raza,mascota2.edad)

TEDDY bichón frisé 2


```

Se puede agregar el método __repr__ a la clase para que de información en un string formateado:

```python 
@dataclass
class Perro:
    nombre: str
    raza: str
    edad: int
    
    def __repr__(self):
        return f"{self.nombre} {self.raza} ({self.edad})"


mascota1 = Perro('RUDY', 'Terrier Australiano', 2)
mascota2 = Perro('TEDDY', 'bichón frisé', 2)
mascota3 = Perro('TEDDY', 'bichón frisé', 2)


print(mascota2)

TEDDY bichón frisé (2)

```


Aparte de comparar si son iguales, se puede comparar si la mascota1 es mayor que la 2. 

```python

print(mascota1  > mascota2)
```

Esto devuelve error, esta comparación no está soportada:

```bash
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_603591/468771088.py in <module>
----> 1 mascota1  > mascota2

TypeError: '>' not supported between instances of 'Perro' and 'Perro'
```

Para poder compararlos es necesario usar el método __post_init__.  El atributo para la comparación será la edad, el código quedará así: 

```python 

from dataclasses import dataclass, field

@dataclass
class Perro:
    sort_index: int = field(init=False)
    nombre: str
    raza: str
    edad: int
    
    def __repr__(self):
        return f"{self.sort_index} {self.nombre} {self.raza} ({self.edad})"  
    
    def __post_init__(self):
      self.sort_index = self.edad

```

Se muestra los argumentos: 

```python 

mascota1 = Perro('RUDY', 'Terrier Australiano', 3)
mascota2 = Perro('TEDDY', 'bichón frisé', 2)
print(mascota2)

#2 TEDDY bichón frisé (2)


print(mascota2.sort_index,mascota2.nombre,mascota2.raza,mascota2.edad)

#2 TEDDY bichón frisé 2

```

Se intenta comparar de nuevo: 

```python 
print(mascota1 > mascota2)
```

Devuelve error: 
```bash
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
/tmp/ipykernel_603591/4142115589.py in <module>
----> 1 mascota1 > mascota2

TypeError: '>' not supported between instances of 'Perro' and 'Perro'
```


## Clases de solo lectura

Se puede crear clases de sólo lectura para evitar que se modifique sus valores iniciales.


Para poder resolver este error se usa el argumento order en el decorador, y se define sólo lectura:

```python 

@dataclass(order=True, frozen=True)
class Perro:
    sort_index: int = field(init=False)
    nombre: str
    raza: str
    edad: int
    
    def __post_init__(self):
      object.__setattr__(self, 'sort_index', self.edad)

mascota1 = Perro('RUDY', 'Terrier Australiano', 3)
mascota2 = Perro('TEDDY', 'bichón frisé', 2)
```

Ahora se hace la comparación y no devuelve error: 

```python 
print(mascota1  > mascota2)

True
```

Se muestra el contenido de la mascota 2: 

```python 

print(mascota2)


Perro(sort_index=2, nombre='TEDDY', raza='bichón frisé', edad=2)


```

Si se intenta asignar un valor a la edad de la mascota 2, devolverá error:

```python 

mascota2.edad = 4

```

```bash 

---------------------------------------------------------------------------
FrozenInstanceError                       Traceback (most recent call last)
/tmp/ipykernel_603591/927787478.py in <module>
----> 1 mascota2.edad = 4

<string> in __setattr__(self, name, value)

FrozenInstanceError: cannot assign to field 'edad'

```

Como se puede ver las dataclasses puede facilitar en la validación de datos de los atributos de los objetos que se definan. En próximo artículo se verá el módulo pydantic que extiende esta característica de validación de datos. 

---
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
