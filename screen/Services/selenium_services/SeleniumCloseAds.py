from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from screen.models import ElementsXpaths
from screen.DB.Repos.XpathRepository import XpathRepository


class SeleniumCloseAds:
    
    def __init__(self, driver) -> None:
        self.repository = XpathRepository()
        self.driver =  driver
        
    def FindUrl(self, url, options = None):
        pages: ElementsXpaths = self.repository.get_all()
        for page  in pages:
            if page.domain in url:
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, page.xpath)))
                    self.driver.execute_script("arguments[0].style.display = 'none';", element) 
                    print("Se ocultó el elemento exitosamente")
                except TimeoutException:
                    print("Elemento no encontrado")
                return  
        print("No se encontró ninguna página coincidente en la URL")  
    
    def ZoomPriceElement(self, element):
        
        self.driver.execute_script("arguments[0].style.fontSize = '30px';", element)          