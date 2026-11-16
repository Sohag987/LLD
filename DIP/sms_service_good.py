from channel_for_good import NotificationChannel 

class SMSService(NotificationChannel): 
     def send(self, message):
          print(f"This message is sent by sms {message}") 