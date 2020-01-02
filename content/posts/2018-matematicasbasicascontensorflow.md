Title: Matemáticas básicas con TensorFlow   
Date: 2018-02-04 15:00  
Category: Tutorial de Python  
Tags: Numpy,Python, TensorFlow
lang: es  
translation: true  

En el [artículo anterior](https://www.seraph.to/hola-mundo-desde-tensorflow.html) se explicó la instalación y mostrar un "hola mundo" desde TensorFlow.

En este artículo se explicará el uso de constantes y variables,  al principio con un arreglo de 1 dimensión de 4 elementos, como se convierte un arreglo numpy a un objeto TensorFlow y mostrar sus elementos; luego se muestra como manejar la ecuación y = x+1 con x = 9.


Manejo de un arreglo de una dimensión con tensorflow
In [1]:
```python
#Se importa numpy y tensorflow
import numpy as np
import tensorflow as tf
```
In [2]:
```python
#Se crea un arreglo de una dimensión
tensor_1d = np.array([5.7, 2, 8.0, 25.99])
```
In [3]:
```python
#Se imprime el arreglo
print (tensor_1d)
[  5.7    2.     8.    25.99]
```
In [4]:
```python
#Se imprime el último elemento del arreglo -> 25.99
print (tensor_1d[-1])
25.99
```
In [5]:
```python
#Dimensiones del arreglo -> 1 dimensión
tensor_1d.ndim
```
Out[5]:
```python
1
```
In [6]:
```python
#Cantidad de elementos del arreglo -> 4 elementos
tensor_1d.shape
```
Out[6]:
```python
(4,)
```
In [7]:
```python
#Tipo de los elementos que contiene el arreglo ->float64
tensor_1d.dtype
```
Out[7]:
```python
dtype('float64')
```
In [8]:
```python
#Convierte el arreglo a un objeto tensorflow
tf_tensor=tf.convert_to_tensor(tensor_1d,dtype=tf.float64)
```
In [9]:
```python
# tipo tensor, constante, 4 elementos y de tipo float64
tf_tensor
```
Out[9]:
```python
<tf.Tensor 'Const:0' shape=(4,) dtype=float64>
```
In [10]:
```python
# Se inicia sesión tensorflow y se corre la la impresión de los elementos
with tf.Session() as sess:
    print (sess.run(tf_tensor))
    print (sess.run(tf_tensor[-1]))
[  5.7    2.     8.    25.99]
25.99
```
#### Ahora se va a realizar un cálculo de una ecuación con unas variables:
```
x = 1  
y = x + 9  
print(y)  
import tensorflow as tf  
x = tf.constant(1,name='x')  
y = tf.Variable(x+9,name='y')  
print(y)  
``` 
In [13]:
```python
#Se define el valor de la constante x = 1
x = tf.constant(1,name='x')
```
In [14]:
```python
#Se define el valor de la variable y = x+9
y = tf.Variable(x+9,name='y')
```
In [16]:
```python
#Se imprime el valor de y, que devuelve el tipo de objeto tensor flow, la variable y, no tiene elementos
#y es de tipo int32.
print(y)
<tf.Variable 'y:0' shape=() dtype=int32_ref>
```
#### Para que funcione se tiene que crear la sesión y ejecutar run

In [20]:
```python
# Inicializa todas las variables
model = tf.global_variables_initializer()
```
In [22]:
```python
#Se inicia la sesión, se corre model y luego y. El resultado es y -> 10
with tf.Session() as session:
    session.run(model)
    print(session.run(y))
10
```
In [ ]:
```

```
 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
