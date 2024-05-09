from injector import Binder
from injector import Injector

from ..Utils.ImageTools.Preprocess import PreprocessImage,IPreproccesImage
def InfraestructureServicesInject(binder : Binder):
    binder.bind(IPreproccesImage, to=PreprocessImage)

DI_INJECTOR = Injector(InfraestructureServicesInject)    