import string
from screen.Services.Notification_options.Email import Email
from screen.Services.Notification_options.Whatsapp import Whatsapp
from screen.Services.Notification_options.SMS import SMS
from screen.Interfaces.Inotification import Inotification


class SelectorNotification:
    
    notification : Inotification
    
    def select_notification(self, notification_type : string) -> Inotification:

        if notification_type == "wsp":
            
            self.notification =  Whatsapp()
        elif notification_type == "sms":
            
            self.notification = SMS()
        elif notification_type == "email":
            
            self.notification = Email()
    
    
    def send_notification(self):
        
        self.notification.notify()
        
    def conf(self, args):
        
        self.notification.conf(args)        