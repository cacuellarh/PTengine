from django import forms
from screen.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['email','name']
    
        
        