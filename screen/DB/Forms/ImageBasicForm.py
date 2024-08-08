from django import forms
from screen.models import ImageBasic

class ImageBasicForm(forms.ModelForm):
    class Meta:
        model = ImageBasic
        fields = ['url', 'EmailContact']
    