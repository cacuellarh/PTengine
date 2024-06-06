from abc import ABC, abstractmethod
from TrackMyPrice.Core.Application.Models.Response.Response import RepositoryResponse

class IBaseRepository(ABC):

    @abstractmethod
    def GetAll(filter:bool = False, predicate = None)-> RepositoryResponse:
        pass

    @abstractmethod
    def GetByColumn(predicate) -> RepositoryResponse:
        pass

    @abstractmethod
    def CreateRecord(data, modelForm)-> RepositoryResponse:
        pass

    @abstractmethod
    def UpdateRecord(id: dict, data: dict)-> RepositoryResponse:
        pass

    @abstractmethod
    def DeleteRecord(id: dict)-> RepositoryResponse:
        pass
