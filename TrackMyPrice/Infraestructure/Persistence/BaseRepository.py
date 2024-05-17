from TrackMyPrice.Core.Application.Contracts.Repository.BaseRepository import IBaseRepository
from django.db import models
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from TrackMyPrice.Core.Application.Models.Response.Response import RepositoryResponse
from TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.FormFactory import IFormFactory
from TrackMyPrice.Core.Application.Models.Request.ApiResponse import ResponseDetails
from django.conf import settings

class BaseRepository(IBaseRepository):

    def __init__(self, currentModel : models.Model)-> None:
        self.model : models.Model= currentModel
        self.__formFactory :IFormFactory = settings.DI_APLICATION.get(IFormFactory)

    def __MakeResponse(self, responseDetails: ResponseDetails) -> RepositoryResponse:
        message = responseDetails.message if responseDetails.status else f"Error trace: {self.__class__.__name__}, details: {responseDetails.message}"
        return RepositoryResponse(responseDetails.status, responseDetails.status_code, message, responseDetails.data)
    
    def GetAll(self, filter: bool = False, kwargs: dict = {}) -> RepositoryResponse:
        if filter: 
            dataResponse =  self.model.objects.filter(**kwargs)
        else:
            dataResponse = self.model.objects.all()

        if dataResponse is not None:
            return self.__MakeResponse(ResponseDetails(status=True, status_code=200, message="Success", data=dataResponse))
        else:
            return self.__MakeResponse(ResponseDetails(False, 404, "Object not found"))

    def GetByColumn(self, predicate) -> RepositoryResponse:
        try:
            dataGet = self.model.objects.get(**predicate)
            return self.__MakeResponse(ResponseDetails(True, 200, "Success", dataGet))
        
        except ObjectDoesNotExist:
            return self.__MakeResponse(ResponseDetails(False, 404, "Object does not exist"))
        except MultipleObjectsReturned:
            return self.__MakeResponse(ResponseDetails(False, 400, "Multiple objects returned"))

    def CreateRecord(self, data, modelForm) -> RepositoryResponse:
        try:
            form = self.__formFactory.CreateFormFactory(modelForm)
            currentForm = form.CreateForm()
            insertData = currentForm(data)

            if insertData.is_valid():
                insertData.save()
                return self.__MakeResponse(ResponseDetails(True, 200, "Success"))
            else:
                return self.__MakeResponse(ResponseDetails(False, 412,f"Validation error, Model:{self.model.__class__.__name__} ", insertData.errors))
            
        except ValueError as valueError:
            return self.__MakeResponse(ResponseDetails(False, 404, str(valueError)))
        except Exception as e:
            return self.__MakeResponse(ResponseDetails(False, 500, str(e)))

    def UpdateRecord(self, id: dict, data: dict) -> RepositoryResponse:
        try:
            recordToUpdate = self.model.objects.get(**id)
            for key, value in data.items():
                setattr(recordToUpdate, key, value)

            recordToUpdate.full_clean()
            recordToUpdate.save()

            return self.__MakeResponse(ResponseDetails(True, 200, "Record updated successfully", recordToUpdate))
        except ObjectDoesNotExist:
            return self.__MakeResponse(ResponseDetails(False, 404, "Object does not exist"))
        except Exception as e:
            return self.__MakeResponse(ResponseDetails(False, 500, str(e)))
        
    def DeleteRecord(self, id : dict)-> RepositoryResponse:   
        
        try:
            recordToDelete = self.model.objects.get(**id)
            recordToDelete.delete()
            return self.__MakeResponse(ResponseDetails(True, 200, "Record delete successfully"))
        except ObjectDoesNotExist as ob:           
            return self.__MakeResponse(ResponseDetails(False, 404, "Object does not exist"))


    
    

