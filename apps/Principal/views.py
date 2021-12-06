import random
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Categoria


def consulta(id):
	try:
		return Post.objects.get(id = id)
	except:
		return None

# Create your views here.

def ObjetivosDesarrollo(request):
	return render(request,'Principal/Objetivos_Desarrollo.html')

class Inicio(ListView):

	def get(self,request,*args,**kwargs):
		posts = list(Post.objects.filter(
			estado = True,
			publicado = True,
			).values_list('id', flat = True))
		principal = random.choice(posts)
		posts.remove(principal)

		principal = consulta(principal)

		post1 = random.choice(posts)
		posts.remove(post1)
		post2 = random.choice(posts)
		posts.remove(post2)
		post3 = random.choice(posts)
		posts.remove(post3),
		post4 = random.choice(posts)
		posts.remove(post4)


		try:
			post_ODS = post.objects.filter(
				estado = True,
				publicado = True,
				categoria = Categoria.objects.get(nombre = 'ODS')
				).latest('fecha_publicación')

		except:
			post_ODS = None


		try:
			post_extra = post.objects.filter(
				estado = True,
				publicado = True,
				categoria = Categoria.objects.get(nombre = 'Recursos extra')
				).latest('fecha_publicación')

		except:
			post_extra = None



		contexto = {

			'principal':principal,
			'post1': consulta(post1),
			'post2': consulta(post2),
			'post3': consulta(post3),
			'post4': consulta(post4),
			'post_ODS': post_ODS,
			'post_extra': post_extra,
		}
		
		return render (request,'index.html',contexto)

