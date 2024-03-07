from typing import Any
from rest_framework import generics
from django.shortcuts import render
from screen.DB.Repos.Image_repos import Image_repos
from django.http import JsonResponse
from screen.DB.Repos.Log_repos import LogRepos
from screen.API.ResponseServer import ResponseServer

class User:
    prices = None
    
    class UserIPriceDetails(generics.ListAPIView):
        
        def __init__(self) -> None:
            #arreglar DI
            self.image_repos = Image_repos()
            self.log_repos = LogRepos()
            self.prices = None
            
        def get(self,request, id_img, price_current):
                  
            img = self.image_repos.filter("id_image", id_img)
            self.prices = self.log_repos.get_history_prices(id_img)
            total = 0
            elements = 1
            #arreglar
            
            for price in self.prices:
                print(price)
                print("hola")
                total+= price["fk_history_events__fk_imagetrack__price"]
                elements+= 1
            
            avg = total / elements
             
            return render(request, "user_check_price.html", 
                {
                              "img_details": img,
                              "h_prices" : self.prices,
                              "current_price": price_current,
                               "db_price": img.price,
                               "avg" : avg
                })
            
    class ApiDetails(generics.ListAPIView):
        
        def __init__(self, **kwargs: Any) -> None:
            self.prices = None
            self.image_repos = Image_repos()
            self.log_repos = LogRepos()
            
        def get(self,request, id_img):
                  
            self.prices = self.log_repos.get_history_prices(id_img)
            
            self.prices
            return JsonResponse(
                ResponseServer(
                    Status= True,
                    Message= "Datos obtenidos correctamente",
                    Data= self.prices
                ).to_dict()
            )