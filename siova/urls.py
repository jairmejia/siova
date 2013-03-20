from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siova.views.home', name='home'),
    # url(r'^siova/', include('siova.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^ingresar/$','gestorObjetos.views.ingresar'),
    url(r'^cerrar/$', 'gestorObjetos.views.cerrar'),
    url(r'^privado/$','gestorObjetos.views.privado'),
    url(r'^objeto/(?P<id_objeto>\d)$','gestorObjetos.views.objeto'),
)
