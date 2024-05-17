from  TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.FormFactory import IFormFactory
from TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.IFormCreators import IFormCreator
import inspect

class FormFactory(IFormFactory):

    def __init__(self) -> None:
        self.__formsRegistered: dict[str, IFormCreator] = {}
        self.__BuildFactories()
    def CreateFormFactory(self,factoryName : str) -> IFormCreator:
        
        if factoryName in self.__formsRegistered:
            return self.__formsRegistered[factoryName]
        else:
            raise ValueError(f"La fabrica con nombre {factoryName} no se encuentra registada")

    def __BuildFactories(self)-> None:

        module = __import__('TrackMyPrice.Core.Application.Factory.FormsCreators', fromlist=["FormsCreators"])
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, IFormCreator) and obj is not IFormCreator:
                self.__formsRegistered[name] = obj
    