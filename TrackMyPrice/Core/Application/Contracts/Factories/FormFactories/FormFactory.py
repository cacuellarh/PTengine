from abc import ABC, abstractmethod
from TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.IFormCreators import IFormCreator

class IFormFactory(ABC):

    @abstractmethod
    def CreateFormFactory(factoryName : str) -> IFormCreator:
        pass