from django.http import JsonResponse
from rest_framework import generics
from screen.API.ResponseServer import ResponseServer
from screen.DB.Forms.ContactForm import ContactForm
from django.shortcuts import render

class Contact:

    class Contact_form (generics.ListAPIView):
        def post(self,request):
            if request.method == 'POST':
                print(request.POST) 
                form = ContactForm(request.POST)
                if form.is_valid():
                    form.save()

            return render(request, "main.html")