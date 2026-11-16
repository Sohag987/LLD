from channel_for_good import NotificationChannel 

class EmailService(NotificationChannel):
    def send(self,message): 
        print(f"This msg is sent via email {message}")