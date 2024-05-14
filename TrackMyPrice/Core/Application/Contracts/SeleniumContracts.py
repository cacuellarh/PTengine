from abc import ABC, abstractmethod

class IConvertImgToFloat(ABC):

    @abstractmethod    
    def Convert(self,imagePath : str) -> float:
        pass

class IPreproccesImage(ABC):

    @abstractmethod    
    def PreprocessImage(self, imagePath:str, pathSave:str):
        pass


class IConfigurateTesseract(ABC):

    @abstractmethod    
    def ChangueConfigurationFlag(self, flagConfiguration:str)-> None:
        pass
