from django.contrib import admin
from .models import PlanoBasico, PlanoIntermediario, PlanoAvancado, TitulosdaPagina

admin.site.register(PlanoBasico)
admin.site.register(PlanoIntermediario)
admin.site.register(PlanoAvancado)
admin.site.register(TitulosdaPagina)
