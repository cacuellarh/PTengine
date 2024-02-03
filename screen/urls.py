from django.urls import path
from .Views.ScreenView import ScreenView, Exec, SaveScreen,AsyncTask
from rest_framework.authtoken import views

urlpatterns = [
    
    path('tracker_price', ScreenView.as_view()),
    path('exec', Exec.as_view(), name="execute"),
    path('save_image', SaveScreen.as_view(), name="save"),
    path('save_image_db', ScreenView.as_view(), name="save_db"),
    # path('validate', ValidatePrice.as_view(), name="save_db")
    path('async_prueba', AsyncTask.as_view(), name="save_db"),
]