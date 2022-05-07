Title: Obtener cotización de criptomonedas y almacenarlas en un archivo csv por medio de pandas   
Date: 2018-03-11 10:00  
Category: Tutorial Python  
Tags: Python, Pandas, CSV, Coinmarketcap,Blockchain, Bitcoin
lang: es  
translation: true  

En el [artículo anterior](https://www.seraph.to/obtener-cotizacion-de-bitcoin-de-coinmarketcap-con-python.html) se obtuvo la cotización de bitcoin del sitio coinmarketcap por medio de request o directamente de una librería que accede al API.

En este artículo se obtiene la información de las primeras 100 criptomonedas que cotizan en coinmarketcap, y se manejará dicha información por medio de pandas.  Luego de ordenar la información de las monedas se van a almacenar en un archivo csv.

Este artículo se basa en un artículo en inglés [Importing Altcoin Data with Python and the CoinmarketCap API](http://blockxchain.org/2017/05/29/importing-altcoin-data-with-python-and-the-coinmarketcap-api/).

Si quieren pueden repasar lo que pueden hacer con pandas revisando los siguientes artículos:

- [Introducción a Pandas](https://www.seraph.to/introduccion-a-pandas.html)  
- [Python Pandas](https://www.tutorialspoint.com/python_pandas/index.htm)


A continuación el código en formato jupyter notebook:

In [1]:
```python
#Se importa coinmarketcap, json, pandas y time
import coinmarketcap
import json
import pandas as pd
import time
```
In [2]:
```python
#SE instancia la clase Market y se consulta la cotización de ethereum.
market = coinmarketcap.Market()
coin = market.ticker("ethereum")
```
In [3]:
```python
#Se muestra el tipo de la variable coin
type(coin)
```
Out[3]:
```python
list
```
In [4]:
```python
#Se muestra que la lista tiene 1 elemento.
print(len(coin))
1
```
In [5]:
```python
#Se muestra el tipo del primer elemento de la lista
type(coin[0])
```
Out[5]:
```python
dict
```
In [6]:
```python
#Se muestra el primer elemento de la lista el cual es un diccionario
print (coin[0])
{'symbol': 'ETH', 'price_btc': '0.0758447', 'price_usd': '725.008', 'cached': False, 'market_cap_usd': '71145122811.0', 'available_supply': '98130121.0', '24h_volume_usd': '1559710000.0', 'percent_change_1h': '0.22', 'percent_change_24h': '6.39', 'name': 'Ethereum', 'id': 'ethereum', 'total_supply': '98130121.0', 'rank': '2', 'last_updated': '1520813352', 'max_supply': None, 'percent_change_7d': '-16.25'}
```
In [7]:
```python
#Se muestra los datos de la variable coin, identado, y ordenada las claves.
print(json.dumps(coin, indent=4, sort_keys=True))
[
    {
        "24h_volume_usd": "1559710000.0",
        "available_supply": "98130121.0",
        "cached": false,
        "id": "ethereum",
        "last_updated": "1520813352",
        "market_cap_usd": "71145122811.0",
        "max_supply": null,
        "name": "Ethereum",
        "percent_change_1h": "0.22",
        "percent_change_24h": "6.39",
        "percent_change_7d": "-16.25",
        "price_btc": "0.0758447",
        "price_usd": "725.008",
        "rank": "2",
        "symbol": "ETH",
        "total_supply": "98130121.0"
    }
]
```
In [8]:
```python
#Ahora se usa panda series, se toma la cotización de ethereum y se guarda en 
#la variable ether
ether = pd.Series(market.ticker("ethereum")[0])
```
In [9]:
```python
#Se muestra el valor de la variable ether
print(ether)
24h_volume_usd         1559710000.0
available_supply         98130121.0
cached                         True
id                         ethereum
last_updated             1520813352
market_cap_usd        71145122811.0
max_supply                     None
name                       Ethereum
percent_change_1h              0.22
percent_change_24h             6.39
percent_change_7d            -16.25
price_btc                 0.0758447
price_usd                   725.008
rank                              2
symbol                          ETH
total_supply             98130121.0
dtype: object
```
In [10]:
```python
#Se muestra la descripción de la serie
print(ether.describe)
<bound method NDFrame.describe of 24h_volume_usd         1559710000.0
available_supply         98130121.0
cached                         True
id                         ethereum
last_updated             1520813352
market_cap_usd        71145122811.0
max_supply                     None
name                       Ethereum
percent_change_1h              0.22
percent_change_24h             6.39
percent_change_7d            -16.25
price_btc                 0.0758447
price_usd                   725.008
rank                              2
symbol                          ETH
total_supply             98130121.0
dtype: object>
```
In [11]:
```python
#Se guardan otras monedas alternativas en el arreglo de pandas
wowcoin = pd.Series(market.ticker("wowcoin")[0])
bitcoin = pd.Series(market.ticker("bitcoin")[0])
coinArray = pd.DataFrame([ether,bitcoin,wowcoin]).set_index("id")
```
In [12]:
```python
#Se muestra los datos del arreglo panda
print(coinArray)
         24h_volume_usd available_supply  cached last_updated market_cap_usd  \
id                                                                             
ethereum   1559710000.0       98130121.0    True   1520813352  71145122811.0   
bitcoin    6292920000.0       16913662.0   False   1520813365   162866556360   
wowcoin         106.405             None   False   1520813347           None   

          max_supply      name percent_change_1h percent_change_24h  \
id                                                                    
ethereum        None  Ethereum              0.22               6.39   
bitcoin   21000000.0   Bitcoin              0.42               9.61   
wowcoin         None   Wowcoin              3.01               4.04   

         percent_change_7d    price_btc     price_usd  rank symbol  \
id                                                                   
ethereum            -16.25    0.0758447       725.008     2    ETH   
bitcoin             -15.97          1.0       9629.29     1    BTC   
wowcoin              -78.7  0.000000002  0.0000163877  1467    WOW   

         total_supply  
id                     
ethereum   98130121.0  
bitcoin    16913662.0  
wowcoin          None  
```
In [13]:
```python
#Ahora se extrae las cotizaciones de 100 cryptomonedas
coins = market.ticker()
```
In [14]:
```python
#El tamaño de la lista es 100
len(coins)
```
Out[14]:
```python
100
```
In [15]:
```python
#Se almacena las 100 monedas en un dataframe de pandas a partir de una serie panda
coinArray2 = pd.DataFrame([pd.Series(coins[i]) for i in range(100)]).set_index('id')    
```
In [17]:
```python
#Obtengo los primeros 3 criptomonedas
coinArray2.head(3)
```
Out[17]:


|   ID    | 24h_volume_usd | available_supply | cached | last_updated | market_cap_usd | max_supply  | name          | percent_change_1h | percent_change_24h |percent_change_7d |  price_btc | price_usd |  rank | symbol | total_supply | 
| :------: | :------:       | :-----:           | :-----: | :------:     | :-----:         | :-------:    | :-----:       | :-----:           | :-------:           | :------:         | :-----:     | :-------:  | :------:       | :-----:       |
| bitcoin | 6292920000.0   | 16913662.0       | False  | 1520813365   | 162866556360   | 21000000.0  | Bitcoin	0.42  | 9.61              | -15.97             | 1.0              | 9629.2     | 1         | BTC           | 16913662.0   |
|ethereum | 1559710000.0   | 98130121.0       | False  | 1520813352   | 71145122811.0  | None        | Ethereum 0.22 | 6.39              | -16.25             | 0.0758447        | 725.008    | 2         | ETH            | 98130121.0   |
|ripple   | 471767000.0    | 39091956706.0    | False  | 1520813341   | 32612386698.0  | 100000000000| Ripple 0.33   | 5.49              | -14.76             | 0.00008727       | 0.834248   | 3         | XRP            | 99992520283.0|


In [18]:
```python
#Se define almacenar los datos en un archivo csv que maneje el tiempo en que se creo el
#archivo como nombre del archivo
location = 'Data/'+str(time.time())+'.csv'
```
In [19]:
```python
#Se almacenan los datos en formato csv
coinArray2.to_csv(location)
```
In [20]:
```python
#Ahora se repiten las instrucciones anteriores con 3 ciclos de cada 2 min
coins = market.ticker()
for i in range(3):
    coinArray = pd.DataFrame([pd.Series(coins[i]) for i in range(100)]).set_index('id')
    location = 'Data/'+str(time.time())+'.csv'
    coinArray.to_csv(location)
    time.sleep(2*60)
```

Al terminar de ejecutar el programa se tienen 4 archivos en formato csv:

![](./images/obtenercotizaciondecriptomonedasyalmacenarlasenunarchivocsvpormediodepandas-1.png)


En siguientes artículos se utilizarán los datos almacenados para hacer analítica de datos con Pandas.

														
											 																

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)

