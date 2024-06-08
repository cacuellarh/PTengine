from abc import ABC, abstractmethod
from TrackMyPrice.Core.Application.Models.Response.Response import RepositoryResponse

class IWriteRecordUseCase(ABC):

    @abstractmethod
    def Execute(self, request) -> RepositoryResponse:
        pass