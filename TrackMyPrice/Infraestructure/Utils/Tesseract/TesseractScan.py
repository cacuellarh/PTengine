from TrackMyPrice.Core.Application.Contracts.SeleniumContracts import * 
from PIL import Image
import pytesseract
from django.conf import settings
from TrackMyPrice.Core.Application.Models.Request.TesseractRequest import TesseractScanRequest

class TesseractScanToFloat(IConvertImgToFloat):

    def __init__(self)-> None:
        self.__preprocessorImages = settings.DI_INJECTOR.get(IPreproccesImage)
        pytesseract.pytesseract.tesseract_cmd = settings.PATHS["tesseract"]
        self.__tesseractConfiguration = settings.TESSERACT_FLAGS
        
    def Convert(self,imagePath : str) -> float:

        processed_image = self.__preprocessorImages.PreprocessImage(imagePath)
        pil_image = Image.fromarray(processed_image)
        extracted_text = pytesseract.image_to_string(pil_image, config=self.__tesseractConfiguration)
        print(f"Informacion extraida: {extracted_text}")
        cleanText = extracted_text.strip()

        if cleanText != "":
            print(f"Precio obtenido {extracted_text}")
            return float(cleanText)
        else:
            print(f"No se puedo convertir{extracted_text}")    
        return 0 

