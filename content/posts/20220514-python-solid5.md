Title: Principios S.O.L.I.D. - 5. Principio de inversión de la dependencia. (DIP - Dependency inversion principle) 
Date:  2022-05-14 14:00
Category: Tutorial Python
Tags: python,solid
lang: es
translation: true
Slug: python_solid5
Authors: Ernesto Crespo
Summary: Quinto y último artículo sobre los principios SOLID, en este caso el Principio de inversión de la dependencia.

En ingeniería de software existe el principio [S.O.L.I.D](https://es.wikipedia.org/wiki/SOLID). Los principios SOLID son guías que pueden ser aplicadas en el desarrollo de software para eliminar malos diseños provocando que el programador tenga que refactorizar hasta que sea legible y extensible. 

Sus principios son:

* Single responsability principle - Principio de responsabilidad única.
* Open/closed principle - Principio abierto/cerrado.
* Liskov substitution principle - Principio de sustitución Liskov.
* Interface segregation principle - Principio de segregación de la interfaz.
* Dependency inversion principle - Principio de inversión de la dependencia.


A continuación dejo un vídeo de [ArjanCodes](https://www.youtube.com/watch?v=pTB30aXS77U&t=1s) que explica con código python los principios S.O.L.I.D:

<iframe width="560" height="315" src="https://www.youtube.com/embed/pTB30aXS77U" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Los artículos anteriores:
* [Principio de responsabilidad única](https://www.seraph.to/python_solid1.html#python_solid1).
* [Principio abierto/cerrado](https://www.seraph.to/python_solid2.html#python_solid2).
* [Principio de sustitución Liskov](https://www.seraph.to/python_solid3.html#python_solid3).
* [Principio de segregación de la interfaz](https://www.seraph.to/python_solid4.html#python_solid4.

El [Principio de inversión de la dependencia](https://es.wikipedia.org/wiki/Principio_de_inversi%C3%B3n_de_la_dependencia) es una forma específica de desacoplar módulos de software. Al seguir el principio, las relaciones de dependencia convencionales establecidas desde los módulos de alto nivel de establecimiento de políticas a los módulos de depencia de bajo nivel se invierten, lo que hace que los módulos de alto nivel sean independientes de los detalles de implementación del módulo de bajo nivel, el principio establece: 
 
1. Los módulos de alto nivel no deberían depender de los módulos de bajo nivel. Ambos deberían depender de abstracciones (p.ej., interfaces).
2. Las abstracciones no deberían depender de los detalles. Los detalles (implementaciones concretas) deben depender de abstracciones.

La dependencia debe estar en abstracciones, no en concreciones. Los módulos de alto nivel no deben depender de módulos de bajo nivel. Tanto las clases de nivel bajo como las de alto nivel deberían depender de las mismas abstracciones. Las abstracciones no deberían depender de los detalles. Los detalles deben depender de abstracciones.



1. Se tiene el código del artículo anterior sobre el Principio de segregación de interfaz. Con solución usando composición.

En este caso, al pasar como argumento de un método un objeto, ya viola este principio.

```python 

class SMSAuth:
    authorized = False
    
    def verify_code(self,code):
        print(f"Verifying code {code}")
        self.authorized = True
        
    def is_authorized(self) -> bool:
        return self.authorized 

# Clase abstracta procesamiento de pago con método pay.
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,order):
        pass 

# Clase procesamiento pago por tarjeta de debito que hereda de la clase abstracta.
# el método init recibe como argumentos el código de seguridad y la clase SMSAuth para autorizar el pago.
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self,security_code, authorizer: SMSAuth):

        self.authorizer = authorizer
        self.security_code = security_code
    
    def pay(self,order):
        # Se consulta si no está autorizado el pago
        # al no tener autorización devuelve una excepción.
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

# Clase de procesamiento de pago con TC, que hereda de la clase abstracta.
# En este caso no se necesita la clase SMSAuth, sólo el código de seguridad.
class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self,security_code):
        self.security_code = security_code
        
    
    def pay(self,order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

# Clase de procesamiento de pago vía paypal, hereda de la misma clase abstracta.
# El init recibe de argumentos dirección de correo y el objecto SMSAuth.
class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self,email_address,authorizer:SMSAuth):
        self.authorizer = authorizer
        self.email_address = email_address
        self.verified = False
        
    
    def pay(self,order):
        # Se valida si se tiene autorización para realizar el pago.
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"

# Ahora se instancia la clase Order, y se agrega los items a comprar en la orden.

order = Order()
order.add_item("Teclado", 1, 50)
order.add_item("Memoria", 1, 150)
order.add_item("Cable USB", 2, 5)

# Imprime el precio total de la orden
print(order.total_price())

# Se define el autorizador.
authorizer = SMSAuth()

# Se define el método de pago debito
# ahora se le pasa el código y el autorizador.

processor = DebitPaymentProcessor("0372846",authorizer)
# Se verifica el pago
authorizer.verify_code(454545)

# Realiza el pago de la orden.
processor.pay(order)

# Se define el método de pago TC
# Para este caso se mantiene igual.
processor = CreditPaymentProcessor("0372846")
processor.pay(order)



# Se define el método de pago paypal
# Se le pasa el correo y el autorizador.
processor = PaypalPaymentProcessor("h@h.com",authorizer)
# Se realiza el pago de la orden.
processor.pay(order)
```

La salida de está ejecución es la siguiente:
```bash

210
Verifying code 454545
Processing debit payment type
Verifying security code: 0372846

Processing debit payment type
Verifying security code: 0372846

Processing credit payment type
Verifying security code: 0372846

Processing paypal payment type
Verifying email address: h@h.com

```

### Solución
Para cumplir el principio de la inversión de la dependencia se crea una clase  abstracta que maneje si se verifica la autenticación junto con la clase AuthSMS, en las respectivas clases del procesamiento de pago que se necesite verificar por SMS, en vez de pasar como argumento el objeto, se pasa la clase abstracta. 

A continuación el código: 

```python

from abc import ABC, abstractmethod

# La clase Order 
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

# Clase abstracta authorizer con método que devuelve si está autorizado o no. 
class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) ->bool:
        pass


# Clase abstracta de procesamiento de pago
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,order):
        pass 

# Clase SMSAutho que hereda de la clase abstracta authorizer
class SMSAuth(Authorizer):
    authorized = False
    
    def verify_code(self,code):
        print(f"Verifying code {code}")
        self.authorized = True
        
    def is_authorized(self) -> bool:
        return self.authorized

# clase pago por tarjeta de debito que recibe en el init authorizer que es la clase abstracta.
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self,security_code, authorizer: Authorizer):

        self.authorizer = authorizer
        self.security_code = security_code
    
    def pay(self,order):
        # Se consulta si no está autorizado el pago
        # al no tener autorización devuelve una excepción.
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

# La clase de procesamiento de TC se mantiene igual.
class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self,security_code):
        self.security_code = security_code
        
    
    def pay(self,order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


# clase dde procesamiento de pago por paypal
# Se le pasa como argumento la clase abstracta.
class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self,email_address,authorizer:Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address
        self.verified = False
        
    
    def pay(self,order):
        # Se valida si se tiene autorización para realizar el pago.
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Verifying email address: {self.email_address}")
        order.status = "paid"

# Ahora se instancia la clase Order, y se agrega los items a comprar en la orden.

order = Order()
order.add_item("Teclado", 1, 50)
order.add_item("Memoria", 1, 150)
order.add_item("Cable USB", 2, 5)

# Imprime el precio total de la orden
print(order.total_price())

# Se define el autorizador.
authorizer = SMSAuth()

# Se define el método de pago debito
# ahora se le pasa el código y el autorizador.

processor = DebitPaymentProcessor("0372846",authorizer)
# Se verifica el pago
authorizer.verify_code(454545)

# Realiza el pago de la orden.
processor.pay(order)

# Se define el método de pago TC
# Para este caso se mantiene igual.
processor = CreditPaymentProcessor("0372846")
processor.pay(order)



# Se define el método de pago paypal
# Se le pasa el correo y el autorizador.
processor = PaypalPaymentProcessor("h@h.com",authorizer)
# Se realiza el pago de la orden.
processor.pay(order)
```

La salida es la siguiente: 

```bash 

210
Verifying code 454545
Processing debit payment type
Verifying security code: 0372846

Processing debit payment type
Verifying security code: 0372846

Processing credit payment type
Verifying security code: 0372846

Processing paypal payment type
Verifying email address: h@h.com



```

Lo que se logro es ocultar la implementación de la composición que se pasa como argumento en los procesadores de pago que tiene que validar vía SMS.

En próximo artículo 


Referencias: 

* [Principios SOLID en Python](https://softwarecrafters.io/python/principios-solid-python)
* [Los principios SOLID ilustrados en ejemplos sencillos de Python](https://blog.damavis.com/los-principios-solid-ilustrados-en-ejemplos-sencillos-de-python/)
* [Principios SOLID explicados en Python con ejemplos.](https://ichi.pro/es/principios-solid-explicados-en-python-con-ejemplos-56291217871103)
* [The S.O.L.I.D Principles in Python](https://medium.com/geekculture/the-s-o-l-i-d-principles-in-python-a041c5aa9969#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImQ2M2RiZTczYWFkODhjODU0ZGUwZDhkNmMwMTRjMzZkYzI1YzQyOTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NDY5NjE2MDYsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwMzA0ODgwMTUxNTE4Mzk4NTA5MyIsImVtYWlsIjoiZWNyZXNwb0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiMjE2Mjk2MDM1ODM0LWsxazZxZTA2MHMydHAyYTJqYW00bGpkY21zMDBzdHRnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IkVybmVzdG8gQ3Jlc3BvIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BT2gxNEdpNzZJNGhTTXQ3U1hYbzZjdHdaNDloeDlKbTF3cU93UXZiTU0zbWtHMD1zOTYtYyIsImdpdmVuX25hbWUiOiJFcm5lc3RvIiwiZmFtaWx5X25hbWUiOiJDcmVzcG8iLCJpYXQiOjE2NDY5NjE5MDYsImV4cCI6MTY0Njk2NTUwNiwianRpIjoiNWM2ZWFkNjRjNjcyOGYxY2VhNmJhNjhkNGYzYTYyZTI3MzUxZTFhZCJ9.jMgz-2c2M8jmF-pepfaLohkEc75VeswUa7S1N6h6VgS7DOHw4rUVBjza_7VYEa_3gPpFHKiX_8OYI9_CjPJa4x1VU2encPP_FEHDU6m0lILEVVYkSV4LS7jfkJRe93GE51E8rQPUdR2IxcPc_P8mlE3Co-plLIktqAmW4_fyyMyLquDj-CjXfTpZ6RZs85rf3XH1qM-LOF8jhydDMKAhY8Iej4PCsT56C-kr26En3SqaA5BNgEftLIxhjQoFuZNCj8c7g5PuUztdmQ6UhjFA1-G392HnMx7rMYsfjeXxs2zaTeSjPh-z4JwyqkBTxZm6_rp37RpeQJFcGKzxWZNx8g)
* [Principios SOLID](https://enmilocalfunciona.io/principios-solid/)

* [ArjanCodes](https://www.youtube.com/watch?v=pTB30aXS77U&t=1s)

* [solid principles with python](https://medium.com/@didemyaniktepe/solid-principles-with-python-97b5e7250ed7#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImZjYmQ3ZjQ4MWE4MjVkMTEzZTBkMDNkZDk0ZTYwYjY5ZmYxNjY1YTIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2NTE5NjI5NzgsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwMzA0ODgwMTUxNTE4Mzk4NTA5MyIsImVtYWlsIjoiZWNyZXNwb0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiMjE2Mjk2MDM1ODM0LWsxazZxZTA2MHMydHAyYTJqYW00bGpkY21zMDBzdHRnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IkVybmVzdG8gQ3Jlc3BvIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hLS9BT2gxNEdpT19yRlhDM0VVWWRocmFLWjBHUmJNVlpRenhwSHRWQnl0MmI0MmU4WT1zOTYtYyIsImdpdmVuX25hbWUiOiJFcm5lc3RvIiwiZmFtaWx5X25hbWUiOiJDcmVzcG8iLCJpYXQiOjE2NTE5NjMyNzgsImV4cCI6MTY1MTk2Njg3OCwianRpIjoiNThhMzllZDhiMDNhZDM0ZDY1NDlhZDc2YzBmN2RkODY3NDNlZTgzMiJ9.db8I06It2VvYgbS6UswUsVGpbL3-OY8fFmQ367BXgF9p21W--y6OcTsKRTQp1yKVUZXbaUUoQYtIfoC00pnn9J7NHM1Fzixx1FIf8qeUm_4Yj4iPGzLwE4QapPbwJYdB1xXOLNGfQkfHb63U6ZwObrzJZrqHatNc7dwNNzpy0757d3BXvgrSNWbLXuNcxBVrdFwHqqtjJZfsyixaTAqYi4mzjg3ljpoxlYP-USeCIASUU6OJkMyCs__XjhC0ez2lWNDuPZwC3WML130U9GsHikAWR_Ue1iOIuQfC7_N2PE-GU0pYWCfIzzTvrhBoRFMhaN5i1koEOQ9w6c9ziCvH9A)

* [SOLID Coding in Python](https://towardsdatascience.com/solid-coding-in-python-1281392a6a94)

* [5 Principles to write SOLID Code](https://towardsdatascience.com/5-principles-to-write-solid-code-examples-in-python-9062272e6bdc)

* [The 5 (SOLID) Principles of Pyhon Readable Code](https://towardsdev.com/the-5-solid-principles-of-pyhon-readable-code-67c5a3fe5693)

* [Designing to Patterns: A Pythonic Example](https://levelup.gitconnected.com/designing-to-patterns-a-pythonic-example-14bc8ce34e81)

* [Python Interface Segregation Principle](https://www.pythontutorial.net/python-oop/python-interface-segregation-principle/)

* [How to Write Clean Code (in Python) With SOLID Principles | Principle #4](https://medium.com/the-brainwave/how-to-write-clean-code-in-python-with-solid-principles-principle-4-2297c45d37e2)

* [The Interface Segregation Principle (ISP) Explained in Python](https://medium.com/better-programming/the-interface-segregation-principle-isp-explained-in-python-46e173241642)

---
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
