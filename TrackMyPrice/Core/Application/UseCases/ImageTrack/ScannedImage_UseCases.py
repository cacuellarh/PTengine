from typing import cast
from django.conf import settings
from TrackMyPrice.Core.Application.Contracts.Repository.IClientRepository import IClientRepository
from TrackMyPrice.Core.Application.Contracts.Repository.IScannedImageRepository import IScannedImageRepository
from TrackMyPrice.Core.Application.Contracts.UnitOfWork import IUnitOfWork
from TrackMyPrice.Core.Application.Contracts.UseCase.ScannedImage_UseCase import IScannedImageCreateUseCase
from TrackMyPrice.Core.Application.Factory.Repository_builder import RepositoryBuilder
from TrackMyPrice.Core.Application.Utils.Email_token import EmailToken



class ScannedImageCreateUseCase(IScannedImageCreateUseCase):

    def __init__(self) -> None:
        self.__unitOfWork : IUnitOfWork = settings.DI_APLICATION.get(IUnitOfWork)
        self.__scannedImageRepository : IScannedImageRepository = cast(IScannedImageRepository, RepositoryBuilder.GetRepository("ScannedImageRepository"))()
        self.__clientRepository : IClientRepository = cast(IClientRepository, RepositoryBuilder.GetRepository("ClientRepository"))()


    def Execute(self, request):

        email = request.POST.get("email")
        token = EmailToken.GenerateToken()
        dataCreation = request.POST.copy()

        with self.__unitOfWork as uow:
            client = self.__getClient(email)

            if client.Status:
                client_fk = client.Data.id_client
            else:
                self.__clientRepository.CreateRecord({"email": email, "name":"prueba"}, "ClientFormCreator")
                clientCreateFoundId = self.__getClient(email)
                client_fk = clientCreateFoundId.Data.id_client

            dataCreation["client_fk"] = client_fk
            dataCreation["email_token"] = token
            ScannedImageCreated = self.__scannedImageRepository.CreateRecord(dataCreation, "ScannedImageCreator")

            uow.commit()
        return ScannedImageCreated  
      
    def __getClient(self,email):
        return   self.__clientRepository.GetByColumn({"email": email})      