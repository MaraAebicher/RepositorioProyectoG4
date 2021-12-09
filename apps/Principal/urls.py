
from django.urls import path
from . import views 
from .views import Inicio,Listado,FormularioContacto,DetallePost,Suscribir
from django.utils.text import slugify


app_name = 'Principal'

urlpatterns = [
 
   path('', Inicio.as_view(), name = 'index'),
   path('post_extra/',Listado.as_view(),{'nombre_categoria':'Información extra'}, name = 'post_extra'),
   path('post_ODS/',Listado.as_view(),{'nombre_categoria':'ODS'}, name = 'post_ODS'),
   path('formulario_contacto/', FormularioContacto.as_view(), name = 'formulario_contacto'),
   path('suscribirse/',Suscribir.as_view(), name = 'suscribirse'),
   path('<slug:slug>/',DetallePost.as_view(), name = 'detalle_post'),
]


  