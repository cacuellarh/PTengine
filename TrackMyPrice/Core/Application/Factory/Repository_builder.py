import inspect
import pkgutil
from TrackMyPrice.Core.Application.Contracts.Repository.IBaseRepository import IBaseRepository
from TrackMyPrice.Core.Application.Utils.SingletonDecorator import singleton
from TrackMyPrice.Infraestructure import Persistence
from TrackMyPrice.Infraestructure.Persistence.BaseRepository import BaseRepository


class RepositoryBuilder:
    __listRepositories : dict = {}

    @staticmethod
    def BuildRepositories():
        
        packPath = Persistence.__path__[0]

        for loader, name, is_pkg in pkgutil.walk_packages([packPath]):
            if not is_pkg:

                module = __import__(f"TrackMyPrice.Infraestructure.Persistence.{name}", fromlist=[name])
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, IBaseRepository) and obj is not IBaseRepository and obj is not BaseRepository:
                        RepositoryBuilder.__listRepositories[name] = obj


    @staticmethod
    def GetRepository(repositoryType : str):

        if repositoryType in RepositoryBuilder.__listRepositories:
            return RepositoryBuilder.__listRepositories[repositoryType]
        raise KeyError(f"El nombre del repositorio {repositoryType} no existe")         