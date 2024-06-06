from abc import ABC, abstractmethod
from TrackMyPrice.Core.Application.Models.Response.Response import RepositoryResponse

class IScannedImageCreateUseCase(ABC):

    @abstractmethod
    def Execute(self, request) -> RepositoryResponse:
        pass