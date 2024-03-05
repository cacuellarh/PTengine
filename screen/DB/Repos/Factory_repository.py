from screen.Interfaces.IRepos import IRepository
from django.db import models
from abc import ABC, abstractmethod
class FactoryRepository(IRepository):
    
    def __init__(self) -> None:
        self.model : models.Model
        
    def get_all(self):
        return self.model.objects.all()
    
    def get(self, column, value):
        try:
            return self.model.objects.get(**{column: value})
        except Exception as e:
            return None
        
    def create(self, model : models.Model):  
        try:
            
            return model.save()

        except Exception as e:
            print(e)
        
        return None    
            