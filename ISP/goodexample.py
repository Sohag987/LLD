from abc import ABC,abstractmethod 

class Employee(ABC):

    is_employee = True 
    @abstractmethod
    def is_employ(self):
        pass 

class Workable(ABC):
    @abstractmethod
    def working(self):
        pass 


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass 



class Worker(Employee,Eatable,Workable):
    # NOe we  can Implement the  method s that we acyually need for the class 
    pass 

class Robot(Employee,Workable):
    pass   


# The avobe code represent  a good practice for interface segregation principle 
