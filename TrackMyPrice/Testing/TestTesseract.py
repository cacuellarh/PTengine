from TrackMyPrice.Infraestructure.Utils.Tesseract.TesseractScan import TesseractScanToFloat
from TrackMyPrice.Core.Application.Models.Request.TesseractRequest import TesseractScanRequest

params = TesseractScanRequest(
    tesseractPath="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract", #ruta del ejecutable de tesseract
    tesseractFlagsConfiguration=r'--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789 outputbase digits', #flags de configuracion
    preprocessorFileSaveTest="C:\\test\\prepros\\test.png" #Ruta donde se guarda la imagen preprocesada para validar
    )

tess = TesseractScanToFloat(params)
tess.Convert("C:\\test\\3.png") #ruta de imagen que se requiere convertir