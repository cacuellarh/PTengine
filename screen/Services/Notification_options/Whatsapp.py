import string
from numpy import integer
#import pywhatkit
from screen.Interfaces.Inotification import Inotification


class Whatsapp(Inotification):
    
    number : integer
    msg : string
    hour : integer
    minute : integer
    
    def conf(self, params):
        
        self.number = params.get("number")
        self.msg = params.get("msg")
        self.hour = params.get("hour")
        self.minute = params.get("minute")
        
    def notify(self):
        pass
        #pywhatkit.sendwhatmsg(self.number, self.msg, self.hour, self.minute, tab_close=True)
        
        