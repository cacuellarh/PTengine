from abc import ABC, abstractmethod

from TrackMyPrice.Core.Application.Models.Response.Response import RepositoryResponse

class IClientGetUseCase(ABC):

    @abstractmethod
    def Execute(dataFilter)-> RepositoryResponse:
        pass