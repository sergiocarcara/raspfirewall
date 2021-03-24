# -*- coding: utf-8 -*-
from django.contrib import admin
from coreraspberry.models import*

# Register your models here.
class Poste_admin(admin.ModelAdmin):
    list_display = ('autor','titulo','data_criacao','data_publicacao')
    search_fields = ['autor']

class Desenvolvedor2_admin(admin.ModelAdmin):
    list_display = ('nome','data_criacao','data_publicacao')
    search_fields = ['nome']

class Atareuniao_admin(admin.ModelAdmin):
    list_display = ('data_criacao','data_publicacao')
    search_fields = ['data_criacao']

class GaleriaFotos_admi(admin.ModelAdmin):
    fieldsets = [('Imagens da Galeria',{'fields':['imagen1','imagen2','imagen3','imagen4','imagen5']}),
                 ('Titulo da Galeria',{'fields':['titulo']}),
                 ('Descrição da Galeria',{'fields':['texto']})
                ]
                
    list_display =('titulo','data_criacao','data_publicacao')
    search_fields = ['titulo']
   
#união de formulário  
#class Fotos_tabular(admin.TabularInline):
    #model = Foto
    #fk_name = 'galeria' #chave primaria da classe galeria
   # extra = 1  # campos
    
#class Galeria_admin(admin.ModelAdmin):
    #inlines = (Fotos_tabular,)
    



admin.site.register(Poster, Poste_admin)
admin.site.register(Desenvolvedor2, Desenvolvedor2_admin)
admin.site.register(Atareuniao, Atareuniao_admin)
admin.site.register(GaleriaFotos,GaleriaFotos_admi)
#admin.site.register(Foto)
#admin.site.register(Galeria,Galeria_admin)