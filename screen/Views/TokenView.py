from rest_framework import generics
from django.shortcuts import render
from screen.DB.Repos.Image_repos import Image_repos
from django.http import JsonResponse

class Token:    
    class TokenConfirm(generics.ListAPIView):
        
        def __init__(self) -> None:
            self.image_repos = Image_repos()
            
        def get(self,request,token):
            is_valid = self.image_repos.activate_notification(token=token)
            if is_valid:
                return render(request, "Token_confirm.html")
            else:    
                raise("El token ingresado no es correcto")
        