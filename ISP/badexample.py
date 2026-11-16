# Like solving the same problem with the help of  multiple inheritance *args

from abc import ABC,abstractmethod 

class Employee(ABC):

    @abstractmethod
    def eat(self):
        pass
    @abstractmethod  
    def working(self):
        pass 


class Worker(Employee):
    def eat(self):
        print("Worker is eating") 

    def working(self):
        print("Worker is eating")  


class Robot(Employee):
    def eat(self):
        raise Exception("Robot can't it ") 
    def working(self):
        print("Robot is working") 



