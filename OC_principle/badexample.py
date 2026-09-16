class PaymentProcess:
    def pay(self,payment_method:str,amount:int):
        if payment_method == "UPI":
            print(f"Start UPI Transaction with {amount} BDT")
            # internal mechanism of UPI would be here 
            print("Payament with  UPI is done")

        elif payment_method == "credit card":
            print(f"Start Credit card Transaction with {amount} BDT")
            # internal mechanism of credit card would be here 
            print("Payament with  credit Card is done")

        elif payment_method =="Net banking":
            print(f"Start net banking transction with {amount} BDT")
            #Internal Mchanism for Net banking  will be here 
            print("Pyament with  Net Banking is done")

        # If I want to add a new payment me=thod here like paypal then --> 
        # we need to edit the existing code 
        # that will spoil the open close principle 
        # open for extension and close for modification 


if __name__ == "__main__":
    pp_obj = PaymentProcess() 
    pp_obj.pay("UPI",100); 
