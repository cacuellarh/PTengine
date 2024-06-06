from TrackMyPrice.Core.Application.Contracts.Repository.IBaseRepository import IBaseRepository
from TrackMyPrice.Core.Application.Contracts.UnitOfWork.IUnitOfWork import IUnitOfWork
from TrackMyPrice.Infraestructure.Persistence.BaseRepository import BaseRepository
import inspect
from TrackMyPrice.Infraestructure import Persistence
import pkgutil
from django.db import transaction

class UnitOfWork(IUnitOfWork):
    
    def __init__(self):
        self.__listRepositories : dict = {}

    def __enter__(self):
        self.__transaction = transaction.atomic()
        self.__transaction.__enter__()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.commit()
        else:
            self.rollback()

    def commit(self):
        self.__transaction.__exit__(None, None, None)        

    def rollback(self):
        self.__transaction.__exit__(Exception, Exception(), None)
     
              


