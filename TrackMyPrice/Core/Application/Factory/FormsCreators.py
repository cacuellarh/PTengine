from TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.IFormCreators import IFormCreator
from django import forms
from screen.DB.Forms.Client_form import ClientForm
from screen.DB.Forms.Image_traker import ImageForm
from screen.DB.Forms.ErrorForm import ErrorForm


class ScannedImageCreator(IFormCreator):

    def CreateForm()-> forms.ModelForm:
        return ImageForm

class ErrorFormCreator(IFormCreator):

    def CreateForm()-> forms.ModelForm:
        return ErrorForm

class ClientFormCreator(IFormCreator):

    def CreateForm()-> forms.ModelForm:
        return ClientForm