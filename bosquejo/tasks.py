from celery import shared_task
from screen.Services.Notification.SelectorNotification import SelectorNotification
from screen.Services.Auto_validate import Validate
from screen.Services.Console_info import Console
from screen.DB.Repos.Image_repos import Image_repos

@shared_task(queue="validate_queue")
def validate():

    img_repos = Image_repos()
    validate = Validate()
 
    prices =  validate.aut_validate()
    
    print(prices["current_price"] != prices["db_price"])

        

@shared_task(queue="email_queue")

def email_token(email,token_email):
    
    notification = SelectorNotification()
    notification.select_notification("email")
    url = f"http://127.0.0.1:8000/api/token_confirm/{token_email}"
    notification.conf({"destiny": email, "body": f"Token recibido: {url}, loprosadasdasd", "affair": "confirmacion de correo"})
    notification.send_notification()
    print("enviando")
    
        