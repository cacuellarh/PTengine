import time
from selenium import webdriver
from ..Services.Console_info import Console


class ScreenShot:

    url = ""
    options : webdriver
    boswer : webdriver
    heigth : int

    def _conf(self):

        Console.info("Iniciando screen")
        self.options.add_argument('--window-size=1024,768')
        self.options.add_argument('--headless')
        self.options.add_argument("--hide-scrollbars")
        self.options.add_argument('--disable-gpu')
        
    def _calculate_height(self):
        
        self.boswer.get(self.url)
        Console.info("Cargando URL")
        time.sleep(4)
        self.heigth = self.boswer.execute_script(
        "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )")    
        time.sleep(2)
        Console.info(f"Calculando altura de screen: {self.heigth}" )
        self.boswer.close()
        
    def take_screen(self, url_, action):
        
        Console.success("Tomando captura")
        self.url = url_
        self.options = webdriver.ChromeOptions()
        self._conf()
        self.boswer = webdriver.Chrome(options=self.options)
        
        self._calculate_height()
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument(f'--window-size=1080,{self.heigth}')
        options.add_argument('--headless')
        options.add_argument("--hide-scrollbars")
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        
        self.browser = webdriver.Chrome(options=options)
        self.browser.get(self.url)
        
        if action == "save":
            self.browser.save_screenshot("C:\\Users\\lolo\\Desktop\\Programacion\\prueba micha_app\\bosquejo\\screen\\static\\img\\prueba_python.png")
            Console.success("Screen guardado")
        elif action == "validate":
            self.browser.save_screenshot("C:\\Users\\lolo\\Desktop\\Programacion\\prueba micha_app\\bosquejo\\screen\\static\\temp\\temp_validate.png")
            Console.success("Screen guardado")       