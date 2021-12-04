from django.shortcuts import render

# Create your views here.

def ObjetivosDesarrollo(request):
	return render(request,'Principal/Objetivos_Desarrollo.html')