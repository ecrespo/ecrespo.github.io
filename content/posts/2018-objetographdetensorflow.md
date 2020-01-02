Title: Objeto Graph de TensorFlow  
Date: 2018-02-11 11:00  
Category: Tutorial de Python  
Tags:Python,TensorFlow
lang: es  
translation: true

Continuando con la serie de artículos sobre Tensorflow, en este caso se explicará el significado y uso de Grapg.

Antes de continuar les dejo la lista de artículos de esta serie:

1. [Hola mundo desde TensorFlow](https://www.seraph.to/hola-mundo-desde-tensorflow.html)  
2. [Matemáticas básicas con TensorFlow](https://www.seraph.to/matematicas-basicas-con-tensorflow.html)
3. [Manejo de matrices con Tensorflow](https://www.seraph.to/manejo-de-matrices-con-tensorflow.html) 
4. [Variables y placeholders en Tensorflow](https://www.seraph.to/variables-y-placeholders-en-tensorflow.html)  

`tf.Graph`:
Cada computo en Tensorflow es representado por un Grafo de flujo de datos, este tiene dos elementos: 

- Un objeto tf.Operation, que representa la unidad de computo.  
- Un objeto tf.Tensor, que representa unidades de datos,  que se necesita para las operaciones.

A continuación se muestra una figura de la representación de un Grafo:

![](./images/objetographdetensorflow-1.png) 

A continuación se muestra el uso de Graph:

In [1]:
```python
#Se importa tensorflow
import tensorflow as tf
```
In [2]:
```python
#Se define dos constantes
n1 = tf.constant(10)
n2 = tf.constant(20)
```
In [3]:
```python
#Se realiza la suma de las dos constantes
n3 = n1+n2
```
In [4]:
```python
#Se instancia la sesión y se ejecuta almacenando el resultado de n3 que se muestra

with tf.Session() as sess:
    result = sess.run(n3)
print (result)

30
```
In [5]:
```python
#Se imprime la constante n3, es una suma, y de tipo int32
print(n3)

Tensor("add:0", shape=(), dtype=int32)
```
In [6]:
```python
#Se obtiene el valor por defecto del grafo en memoria
print (tf.get_default_graph())

<tensorflow.python.framework.ops.Graph object at 0x7f1026aa1cf8>
```
In [7]:
```python
#Se instancia el objeto grafo 
g = tf.Graph()
```
In [8]:
```python
#Se imprime su valor, los valores en memoria serán distintos del por defecto al creado.
print(g)

<tensorflow.python.framework.ops.Graph object at 0x7f1026ad00b8>
```
In [9]:
```python
#Se define graph1 como el grafo por defecto
graph1 = tf.get_default_graph()
```
In [10]:
```python
#Se imprime graph1, será el valor por defecto en memoria
print(graph1)

<tensorflow.python.framework.ops.Graph object at 0x7f1026aa1cf8>
```
In [11]:
```python
#Se instancia el grafo2
graph2 = tf.Graph()
```
In [12]:
```python
#Se muestra el valor de grafo2
print(graph2)

<tensorflow.python.framework.ops.Graph object at 0x7f1026ad0390>
```
In [13]:
```python
#Se define el grafo2 como si fuera  por defecto y se muestra si en verdad es por defecto 
with graph2.as_default():
    print(graph2 is tf.get_default_graph())

True
```
In [14]:
```python
#Se evalua si grafo 2, es el de por defecto
print(graph2 is tf.get_default_graph())

False
```
Otro ejemplo de Grafo  

In [15]:
```python
#Se define el grafo
grafo = tf.Graph()
```
In [16]:
```python
#Se define la sesión pasandole el grafo
with tf.Session(graph=grafo) as sess:
    #Se define las constantes x y y que son arreglos
    x = tf.constant([11,13,16])
    y = tf.constant([10,10,10])
    #Se realiza la operación de suma de x+y
    op = tf.add(x,y)
    #Se ejecuta la operación en la sesión
    resultado = sess.run(fetches=op)
    print(resultado)

[21 23 26]
```
In [ ]:
```

```
 
Si quiere investigar más sobre Graph puede revisar su documentación en tensorflow ([documentación del api](http://www.tensorflow.org/api_docs/python/tf/Graph) y [guía para los progamadores](http://www.tensorflow.org/programmers_guide/graphs)), pueden revisar el artículo en [medium Tensorflow in a nutshell-Part 1: Basics](http://medium.com/@camrongodbout/tensorflow-in-a-nutshell-part-one-basics-3f4403709c9d), también pueden revisar el tutorial de la gente de datacamp [Tensorflow tutorial for beginners](http://www.datacamp.com/community/tutorials/tensorflow-tutorial).


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
