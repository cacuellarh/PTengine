import inspect
import pkgutil
from TrackMyPrice.Core.Application.Contracts.UseCase.WriteRecord_useCase import IWriteRecordUseCase
from TrackMyPrice.Core.Application.UseCases import WriteUseCases



class WriteUseCaseBuilder:
    __listWriteUseCases : dict = {}

    @staticmethod
    def _BuildWriteUseCases():
        
        packPath = WriteUseCases.__path__[0]
        for loader, name, is_pkg in pkgutil.walk_packages([packPath]):
            if not is_pkg:
                module = __import__(f"TrackMyPrice.Core.Application.UseCases.WriteUseCases.{name}", fromlist=[name])
                for name, obj in inspect.getmembers(module, inspect.isclass):
                    if issubclass(obj, IWriteRecordUseCase) and obj is not IWriteRecordUseCase:
                        WriteUseCaseBuilder.__listWriteUseCases[name] = obj


    @staticmethod
    def GetWriteUseCase(repositoryType : str):

        if repositoryType in WriteUseCaseBuilder.__listWriteUseCases:
            return WriteUseCaseBuilder.__listWriteUseCases[repositoryType]
        raise KeyError(f"El nombre del caso de uso {repositoryType} no existe")