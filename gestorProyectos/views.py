# Create your views here.
from gestorProyectos.models import Proyecto, Facultad, Programa, Estandar_competencia
from django.shortcuts import render_to_response

def lista_proyectos(request):
	proyectox = Proyecto.objects.all()
	return render_to_response('lista_proyectos.html',{'lista':proyectox})

def lista_facultades(request):
	facultad = Facultad.objects.all()
	return render_to_response('lista_facultades.html',{'lista':facultad})

def lista_programas(request):
	programa = programa.objects.all()
	return render_to_response('lista_programas.html',{'lista':programa})

def lista_estandares(request):
	estandares = estandares.objects.all()
	return render_to_response('lista_estandares.html',{'lista':estandares})
