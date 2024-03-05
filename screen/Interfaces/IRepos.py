from abc import ABC, abstractmethod

class IRepository:
    
    @abstractmethod
    def get_all():
        pass
    
    def get(column,value):
        pass
    
    def create(data):
        pass