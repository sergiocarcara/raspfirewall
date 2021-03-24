
from django.conf.urls import url
from coreraspberry import views

urlpatterns = [
    url(r'^$',views.home),
    url(r'^desenvol/$', views.desevol),
    url(r'^contato/$', views.cont),
    url(r'^projetos/$', views.projt),
    url(r'^firewall/$', views.fire),
    url(r'^ata/$', views.ata),
    url(r'^reuniao/$', views.reuniao),
    url(r'^galeriaFotos/$',views.galeriaFotos),
    url(r'^desevol_detalhes/$', views.desevol_detalhes),
    url(r'^desevol_detalhes/(?P<id_poster>\d+)/$',views.desevol_detalhes),
]