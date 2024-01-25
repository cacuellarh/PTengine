from celery import shared_task
from screen.Engine.OCR import OCR
from screen.Engine.Screen import ScreenShot
from screen.Services.Notification.SelectorNotification import SelectorNotification
from screen.Services.Auto_validate import Validate
from screen.Services.Console_info import Console

@shared_task
def prueba():

    notificator = SelectorNotification()
    notificator.select_notification("email")
    
    validate = Validate()
 
    prices =  validate.aut_validate()
    
    print(prices)
    if prices["current_price"] != prices["db_price"]:
        
        # price = prices["current_price"]
        # o_price = prices["db_price"]
        notificator.conf({"destiny": "camiloandres_kane@hotmail.com", "body": "El precio cambió, mi rey", "affair": "cambio de precio"})
        notificator.send_notification()
        
    else:
        
        Console.warning("El precio no ha cambiado!")