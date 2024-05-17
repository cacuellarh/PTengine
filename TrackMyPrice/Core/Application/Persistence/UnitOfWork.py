from abc import ABC
import abc
from TrackMyPrice.Core.Application.Contracts.Repository.BaseRepository import IBaseRepository
from TrackMyPrice.Infraestructure.Persistence.BaseRepository import BaseRepository
import inspect
from TrackMyPrice.Infraestructure import Persistence
import pkgutil

class UnitOfWork:
    
    def __init__(self):
        self.__listRepositories : dict = {}

    def BuildRepositories(self):
        
        packPath = Persistence.__path__[0]

        for loader, name, is_pkg in pkgutil.walk_packages([packPath]):
            if not is_pkg:

                module = __import__(f"TrackMyPrice.Infraestructure.Persistence.{name}", fromlist=[name])
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, IBaseRepository) and obj is not IBaseRepository and obj is not BaseRepository:
                        self.__listRepositories[name] = obj

              

            #print(f"{loader}, {name}, {is_pkg}")

            # if issubclass(obj, IBaseRepository) and obj is not IFormCreator:
            #     self.__formsRegistered[name] = obj    