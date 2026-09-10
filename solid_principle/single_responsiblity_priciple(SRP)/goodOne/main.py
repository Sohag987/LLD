from user import User 
from userRepo import UserRepo 

if __name__ == "__main__":
    user_obj = User("Sohag","sohag987",'sohagmodak987@gmail.com',19)
    user_repo_obj = UserRepo('pqsl',user_obj)

    print(user_obj.is_adult())
    print(user_obj.get_info())

    print(user_repo_obj.save_to_db())
    print(user_repo_obj.delete_from_db())
