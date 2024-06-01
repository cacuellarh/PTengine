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
                    print("as")
                    return JsonResponse(ResponseServer(
                    
                        Status= True,
                        Message = "Registro completado con exíto",
                        Data = {}
                    ).to_dict())
                else:
                    for field, errors in form.errors.items():
                           form = ContactForm()
                           print(f"{field},{errors}")
            
            return render(request, "main.html")