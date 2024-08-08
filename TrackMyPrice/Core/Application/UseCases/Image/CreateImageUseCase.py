from TrackMyPrice.Core.Application.Contracts.UseCase.IUseCase import IUseCase
from TrackMyPrice.Core.Application.Models.Response.Response import RepositoryResponse
from TrackMyPrice.Infraestructure.Persistence.ImageBasicRepository import ImageBasicRepositoryImp

class CreateImageUseCase(IUseCase):

    def __init__(self):
        self.repository = ImageBasicRepositoryImp()
        
    def Execute(self,data) -> RepositoryResponse:
        return self.repository.CreateRecord(data,"ImageFormCreator")