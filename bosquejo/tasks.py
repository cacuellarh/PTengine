import queue
from celery import shared_task
from screen.Engine.OCR import OCR
from screen.Engine.Screen import ScreenShot
from screen.Services.Notification.SelectorNotification import SelectorNotification
from screen.Services.Auto_validate import Validate
from screen.Services.Console_info import Console
from screen.Services.Email_token import Email_token

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
        
@shared_task
def prueba2():
    
       try:
        notificator = SelectorNotification()
        notificator.select_notification("email")

        notificator.conf({"destiny": "camiloandres_kane@hotmail.com", "body": "El precio cambió, mi rey", "affair": "cambio de precio"})
        notificator.send_notification()
        Console.warning("Ejecutando prueba 2")
        print("si")
       except Exception as e:
        print(f"Error en tarea_intensa: {e}")
        Console.warning("Ejecutando prueba 2")
        raise  # Re-raise the exception after logging it

@shared_task(queue="email_queue")

def email_token(token_email):
    
    notification = SelectorNotification()
    notification.select_notification("email")
    notification.conf({"destiny": "camiloandres_kane@hotmail.com", "body": f"Token recibido: {token_email}", "affair": "confirmacion de correo"})
    notification.send_notification()
    
        