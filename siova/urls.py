from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^proyectos','gestorProyectos.views.lista_proyectos'),
    url(r'^facultades','gestorProyectos.views.lista_facultades'),
    url(r'^programas','gestorProyectos.views.lista_programas'),
    url(r'^estandares','gestorProyectos.views.lista_estandares'),
    #url(r'^siova/', include('siova.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','gestorObjetos.views.principal'),
    url(r'^ingresar/$','gestorObjetos.views.ingresar'),
    url(r'^cerrar/$', 'gestorObjetos.views.cerrar'),
    url(r'^privado/$','gestorObjetos.views.privado'),
    url(r'^objeto/(?P<id_objeto>\d+)$','gestorObjetos.views.objeto'),
    url(r'^editObjeto/(?P<id_objeto>\d+)$','gestorObjetos.views.editObjeto'),
    url(r'^buscar/$','gestorObjetos.views.buscar', name='buscar'),
    url(r'^busqueda/$','gestorObjetos.views.busqueda', name='busqueda'),
    url(r'^crearAutor/$','gestorObjetos.views.crearAutor', name='crearAutor'),
    url(r'^categoria/(?P<id_categoria>\d+)$','gestorObjetos.views.categoria'),
    url(r'^docente/$','gestorObjetos.views.docObjeto'),
    url(r'^descarga/(?P<id>.+)$', 'gestorObjetos.views.download'),
    url(r'^editObjeto/objetos/(?P<id>.+)$', 'gestorObjetos.views.downloadEdit'),
    url(r'^admin/gestorObjetos/objeto/(?P<id>.+)/objetos/.+$', 'gestorObjetos.views.download'),
    url(r'^admin/logout/$', 'gestorObjetos.views.redirige'),
    url(r'^proyecto/$','gestorProyectos.views.Proyecto'),
    url(r'^revisor/$','gestorProyectos.views.Proyecto'),
)