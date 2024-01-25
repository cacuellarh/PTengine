from email.policy import default
from django.db import models

class ImageTrack(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    x = models.DecimalField(max_digits=30, decimal_places=20)
    y = models.DecimalField(max_digits=30, decimal_places=20)
    width = models.DecimalField(max_digits=30, decimal_places=20)
    height = models.DecimalField(max_digits=30, decimal_places=20)
    rotate = models.DecimalField(max_digits=30, decimal_places=20)
    scaleX = models.DecimalField(max_digits=30, decimal_places=20)
    scaleY = models.DecimalField(max_digits=30, decimal_places=20)
    url = models.CharField(max_length=500)

    def __str__(self):
        return f"ImageTrack {self.id}"