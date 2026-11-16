from email_service_bad import EmailService 
from sms_service_bad import SMSService 

class Notification: 

    def __init__(self):
        self.email_service = EmailService() 
        self.sms_service = SMSService() 

    def notificationbyemail(self,message):
        self.email_service.send_email(message) 

    def notificationbysms(self,message):
        self.sms_service.send_sms(message) 



ns = Notification()
ns.notificationbyemail("This msg is sent via email") 
ns.notificationbysms("This msg is sent via sms")
