# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage
from ckeditor.fields import RichTextField

fs = FileSystemStorage(location='media/')#local de armazenamento de imagens 
fsg = FileSystemStorage(location='media/galeria/')#local de armazenamento de imagens 

# Create your models here.

#tabela de postagem 
class Poster (models.Model):
    autor  = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    fontr  = models.CharField('Fonte',max_length=200)
    imagem = models.ImageField(storage=fs)
    texto  = RichTextField()
    data_criacao = models.DateTimeField('Data da criação',default=timezone.now)
    data_publicacao = models.DateTimeField('Data da publicação', blank=True,null=True)
    
    def publicacao(self):
        
        self.data_publcacao=timezone
        self.save()

    def __str__(self):
        return self.titulo

    class Meta:
        ordering= ('-data_publicacao',)


#Tabela Desenvolvedor
class Desenvolvedor2(models.Model):
    nome             = models.CharField('Nome Usado', max_length=200)
    segundonome      = models.CharField('Nome Copleto',max_length=200)
    tipo             = models.CharField('Tipo', max_length=200)
    idade            = models.IntegerField('Idade')
    imagem           = models.ImageField(storage=fs)
    texto            = RichTextField('Resulmo do Perfil')
    textocompleto    = RichTextField('Perfil Completo')
    data_criacao     = models.DateTimeField('Data da criação',default=timezone.now)
    data_publicacao  = models.DateTimeField('Data da publicação', blank=True,null=True)
    
    def publicacao(self):
        
        self.data_publcacao=timezone
        self.save()

    def __str__(self):
        return self.nome

    class Meta:
        ordering= ('-data_publicacao',)
        verbose_name = 'Desenvolvedor'
        verbose_name = 'Desenvolvedore'


#Tabela ata de reuniaão
class Atareuniao(models.Model):
    texto            = RichTextField('Descrição da Ata')
    data_criacao     = models.DateTimeField('Data da criação',default=timezone.now)
    data_publicacao  = models.DateTimeField('Data da publicação', blank=True,null=True)
    
    def publicacao(self):
        
        self.data_publcacao=timezone
        self.save()

    def __str__(self):
        return self.texto

    class Meta:
        ordering= ('-data_publicacao',)
        verbose_name = 'Ata de Reunião'
        verbose_name = 'Ata de Reuniõe'



class Galeria(models.Model):
    nome  = models.CharField('Nome da Galeria',max_length=200)
    texto = models.CharField('Descrição da Galeria', max_length=300)

    def __str__(self):
        return self.nome
        
    class Meta:
        ordering= ('nome',)
        verbose_name = 'Galeria Foto'
        verbose_name_plural= 'Galeria de Foto'    
        
#
class Foto(models.Model):
    galeria = models.ForeignKey(Galeria, related_name='fotos_da_galeria_model')
    titulo = models.CharField('Titulo da Foto',max_length=200)
    imagen = models.ImageField('Imagem', storage=fs)
    data_criacao     = models.DateTimeField('Data da criação',auto_now_add=True)
    data_publicacao  = models.DateTimeField('Data da publicação', blank=True,null=True)
    
    def __str__(self):
        return self.titulo

    class Meta:
        ordering= ('-data_publicacao',)
        verbose_name = 'Galeria Foto'
        verbose_name_plural= 'Galeria de Foto'
        


#tabela da galeria de fotos 
class GaleriaFotos(models.Model):
    titulo = models.CharField(max_length=200)
    imagen1 = models.ImageField('Imagem - 1', storage=fs)
    imagen2 = models.ImageField('Imagem - 2', storage=fs)
    imagen3 = models.ImageField('Imagem - 3', storage=fs)
    imagen4 = models.ImageField('Imagem - 4', storage=fs)
    imagen5 = models.ImageField('Imagem - 5', storage=fs)
    texto = models.CharField('Descrição', max_length=300)
    data_criacao     = models.DateTimeField('Data da criação',default=timezone.now)
    data_publicacao  = models.DateTimeField('Data da publicação', blank=True,null=True)
    
        
    def __str__ (self):
        return self.titulo
    
    class Meta:
        verbose_name = 'Galeria'
        verbose_name = 'Galeria'