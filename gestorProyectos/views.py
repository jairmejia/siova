# Create your views here.
#encoding:utf-8
from gestorProyectos.models import Proyecto, Facultad, Programa, Estandar_competencia
from django.shortcuts import render_to_response
from gestorObjetos.models import Objeto
from gestorProyectos.forms import ProyectoForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from gestorObjetos.forms import EspecificacionForm, cEspecificacionForm, ObjetosForm, cObjetosForm
from django.contrib import messages

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

def Proyecto(request):
	"""
	Vista de acceso al usuario con rol de Docente, de esta manera se le permitirá crearProyectos	
	"""
	if request.user.profile.rol == 'rcat':
		proyectoObj= Objeto.objects.filter(creador=request.user.id).filter(proyecto__isnull=False)
		'''if  request.user.profile.rol == 'rrev':
			proyectoPro1= Objeto.objects.filter(creador=request.user.id).filter(proyecto__isnull=False)'''
	'''gruposu = request.user.groups.all()
		errores = False
		error1 = False
		l_errores=[]
		if request.method == 'POST':
			if not request.POST.get('autores1'):
				l_errores.append('No incluyó au tores al objeto.')
				error1=True
			if not request.POST.get('palabras_claves'):
				l_errores.append('No incluyó palabras claves al objeto.')
				error1=True
			if not request.POST.get('repositorio'):
				l_errores.append('No seleccionó repositorio. Si no hay repositorios asociados, consulte a un administrador del sistema para agregar alguno.')
				error1=True
			l_autores = request.POST.getlist('autores1')
			formularioEsp = EspecificacionForm(request.POST)
			formularioPro = ProyectoForm(gruposu, request.POST, request.FILES)
			formularioObj = ObjetosForm(gruposu, request.POST, request.FILES)
			if not error1:
				if formularioEsp.is_valid():
					if formularioPro.is_valid():#si el válido el objeto
						esp=formularioEsp.save()#se guarda la especificaciónLOM primero
						pc = formularioObj.cleaned_data['palabras_claves']#se toman las palabras claves digitadas
						re = formularioObj.cleaned_data['repositorio']#se toma el repositorio
						f=formularioPro.save(commit=False)#se guarda un instancia temporañ
						f.espec_lom = esp # se asocia el objeto con su especificaciónLOM
						f.creador=request.user # Se asocia el objeto con el usuario que lo crea
						f.repositorio=re
						f.save() # se guarda el objeto en la base de datos.	
						if ',' in pc: #si hay comas en las palabras claves
							lpc=[x.strip() for x in pc.split(',')] # se utilizan las palabras claves como una lista de palabras separadas sin comas ni espacios
						else:
							lpc=[x.strip() for x in pc.split(' ')] # se utilizan las palabras claves como una lista de palabras separadas sin espacios
						for l in lpc:
							p,b=PalabraClave.objects.get_or_create(palabra_clave=l) # Se crea una palabra clave por cada palabra en la lista
							if not b: #Si ya existe la palabra entonces se obvia el proceso de crearla
								p.save() #se guarda la palabra clave en la bd
							f.palabras_claves.add(p) # se añade cada palabra clave al objeto
						for l in l_autores: #como el objeto llega como una lista... se debe recorrer per en realidad siempre tiene un solo objeto
							stri=l.split(',') #se divide la lista por comas que representa cada string de campos del autor
							for st in stri: # se recorre cada autor
								s=st.split(' ') # se divide los campos nombres, apellidos y rol en una lista
								aut,cr=Autor.objects.get_or_create(nombres=s[0].replace('-',' '), apellidos=s[1].replace('-',' '), rol=s[2].replace('-',' '))
								if not cr: #Si ya existe el autor entonces se obvia el proceso de crearlo
									aut.save() #se guarda el autor en la bd
								f.autores.add(aut) # se añade al campo manytomany con Autores.
						messages.add_message(request, messages.SUCCESS, 'Objeto Agregado Exitosamente')
						formularioObj=ObjetosForm(gruposu)
						formularioEsp=EspecificacionForm()
						formularioPro=ProyectoForm()
					else:
						errores=True
				else:
					errores = True					
		else:
			formularioPro=ProyectoForm(gruposu)
			formularioEsp=EspecificacionForm()
			formularioPro=ProyectoForm()

		return render_to_response('proyecto.html', {'usuario':request.user, 'proyecto':proyectoObj, 'formPro':formularioPro, 'formEsp':formularioEsp,'errores':errores,'l_errores':l_errores}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
		'''
	return render_to_response('proyecto.html', {'usuario':request.user, 'proyecto':proyectoObj}, context_instance=RequestContext(request))

