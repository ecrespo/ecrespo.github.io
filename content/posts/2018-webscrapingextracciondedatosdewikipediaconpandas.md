Title: WebScraping (extracción de datos) de wikipedia con Pandas   
Date: 2018-04-19 09:00  
Category: Tutorial Python
Tags: Python,Webscraping,Pandas,Wikipedia
lang: es  
translation: true  

Continuando con la serie de artículos sobre [Pandas](https://www.seraph.to/tag/pandas.html), en este artículo se muestra un proceso de extracción de datos web de la [página que contiene información sobre  los Estados de Venezuela de Wikipedia](https://es.wikipedia.org/wiki/Estados_de_Venezuela).

En los procesos anteriores de WebScraping se trabajaba practicamente a mano para indentificar  las secciones del código html donde se encuentra la información útil, para el caso con Pandas este abstrae ese proceso.

A continuación se muestra una captura de pantalla de la página donde se quiere extraer la información:

![](./images/webscrapingextracciondedatosdewikipediaconpandas-1.png)

La información que maneja la página son los estados con sus capitales, densidad poblacional, superficie, año de admisión, población, densidad, región y código ISO, la parte de la bandera ni del mapa no se muestra por que son imágenes y no se obtiene información útil de ellas.

A continuación todo el proceso de extracción de información de la página:

In [1]:
```python
#Se importa pandas como pd
import pandas as pd
#Se lee los datos de wikipedia de los estados de venezuela, este devuelve una lista
estados=   pd.read_html('https://es.wikipedia.org/wiki/Estados_de_Venezuela') 
estados
```
Out[1]:
```python
[    0                                                  1
 0 NaN  Este artículo o sección necesita referencias q...,
                                                    0
 0                     Estados Federales de Venezuela
 1  Bolívar Amazonas Apure Zulia Táchira Barinas M...,
           0                       1                       2           3  \
 0   Bandera         Entidad federal                 Capital  Código ISO   
 1       NaN                Amazonas         Puerto Ayacucho        VE-Z   
 2       NaN              Anzoátegui               Barcelona        VE-B   
 3       NaN                   Apure   San Fernando de Apure        VE-C   
 4       NaN                  Aragua                 Maracay        VE-D   
 5       NaN                 Barinas                 Barinas        VE-E   
 6       NaN                 Bolívar          Ciudad Bolívar        VE-F   
 7       NaN                Carabobo                Valencia        VE-G   
 8       NaN                 Cojedes              San Carlos        VE-H   
 9       NaN           Delta Amacuro                Tucupita        VE-Y   
 10      NaN        Distrito Capital                 Caracas        VE-A   
 11      NaN                  Falcón                    Coro        VE-I   
 12      NaN                 Guárico  San Juan de Los Morros        VE-J   
 13      NaN                    Lara            Barquisimeto        VE-K   
 14      NaN                  Mérida                  Mérida        VE-L   
 15      NaN                 Miranda              Los Teques        VE-M   
 16      NaN                 Monagas                 Maturín        VE-N   
 17      NaN           Nueva Esparta             La Asunción        VE-O   
 18      NaN              Portuguesa                 Guanare        VE-P   
 19      NaN                   Sucre                  Cumaná        VE-R   
 20      NaN                 Táchira           San Cristóbal        VE-S   
 21      NaN                Trujillo                Trujillo        VE-T   
 22      NaN                  Vargas               La Guaira        VE-X   
 23      NaN                 Yaracuy              San Felipe        VE-U   
 24      NaN                   Zulia               Maracaibo        VE-V   
 25      NaN  Dependencias Federales              Gran Roque        VE-W   
 
                   4                                 5  \
 0   Año de admisión              Población (2011)[2]​   
 1              1992    &&&&&&&&&0161844.&&&&&0161 844   
 2              1909  &&&&&&&&02179838.&&&&&02 179 838   
 3              1864    &&&&&&&&&0501404.&&&&&0501 404   
 4              1909  &&&&&&&&01819630.&&&&&01 819 630   
 5              1937    &&&&&&&&&0853949.&&&&&0853 949   
 6              1901  &&&&&&&&02069064.&&&&&02 069 064   
 7              1865  &&&&&&&&02342665.&&&&&02 342 665   
 8              1864    &&&&&&&&&0367020.&&&&&0367 020   
 9              1992    &&&&&&&&&0180363.&&&&&0180 363   
 10             1999  &&&&&&&&04033186.&&&&&04 033 186   
 11             1872  &&&&&&&&01064615.&&&&&01 064 615   
 12             1864    &&&&&&&&&0746174.&&&&&0746 174   
 13             1909  &&&&&&&&01892439.&&&&&01 892 439   
 14             1909    &&&&&&&&&0903955.&&&&&0903 955   
 15             1909  &&&&&&&&03112851.&&&&&03 112 851   
 16             1909    &&&&&&&&&0938185.&&&&&0938 185   
 17             1909    &&&&&&&&&0525139.&&&&&0525 139   
 18             1909    &&&&&&&&&0897104.&&&&&0897 104   
 19             1909    &&&&&&&&&0892990.&&&&&0892 990   
 20             1899  &&&&&&&&01277241.&&&&&01 277 241   
 21             1864    &&&&&&&&&0901239.&&&&&0901 239   
 22             1998    &&&&&&&&&0419928.&&&&&0419 928   
 23             1899    &&&&&&&&&0645688.&&&&&0645 688   
 24             1864  &&&&&&&&04694856.&&&&&04 694 856   
 25             1938       &&&&&&&&&&&02155.&&&&&02155   
 
                                  6                              7  \
 0                 Superficie (km²)             Densidad (hab/km²)   
 1   &&&&&&&&&0177617.&&&&&0177 617    &&&&&&&&&&&&&&00.9900000,99   
 2    &&&&&&&&&&043300.&&&&&043 300    &&&&&&&&&&&&&033.90000033,9   
 3    &&&&&&&&&&076500.&&&&&076 500     &&&&&&&&&&&&&&06.&&&&&06,0   
 4      &&&&&&&&&&&07014.&&&&&07014   &&&&&&&&&&&&0235.600000235,6   
 5    &&&&&&&&&&035200.&&&&&035 200    &&&&&&&&&&&&&023.20000023,2   
 6   &&&&&&&&&0240528.&&&&&0240 528    &&&&&&&&&&&&&&07.8700007,87   
 7      &&&&&&&&&&&04650.&&&&&04650  &&&&&&&&&&&&0713.&10000713,01   
 8    &&&&&&&&&&014800.&&&&&014 800    &&&&&&&&&&&&&021.80000021,8   
 9    &&&&&&&&&&040200.&&&&&040 200    &&&&&&&&&&&&&&04.6500004,65   
 10      &&&&&&&&&&&&0433.&&&&&0433  &&&&&&&&&&&07246.4000007246,4   
 11   &&&&&&&&&&024800.&&&&&024 800    &&&&&&&&&&&&&036.40000036,4   
 12   &&&&&&&&&&064986.&&&&&064 986    &&&&&&&&&&&&&011.50000011,5   
 13   &&&&&&&&&&019800.&&&&&019 800    &&&&&&&&&&&&&089.60000089,6   
 14   &&&&&&&&&&011300.&&&&&011 300    &&&&&&&&&&&&&092.80000092,8   
 15     &&&&&&&&&&&07950.&&&&&07950   &&&&&&&&&&&&0336.500000336,5   
 16   &&&&&&&&&&028900.&&&&&028 900    &&&&&&&&&&&&&031.30000031,3   
 17     &&&&&&&&&&&01150.&&&&&01150  &&&&&&&&&&&&0480.&10000480,01   
 18   &&&&&&&&&&015200.&&&&&015 200    &&&&&&&&&&&&&057.70000057,7   
 19   &&&&&&&&&&011800.&&&&&011 800    &&&&&&&&&&&&&076.&&&&&076,0   
 20   &&&&&&&&&&011100.&&&&&011 100   &&&&&&&&&&&&0105.300000105,3   
 21     &&&&&&&&&&&07400.&&&&&07400    &&&&&&&&&&&&&092.80000092,8   
 22     &&&&&&&&&&&01497.&&&&&01497   &&&&&&&&&&&&0235.800000235,8   
 23     &&&&&&&&&&&07100.&&&&&07100    &&&&&&&&&&&&&084.60000084,6   
 24   &&&&&&&&&&063100.&&&&&063 100    &&&&&&&&&&&&&073.70000073,7   
 25      &&&&&&&&&&&&0120.&&&&&0120    &&&&&&&&&&&&&018.&&&&&018,0   
 
                     8     9  
 0              Región  Mapa  
 1             Guayana   NaN  
 2      Nor - Oriental   NaN  
 3              Llanos   NaN  
 4             Central   NaN  
 5              Andina   NaN  
 6             Guayana   NaN  
 7             Central   NaN  
 8             Central   NaN  
 9             Guayana   NaN  
 10            Capital   NaN  
 11  Centro-Occidental   NaN  
 12             Llanos   NaN  
 13  Centro-Occidental   NaN  
 14             Andina   NaN  
 15            Capital   NaN  
 16     Nor - Oriental   NaN  
 17            Insular   NaN  
 18  Centro-Occidental   NaN  
 19     Nor - Oriental   NaN  
 20             Andina   NaN  
 21             Andina   NaN  
 22            Capital   NaN  
 23  Centro-Occidental   NaN  
 24            Zuliana   NaN  
 25            Insular   NaN  ]
```
In [2]:
```python
#Tipo de los estados
type(estados)
```
Out[2]:
```python
list
```
In [3]:
```python
#Tipo del primer elemento es un dataframe
type(estados[0])
```
Out[3]:
```python
pandas.core.frame.DataFrame
```
In [4]:
```python
#Se listan del dataframe estados y capitales (elementos 1 y 2 del dataframe, y se recorre)
for i in range(1,26):
    print(estados[2][1][i],estados[2][2][i])
Amazonas Puerto Ayacucho
Anzoátegui Barcelona
Apure San Fernando de Apure
Aragua Maracay
Barinas Barinas
Bolívar Ciudad Bolívar
Carabobo Valencia
Cojedes San Carlos
Delta Amacuro Tucupita
Distrito Capital Caracas
Falcón Coro
Guárico San Juan de Los Morros
Lara Barquisimeto
Mérida Mérida
Miranda Los Teques
Monagas Maturín
Nueva Esparta La Asunción
Portuguesa Guanare
Sucre Cumaná
Táchira San Cristóbal
Trujillo Trujillo
Vargas La Guaira
Yaracuy San Felipe
Zulia Maracaibo
Dependencias Federales Gran Roque
```
In [5]:
```python
#Ahora se crea una lista de diccionarios donde estará la información de cada estado
lista = []
for i in range(1,26):
    lista.append({'Estado':estados[2][1][i],
                  'Capital': estados[2][2][i],
                  'codigo_iso': estados[2][3][i],
                  u'año_admision': estados[2][4][i],
                  'Poblacion': int(estados[2][5][i].split(".")[0].split("&")[-1]),
                  'Superficie': int(estados[2][6][i].split(".")[0].split("&")[-1]),
                  'Densidad': float(estados[2][7][i].split(",")[0].split("&")[-1]),
                  'Region': estados[2][8][i]
                 })
    
print(lista)
[{'Region': 'Guayana', 'Densidad': 0.99, 'Superficie': 177617, 'Estado': 'Amazonas', 'codigo_iso': 'VE-Z', 'Poblacion': 161844, 'Capital': 'Puerto Ayacucho', 'año_admision': '1992'}, {'Region': 'Nor - Oriental', 'Densidad': 33.90000033, 'Superficie': 43300, 'Estado': 'Anzoátegui', 'codigo_iso': 'VE-B', 'Poblacion': 2179838, 'Capital': 'Barcelona', 'año_admision': '1909'}, {'Region': 'Llanos', 'Densidad': 6.0, 'Superficie': 76500, 'Estado': 'Apure', 'codigo_iso': 'VE-C', 'Poblacion': 501404, 'Capital': 'San Fernando de Apure', 'año_admision': '1864'}, {'Region': 'Central', 'Densidad': 235.600000235, 'Superficie': 7014, 'Estado': 'Aragua', 'codigo_iso': 'VE-D', 'Poblacion': 1819630, 'Capital': 'Maracay', 'año_admision': '1909'}, {'Region': 'Andina', 'Densidad': 23.20000023, 'Superficie': 35200, 'Estado': 'Barinas', 'codigo_iso': 'VE-E', 'Poblacion': 853949, 'Capital': 'Barinas', 'año_admision': '1937'}, {'Region': 'Guayana', 'Densidad': 7.8700007, 'Superficie': 240528, 'Estado': 'Bolívar', 'codigo_iso': 'VE-F', 'Poblacion': 2069064, 'Capital': 'Ciudad Bolívar', 'año_admision': '1901'}, {'Region': 'Central', 'Densidad': 10000713.0, 'Superficie': 4650, 'Estado': 'Carabobo', 'codigo_iso': 'VE-G', 'Poblacion': 2342665, 'Capital': 'Valencia', 'año_admision': '1865'}, {'Region': 'Central', 'Densidad': 21.80000021, 'Superficie': 14800, 'Estado': 'Cojedes', 'codigo_iso': 'VE-H', 'Poblacion': 367020, 'Capital': 'San Carlos', 'año_admision': '1864'}, {'Region': 'Guayana', 'Densidad': 4.6500004, 'Superficie': 40200, 'Estado': 'Delta Amacuro', 'codigo_iso': 'VE-Y', 'Poblacion': 180363, 'Capital': 'Tucupita', 'año_admision': '1992'}, {'Region': 'Capital', 'Densidad': 7246.4000007246, 'Superficie': 433, 'Estado': 'Distrito Capital', 'codigo_iso': 'VE-A', 'Poblacion': 4033186, 'Capital': 'Caracas', 'año_admision': '1999'}, {'Region': 'Centro-Occidental', 'Densidad': 36.40000036, 'Superficie': 24800, 'Estado': 'Falcón', 'codigo_iso': 'VE-I', 'Poblacion': 1064615, 'Capital': 'Coro', 'año_admision': '1872'}, {'Region': 'Llanos', 'Densidad': 11.50000011, 'Superficie': 64986, 'Estado': 'Guárico', 'codigo_iso': 'VE-J', 'Poblacion': 746174, 'Capital': 'San Juan de Los Morros', 'año_admision': '1864'}, {'Region': 'Centro-Occidental', 'Densidad': 89.60000089, 'Superficie': 19800, 'Estado': 'Lara', 'codigo_iso': 'VE-K', 'Poblacion': 1892439, 'Capital': 'Barquisimeto', 'año_admision': '1909'}, {'Region': 'Andina', 'Densidad': 92.80000092, 'Superficie': 11300, 'Estado': 'Mérida', 'codigo_iso': 'VE-L', 'Poblacion': 903955, 'Capital': 'Mérida', 'año_admision': '1909'}, {'Region': 'Capital', 'Densidad': 336.500000336, 'Superficie': 7950, 'Estado': 'Miranda', 'codigo_iso': 'VE-M', 'Poblacion': 3112851, 'Capital': 'Los Teques', 'año_admision': '1909'}, {'Region': 'Nor - Oriental', 'Densidad': 31.30000031, 'Superficie': 28900, 'Estado': 'Monagas', 'codigo_iso': 'VE-N', 'Poblacion': 938185, 'Capital': 'Maturín', 'año_admision': '1909'}, {'Region': 'Insular', 'Densidad': 10000480.0, 'Superficie': 1150, 'Estado': 'Nueva Esparta', 'codigo_iso': 'VE-O', 'Poblacion': 525139, 'Capital': 'La Asunción', 'año_admision': '1909'}, {'Region': 'Centro-Occidental', 'Densidad': 57.70000057, 'Superficie': 15200, 'Estado': 'Portuguesa', 'codigo_iso': 'VE-P', 'Poblacion': 897104, 'Capital': 'Guanare', 'año_admision': '1909'}, {'Region': 'Nor - Oriental', 'Densidad': 76.0, 'Superficie': 11800, 'Estado': 'Sucre', 'codigo_iso': 'VE-R', 'Poblacion': 892990, 'Capital': 'Cumaná', 'año_admision': '1909'}, {'Region': 'Andina', 'Densidad': 105.300000105, 'Superficie': 11100, 'Estado': 'Táchira', 'codigo_iso': 'VE-S', 'Poblacion': 1277241, 'Capital': 'San Cristóbal', 'año_admision': '1899'}, {'Region': 'Andina', 'Densidad': 92.80000092, 'Superficie': 7400, 'Estado': 'Trujillo', 'codigo_iso': 'VE-T', 'Poblacion': 901239, 'Capital': 'Trujillo', 'año_admision': '1864'}, {'Region': 'Capital', 'Densidad': 235.800000235, 'Superficie': 1497, 'Estado': 'Vargas', 'codigo_iso': 'VE-X', 'Poblacion': 419928, 'Capital': 'La Guaira', 'año_admision': '1998'}, {'Region': 'Centro-Occidental', 'Densidad': 84.60000084, 'Superficie': 7100, 'Estado': 'Yaracuy', 'codigo_iso': 'VE-U', 'Poblacion': 645688, 'Capital': 'San Felipe', 'año_admision': '1899'}, {'Region': 'Zuliana', 'Densidad': 73.70000073, 'Superficie': 63100, 'Estado': 'Zulia', 'codigo_iso': 'VE-V', 'Poblacion': 4694856, 'Capital': 'Maracaibo', 'año_admision': '1864'}, {'Region': 'Insular', 'Densidad': 18.0, 'Superficie': 120, 'Estado': 'Dependencias Federales', 'codigo_iso': 'VE-W', 'Poblacion': 2155, 'Capital': 'Gran Roque', 'año_admision': '1938'}]
```
In [6]:
```python
#Luego se crea un dataframe de la lista de diccionarios
df = pd.DataFrame(lista)
df
```
Out[6]:
| ID | Capital               | Densidad     | Estado          | Poblacion    | Region           | Superficie  | año_admision  | codigo_iso |
| :- | :----------------:    | :----------: | :-------------  | :------:     | :-------------:  | :-------    | :-----:       | :-------:  |
| 0  | Puerto Ayacucho       | 9.900000e-01 | Amazonas        | 161844       | Guayana          | 177617      | 1992          | VE-Z       |
| 1  | Barcelona             | 3.390000e+01 | Anzoátegui      | 2179838      | Nor - Oriental   | 43300       | 1909          | VE-B       |
| 2  | San Fernando de Apure | 6.000000e+00 | Apure           | 501404       | Llanos           | 76500       | 1864          | VE-C       |
| 3  | Maracay               | 2.356000e+02 | Aragua          | 1819630      | Central          | 7014        | 1909          | VE-D       |
| 4  | Barinas               | 2.320000e+01 | Barinas         | 853949       | Andina           | 35200       | 1937          | VE-E       |
| 5  | Ciudad Bolívar        | 7.870001e+00 | Bolívar         | 2069064      | Guayana          | 240528      | 1901          | VE-F       |
| 6  | Valencia              | 1.000071e+07	| Carabobo	      | 2342665      | Central          | 4650	      | 1865          | VE-G       |
| 7  | San Carlos            | 2.180000e+01 | Cojedes         | 367020       | Central          | 14800       | 1864          | VE-H       |
| 8  | Tucupita              | 4.650000e+00 | Delta Amacuro   | 180363       | Guayana          | 40200       | 1992          | VE-Y       |
| 9  | Caracas               | 7.246400e+03 | Distrito Capital| 4033186      | Capital          | 433         | 1999          | VE-A       |
| 10 | Coro                  | 3.640000e+01 | Falcón          | 1064615      |Centro-Occidental | 24800       | 1872          | VE-I       |
| 11 | San Juan de Los Morros| 1.150000e+01 | Guárico         | 746174       | Llanos           | 64986       | 1864          | VE-J       |
| 12 | Barquisimeto          | 8.960000e+01 | Lara            | 1892439      | Centro-Occidental| 19800       | 1909          | VE-K       |
| 13 | Mérida                | 9.280000e+01 | Mérida          | 903955       | Andina           | 11300       | 1909          | VE-L       |
| 14 | Los Teques            | 3.365000e+02 | Miranda         | 3112851      | Capital          | 7950        | 1909          | VE-M       |
| 15 | Maturín               | 3.130000e+01 | Monagas         | 938185       | Nor - Oriental   | 28900       | 1909          | VE-N       |
| 16 | La Asunción           | 1.000048e+07 | Nueva Esparta   | 525139       | Insular          | 1150        | 1909          | VE-O       |
| 17 | Guanare               | 5.770000e+01 | Portuguesa      | 897104       | Centro-Occidental| 15200       | 1909          | VE-P       |
| 18 | Cumaná                | 7.600000e+01 | Sucre           | 892990       | Nor - Oriental   | 11800       | 1909          | VE-R       |
| 19 | San Cristóbal         | 1.053000e+02 | Táchira         | 1277241      | Andina           | 11100       | 1899          | VE-S       |
| 20 | Trujillo              | 9.280000e+01 | Trujillo        | 901239       | Andina           | 7400        | 1864          | VE-T       |
| 21 | La Guaira             | 2.358000e+02 | Vargas          | 419928       | Capital          | 1497        | 1998          | VE-X       |
| 22 | San Felipe            | 8.460000e+01 | Yaracuy         | 645688       | Centro-Occidental| 7100        | 1899          | VE-U       |
| 23 | Maracaibo             | 7.370000e+01 | Zulia           | 4694856      | Zuliana          | 63100       | 1864          | VE-V       |
| 24 | Gran Roque            | 1.800000e+01 | D. Federales    |2155          | Insular          |  120        | 1938          | VE-W       |

In [7]:
```python
#Si se quiere la información de Carabobo
mascara = df["Estado"] == "Carabobo"
df[mascara]
```
Out[7]:
| ID | Capital               | Densidad     | Estado          | Poblacion    | Region           | Superficie  | año_admision  | codigo_iso |
| :- | :----------------:    | :----------: | :-------------  | :------:     | :-------------:  | :-------    | :-----:       | :-------:  |
| 6  | Valencia              | 1.000071e+07	| Carabobo	      | 2342665      | Central          | 4650	      | 1865          | VE-G       |
	
In [8]:
```python
#Otra forma de traer la información de Carabobo
df.iloc[6]
Out[8]:
Capital            Valencia
Densidad        1.00007e+07
Estado             Carabobo
Poblacion           2342665
Region              Central
Superficie             4650
año_admision           1865
codigo_iso             VE-G
Name: 6, dtype: object
```
In [9]:
```python
#Para obtener la capital del estado
df.iloc[6]["Capital"]
```
Out[9]:
```python
'Valencia'
```
In [ ]:
```

```
El proceso de eliminar la basura dentro del texto de algunos campos no se muestra, pero se usa en la construcción del diccionario.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)


