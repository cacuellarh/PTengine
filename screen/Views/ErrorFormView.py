from django.http import JsonResponse
from rest_framework import generics
from TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.FormFactory import IFormFactory
from TrackMyPrice.Core.Application.Contracts.Repository.IErrorFormRepository import IErrorFormRepository
from screen.API.ResponseServer import ResponseServer
from screen.DB.Forms.ErrorForm import ErrorForm
from django.conf import settings

class Error:

    class Error_form (generics.ListAPIView):

        def __init__(self):
            self.__errorFormRepository : IErrorFormRepository = settings.DI_INJECTOR.get(IErrorFormRepository)
            self.__formFactory: IFormFactory = settings.DI_APLICATION.get(IFormFactory)
            
        def post(self,request):

            if request.method == 'POST':
                self.__formFactory.CreateFormFactory("")
                self.ErrorFormRepository.CreateRecord()
                