from django import forms
from screen.models import Error_form

class ErrorForm(forms.ModelForm):
    class Meta:
        model = Error_form
        fields = ['email_error','comment_error','image_error']

        
        
        