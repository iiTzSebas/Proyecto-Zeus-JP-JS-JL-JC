from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='saludo'),
    path('despedir/', views.despedir, name='despedir'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('inicio/', views.inicio, name='inicio'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
]