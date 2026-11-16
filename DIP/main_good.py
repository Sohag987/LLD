from goodex import NotificationService 
from email_service_good import EmailService 
from sms_service_good import SMSService 


sms_service = SMSService() 

ns  = NotificationService(sms_service) 
ns.notify("You are welcome")