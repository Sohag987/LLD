from user import User 

if __name__ == '__main__':
    user_obj = User("Sohag","sohag987",'sohagmodak987@gmail.com',19)

    print(user_obj.get_info()) 
    print(user_obj.is_adult())