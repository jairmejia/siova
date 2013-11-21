from gestorProyectos.models import Proyecto, Facultad, Programa, Grado, Factor_competencias, Enunciado, Indicador, Parametro, Validacion
from django.contrib import admin

admin.site.register(Proyecto),
admin.site.register(Facultad),
admin.site.register(Programa),
admin.site.register(Grado),
admin.site.register(Factor_competencias),
admin.site.register(Enunciado),
admin.site.register(Indicador),
admin.site.register(Parametro),
admin.site.register(Validacion)