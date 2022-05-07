Title: Variables y placeholders en Tensorflow  
Date: 2018-02-10 09:00  
Category: Tutorial de Python  
Tags: Python,TensorFlow
lang: es  
translation: true  

Continuando con la serie sobre Tensorflow, se tienen los siguientes artículos:

1. [Hola mundo desde TensorFlow](https://www.seraph.to/hola-mundo-desde-tensorflow.html)  
2. [Matemáticas básicas con TensorFlow](https://www.seraph.to/matematicas-basicas-con-tensorflow.html)
3. [Manejo de matrices con Tensorflow](https://www.seraph.to/manejo-de-matrices-con-tensorflow.html) 

El objeto Variable de Tensorflow permite definir una variable (almacenar un estado en un objeto Graph con un valor inicial), en cambio, el objeto placeholder se usa para agregar datos externos dentro de un Objeto Graph, pero los datos a agregar no se agregan al crear el placeholder, para ello se usa la inicialización de las variables.

A continuación el ejemplo de uso de variables y placeholder desde `jupyter notebook`:

In [1]:
```python
#Se importa tensofflow
import tensorflow as tf
```
In [2]:
```python
#Se crea una sesión interactiva ( útil cuando se usa jupyter notebook)
sess = tf.InteractiveSession()
```
In [3]:
```python
#Se crea tensor como un número uniforme aleatorio, una matrix de 4x4, de elementos
#de valores entre 0 a 1.
tensor = tf.random_uniform((4,4),0,1)
```
In [4]:
```python
#tensor es un objeto Tensor, de números aleatorios uniformes, de una matrix 4x4 y de typo float32.
tensor
```
Out[4]:
```python
<tf.Tensor 'random_uniform:0' shape=(4, 4) dtype=float32>
```
In [5]:
```python
#se crea variable como un objeto variable que se le pasa como valor inicial el objeto tensor.
variable = tf.Variable(initial_value=tensor)
```
In [6]:
```python
#Se imprime el valor de la variable, 
#esta devuelve tipo Variable, con una matriz 4x4 con elementos de tipo float32
print(variable)

<tf.Variable 'Variable:0' shape=(4, 4) dtype=float32_ref>
```
In [7]:
```python
#Se inicializa las variables con init
init = tf.global_variables_initializer()
```
In [8]:
```python
#Se corre la inicialización
sess.run(init)
```
In [9]:
```python
#Se muestra el valor de la variable corriendo la sesión, se nota los elementos
#entre 0 a 1 y de tipo float32
sess.run(variable)
```
Out[9]:
```python
array([[0.05263364, 0.94140494, 0.4843645 , 0.36463213],
       [0.9149779 , 0.01328921, 0.3837136 , 0.7204586 ],
       [0.5955255 , 0.70812213, 0.19933975, 0.40913558],
       [0.359192  , 0.82358146, 0.1225971 , 0.24963093]], dtype=float32)
```
In [10]:
```python
#Se crea el placeholder, lo cual reserva el espacio, pero no tiene datos como una variable.
ph = tf.placeholder(tf.float32,shape=(None,5))
```
In [11]:
```python
#Se muestra el objeto placeholder, sólo tiene definido el tipo de datos el cual es float32
print(ph)

Tensor("Placeholder:0", shape=(?, 5), dtype=float32)
```
In [ ]:
```
 
```

En próximo artículo se explicará el uso de Graph.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
