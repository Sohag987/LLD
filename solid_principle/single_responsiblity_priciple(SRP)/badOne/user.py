class User:
     def __init__(self,name:str,password:str,email:str,age:int):
           self.name = name 
           self.password = password 
           self.email = email 
           self.age = age 

     def get_info(self)->str:
           return f"Name:{self.name} && Age:{self.age}"

     def is_adult(self)->bool:
        return self.age>=18 

     def save_to_db(self)->str:
          return f"{self.name} data has uploaded"

     def delete_from_db(self)->str:
          return f"{self.name} data deleted" 



     
          
     