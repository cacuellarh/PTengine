from abc import ABC, abstractmethod
from TrackMyPrice.Core.Application.Models.Response.Response import RepositoryResponse

class IUseCase(ABC):

    @abstractmethod
    def Execute(self,data) -> RepositoryResponse:
        pass