from abc import ABC, abstractmethod

from TrackMyPrice.Core.Application.Contracts.Repository.IBaseRepository import IBaseRepository

class IUnitOfWork(ABC):

    @abstractmethod
    def commit(self)-> None:
        pass
    @abstractmethod    
    def rollback(self)-> None:
        pass
