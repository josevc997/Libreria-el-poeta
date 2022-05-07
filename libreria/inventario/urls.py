from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('autores', views.autores, name='autores'),
    path('autores/registro', views.registroAutores, name='registroAutores'),
]
