from abc import ABC, abstractmethod


class Inotification(ABC):
    
    @abstractmethod
    def notify(self):
        pass
    
    @abstractmethod
    def conf(self, args):
        pass
        