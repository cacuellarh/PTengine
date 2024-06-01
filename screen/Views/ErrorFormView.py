from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from screen.API.ResponseServer import ResponseServer
from screen.models import Error_form
from screen.DB.Forms.ErrorForm import ErrorForm

class Error:

    class Error_form (generics.ListAPIView):
        def post(self,request):
            print(f"{request.POST}, {request.FILES}")
            if request.method == 'POST':
                
                form = ErrorForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()

            return render(request, "main.html")
                           
            
                