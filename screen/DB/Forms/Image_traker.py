from django import forms
from screen.models import ImageTrack

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageTrack
        fields = ['price', 'x', 'y','width','height','ImageTrackDescription','url', 'client_fk','email_token']

        
        
        