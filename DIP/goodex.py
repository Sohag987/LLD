from channel_for_good import NotificationChannel 


class NotificationService: 
    def __init__(self,channel:NotificationChannel): 
         self.channel = channel 

    def notify(self,message):
         self.channel.send(message)  