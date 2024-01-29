from selenium import webdriver
from ..Services.Console_info import Console
from selenium.webdriver.chrome.service import Service
import time

class ScreenShot:

    url = ""
    options : webdriver
    boswer : webdriver
    heigth : int
    save_path_img = "/home/ec2-user/entornos/ptengine/PTengine/screen/static/img/"
    save_path_temp = "/home/ec2-user/entornos/ptengine/PTengine/screen/static/temp/"
    
    def _conf(self):
        Console.info("Iniciando screen")
        self.options.add_argument('--disable-software-rasterizer')
        self.options.add_argument('--window-size=1024,768')
        self.options.add_argument('--headless')
        self.options.add_argument("--hide-scrollbars")
        self.options.add_argument('--disable-gpu')

    def _calculate_height(self):
        try:
            self.boswer.get(self.url)
            Console.info("Cargando URL")
            time.sleep(6)  # Puedes ajustar el tiempo de espera según sea necesario
            self.height = self.boswer.execute_script(
                "return Math.max( document.body.scrollHeight, document.documentElement.scrollHeight)")
            Console.info(f"Calculando altura de screen: {self.height}")
            
        except Exception as e:
            Console.error(f"Error al calcular la altura: {str(e)}")

    def take_screen(self, url_, action):
        #try:
            Console.success("Tomando captura")
            self.url = url_
            self.options = webdriver.ChromeOptions()
            self._conf()
            self.boswer = webdriver.Chrome(options=self.options)
            
            self._calculate_height()

            options = webdriver.ChromeOptions()
            options.add_argument('--disable-software-rasterizer')
            options.add_argument('--no-sandbox')
            options.add_argument(f'--window-size=1080,{self.height}')
            options.add_argument('--headless')
            options.add_argument("--hide-scrollbars")
            options.add_argument('--disable-gpu')
            options.add_argument('--ignore-certificate-errors')

            self.boswer = webdriver.Chrome(options=options)
            self.boswer.get(self.url)

            if action == "save":
                self.boswer.save_screenshot(f"{self.save_path_img}prueba_python.png")
                Console.success("Screen guardado")
                Console.success(f"Ruta del screen {self.save_path_img}prueba_python.png")
            elif action == "validate":
                self.boswer.save_screenshot(self.save_path_temp + "temp_validate.png")
                Console.success("Screen guardado")
        # except Exception as e:
        #     Console.warning(f"Error al tomar la captura de pantalla: {str(e)}")
        # finally:
        #     self.boswer.quit()  # Asegúrate de cerrar la instancia del navegador al finalizar       