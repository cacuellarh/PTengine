from celery import shared_task
from screen.Services.Notification.SelectorNotification import SelectorNotification
from screen.Services.Auto_validate import Validate
from screen.Services.Notification.SelectorNotification import SelectorNotification
from django.core.serializers import deserialize

# celery -A bosquejo worker -Q email_queue -l info

@shared_task(queue="validate_queue")
def validate(img):
    notify = SelectorNotification()
    notify.select_notification("email")
    
    validate = Validate()
    for obj in deserialize("json", img):
        ins = obj.object
   
        prices =  validate.aut_validate(ins)
        current =prices["current_price"]
        db = prices["db_price"]
        
        #if current != db:
        notify.conf({"destiny": ins.client_fk.email,
                    "body": F"El precio de su producto ah cambiado, Precio actual:{current}, Precio anterior:{db}", "affair": "Notificacion cambio de precio"})
            #print(f"precio actual:{current} , precio db; {db}")
        notify.send_notification()

@shared_task(queue="email_queue")

def email_token(email,token_email):
    
    notification = SelectorNotification()
    notification.select_notification("email")
    url = f"http://195.35.14.162:8002/api/token_confirm/{token_email}"
    #url = f"http://127.0.0.1:8000/api/token_confirm/{token_email}"
    notification.conf({"destiny": email, "body": f"Token recibido: {url}", "affair": "confirmacion de correo"})
    notification.send_notification()
    print("enviando")
    
        