from celery import shared_task
from screen.Services.Notification.SelectorNotification import SelectorNotification
from screen.Services.Auto_validate import Validate
from screen.Services.Console_info import Console
from screen.DB.Repos.Image_repos import Image_repos
from django.core.serializers import deserialize

@shared_task(queue="validate_queue")
def validate(img):
    validate = Validate()
    for obj in deserialize("json", img):
        ins = obj.object
        prices =  validate.aut_validate(ins)
        current =prices["current_price"]
        db = prices["db_price"]
        print(f"precio actual:{current} , precio db; {db}")
    

@shared_task(queue="email_queue")

def email_token(email,token_email):
    
    notification = SelectorNotification()
    notification.select_notification("email")
    url = f"http://127.0.0.1:8000/api/token_confirm/{token_email}"
    notification.conf({"destiny": email, "body": f"Token recibido: {url}, loprosadasdasd", "affair": "confirmacion de correo"})
    notification.send_notification()
    print("enviando")
    
        