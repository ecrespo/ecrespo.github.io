Title: Hola Mundo desde TensorFlow  
Date: 2018-02-04 08:00  
Category: Tutorial Python  
Tags: Python, TensorFlow
lang: es  
translation: true  


[TensorFlow](https://www.tensorflow.org/) es una biblioteca de código abierto para aprendizaje automático (Machine Learning) a través de un rango de tareas y desarrollado por Google para satisfacer sus necesidades de sistemas capaces de construir y entrenar redes neuronales para detectar y descifrar patrones y correlaciones, análogos al aprendizaje y razonamientos usados por los humanos (más información en [wikipedia](https://es.wikipedia.org/wiki/TensorFlow)).

Para instalar en Linux se usa pip:
```
pip3 install TensorFlow
```

El primer ejercicio que se hará es el de escribir un Hola mundo desde TensorFlow (se usa jupyter notebook).

In [1]:
```python
#Se importa tensorflow
import tensorflow as tf
```
In [2]:
```python
#Se crea una constante en la variable hola, donde se le pasa un string
hola = tf.constant("Hola mundo desde TensorFlow!")
```
In [3]:
```python
#Veamos que devuelve la variable hola
print(hola)
Tensor("Const:0", shape=(), dtype=string)
```
#### Devuelve un objeto tensor, con una constante de tipo string

In [4]:
```python
hola
```
Out[4]:
```python
<tf.Tensor 'Const:0' shape=() dtype=string>
```
In [5]:
```python
#Se crea la sesión de tensorflow
sess=tf.Session()
```
In [6]:
```python
#Se corre la sesión pasandole la variable hola
print(sess.run(hola))
b'Hola mundo desde TensorFlow!'
```
In [ ]:
```

```
 
Como se puede ver, para poder visualizar el valor de una constante de TensorFlow se 
tiene que crear la sesión y ejecutar en la sesión la constante.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
