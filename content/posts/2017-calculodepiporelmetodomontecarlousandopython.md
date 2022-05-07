Title: Cálculo de Pi por el método MonteCarlo usando Python.
Date: 2017-05-08 09:00
Category: Tutorial Python
Tags: General,Numpy,Python,Método de Montecarlo
lang: es
translation: true

El método MonteCarlo es un método estadístico numérico que se usa para aproximar expresiones matemáticas complejas y costosas de evaluar conexactitud. Para más información pueden revisar [wikipedia](http://es.wikipedia.org/wiki/M%C3%A9todo_de_Montecarlo).

La expresión matemática que se va a resolver es el cálculo de Pi.

En este artículo mostraré dos versiones del uso del Método MonteCarlo.

El primer ejemplo el algoritmo fue tomado de un código en Pascal y llevado a Python. A continuación el código:

```python
#!/usr/bin/env python

#Se importa el modulo random

import random



#Se define la funcion

def Pi(limite=10000000):

    dentro = 0

    contador = 0

    #Se hace un ciclo hasta que contador sea igual al limite

    while contador < limite:

        #Se calcula  que los puntos esten dentro del radio del circulo

        #Si es asi se incrementa la variable dentro. y luego se incrementa

        #contador para pasar al siguiente ciclo.

        if ((random.random()**2 + random.random()**2) <= 1):

            dentro += 1

        contador += 1

    #Se retorna el resultado de la cantida de puntos dentro del circulo

    #entre el limite por 4.

    return 4.0*float(dentro)/limite



if __name__ == "__main__":

    n = (10000, 1000000,100000000)

    for i in n:

        print ("El valor de pi es: {0:2.8f} para n {1}".format(Pi(i),i))

```  

Al ejecutar el código se tiene:

```
El valor de pi es: 3.14960000 para n 10000
El valor de pi es: 3.14308000 para n 1000000
El valor de pi es: 3.14141900 para n 100000000
```

Al aumentar el valor de n se logra tener un número más preciso del valor de PI, claro también se llevará más tiempo en calcular.

En el siguiente ejemplo se basa en un articulo en inglés publicado en Medium que se llama [Day 9: Monte Carlo Pi](http://medium.com/100-days-of-algorithms/day-9-monte-carlo-%CF%80-7ae010743bde) y el código del mismo se encuentra en [github](http://github.com/coells/100days/blob/master/day%2009%20-%20monte%20carlo%20-%20pi.ipynb).

El código se muestra a continuación:

```python

#!/usr/bin/env python

#Se importa el modulo numpy

import numpy as np





def pi(n, batch=1000):

    t = 0

    for i in range(n // batch):

        p = np.random.rand(batch, 2)

        p = (p * p).sum(axis=1)

        t += (p <= 1).sum()

    return 4 * float(t) / n





if __name__ == "__main__":

    print ("El valor de pi es: {0:2.8f} para n {1}".format(pi(10**8),10**8))

```

Al ejecutarlo se obtiene:
```
El valor de pi es: 3.14146076 para n 100000000
```

Como ven la última versión es menos la cantidad de líneas de código y más rápida. 



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
