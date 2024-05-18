from TrackMyPrice.Core.Application.Contracts.Factories.FormFactories.IFormCreators import IFormCreator
from django import forms
from screen.DB.Forms.Image_traker import ImageForm


class ImageTrackFormCreator(IFormCreator):

    def CreateForm()-> forms.ModelForm:
        return ImageForm

class ErrorFormCreator(IFormCreator):

    def CreateForm()-> forms.ModelForm:
        return Error
