from abc import ABC, abstractmethod
from django import forms

class IFormCreator(ABC):

    @abstractmethod
    def CreateForm()-> forms.ModelForm:
        pass