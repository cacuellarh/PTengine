from django.db import models

class RepositoryBase:
    
    def __init__(self,entity) -> None:
        self.entity : models.Model = entity
        
        
    def get_all(self):
        
        return self.entity.objects.all()