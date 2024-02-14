from screen.models import Client

class Client_repos():
    
    
    def get(self,column,value):
        
        try:
            return Client.objects.get(**{column: value})
        except Exception as e:
            return None
        
    def create(self,data):
        
        return Client.objects.create(email= data["email"])
    
        