from ..DB.Repos.Frecuency_repos import Frequency_repos
from ..API.ResponseServer import ResponseServer
from django.http import JsonResponse
from ..Engine.Screen import ScreenShot
from django.shortcuts import render
from rest_framework import generics
from ..Engine.OCR import OCR
from screen.models import Client
from bosquejo.tasks import email_token, execute_auto_task;
from bosquejo.tasks import validate;
from ..Services.Console_info import Console
from ..Services.Session import App_session
from ..Services.Email_token import Email_token
from screen.Services.Email_token import Email_token
from screen.DB.Repos.Client_repos import Client_repos
from screen.DB.Repos.Image_repos import Image_repos
from django.core.serializers import serialize
from django.shortcuts import redirect
from django.conf import settings
class ScreenView(generics.ListAPIView):    
    screen : ScreenShot
    session_app : App_session
    token = Email_token
    
    def __init__(self):
        
        self.screen = ScreenShot()
        Console.info("Iniciando controlador")
        self.session_app = App_session()
        self.token = Email_token()
        self.img_repos = Image_repos()
        self.client_repos = Client_repos()
        
    def get(self, request):
        
        self.session_app.create_sesion_key(request)
        return render(request, "main.html")
    
    def post(self,request):
        client_on_exist : Client = None
        email = request.POST.get("email")
        image = False
        if request.method == 'POST':
            post = request.POST.copy()
            token_email = self.token.generate_token()
            post["email_token"] = token_email
    
            client_on_exist = self.client_repos.get(column="email", value=email)
            if client_on_exist is None:
                client = self.client_repos.create({"email": email})
                post["client_fk"] = client.id_client
                image = self.img_repos.create(data=post)
                email_token.delay(email,token_email)
                print("publicando tarea email")  
                      
            else:
                
                post["client_fk"] = client_on_exist.id_client
                image = self.img_repos.create(data=post)
                email_token.delay(email,token_email)
                print("publicando tarea email") 
                
            if image:
                
                return JsonResponse(ResponseServer(
                
                    Status= True,
                    Message = "Metadatos guardados correctamente",
                    Data = {}
                ).to_dict())
            else:
                return JsonResponse(ResponseServer(
                    Status=False,
                    Message="Error al crear la imagen",
                    Data={}
                ).to_dict())
                    
        

#End-point post, donde llega la informacion de la URL para ser renderizada 
class Exec(generics.CreateAPIView):
    def __init__(self):
        
        self.screen = ScreenShot()
    def get(self, request):

        if request.method == "GET":
            return redirect("main_menu")  
          
    def post(self, request):
        
        if request.method == "POST":
            file_id = request.session.get("user_key_session")
            url_form = request.POST.get("url")
            Console.info(f"URL ingresada: {url_form}")
            #Usando screen, para tomar la captura con selenium segun la URL insertada.
            self.screen.take_screen(url_= url_form, action="save", file_name=file_id)
            
            return  render(request, "ScreenView.html", {"url" : url_form , "img_name" : file_id, "frequency" : Frequency_repos.get_all()})

        
         
class SaveScreen(generics.CreateAPIView):
    
    ocr : OCR  
    
    def __init__(self) -> None:
        self.ocr = OCR(settings.PATHS["tmp"], settings.PATHS["tesseract"])
         
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

class EmailToken(generics.ListAPIView):
    
    def get(self, request):
        
        email_token.delay()
        return JsonResponse({"msg": "enviado"})
        
        
                
class AsyncTask(generics.CreateAPIView):
    
    def get(self, request):
        img_repos = Image_repos()
        img_all = img_repos.gel_all()

        for img in img_all:
            if img.notify_validate:
                data = serialize("json", [img])
                Console.info("Tarea publicada")
                validate.delay(data)
        
        return JsonResponse({"msg" : "si"})       
               
        
class ApiProof(generics.CreateAPIView):
    
    def get(self, request):
         execute_auto_task.delay()