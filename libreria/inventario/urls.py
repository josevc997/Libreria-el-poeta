from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('autores', views.autores, name='autores'),
    path('autores/registro', views.registroAutores, name='registroAutores'),
    path('productos', views.productos, name='productos'),
    path('productos/registro', views.registroProductos, name='registroProductos'),
    path('bodegas', views.bodegas, name='bodegas'),
    path('bodegas/<int:bodega_id>', views.detalleBodegas, name='detalleBodegas'),
    path('bodegas/registro', views.registroBodegas, name='registroBodegas'),
    path('editoriales', views.editoriales, name='editoriales'),
    path('editoriales/registro', views.registroEditoriales, name='registroEditoriales'),
]
