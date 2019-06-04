from django.shortcuts import render, redirect
from .models import PlanoBasico, PlanoIntermediario, PlanoAvancado, TitulosdaPagina

def home(request):
    template_name = 'core/home.html'
    planobasico = PlanoBasico.objects.all()
    planointermediario = PlanoIntermediario.objects.all()
    planoavancado = PlanoAvancado.objects.all()
    titulosdapagina = TitulosdaPagina.objects.all()
    context = {
    'planobasico': planobasico,
    'planointermediario': planointermediario,
    'planoavancado': planoavancado,
    'titulosdapagina': titulosdapagina,
    }

    return render(request, template_name, context)


def contato(request):
    template_name = 'core/contato_email.html'
    return render(request, template_name)
