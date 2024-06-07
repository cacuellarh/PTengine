
from TrackMyPrice.Core.Application.Contracts.Repository.IClientRepository import IClientRepository
from TrackMyPrice.Core.Application.Contracts.UnitOfWork import IUnitOfWork
from TrackMyPrice.Core.Application.Contracts.UseCase.WriteRecord_useCase import IWriteRecordUseCase
from django.conf import settings

from TrackMyPrice.Core.Application.Models.Response.Response import RepositoryResponse

class ClientWriteUseCase(IWriteRecordUseCase):

    def __init__(self) -> None:
        self.__clientRepository : IClientRepository  = settings.DI_APLICATION.get(IClientRepository)
        self.__unitOfWork = settings.DI_APLICATION.get(IUnitOfWork)

    def Execute(self, request) -> RepositoryResponse:

        return self.__clientRepository.CreateRecord(request.POST, "ClientFormCreator")
        
