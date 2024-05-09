from TrackMyPrice.Core.Application.Contracts.SeleniumContracts import * 
from PIL import Image
import pytesseract
from TrackMyPrice.Infraestructure.ServicesRegistration.InfraestructureServicesRegistration import DI_INJECTOR
from TrackMyPrice.Core.Application.Models.Request.TesseractRequest import TesseractScanRequest

class TesseractScanToFloat(IConvertImgToFloat):

    def __init__(self, tesseractConfiguration: TesseractScanRequest)-> None:
        self.__preprocessorImages = DI_INJECTOR.get(IPreproccesImage)
        pytesseract.pytesseract.tesseract_cmd = tesseractConfiguration.tesseractPath
        self.__tesseractConfiguration = tesseractConfiguration
        
    def Convert(self,imagePath : str) -> float:

        processed_image = self.__preprocessorImages.PreprocessImage(imagePath,pathSave=self.__tesseractConfiguration.preprocessorFileSaveTest)
        pil_image = Image.fromarray(processed_image)
        extracted_text = pytesseract.image_to_string(pil_image, config=self.__tesseractConfiguration.tesseractFlagsConfiguration)
        print(f"Informacion extraida: {extracted_text}")
        cleanText = extracted_text.strip()

        if cleanText != "":
            print(f"Precio obtenido {extracted_text}")
            return float(cleanText)
        else:
            print(f"No se puedo convertir{extracted_text}")    
        return 0 

