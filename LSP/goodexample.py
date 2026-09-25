from abc import ABC,abstractmethod 

class Bird(ABC):
    
    def eat(self):
        pass 


class Flybird(Bird):
    def fly(self):
            pass 



class Penguien(Bird):
    
    def eat(self):
        print("The Penguien is eating") 


class Sparrow(Flybird):
    def fly(self):
        print("Sparrow is flying")
    def eat(self):
        print("The Sparrow is eating")

p_o = Penguien() 
p_o.eat() 

s_o = Sparrow() 
s_o.eat() 
s_o.fly()      