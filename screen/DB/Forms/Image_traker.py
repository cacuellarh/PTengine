from django import forms
from screen.models import ImageTrack

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageTrack
        fields = ['price', 'x', 'y','width','height','rotate','scaleX','scaleY','url','email','email_token','frequency_fk']

        
        
        