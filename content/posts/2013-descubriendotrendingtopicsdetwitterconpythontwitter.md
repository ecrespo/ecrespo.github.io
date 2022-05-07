Title: Descubriendo trending topics de twitter con python-twitter.  
Date: 2013-04-27 09:00  
Category: Tutorial Python  
Tags: General,Python,Twitter  
lang: es
translation: true


Recuerdo la presentación de Efrain en el PyDay en Mérida, donde hablo de la librería tweepy ([acá artículo de Efrain sobre el tema](https://effiejayx.wordpress.com/2010/10/25/jugando-con-las-apis-de-twitter-y-python/)) que permite acceder a una cuenta de twitter, actualizar estado entre otras cosas.

Con el auge de twitter como red social en el país me dispuse a probar otra librería de python para twitter llamada [python-twitter](https://github.com/bear/python-twitter), la documentación de la librería se puede acceder desde [acá](https://github.com/bear/python-twitter/wiki). Existe una serie de ejemplos de como usar la librería python-twitter en [github](https://github.com/ideoforms/python-twitter-examples/).

Instalar la librería de twitter:
Se usará el comando `easy_install` o `pip` como `root`:
```
easy_install twitter
```
ó
```
pip install twitter
```
El código que se muestra a continuación lista el ID de los Países, el número ID de cada País. El código original lo pueden ver en el siguiente [enlace](https://github.com/ideoforms/python-twitter-examples/blob/master/twitter-trends-available.py):
Se ejecuta python:
```python
(python2.7)ernesto@jewel:~/prueba$ python

Python 2.7.3 (default, Jan  2 2013, 16:53:07) 

[GCC 4.7.2] on linux2

Type "help", "copyright", "credits" or "license" for more information.

>>>
```
Se importa el módulo `python-twitter`:
```python
>>> import twitter
```
Se instancia la clase Twitter pasando el dominio (el url de la api de twitter) y la versión del api que en este caso es la versión 1:
```python
>>> twitter_api = twitter.Twitter(domain="api.twitter.com", api_version='1')
```
Se captura los trends disponibles:
```python
>>> trends1 = twitter_api.trends.available()
```
Se lista los ID de los Países:

```python
>>> for location in trends1:


...     name = location["name"].encode('ascii', 'replace')


...     print "(%d) %s" % (location["woeid"], name)


... 


(1) Worldwide


(2972) Winnipeg


(3369) Ottawa


(3444) Quebec


(3534) Montreal


(4118) Toronto


(8676) Edmonton


(8775) Calgary


(9807) Vancouver


(12723) Birmingham


(13911) Brighton


(13963) Bristol


(15127) Cardiff


(19344) Edinburgh


(21125) Glasgow


(26042) Leeds


(26062) Leicester


(26734) Liverpool


(28218) Manchester


(30079) Newcastle


(30720) Nottingham


(32452) Portsmouth


(34503) Sheffield


(44418) London


(44544) Belfast


(76456) Santo Domingo


(116545) Mexico City


(124162) Guadalajara


(131068) Le?n


(134047) Monterrey


(137612) Puebla


(149361) Tijuana


(332471) Mendoza


(349859) Santiago


(349860) Concepcion


(349861) Valparaiso


(368148) Bogot?


(395269) Caracas


(395270) Maracaibo


(395272) Valencia


(418440) Lima


(455819) Bras?lia


(455820) Bel?m


(455821) Belo Horizonte


(455822) Curitiba


(455823) Porto Alegre


(455824) Recife


(455825) Rio de Janeiro


(455826) Salvador


(455827) S?o Paulo


(455828) Campinas


(455830) Fortaleza


(455831) Goi?nia


(455833) Manaus


(455834) S?o Lu?s


(455867) Guarulhos


(466861) C?rdoba


(466862) Rosario


(468382) Barquisimeto


(468739) Buenos Aires


(560743) Dublin


(580778) Bordeaux


(608105) Lille


(609125) Lyon


(610264) Marseille


(612977) Montpellier


(613858) Nantes


(615702) Paris


(619163) Rennes


(627791) Strasbourg


(628886) Toulouse


(638242) Berlin


(641142) Bremen


(645458) Dortmund


(645686) Dresden


(646099) Dusseldorf


(648820) Essen


(650272) Frankfurt


(656958) Hamburg


(667931) Cologne


(671072) Leipzig


(676757) Munich


(698064) Stuttgart


(718345) Milan


(719258) Naples


(721943) Rome


(725003) Turin


(726874) Den Haag


(727232) Amsterdam


(733075) Rotterdam


(753692) Barcelona


(766273) Madrid


(766356) Malaga


(774508) Seville


(776688) Valencia


(779063) Zaragoza


(906057) Stockholm


(1030077) Bekasi


(1044316) Surabaya


(1047180) Bandung


(1047378) Jakarta


(1062617) Singapore


(1098081) Perth


(1099805) Adelaide


(1100661) Brisbane


(1100968) Canberra


(1101597) Darwin


(1103816) Melbourne


(1105779) Sydney


(1110809) Kitakyushu


(1117034) Chiba


(1117099) Fukuoka


(1117227) Hiroshima


(1117502) Kawasaki


(1117545) Kobe


(1117817) Nagoya


(1118108) Sapporo


(1118129) Sendai


(1118285) Takamatsu


(1118370) Tokyo


(1118550) Yokohama


(1132447) Busan


(1132466) Daegu


(1132481) Gwangju


(1132496) Incheon


(1132567) Suwon


(1132578) Ulsan


(1132599) Seoul


(1154726) Klang


(1154781) Kuala Lumpur


(1167715) Calocan


(1199136) Davao City


(1199477) Manila


(1199682) Quezon City


(1398823) Lagos


(1582504) Johannesburg


(2077746) Samara


(2112237) Yekaterinburg


(2122265) Moscow


(2122471) Nizhny Novgorod


(2122541) Novosibirsk


(2122641) Omsk


(2123260) Saint Petersburg


(2282863) Nagpur


(2295377) Lucknow


(2295378) Kanpur


(2295386) Kolkata


(2295388) Amritsar


(2295401) Jaipur


(2295402) Ahmedabad


(2295408) Indore


(2295411) Mumbai


(2295412) Pune


(2295414) Hyderabad


(2295420) Bangalore


(2295424) Chennai


(2343678) Adana


(2343732) Ankara


(2343843) Bursa


(2344116) Istanbul


(2344117) Izmir


(2345896) Okinawa


(2345975) Daejeon


(2357024) Atlanta


(2357536) Austin


(2358820) Baltimore


(2359991) Baton Rouge


(2364559) Birmingham


(2367105) Boston


(2378426) Charlotte


(2379574) Chicago


(2380358) Cincinnati


(2381475) Cleveland


(2383660) Columbus


(2388929) Dallas-Ft. Worth


(2391279) Denver


(2391585) Detroit


(2414469) Greensboro


(2418046) Harrisburg


(2424766) Houston


(2427032) Indianapolis


(2428184) Jackson


(2436704) Las Vegas


(2442047) Los Angeles


(2449323) Memphis


(2450022) Miami


(2451822) Milwaukee


(2452078) Minneapolis


(2457170) Nashville


(2458410) New Haven


(2458833) New Orleans


(2459115) New York


(2460389) Norfolk


(2466256) Orlando


(2471217) Philadelphia


(2471390) Phoenix


(2473224) Pittsburgh


(2475687) Portland


(2477058) Providence


(2478307) Raleigh


(2480894) Richmond


(2486340) Sacramento


(2486982) St. Louis


(2487610) Salt Lake City


(2487796) San Antonio


(2487889) San Diego


(2487956) San Francisco


(2490383) Seattle


(2503713) Tallahassee


(2503863) Tampa


(2514815) Washington


(15015370) Osaka


(15015372) Kyoto


(20070458) Delhi


(23424738) United Arab Emirates


(23424747) Argentina


(23424748) Australia


(23424768) Brazil


(23424775) Canada


(23424782) Chile


(23424787) Colombia


(23424800) Dominican Republic


(23424801) Ecuador


(23424803) Ireland


(23424819) France


(23424829) Germany


(23424834) Guatemala


(23424846) Indonesia


(23424848) India


(23424853) Italy


(23424856) Japan


(23424868) Korea


(23424900) Mexico


(23424901) Malaysia


(23424908) Nigeria


(23424909) Netherlands


(23424916) New Zealand


(23424919) Peru


(23424922) Pakistan


(23424934) Philippines


(23424936) Russia


(23424942) South Africa


(23424948) Singapore


(23424950) Spain


(23424954) Sweden


(23424969) Turkey


(23424975) United Kingdom


(23424977) United States


(23424982) Venezuela


(56013632) Petaling


(56013645) Hulu Langat
```

EL ID 1 es para listar los trending topics  mundial, para Venezuela se tiene el ID 23424982, se resalta en negrita los IDs de las ciudades de Venezuela. 

Ahora se va a desplegar la lista de trending topic global(1): 
Se define el valor 1 a WOE_ID para capturar el trending topic global, se instancia la clase Twitter con el dominio api.twitter.com y se define la versión del api como la versión 1. A continuación se captura los trending topic, se muestra los 10 tópicos del mundo.

```python
>>>WORLD_WOE_ID = 1


>>> twitter_api = twitter.Twitter(domain="api.twitter.com", api_version='1')


>>> world_trends = twitter_api.trends._(WORLD_WOE_ID)


>>> trends = world_trends()


>>> for i in range(10):


...     print trends[0]['trends'][i][u'name']


... 


#ILoveCheese


#CaprilesVenezuelayELMUNDOestácontigo


#MiMamáDice


#VamosMaravilla


#AJuicioCaprilesAsesino


Sara McMann


Rene de Calle 13


Sheila Gaff


RDMA


Rene

```

Al cambiar el valor de la variable WORLD_WOE_ID a la de Venezuela (23424982) se tiene:

```python
>>> WORLD_WOE_ID = 23424982


>>> twitter_api = twitter.Twitter(domain="api.twitter.com", api_version='1')


>>> world_trends = twitter_api.trends._(WORLD_WOE_ID)


>>> trends = world_trends()


>>> for i in range(10):


...     print trends[0]['trends'][i][u'name']


... 


#CaprilesVenezuelayELMUNDOestácontigo


#AJuicioCaprilesAsesino


#MiMamáDice


#MeArrechoCuando


#QueVivan


Feliz Día del Diseñador Gráfico


Estuvimos 5


Dayana Mendoza


Omar Borkan Al Gala


Antonio Rivero

```


Para el caso de Valencia (395272):

```python
>>> WORLD_WOE_ID = 395272


>>> twitter_api = twitter.Twitter(domain="api.twitter.com", api_version='1')


>>> world_trends = twitter_api.trends._(WORLD_WOE_ID)


>>> trends = world_trends()


>>> for i in range(10):


...     print trends[0]['trends'][i][u'name']


... 


#CaprilesVenezuelayELMUNDOestácontigo


#AJuicioCaprilesAsesino


#MeArrechoCuando


#MiMamáDice


Omar Borkan Al Gala


#TROPA


Feliz Día del Diseñador Gráfico


Estuvimos 5


Dayana Mendoza


Antonio Rivero

```

De esta forma se puede listar los 10 tópicos  según el País o ciudad utilizando Python. 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)