
from django.urls import path
from . import views 
from .views import Inicio


app_name = 'Principal'

urlpatterns = [
   path('Objetivos/', views.ObjetivosDesarrollo, name = 'Objetivos_Desarrollo'),
   path('', Inicio.as_view(), name = 'index'),

]

 