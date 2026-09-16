# Let have a good example 
from abc import ABC,abstractclassmethod 
class PaymentMethod(ABC):
    @classmethod
    @abstractclassmethod
    def pay(cls,amount:int):
        pass 


class UPI(PaymentMethod):

    def pay(self,amount):
        print(f"Start UPI Transaction with {amount} BDT")
        print("Payament with  UPI is done")


class CreditCard(PaymentMethod):
    def pay(self,amount):
        print(f"Start Credit card Transaction with {amount} BDT")
        print("Payament with  credit Card is done")


class PaymentProcessor:
    def payment(self,payment_method:PaymentMethod,amount:int):

        payment_method.pay(amount)


if __name__ == "__main__":
    upi_obj = UPI() 
    credit_obj = CreditCard()

    pp = PaymentProcessor()
    pp.payment(upi_obj,1000)
    pp.payment(credit_obj,20000)