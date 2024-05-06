from django.http import JsonResponse
from rest_framework import generics
from screen.API.ResponseServer import ResponseServer
from screen.models import Error_form
from screen.DB.Forms.ErrorForm import ErrorForm

class Error:

    class Error_form (generics.ListAPIView):
        def post(self,request):
            if request.method == 'POST':
                print('llega')
                print(request.POST) 
                form = ErrorForm(request.POST)
                if form.is_valid():
                    form.save()
                    return JsonResponse(ResponseServer(
                    
                        Status= True,
                        Message = "Registro completado con exíto",
                        Data = {}
                    ).to_dict())
                else:
                    for field, errors in form.errors.items():
                           form = ErrorForm()
                           print(f"{field},{errors}")
            return JsonResponse(ResponseServer(
            
                Status= False,
                Message = "Error al procesar el registro",
                Data = {}
            ).to_dict())
                