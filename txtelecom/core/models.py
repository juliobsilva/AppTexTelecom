from django.db import models

class PlanoBasico(models.Model):

    nome = models.CharField('Nome', max_length=30, blank=True, null=True)
    preco = models.IntegerField()
    texto1 = models.TextField('Texto1', blank=True)
    texto2 = models.TextField('Texto2',blank=True)
    texto3 = models.TextField('Texto3',blank=True)
    texto4 = models.TextField('Texto4',blank=True)
    texto5 = models.TextField('Texto5',blank=True)
    texto6 = models.TextField('Texto6',blank=True)


    def __str__(self):

        return self.nome


class PlanoIntermediario(models.Model):

    nome = models.CharField('Nome', max_length=30, blank=True, null=True)
    preco = models.IntegerField()
    texto1 = models.TextField('Texto1',blank=True)
    texto2 = models.TextField('Texto2',blank=True)
    texto3 = models.TextField('Texto3',blank=True)
    texto4 = models.TextField('Texto4',blank=True)
    texto5 = models.TextField('Texto5',blank=True)
    texto6 = models.TextField('Texto6',blank=True)


    def __str__(self):

        return self.nome


class PlanoAvancado(models.Model):

    nome = models.CharField('Nome', max_length=30, blank=True, null=True)
    preco = models.IntegerField()
    texto1 = models.TextField('Texto1',blank=True)
    texto2 = models.TextField('Texto2',blank=True)
    texto3 = models.TextField('Texto3',blank=True)
    texto4 = models.TextField('Texto4',blank=True)
    texto5 = models.TextField('Texto5',blank=True)
    texto6 = models.TextField('Texto6',blank=True)

    def __str__(self):

        return self.nome

class TitulosdaPagina(models.Model):

    primeirotitulo = models.CharField('Primeiro Título', max_length=150, blank=True, null=True)
    texto1 = models.TextField('Primeira secao', blank=True)
    segundotitulo = models.CharField('Segundo Título', max_length=150, blank=True, null=True)
    texto2 = models.TextField('Segunda secao', blank=True)
    terceirotitulo = models.CharField('Terceiro Título', max_length=150, blank=True, null=True)
    texto3 = models.TextField('Terceira secao', blank=True)
    quartotitulo = models.CharField('Quarto Título', max_length=150, blank=True, null=True)
    texto4 = models.TextField('Quarta secao', blank=True)

    def __str__(self):

        return self.primeirotitulo
