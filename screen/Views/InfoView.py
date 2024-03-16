from rest_framework import generics
from django.shortcuts import render

class Info():
    
    class About(generics.ListAPIView):
        
        def get(self, request):
            
            return render(request,"about_us.html")
    
    class Contact(generics.ListAPIView):
        
        def get(self, request):
            
            return render(request,"contact.html")
    
    class Terms(generics.ListAPIView):
        
        def get(self, request):
            
            return render(request,"terms.html")
    
    class Privacy(generics.ListAPIView):
        
        def get(self, request):
            
            return render(request,"privacy.html")                 