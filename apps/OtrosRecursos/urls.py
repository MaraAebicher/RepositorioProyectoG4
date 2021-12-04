from django.urls import path
from . import views 

app_name = 'OtrosRecursos'

urlpatterns = [
   path('OtrosRecursos/', views.OtrosRecursos, name = 'Otros_Recursos')

]
