from django.db import models
# Create your models here.
class Facultad(models.Model):
	nombre = models.CharField(help_text="nombre de la facultad", verbose_name = 'facultad', max_length=50)
	class Meta:
		verbose_name_plural= "facultades"
	def __unicode__(self):
		return self.nombre

class Programa(models.Model):
	nombre = models.CharField(help_text="nombre del programa", verbose_name = 'programa', max_length=50)
	modalidad = models.TextField()
	facultad = models.ForeignKey(Facultad, help_text="nombre de la facultad", verbose_name= 'facultad', max_length=50)
	class Meta:
		verbose_name_plural= "programas"
	def __unicode__(self):
		return self.nombre

class Estandar_competencia(models.Model):
	nombre = models.CharField(help_text="estandar de competencia", verbose_name = 'estandar de  competencia', max_length=50, unique=True)
	descripcion = models.TextField()
	area = models.TextField()
	class Meta:
		verbose_name_plural= "estandares de competencias"
	def __unicode__(self):
		return self.nombre

class Proyecto(models.Model):
	nombre = models.CharField(help_text="Nombre para el proyecto", verbose_name ='proyecto', max_length=50)
	descripcion = models.TextField()
	fecha = models.TextField()
	fase = models.TextField()
	estandar_Competencia =models.TextField()
	"""Atributo que relaciona al proyecto con un :model:'gestorProyectos.Programa'."""
	programa = models.ForeignKey(Programa, help_text='programa al que pertenece el proyecto', verbose_name='programa')
	class Meta:
		verbose_name ="Proyecto"
	def __unicode__(self):
		return self.nombre
