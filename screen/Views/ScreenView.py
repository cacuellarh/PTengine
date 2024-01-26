from ..Services.Auto_validate import Validate
from ..API.ResponseServer import ResponseServer
from django.http import JsonResponse
from ..Engine.Screen import ScreenShot
from django.shortcuts import render
from rest_framework import generics
from ..Engine.OCR import OCR
from ..DB.Forms.Image_traker import ImageForm
import os
from ..Services.Console_info import Console


class ScreenView(generics.ListAPIView):    
    screen : ScreenShot
    
    def __init__(self):
        
        self.screen = ScreenShot()
        Console.info("Iniciando controlador")
        
        
    def get(self, request):
        return render(request, "Base.html")
    
    def post(self,request):
        
        if request.method == 'POST':
            image = ImageForm(request.POST)
            
            if image.is_valid():
                try:
                    
                    image.save()

                    return JsonResponse(ResponseServer(
                
                Status= True,
                Message = "Metadatos guardados correctamente",
                Data = {}
            ).to_dict())
                
                except Exception as e:
                    
                    print("Error : " + e)
                        

            else:
                image = ImageForm()
        
          
        return JsonResponse(ResponseServer(
            
            Status= False,
            Message = "Error al guardar metadatos",
            Data = {}
        ).to_dict())
        

class Exec(generics.CreateAPIView):
    def __init__(self):
        
        self.screen = ScreenShot()
        
    def post(self, request):
        
        if request.method == "POST":
            
            url_form = request.POST.get("url")
            Console.info(f"URL ingresada: {url_form}")
            self.screen.take_screen(url_= url_form, action="save")
            
            return  render(request, "ScreenView.html", {"url" : url_form})

class SaveScreen(generics.CreateAPIView):
    
    ocr : OCR  
    
    def __init__(self) -> None:
        self.ocr = OCR()
         
    def post(self, request):
        
        if request.method == "POST":
            
            files = request.FILES.getlist('image')
            
            for file in files:
                
                with open("c:\\p\\aaaa.png", "wb") as destiny:
                    
                    for part in file.chunks():
                        destiny.write(part)                        
        
        price = self.ocr.convert("c:\\p\\aaaa.png")
        
        return JsonResponse(ResponseServer(
            
            Status= True,
            Message = "Convercion realizada con exito",
            Data = {"price" : price}
        ).to_dict())
        
