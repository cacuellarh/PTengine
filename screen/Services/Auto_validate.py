from ..models import History_events
from ..Engine.OCR import OCR
from ..Engine.Screen import ScreenShot
from ..models import ImageTrack
from PIL import Image
from ..Services.Console_info import Console
from ..DB.Repos.Log_repos import LogRepos
from django.conf import settings


#CLASE QUE AJUSTA LAS COORDENADAS DE LA IMAGEN, ESCALA EN PROPORCIO AL PORCENTAGE INGRESADO EN EL PARAMETRO {PERCENTAGE}

#CLASE QUE REALIZA VALIDACION AUTOMATICA DEL LOS PRECIOS
class Validate:
    
    #ATRIBUTOS DE CLASE, RUTAS DE LA CARPETA TEMPORAL Y OBJETO DEL OCR
    _temp_path = settings.PATHS["tmp"]
    _error_path = settings.PATHS["error"]
    #_temp_path = "/usr/ptengine/PTengine/screen/static/temp/"
    ocr : OCR  
    
    #INICIALIZACION DE ATRIBUTOS
    def __init__(self):
        
        #corregir DI
        self.screen = ScreenShot()
        self.ocr = OCR(settings.PATHS["tmp"], settings.PATHS["tesseract"])
        self.log_repos = LogRepos()
        self.event = History_events
        
    #Metodo para guardar evento a realizar
      
    #METODO PRINCIPAL, ENCARGADO DE CONECTAR CON EL OCR Y REALIZAR VALIDACIONES DE LOS PRECIOS    
    def aut_validate(self, img : ImageTrack):
        
        #Se guarda registro del evento inicial
        self.event = self.log_repos.save_event(img)
        #METODO ENCARGADO DE TOMAR EL SCREEN SEGUN LA URL GUARDADA EN BASE   
        self.screen.take_screen(url_= img.url, action="validate", file_name=img.email_token)
        #ABRE LA IMAGEN TEMPORAL Y SE REALIZAR CORTE DE ESTA MISMA SEGUN LAS COORDENADAS GUARDADAS EN DB
        return self._process_image(img)
        
        
    def _process_image(self,img):
        
        #SE ASIGNAN LAS RUTAS DONDE SERAN GUARDADAS LAS IAMGENES TEMPORALES PARA SER ANALIZADAS
         
        ruta_entrada = f"{self._temp_path}temp_validate.png"
        ruta_salida = f"{self._temp_path}price_cut_{img.email_token}.png"
        route_calibrate = f"{self._temp_path}{img.email_token}.png"
        route_err = f"{self._error_path}{img.email_token}.png"
        
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
                    #Si el valor si es un precio valido se guarda en el historial de precios
                    self.log_repos.save_history_prices(self.event, price_found)
                    self.log_repos.update_status_event(self.event)
                    return  {"current_price" : price_found, "db_price" : img.price}
            
            else: #SI NO CONTIENE NUMERO SE REALIZA AJUSTE DE TAMAÑO DE RECORTE EN H Y W, CON EL FIN DE ENCONTRAR UN NUMERO CERCANO
                  #Adiccionalmente, se guarda en la tabla de eventos fallidos el registro.
                img_cortada.save(route_err)
                self.log_repos.save_event_error(self.event, route_err)
                Console.warning(f"Log de error guardado de DB, ruta de imagen{route_err}")   
                #SE CALIBRA EL TAMAÑO Y SE TOMA SCREEN
                # Console.warning("Re calibrando coordenadas")
                # c = CalibrateCordinates.calibrate(img, 1.05)
                # Console.warning(f"Coordenadas re calibradas: {c.x}, {c.y}, {c.width}, {c.height}")
                # img_cut = img_cut.crop((c.x, c.y, c.x + c.width, c.y + c.height))
                # img_cut.save(route_calibrate)