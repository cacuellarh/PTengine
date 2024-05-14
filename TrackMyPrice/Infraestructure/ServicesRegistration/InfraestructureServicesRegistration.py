from injector import Binder
from ..Utils.ImageTools.Preprocess import PreprocessImage, IPreproccesImage
from ..Utils.Tesseract.TesseractScan import TesseractScanToFloat, IConvertImgToFloat

def InfraestructureServicesInject(binder: Binder):
    binder.bind(IPreproccesImage, to=PreprocessImage)
    binder.bind(IConvertImgToFloat, to=TesseractScanToFloat)
    return binder