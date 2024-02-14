from screen.models import ImageTrack
from screen.DB.Forms.Image_traker import ImageForm
from screen.API.ResponseServer import ResponseServer
from screen.DB.Repos.Client_repos import Client_repos
from screen.Services.Console_info import Console
class Image_repos():
    
    
    def __init__(self) -> None:
        
        self.client = Client_repos()
        
    def filter(self,column,value):
        
        try:
            
            return ImageTrack.objects.get(**{column: value})
        except:
            
            return None
    
    def create(self,data):
        
        img = ImageForm(data)
        print(img.errors)
        if img.is_valid():          

                
                img.save()           
                return True
        else:
            
            return False        

    def gel_all(self):
        return ImageTrack.objects.all()
            
       
    def activate_notification(self, token):
        

        token_db = self.filter(column="email_token", value=token)
        if token_db is not None:
            token_db.notify_validate = True
            token_db.save()
            return True
        else:
            Console.warning(f"El token no es valido.") 
            return False      

          
                 
    def get_all_joins(self):
        
        return ImageTrack.objects.select_related("client_fk")
                    