import string
import pytesseract
from PIL import Image
from ..Services.Console_info import Console
import cv2
from TrackMyPrice.Core.Application.Contracts.SeleniumContracts import *
import sys
sys.path.append(".")

class OCR(IConvertImgToFloat, IPreproccesImage):
    
    #Configuracion de flags para tesseract
    custom_config :string = r'--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789 outputbase digits'
    #_temp_path = "/usr/ptengine/PTengine/screen/static/temp/"

    def __init__(self, temporalPath:string, tesseractPath:string) -> None:
        
        pytesseract.pytesseract.tesseract_cmd = tesseractPath
        self._temp_path = temporalPath
        Console.info("Iniciando OCR")
        
    def PreprocessImage(self,image_path):
        image = cv2.imread(image_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return threshold_image
    
    def Convert(self,image_path : str) -> float:
        processed_image = self.PreprocessImage(image_path)
        pil_image = Image.fromarray(processed_image)
        extracted_text = pytesseract.image_to_string(pil_image, config=self.custom_config)
        Console.info(f"Precio obtenido {extracted_text}")
        cleanText = extracted_text.strip()

        if cleanText != "":
            return float(cleanText)

        return 0    
    
    def validate_number(self, path_img_cut) -> bool:
        
        path_img = f"{self._temp_path}img_cut_validate.png"
        with Image.open(path_img_cut) as img:
           img_to_binary = img.point(lambda p: p > 128 and 255)
           img_to_binary.save(path_img)
           
           price_convert = self.convert(path_img)
           
           if isinstance(price_convert, (int, float)):
               Console.success(f"Precio convertido analizado, si es un numero valido {price_convert}")
               return {"status" : True, "price" : price_convert}
           else:
               
               Console.warning(f"El precio convertido no es un numero{price_convert}")
               return {"status" : False, "price" : price_convert}
           
    def ChangueConfigurationFlag(self, flagConfiguration:string)-> None:

        self.custom_config = flagConfiguration

    def ShowCurrentFlagConfiguration(self)-> None:
        print(self.custom_config )