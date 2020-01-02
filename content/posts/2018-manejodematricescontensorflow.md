Title: Manejo de matrices con TensorFlow  
Date: 2018-02-04 09:00  
Category: Tutorial de Python  
Tags: Python,Numpy,TensorFlow
lang: es  
translation: true  


Los artículos anteriores sobre TensorFlow son:

1. [Hola mundo desde TensorFlow](https://www.seraph.to/hola-mundo-desde-tensorflow.html)  
2. [Matemáticas básicas con TensorFlow](https://www.seraph.to/matematicas-basicas-con-tensorflow.html)

En este artículo se explica algunas operaciones con matrices, y funciones que se pueden utilizar con matrices, en el siguiente enlace se encuentra la [documentación de funciones con matrices en TensorFlow](https://www.tensorflow.org/versions/r0.12/api_docs/python/math_ops/matrix_math_functions).

A continuación se muestran los ejemplos usando `jupyter notebook`:

In [1]:
```python
# Se importa numpy y tensorflow
import numpy as np
import tensorflow as tf
```
In [2]:
```python
#Se crea una matriz de 4x4
tensor_2d=np.array([(4,3,2,1),(4,5,6,7),(11,10,9,8),(12,13,14,15)])
```
In [3]:
```python
#Se imprime la matriz
print(tensor_2d)
[[ 4  3  2  1]
 [ 4  5  6  7]
 [11 10  9  8]
 [12 13 14 15]]
```
In [4]:
```python
#Se muestra el elemento 3,3 de la matriz
tensor_2d[3][3]
```
Out[4]:
```
15
```
In [5]:
```python
#Se muestra una sub matriz
tensor_2d[0:2,0:2]
```
Out[5]:
```python
array([[4, 3],
       [4, 5]])
```
In [6]:
```python
#Se crean dos matrices 3x3 de tipo int32
matriz1 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype='int32')
matriz2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype='int32')
```
In [7]:
```python
#Se muestra la matriz 1
print ("Matriz 1-> \n{}".format(matriz1))
Matriz 1-> 
[[2 2 2]
 [2 2 2]
 [2 2 2]]
```
In [8]:
```python
#Se muestra la matriz 2
print ("Matriz 2-> \n{}".format(matriz2))
Matriz 2-> 
[[1 1 1]
 [1 1 1]
 [1 1 1]]
```
In [9]:
```python
#Se define las 2 matrices como objeto tensorflow
matriz1 = tf.constant(matriz1)
matriz2 = tf.constant(matriz2)
```
In [10]:
```python
# Se calcula el producto y la suma de dos matrices
matriz_prod = tf.matmul(matriz1, matriz2)
matriz_suma = tf.add(matriz1,matriz2)
```
In [11]:
```python
#Se crea una matriz 3x3
matriz3 = np.array([(2,7,2),(1,4,2),(9,0,2)],dtype='float32')
```
In [12]:
```python
#Se imprime la matriz3
print ("Matriz 3-> \n{}".format(matriz3))
Matriz 3-> 
[[ 2.  7.  2.]
 [ 1.  4.  2.]
 [ 9.  0.  2.]]
```
In [13]:
```python
#Se calcula la matriz determinante
matriz_det = tf.matrix_determinant(matriz3)
```
In [14]:
```python
#Se crea la sesión y se ejecuta las matrices calculadas
with tf.Session() as sess:
    res1 = sess.run(matriz_prod)
    res2 = sess.run(matriz_suma)
    res3 = sess.run(matriz_det)
```
In [15]:
```python
#Se imprime el producto de las matrices
print ("matriz1*matriz2-> \n{}".format(res1))
matriz1*matriz2-> 
[[6 6 6]
 [6 6 6]
 [6 6 6]]
```
In [16]:
```python
##Se imprime la suma de las matrices
print ("matriz1+matriz2-> \n{}".format(res2))
matriz1+matriz2-> 
[[3 3 3]
 [3 3 3]
 [3 3 3]]
```
In [17]:
```python
# Se imprime el determinante de la matriz 3
print ("det(matriz3)-> {}".format(res3))
det(matriz3)-> 56.00001907348633
```
In [18]:
```python
#Se muestra la dimensión de la matriz1
matriz1.shape
```
Out[18]:
```
TensorShape([Dimension(3), Dimension(3)])
```
In [19]:
```python
#Se crea un arreglo
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
```
In [20]:
```python
#Se muestra el arreglo
a
```
Out[20]:
```python
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
```
In [21]:
```python
#Se muestra el elemento [0,1] 
a[0,1]
```
Out[21]:
```
2
```
In [22]:
```python
#Se muestra el elemento a[0][1], 2 que es igual a a[0,1]
a[0][1]
Out[22]:
2
```
In [23]:
```python
#Se crea el objeto tensorflow del arreglo a
a1 = tf.constant(a)
```
In [24]:
```
#Se muestra el objeto tensorflow
a1
```
Out[24]:
```python
<tf.Tensor 'Const_2:0' shape=(3, 3) dtype=int64>
```
In [25]:
```python
#Se muestra los valores del arreglo
with tf.Session() as sess:
    print(sess.run(a1))
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```
In [26]:
```python
#Se crea un arreglo input, se define como objeto tensorflow
input = np.array([[1, 0, 0, 0],[0, 2, 0, 0],[0, 0, 3, 0],[0, 0, 0, 4]])
with tf.Session() as sess:
    print(sess.run(tf.constant(input)))
[[1 0 0 0]
 [0 2 0 0]
 [0 0 3 0]
 [0 0 0 4]]
```
In [27]:
```python
#Se calcula la matriz diagonal
diag = tf.diag_part(input)
```
In [28]:
```python
#Se muestra la matriz diagonal
with tf.Session() as sess:
    print(sess.run(diag))
[1 2 3 4]
```
In [29]:
```python
#Se muestra la suma de la matriz diagonal
with tf.Session() as sess:
    print(sess.run(tf.trace(input)))
10
```
In [30]:
```python
#Se crea un arreglo y se calcula la traspuesta
b = np.array([[1,2,3],[4,5,6]])
with tf.Session() as sess:
    print(sess.run(tf.transpose(b)))
[[1 4]
 [2 5]
 [3 6]]
```
In [31]:
```python
#Matriz identidad
i = tf.eye(3)
with tf.Session() as sess:
    print(sess.run(i))
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
```
In [32]:
```python
#Se crea una matriz 
diagonal = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
```
In [33]:
```python
#Se muestra las dimensiones de la matriz
diagonal.shape
```
Out[33]:
```python
(2, 4)
```
In [34]:
```python
#Se muestra la matriz diagonal
with tf.Session() as sess:
    print(sess.run(tf.matrix_diag(diagonal)))
[[[1 0 0 0]
  [0 2 0 0]
  [0 0 3 0]
  [0 0 0 4]]

 [[5 0 0 0]
  [0 6 0 0]
  [0 0 7 0]
  [0 0 0 8]]]
```
In [35]:
```python
#Se crea una matriz 
input = np.array([[[1, 0, 0, 0],[0, 2, 0, 0],[0, 0, 3, 0],[0, 0, 0, 4]],
                  [[5, 0, 0, 0],[0, 6, 0, 0],[0, 0, 7, 0],[0, 0, 0, 8]]])
```
In [36]:
```python
#Se muestra las dimensiones de la matriz input
input.shape
```
Out[36]:
```python
(2, 4, 4)
```
In [37]:
```python
#Se muestra la matriz diagonal y sus dimensiones
with tf.Session() as sess:
    res = sess.run(tf.matrix_diag_part(input))
print(res)
print(res.shape)
[[1 2 3 4]
 [5 6 7 8]]
(2, 4)
```
In [38]:
```python
#Se crea una matriz 3x3 y se define como tensorflow de tipo int32
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
a.shape
a = tf.constant(a,shape=[3,3],dtype="int32")
a
```
Out[38]:
```python
<tf.Tensor 'Const_4:0' shape=(3, 3) dtype=int32>
```
In [39]:
```python
#Se crea otra matriz 3x3
b = tf.constant(np.array([[9,8,7],[6,5,4],[3,2,1]]),shape=[3,3],dtype="int32")
b
```
Out[39]:
```python
<tf.Tensor 'Const_5:0' shape=(3, 3) dtype=int32>
```
In [40]:
```python
#Se realiza la multiplicación de las matrices a y b
c = tf.matmul(a, b)
```
In [41]:
```python
#Se muestra el resultado de la multiplicación y las dimensiones de la nueva matriz
with tf.Session() as sess:
    res = sess.run(c)
print(res)
print(res.shape)
[[ 30  24  18]
 [ 84  69  54]
 [138 114  90]]
(3, 3)
```
In [42]:
```python
#Se define la matriz 3x3 como objeto tensorflow de tipo float32
input = tf.constant(np.array([[1,0,0],[-1,2,3],[0,1,2]]),shape=[3,3],dtype="float32")
```
In [43]:
```python
#Se calcula la matriz inversa de la matriz anterior
inverse = tf.matrix_inverse(input)
```
In [44]:
```python
#Se muestra el objeto tensorflow de la matriz inversa.
inverse
```
Out[44]:
```python
<tf.Tensor 'MatrixInverse:0' shape=(3, 3) dtype=float32>
```
In [45]:
```python
#Se muestra los elementos de la matriz inversa calculada de la matriz input
with tf.Session() as sess:
    print(sess.run(inverse))
[[ 1.  0.  0.]
 [ 2.  2. -3.]
 [-1. -1.  2.]]
```
In [46]:
```python
#Se crea una matriz 4x4 con puros números 10.
fill_mat = tf.fill((4,4),10)
```
In [47]:
```python
#Se muestra la matriz
with tf.Session() as sess:
    print(sess.run(fill_mat))
[[10 10 10 10]
 [10 10 10 10]
 [10 10 10 10]
 [10 10 10 10]]
```
In [48]:
```python
#Se crea una matriz 4x4 de ceros
ceros_mat = tf.zeros((4,4))
```
In [49]:
```python
#Se muestra la matriz
with tf.Session() as sess:
    print(sess.run(ceros_mat))
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
```
In [50]:
```python
#Se crea una matriz 4x4 de puros 1s.
unos_mat = tf.ones((4,4))
```
In [51]:
```python
#Se muestra la matriz
with tf.Session() as sess:
    print(sess.run(unos_mat))
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]
```
In [52]:
```python
#Se crea una matriz 4x4 de números aleatorios
random = tf.random_normal((4,4),mean=0,stddev=1.0)
```
In [53]:
```python
#Se muestra la matriz
with tf.Session() as sess:
    print(sess.run(random))
[[ 0.48763195 -0.30092272  0.19232044  0.31226188]
 [-0.41430238  0.42101797  1.77855754  0.07280751]
 [-1.41810405 -0.58018923 -0.43785188 -0.41393659]
 [ 1.32442439 -0.78680986 -0.47751999  0.87710148]]
```
In [54]:
```python
#Se crea una matriz 4x4 de números aleatorios uniformes,con valor mínimo 0 y un valor máximo 1s. 
ramdonu = tf.random_uniform((4,4),minval=0,maxval=1)
```
In [55]:
```python
#Se muestra la matriz
with tf.Session() as sess:
    print(sess.run(ramdonu))
[[ 0.89437163  0.44275856  0.09911788  0.81197321]
 [ 0.60750782  0.93167293  0.31275058  0.85452628]
 [ 0.36725163  0.51979959  0.61648357  0.43575656]
 [ 0.26617634  0.65706372  0.2386142   0.88543487]]
```
In [56]:
```python
#Se crea una lista de los objetos tensorflow.
operaciones = [fill_mat,ceros_mat,unos_mat,random,ramdonu]
```
In [57]:
```python
#Se crea una sesión interactiva, se usa normalmente con jupyter.
sess = tf.InteractiveSession()
```
In [58]:
```python
#Se muestra las matrices
for op in operaciones:
    print(sess.run(op))
    print("\n")
[[10 10 10 10]
 [10 10 10 10]
 [10 10 10 10]
 [10 10 10 10]]


[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]


[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]


[[-0.58866209  0.9165706   0.80280447  0.49312767]
 [ 1.59473944  0.52477682  2.11727142  1.67061532]
 [ 0.02045015 -0.41936889 -0.86903268 -0.41808063]
 [ 0.68307805  1.5401181  -0.66720027 -0.79585057]]


[[ 0.17621791  0.11907017  0.93286264  0.74120772]
 [ 0.11641097  0.11936057  0.59562981  0.13035727]
 [ 0.87772381  0.30514657  0.91652596  0.08015275]
 [ 0.41316867  0.63185382  0.94313562  0.97722518]]
```

In [59]:
```python
#Se muestra las matrices usando eval
for op in operaciones:
    print(op.eval())
    print("\n")
[[10 10 10 10]
 [10 10 10 10]
 [10 10 10 10]
 [10 10 10 10]]


[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]


[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]


[[-1.56096065 -0.07210996 -0.25554755  0.4873071 ]
 [-1.46382582  1.37537384 -0.5594331  -0.14968663]
 [-0.38434446  1.24772871  0.90822452 -0.72924012]
 [ 0.85642397  0.3183746  -0.10567457 -1.39979196]]


[[ 0.57379103  0.7317698   0.02952981  0.26845372]
 [ 0.95550442  0.10524487  0.68452525  0.94136262]
 [ 0.17415774  0.6024276   0.51809859  0.86097646]
 [ 0.0080744   0.9969902   0.47532237  0.76927459]]

```

Continuaré con la serie de artículos sobre TensorFlow.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)

