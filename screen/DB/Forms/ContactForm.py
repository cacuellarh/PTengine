from django import forms
from screen.models import Contact_form

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_form
        fields = ['name_contact','email_contact','phone_contact','company_contact','message_contact']
