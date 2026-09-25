from abc import ABC,abstractmethod 

class Bird(ABC):
    def fly(self):
        pass 
    def eat(self):
        pass 

class Penguien(Bird):
    def fly(self):
        raise Exception("Peguien Can not fly") # Here the child class is not behaving like the parent class
    def eat(self):
        print("The Penguien is eating") 

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")
    def eat(self):
        print("The Sparrow is eating")


p_o = Penguien() 
p_o.eat()
# p_o.fly()



