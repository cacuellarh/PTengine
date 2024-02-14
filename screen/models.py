from email.policy import default
from django.db import models

class Frequency(models.Model):
    
    id_frequency = models.AutoField(primary_key=True)
    frecuency = models.CharField(max_length=50)
class Client(models.Model):
    
    id_client = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=254, default="@")
    name = models.CharField(max_length=50, default=" ")  
    
class ImageTrack(models.Model):
    id_image = models.AutoField(primary_key=True)
    price = models.IntegerField()
    x = models.DecimalField(max_digits=30, decimal_places=20)
    y = models.DecimalField(max_digits=30, decimal_places=20)
    width = models.DecimalField(max_digits=30, decimal_places=20)
    height = models.DecimalField(max_digits=30, decimal_places=20)
    rotate = models.DecimalField(max_digits=30, decimal_places=20)
    scaleX = models.DecimalField(max_digits=30, decimal_places=20)
    scaleY = models.DecimalField(max_digits=30, decimal_places=20)
    url = models.CharField(max_length=500)
    delete_soft = models.BooleanField(default= False)
    frequency_fk = models.ForeignKey(Frequency, on_delete=models.CASCADE, default=1)
    client_fk = models.ForeignKey(Client, on_delete=models.CASCADE, default=1)
    notify_validate = models.BooleanField(default= False)
    email_token =  models.CharField(max_length=100, default=None)  

    def __str__(self):
        return f"ImageTrack {self.id}"