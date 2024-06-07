from django.http import JsonResponse
from rest_framework import generics
from django.shortcuts import render
from django.conf import settings
from typing import cast
from TrackMyPrice.Core.Application.Factory.WriteUseCase_Builder import WriteUseCaseBuilder
from TrackMyPrice.Core.Application.UseCases.WriteUseCases.ScannedImage_UseCases import ScannedImageCreateUseCase
from TrackMyPrice.Infraestructure.Persistence.ImageTrackRepository import ScannedImageRepository

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

    class Prueba(generics.ListAPIView):
        def post(self, request):
            
            WriteUseCaseBuilder.BuildWriteUseCases()
            # use = ScannedImageCreateUseCase()

            # res = use.Execute(request)

            # return JsonResponse(res.ToDict())
            