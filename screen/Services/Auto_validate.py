import decimal
from ..Engine.OCR import OCR
from ..Engine.Screen import ScreenShot
from ..models import ImageTrack
from PIL import Image
from ..Services.Console_info import Console

#CLASE QUE AJUSTA LAS COORDENADAS DE LA IMAGEN, ESCALA EN PROPORCIO AL PORCENTAGE INGRESADO EN EL PARAMETRO {PERCENTAGE}

#CLASE QUE REALIZA VALIDACION AUTOMATICA DEL LOS PRECIOS
class Validate:
    
    #ATRIBUTOS DE CLASE, RUTAS DE LA CARPETA TEMPORAL Y OBJETO DEL OCR
    #_temp_path = "C:\\Users\\lolo\\Desktop\\Programacion\\prueba micha_app\\bosquejo\\screen\\static\\temp\\"
    _temp_path = "/usr/ptengine/PTengine/screen/static/temp/"
    ocr : OCR  
    
    #INICIALIZACION DE ATRIBUTOS
    def __init__(self):
        
        self.screen = ScreenShot()
        self.ocr = OCR()
    
    #METODO PRINCIPAL, ENCARGADO DE CONECTAR CON EL OCR Y REALIZAR VALIDACIONES DE LOS PRECIOS    
    def aut_validate(self, img : ImageTrack):
        

        #METODO ENCARGADO DE TOMAR EL SCREEN SEGUN LA URL GUARDADA EN BASE   
        self.screen.take_screen(url_= img.url, action="validate", file_name=img.email_token)

        #SE ASIGNAN LAS RUTAS DONDE SERAN GUARDADAS LAS IAMGENES TEMPORALES PARA SER ANALIZADAS 
        ruta_entrada = f"{self._temp_path}temp_validate.png"
        ruta_salida = f"{self._temp_path}price_cut_{img.email_token}.png"
        route_calibrate = f"{self._temp_path}{img.email_token}.png"
        
        #ABRE LA IMAGEN TEMPORAL Y SE REALIZAR CORTE DE ESTA MISMA SEGUN LAS COORDENADAS GUARDADAS EN DB
        with Image.open(f"{self._temp_path}{img.email_token}.png") as img_cut:
    
            x =  img.x
            y =  img.y
            h =  img.height
            w = img.width
            
            img_cortada = img_cut.crop((x, y, x + w, y + h))
            
            img_cortada.save(ruta_salida) #SE GUARDA IMAGEN CORTADA
            
            price_check = self.ocr.validate_number(ruta_salida) #SE VALIDA SI LA IMAGEN CONTIENE UN NUMERO
            
            if price_check["status"]: #SE VALIDA SI LA IMAGEN RECIEN CORTADA AL SER CONVERTIDA A STRING, CONTIENE UN NUMERO
                #if self.ocr.validate_consistency(price_check, img.price): #!IMPORTANTE, SE REALIZA CERCANIA DEL NUMERO CONVERTIDO CONTRA EL NUMERO GUARDADO
                                                                          #ESTO CON EL FIN DE EVITAR QUE CUALQUIER NUMERO QUE SE ESCANEE SEA APROVADO COMO UN CAMBIO DE PRECIO  
                    
                    price_found = self.ocr.convert(ruta_salida)    
                    return  {"current_price" : price_found, "db_price" : img.price}
            
            #else: #SI NO CONTIENE NUMERO SE REALIZA AJUSTE DE TAMAÑO DE RECORTE EN H Y W, CON EL FIN DE ECONTRAR UN NUMERO CERCANO
                
                #SE CALIBRA EL TAMAÑO Y SE TOMA SCREEN
                # Console.warning("Re calibrando coordenadas")
                # c = CalibrateCordinates.calibrate(img, 1.05)
                # Console.warning(f"Coordenadas re calibradas: {c.x}, {c.y}, {c.width}, {c.height}")
                # img_cut = img_cut.crop((c.x, c.y, c.x + c.width, c.y + c.height))
                # img_cut.save(route_calibrate)