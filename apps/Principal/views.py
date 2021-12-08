import random
from django.shortcuts import render,redirect
from django.views.generic import ListView,View,DetailView
from django.core.mail import send_mail
from ProyectoG4.settings.base import EMAIL_HOST_USER
from .models import Post,Categoria,RedesSociales,Web,Suscriptor
from .utils import *
from .forms import ContactoForm


class Inicio(ListView):

    def get(self,request,*args,**kwargs):
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True
                ).values_list('id',flat = True))
        principal = random.choice(posts)
        posts.remove(principal)
        principal = consulta(principal)

        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)
        post4 = random.choice(posts)
        posts.remove(post4)

        try:
            post_extra = Post.objects.filter(
                                estado = True,
                                publicado = True,
                                categoria = Categoria.objects.get(nombre = 'Información extra')
                                ).latest('fecha_publicacion')
        except:
            post_extra = None

        try:
            post_ODS = Post.objects.filter(
                            estado = True,
                            publicado = True,
                            categoria = Categoria.objects.get(nombre = 'ODS')
                            ).latest('fecha_publicacion')
        except:
            post_ODS = None

        contexto = {
            'principal':principal,
            'post1': consulta(post1),
            'post2': consulta(post2),
            'post3': consulta(post3),
            'post4': consulta(post4),
            'post_ODS':post_ODS,
            'post_extra':post_extra,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
        }

        return render(request,'index.html',contexto)

class Listado(ListView):

    def get(self,request,nombre_categoria,*args,**kwargs):
        contexto = generarCategoria(request,nombre_categoria)
        return render(request,'categoria.html',contexto)

class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
        form = ContactoForm()
        contexto = {
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'form':form,
        }
        return render(request,'contacto.html',contexto)

    def post(self,request,*args,**kwargs):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Principal:index')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'contacto.html',contexto)

class DetallePost(DetailView):
    def get(self,request,slug,*args,**kwargs):
        try:
            post = Post.objects.get(slug = slug)
        except:
            post = None
        posts = list(Post.objects.filter(
                estado = True,
                publicado = True,
                ).values_list('id',flat = True))
        posts.remove(post.id)
        post1 = random.choice(posts)
        posts.remove(post1)
        post2 = random.choice(posts)
        posts.remove(post2)
        post3 = random.choice(posts)
        posts.remove(post3)

        contexto = {
            'post':post,
            'sociales':obtenerRedes(),
            'web':obtenerWeb(),
            'post1':consulta(post1),
            'post2':consulta(post2),
            'post3':consulta(post3),
        }
        return render(request,'post.html',contexto)

class Suscribir(View):
    def post(self,request,*args,**kwargs):
        correo = request.POST.get('correo')
        Suscriptor.objects.create(correo = correo)
        asunto = 'GRACIAS POR SUSCRIBIRTE A NUESTRO BLOG!'
        mensaje = 'Te haz suscrito exitosamente, ¡Muchas gracias!'
        try:
            send_mail(asunto,mensaje,EMAIL_HOST_USER,[correo])
        except:
            pass

        return redirect('Principal:index')
