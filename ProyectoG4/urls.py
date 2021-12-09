"""ProyectoG4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views  
from django.conf import settings
from django.views.static import serve 
from django.utils.text import slugify


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.Grupo4, name = 'primera_vista'), lo comento por ahora! (Mar)
    path('', include(('apps.Principal.urls','Principal'))),

#PATH QUE APUNTA A APPS

#path('OtrosRecursos/', include('apps.OtrosRecursos.urls')), Estoy probando algo, lo comento tambien por ahora :) (Mar)


]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve , {
            'document_root':settings.MEDIA_ROOT,
        }),
    ]

