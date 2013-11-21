#encoding:utf-8
from django.forms import ModelForm, Textarea, TextInput
from django import forms
import datetime
from django.contrib.admin.widgets import AdminFileWidget
#from django.forms.widgets import ClearableFileInput
from gestorObjetos.models import EspecificacionLOM, Objeto, Repositorio, PalabraClave
from gestorProyectos.models import Proyecto, Programa, Facultad, Estandar_competencia
import siova.lib.Opciones as opc
"""
Formulario basado en el modelo Proyecto
"""
class ProyectoForm(ModelForm):
	class Meta:
		model=Proyecto
		#modificación de cada uno de los campos que se muestran en la plantilla para que tengan un tamaño fijo
		widgets = {
			'nombre': TextInput(attrs={'size': 40}),
			'descripcion': Textarea(attrs={'cols': 40, 'rows': 5}),
			'fase': Textarea(attrs={'cols': 40, 'rows': 3}),
			'estandar_Competencia': Textarea(attrs={'cols': 40, 'rows': 5}),
		}
	fecha = forms.DateField(initial=datetime.date.today, label="Fecha", help_text='Fecha en que el proyecto fue creado')