from django.urls import path, include
from .views import home, contato

urlpatterns = [
    path('', home, name='home'),
    path('contato/', contato, name='contato'),

]
