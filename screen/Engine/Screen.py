from selenium import webdriver
from screen.Services.selenium_services.SeleniumCloseAds import SeleniumCloseAds
from bosquejo.Domain.Contracts import ISeniumScreenService
from ..Services.Console_info import Console
from django.conf import settings
import time
import logging

class ScreenShot():

    url = ""
    options : webdriver 
    browser : webdriver 

    width : int
    
    ## WINDOWS MODE
    
    save_path_img = settings.PATHS["img_folder"]
    save_path_temp = settings.PATHS["tmp"]
    
    ## LINUX MODE
    
    #save_path_img = "/usr/ptengine/PTengine/screen/static/img/"
    #save_path_temp = "/usr/ptengine/PTengine/screen/static/temp/"
    
        
    def _ConfigSelenium(self):
        
        logging.getLogger('selenium').setLevel(logging.WARNING)
        self.options = webdriver.ChromeOptions()

        #self.options.add_argument('--headless')
        #self.options.add_argument('--disable-software-rasterizer')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--window-size=1080,380')
        self.options.add_argument("--hide-scrollbars")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--ignore-certificate-errors')
        #self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-extensions')
        self.options.add_argument('--disable-infobars')
        self.options.add_argument('--disable-notifications')
        #self.options.add_argument('--disable-popup-blocking')
        self.options.add_argument('--disable-logging')
        #self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.140 Safari/537.3")
        self.browser = webdriver.Chrome(options=self.options)
        
    def _calculate_height(self):
        self._ConfigSelenium()
        try:
          
            self.browser.get(self.url)
            Console.info("Cargando URL")
            
            time.sleep(2)

            height = self.browser.execute_script(
                "return Math.max( document.body.scrollHeight, document.documentElement.scrollHeight)")
            Console.info(f"Calculando altura de screen: {height}")
            Console.info(f"ALTURA TESTEADA {height}")
            return height
            
        except Exception as e:
            Console.warning(f"Error al calcular la altura: {str(e)}")
        finally:
            self._CloseAllWindows()
            self.browser.quit()

    def take_screen(self, url_, action, file_name):
        try:
            Console.success("Tomando captura")
            self.url = url_    
            height = self._calculate_height()
            Console.info(f"altura obtenida{height}")
            self.options.add_argument(f'--window-size=1080,{height}')

            self.browser.quit()
            self.browser = webdriver.Chrome(options=self.options)

            self.browser.get(self.url)
            seleniumServices = SeleniumCloseAds(self.browser)
            seleniumServices.FindUrl(self.url)
            # time.sleep(10)

            if action == "save":
                self.browser.save_screenshot(f"{self.save_path_img}{file_name}.png")
                Console.success("Screen guardado")
                Console.success(f"Ruta del screen {self.save_path_img}prueba_python.png")
            elif action == "validate":
                self.browser.save_screenshot(f"{self.save_path_temp}{file_name}.png")
                Console.success("Screen guardado")          
        except Exception as e:
            Console.warning(f"Error al tomar la captura de pantalla: {str(e)}")
        finally:
            self._CloseAllWindows()
            self.browser.quit()

    def _CloseAllWindows(self):

        for windowsHandle in self.browser.window_handles:
            self.browser.switch_to.window(windowsHandle)   
            self.browser.close()
            
       