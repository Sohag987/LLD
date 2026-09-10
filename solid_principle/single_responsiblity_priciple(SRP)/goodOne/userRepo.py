from user import User 

class UserRepo:
     def __init__(self,db:str,user:User):
          self.db=db 
          self.user=user 
          
           

     

     def save_to_db(self)->str:
          return f"{self.user.name} data has uploaded"

     def delete_from_db(self)->str:
          return f"{self.user.name} data deleted" 



     
          
     