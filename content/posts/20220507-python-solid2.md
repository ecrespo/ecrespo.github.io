Title: Principios S.O.L.I.D. - 2. Principio abierto/cerrado. (OCP - Open/closed principle) 
Date:  2022-05-07 13:00
Category: Tutorial Python
Tags: python,solid
lang: es
translation: true
Slug: python_solid2
Authors: Ernesto Crespo
Summary: Segundo artículo sobre los principios SOLID, en este caso el principio de abierto cerrado.

En ingeniería de software existe el principio [S.O.L.I.D](https://es.wikipedia.org/wiki/SOLID). Los principios SOLID son guías que pueden ser aplicadas en el desarrollo de software para eliminar malos diseños provocando que el programador tenga que refactorizar hasta que sea legible y extensible. 

Sus principios son:

* Single responsability principle - Principio de responsabilidad única.
* Open/closed principle - Principio abierto/cerrado.
* Liskov substitution principle - Principio de sustitución Liskov.
* Interface segregation principle - Principio de segregación de la interfaz.
* Dependency inversion principle - Principio de inversión de la dependencia.


A continuación dejo un vídeo de [ArjanCodes](https://www.youtube.com/watch?v=pTB30aXS77U&t=1s) que explica con código python los principios S.O.L.I.D:

<iframe width="560" height="315" src="https://www.youtube.com/embed/pTB30aXS77U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

El [artículo anterior](https://www.seraph.to/python_solid1.html#python_solid1) sobre el principio de responsabilidad única.


El [principio abierto/cerrado](https://es.wikipedia.org/wiki/Principio_de_abierto/cerrado) establece que una entidad de software (clase, módulo, función, etc) debe quedarse abierta para su extensión, pero cerrado para su modificación. Es decir, se debe poner extender el comportamiento de tal entidad pero sin modificar su código fuente.  

En otros términos, el código debería estar escrito de tal manera que, a la hora de añadir nuevas funcionalidades, no se deba modificar el código escrito previamente, que pueda estar siendo utilizado por otros usuarios



1. Del principio de responsabilidad única se tiene el siguiente código, donde se separo la clase Order de la clase PaymentProcess: 


```python

# Ahora se tiene una clase que sólo manejará métodos de la orden y se separa el método de pago en otra clase llamada PaymentProcessor


class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


# Clase PaymentProcessor con los métodos: pago con debito y pago a credito. 

class PaymentProcessor:
    def pay_debit(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"



# Ahora se instancia la clase Order, y se agrega los items a comprar en la orden.

order = Order()
order.add_item("Teclado", 1, 50)
order.add_item("Memoria", 1, 150)
order.add_item("Cable USB", 2, 5)

# Imprime el precio total de la orden
print(order.total_price())

# Instancia la clase de procesador de pago y se llama al método pagar con debito pasando como argumento la orden y el código de seguridad de la tarjeta.

processor = PaymentProcessor()
processor.pay_debit(order, "0372846")

```

La salida es la siguiente:

```bash 

210
Processing debit payment type
Verifying security code: 0372846

```

Para cumplir con el principio de abierto/cerrado, se usará una clase Abstracta que define el Proceso de pago, y se crean clases por cada tipo de pago que hereda de esa clase abstracta, ahora se separa los métodos del proceso de pago en clases con un sólo método.

```python 

from abc import ABC, abstractmethod

# La clase Order se mantiene igual:

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


# Se crea una clase abstracta del proceso de pago:
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,order,security_code):
        pass 


# Se crea la clase de pago con debito que hereda de la clase abstracta
class DebitPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

# Se crea la clase de pago con TC que hereda de la clase abstracta
class CreditPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


# Se crea el método de pago paypal
class PaypalPaymentProcessor(PaymentProcessor):
    def pay(self,order,security_code):
        print("Processing paypal payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


# Ahora se instancia la clase Order, y se agrega los items a comprar en la orden.

order = Order()
order.add_item("Teclado", 1, 50)
order.add_item("Memoria", 1, 150)
order.add_item("Cable USB", 2, 5)

# Imprime el precio total de la orden
print(order.total_price())


# Se define el método de pago debito

processor = DebitPaymentProcessor()
processor.pay(order, "0372846")

# Se define el método de pago TC

processor = CreditPaymentProcessor()
processor.pay(order, "0372846")



# Se define el método de pago paypal
processor = PaypalPaymentProcessor()
processor.pay(order, "0372846")

```

La salida es la siguiente: 

```bash 

210
Processing debit payment type
Verifying security code: 0372846

Processing debit payment type
Verifying security code: 0372846

Processing credit payment type
Verifying security code: 0372846

Processing credit payment type
Verifying security code: 0372846
```

Ahora cuando se requiera un nuevo método de pago simplemente se crea una clase de ese método que hereda de la clase abstracta, ya no se necesita tocar las clases o métodos del resto de los métodos de pago.


2. Generación de código QR. 

Del artículo sobre el principio de responsabilidad única se tiene el siguiente código: 

```python

class GenerateQR:
    
    def __init__(self,version):
        self.version = version
    
    def myqr(self,my_qr,text,save_name,colorize,save_dir,picture=None):
        if not picture: 
            return myqr.run(words=text, version=my_qr.version, save_name=save_name,
                            save_dir=save_dir, colorized=colorize, contrast=1.0, brightness=1.0)
            
        return myqr.run(words=text, version=my_qr.version, save_name=save_name, picture=picture,
                        save_dir=save_dir, colorized=colorize, contrast=1.0, brightness=1.0)

    
    def qrcode(self,my_qr,text,save_name,box_size,border,fit,fill,back_color):
        self.qr = qrc.QRCode(
            version=my_qr.version,
            box_size=box_size,
            border=border
        )
        self.qr.add_data(text)
        self.qr.make(fit=fit)
        self.img = self.qr.make_image(
            fill=fill, back_color=back_color)
        self.img.save(save_name)

gen_qr = GenerateQR(version=1)
# Generar QR con myqr
gen_qr.myqr(my_qr,"hola mundo!","hola.png",True,"./")
# generar qr con qrcode
gen_qr.qrcode(my_qr,"hola mundo2!",'hola2.png',10,5,True,'black','white')

```

Se tiene una sóla clase con un método para cada librería,  pero si se quiere agregar una nueva librería toca modificar  la clase y esto rompe el principio. Para evitarlo se crea la clase abstracta y una clase por cada librería que hereda de la clase abstracta, así si se tiene una nueva librería, lo que se hace es crear una clase nueva sin necesitar modificar las clases ya existentes.

```python 

from abc import ABC, abstractmethod
import qrcode as qrc
from MyQR import myqr

# Clase abstracta
class GenerateQR(ABC):
    @abstractmethod
    def generate(self,my_qr,text,save_name,**kwargs):
        pass 


# Clase para la librería MyQR que hereda de la clase abstracta.
class GenerateMyQR(GenerateQR):

    def __init__(self, version):
        self.version = version
    
    def generate(self,my_qr,text,save_name,**kwargs):
        # colorize,save_dir,picture=None
        colorize = kwargs.get("colorize", True)
        save_dir = kwargs.get("save_dir","./")
        picture = kwargs.get("picture",None)
        if not picture: 
            return myqr.run(words=text, version=self.version, save_name=save_name,
                            save_dir=save_dir, colorized=colorize, contrast=1.0, brightness=1.0)
            
        return myqr.run(words=text, version=my_qr.version, save_name=save_name, picture=picture,
                        save_dir=save_dir, colorized=colorize, contrast=1.0, brightness=1.0)

# Clase de la librería qr_code que hereda de la clase abstracta.
class GenerateQRCode(GenerateQR):
    
    def __init__(self, version):
        self.version = version

    def generate(self,my_qr,text,save_name,**kwargs):
        # box_size,border,fit,fill,back_color
        box_size = kwargs.get("box_size",10)
        border = kwargs.get("border",5)
        fit = kwargs.get("fit",True)
        fill = kwargs.get("fill","black")
        back_color = kwargs.get("back_color","white")
        self.qr = qrc.QRCode(
            version=self.version,
            box_size=box_size,
            border=border
        )
        self.qr.add_data(text)
        self.qr.make(fit=fit)
        self.img = self.qr.make_image(
            fill=fill, back_color=back_color)
        self.img.save(save_name)

# Se crea la instancia de la clase pasandole la versión del código QR que se quiere usar 
# para la librería MyQR y luego para qr_code
gen_qr = GenerateMyQR(version=1)
gen_qr.generate(my_qr,"Hola mundo","hola1c.png")

gen_qrcode = GenerateQRCode()
gen_qrcode.generate(my_qr,"Hola mundo","hola2c.png")
```

Como se explico, ya no es necesario tocar el código de las clases de las librerías existentes, y si se tiene una nueva librería sólo se necesita crear una nueva clase heredando de la clase abstracta.

Referencias: 

* [Principios SOLID](https://enmilocalfunciona.io/principios-solid/)

* [ArjanCodes](https://www.youtube.com/watch?v=pTB30aXS77U&t=1s)

* [solid principles with python](https://medium.com/@didemyaniktepe/solid-principles-with-python-97b5e7250ed7#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImZjYmQ3ZjQ4MWE4MjVkMTEzZTBkMDNkZDk0ZTYwYjY5ZmYxNjY1YTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NTE5NjI5NzgsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwMzA0ODgwMTUxNTE4Mzk4NTA5MyIsImVtYWlsIjoiZWNyZXNwb0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiMjE2Mjk2MDM1ODM0LWsxazZxZTA2MHMydHAyYTJqYW00bGpkY21zMDBzdHRnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IkVybmVzdG8gQ3Jlc3BvIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BT2gxNEdpT19yRlhDM0VVWWRocmFLWjBHUmJNVlpRenhwSHRWQnl0MmI0MmU4WT1zOTYtYyIsImdpdmVuX25hbWUiOiJFcm5lc3RvIiwiZmFtaWx5X25hbWUiOiJDcmVzcG8iLCJpYXQiOjE2NTE5NjMyNzgsImV4cCI6MTY1MTk2Njg3OCwianRpIjoiNThhMzllZDhiMDNhZDM0ZDY1NDlhZDc2YzBmN2RkODY3NDNlZTgzMiJ9.db8I06It2VvYgbS6UswUsVGpbL3-OY8fFmQ367BXgF9p21W--y6OcTsKRTQp1yKVUZXbaUUoQYtIfoC00pnn9J7NHM1Fzixx1FIf8qeUm_4Yj4iPGzLwE4QapPbwJYdB1xXOLNGfQkfHb63U6ZwObrzJZrqHatNc7dwNNzpy0757d3BXvgrSNWbLXuNcxBVrdFwHqqtjJZfsyixaTAqYi4mzjg3ljpoxlYP-USeCIASUU6OJkMyCs__XjhC0ez2lWNDuPZwC3WML130U9GsHikAWR_Ue1iOIuQfC7_N2PE-GU0pYWCfIzzTvrhBoRFMhaN5i1koEOQ9w6c9ziCvH9A)

* [SOLID Coding in Python](https://towardsdatascience.com/solid-coding-in-python-1281392a6a94)

* [5 Principles to write SOLID Code](https://towardsdatascience.com/5-principles-to-write-solid-code-examples-in-python-9062272e6bdc)

* [The 5 (SOLID) Principles of Pyhon Readable Code](https://towardsdev.com/the-5-solid-principles-of-pyhon-readable-code-67c5a3fe5693)

* [Designing to Patterns: A Pythonic Example](https://levelup.gitconnected.com/designing-to-patterns-a-pythonic-example-14bc8ce34e81)

* [Python Open–closed principle](https://www.pythontutorial.net/python-oop/python-open-closed-principle/)

* [How to Write Clean Code (in Python) With SOLID Principles | Principle #2](https://medium.com/the-brainwave/how-to-write-clean-code-in-python-with-solid-principles-principle-2-c54fb647f5b7)

* [The Open-Closed Principle Explained in Python](https://betterprogramming.pub/the-open-closed-principle-explained-in-python-f5517488f990)

---
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
