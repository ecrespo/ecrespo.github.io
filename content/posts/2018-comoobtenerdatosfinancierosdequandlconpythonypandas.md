Title: Como obtener datos Financieros de Quandl con Python y Pandas  
Date: 2018-05-25 09:00  
Category: Tutorial Python
Tags: Python, Matplotlib, Pandas, Quandl
lang: es  
translation: true  

La idea de este artículo es explicar de manera básica el uso de Pandas para obtener datos financieros, en este caso el valor de las divisas de Países como Argentina, Brasil, Chile, Mexico y Venezuela.
Quandl es una plataforma financiera y económica de datos alternativos que sirve para inversores profesionales. El API de Quandl permite el acceso a sus datos por medio de Lenguaje R, Python, Matlab, Maple y Stata. Más información en [wikipedia](https://en.wikipedia.org/wiki/Quandl) y en su [página](https://www.quandl.com/).  

Para este caso se accederá a los datos vía Python y se visualizará por medio de Pandas y matplotlib.  

La información de Quandl para los países:  
- Venezuela : [Dicom](https://www.quandl.com/data/BUNDESBANK/BBEX3_M_VEF_USD_CA_AB_B09-Exchange-Rates-For-The-Us-Dollar-In-The-Bolivarian-Republic-Of-Venezuela-Dicom-Usd-1-Vef-selling) y [Dolar Today](https://www.quandl.com/data/DOLARTODAY/BSF_USD-DolarToday-Bolivar-Fuerte-USD-Exchange-Rate)  
- [Argentina](https://www.quandl.com/data/BUNDESBANK/BBEX3_D_ARS_USD_CA_AC_000-Exchange-Rates-For-The-Us-Dollar-In-Argentina-Usd-1-Ars-middle)  
- [Brasil](https://www.quandl.com/data/BUNDESBANK/BBEX3_D_BRL_USD_CA_AC_000-Exchange-Rates-For-The-Us-Dollar-In-Brazil-Usd-1-Brl-middle)  
- [Chile](https://www.quandl.com/data/BUNDESBANK/BBEX3_D_CLP_USD_CA_AC_000-Exchange-Rates-For-The-Us-Dollar-In-Chile-Usd-1-Clp-middle)  
- [México](https://www.quandl.com/data/BUNDESBANK/BBEX3_M_MXN_USD_CA_AB_A01-Exchange-Rates-For-The-Us-Dollar-In-Mexico-Usd-1-Mxn-selling)  

El proceso sería el siguiente:


1. Importar librerías  
2. Acceso a los datos de los países en Quandl  
3. Ordenar las columnas, eliminar NaN.  
4. Crear portafolio  
5. Visualizar los datos  

Los códigos para acceder a los datos los pueden ver por ejemplo para México en la siguiente imagen.

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-1.png)

Página de Quandl de la información del Dolar para México

1. Se importan las librerías pandas, quandl y matplotlib

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-2.png)

2. Se definen las fechas de inicio y fin del analísis

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-3.png)

3. Obtener datos de quandl

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-4.png)

4. Se visualizan los datos de Dicom y Dolar today

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-5.png)

5. Se crea el portafolio donde se agrupa todas las cotizaciones

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-6.png)

6. Se descartan los campos NaN y se renombran las columnas

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-7.png)

7. Se gráfican todas las cotizaciones

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-8.png)

8. Gráfica de Argentina

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-9.png)

9. Gráfica de Brasil

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-10.png)

10. Gráfia de Chile

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-11.png)

11. Gráfica de México

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-12.png)

12. Gŕafica de Venezuela

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-13.png)

13. Gráfica Dicom y Dolar Today por separado

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-14.png)  

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-15.png)  

![](./images/comoobtenerdatosfinancierosdequandlconpythonypandas-16.png)

El notebook lo pueden ver completo en:  
[ecrespo/articulos-cienciadedatos
Contribute to articulos-cienciadedatos development by creating an account on GitHub.github.com](https://github.com/ecrespo/articulos-cienciadedatos/blob/master/quandl/cotizaciones-dolar.ipynb)


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
