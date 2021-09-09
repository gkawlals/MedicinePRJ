from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ocr_upload', views.ocr_upload, name="ocr_upload"),
    path('ocr_list', views.ocr_list, name="ocr_list"),
    path('FindPass', views.FindPass, name="FindPass"),
    path('LoginPage', views.LoginPage, name="LoginPage"),
    path('NewCreate', views.NewCreate, name="NewCreate"),
]

