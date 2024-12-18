from django.db import models
import uuid
from django.forms import model_to_dict
from django.utils import timezone
from screen.Utils.CurrentDateColombia.DateConfig import SetCurrentTimeCo
class Client(models.Model):
    
    id_client = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, default="@")
    name = models.CharField(max_length=50, default=" ")  
    
class ImageTrack(models.Model):
    id_image = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.DecimalField(max_digits=12,decimal_places=3)
    x = models.DecimalField(max_digits=30, decimal_places=20)
    y = models.DecimalField(max_digits=30, decimal_places=20)
    width = models.DecimalField(max_digits=30, decimal_places=20)
    height = models.DecimalField(max_digits=30, decimal_places=20)
    ImageTrackDescription = models.CharField(max_length=100, default=None)
    url = models.CharField(max_length=1000)
    delete_soft = models.BooleanField(default= False)
    client_fk = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    notify_validate = models.BooleanField(default= False)
    email_token =  models.CharField(max_length=100, default=None) 
    DateTimeTrack = models.DateTimeField(default=SetCurrentTimeCo.SetTimeCo(timezone.now())) 

    def to_dict(self):
        data = model_to_dict(self, exclude=["client_fk"])  # Excluye la clave foránea
        data['client_fk'] = self.client_fk.id_client  # Agrega manualmente el ID del cliente
        return data
    
class History_events(models.Model):
    id_event = models.AutoField(primary_key=True)
    fk_imagetrack = models.ForeignKey(ImageTrack, on_delete=models.CASCADE)
    date =    models.DateTimeField()
    delete_soft = models.BooleanField(default= False)
    status_scan =  models.BooleanField(default= False)     
class History_prices(models.Model):
    id_history_prices = models.AutoField(primary_key=True)
    fk_history_events = models.ForeignKey(History_events, on_delete=models.CASCADE)
    price_scan = models.FloatField()
    delete_soft = models.BooleanField(default= False)

class History_events_fails(models.Model):
    id_history_events_fails = models.AutoField(primary_key=True)
    fk_history_events = models.ForeignKey(History_events, on_delete=models.CASCADE)
    img_route_err = models.CharField(max_length=300)
    delete_soft = models.BooleanField(default= False)
    
class ElementsXpaths(models.Model):
    id_ElementsXpaths = models.AutoField(primary_key=True),
    domain = models.CharField(max_length=200, default=None)
    xpath = models.CharField(max_length=200, default=None)
    type_element = models.CharField(max_length=200, default=None)

class Error_form (models.Model):
    id_error = models.AutoField(primary_key=True)
    date_log_error = models.DateTimeField(default=SetCurrentTimeCo.SetTimeCo(timezone.now()))
    email_error = models.EmailField()
    comment_error = models.CharField(max_length=500)
    image_error = models.FileField(max_length=500, upload_to="screen/static/ErrorFormImg")

class Contact_form (models.Model):
    id_contact_form = models.AutoField(primary_key=True)
    name_contact = models.CharField(max_length=40, default=None)
    email_contact = models.EmailField(null=None)
    phone_contact = models.CharField(max_length=15)
    company_contact = models.CharField(max_length=10)
    message_contact = models.CharField(max_length=1000)

class ImageBasic (models.Model):
    idImage = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.CharField(max_length=500, default=None)
    EmailContact = models.EmailField(null=None)
