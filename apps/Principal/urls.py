
from django.urls import path
from . import views 


app_name = 'Principal'

urlpatterns = [
   path('Objetivos/', views.ObjetivosDesarrollo, name = 'Objetivos_Desarrollo')

]

 