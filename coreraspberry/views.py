# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404

#Importado as tabela do banco
from coreraspberry.models import Desenvolvedor2
from coreraspberry.models import Atareuniao
from coreraspberry.models import GaleriaFotos
from coreraspberry.models import Galeria
#from coreraspberry.models import Foto



# Create your views here.

#Função para direcionar as pagina na web

#Página principal
def home(request):
    return render(request,'index.html',{})
  
#Página dos desenvolvedor    
def desevol(request):
    desenvolve = Desenvolvedor2.objects.filter()
    return render(request, 'desenvol.html', {'desenvolve':desenvolve})
    
#Página dos contato  
def cont(request):
    return render(request, 'contato.html', {})

#Página dos projetos  
def projt(request):
   return render(request, 'projetos.html', {})
   
#Página dos ferewall     
def fire(request):
    return render(request, 'firewall.html',{})
    
#Página ata de reuniao     
def ata(request):
    atas = Atareuniao.objects.filter()
    return render(request, 'ata.html',{'atas':atas})
    
#Página de Reuniões
def reuniao(request):
    return render(request, 'reuniao.html',{})
    


#Buscando Detalhes de cada pagina
def desevol_detalhes(request,id_poster):
    detalhes = get_object_or_404(Desenvolvedor2, pk=id_poster)
    return render (request, 'desenvolvedor_detalhes.html', {'detalhes':detalhes})

#galeria de fotos 
def galeriaFotos(request):
    fotos = GaleriaFotos.objects.filter()
    galerias = Galeria.objects.select_related().all()
    #galerias_foto = Foto.objects.all()
    return render(request, 'galeria_fotos.html',{'fotos':fotos, 'galerias':galerias })
    
    