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
    path('personas/registro', views.registroPersonas, name='registroPersonas'),
    path('personas/lista', views.listaPersonas, name='listaPersonas'),
    path('personas/detalle/<int:id_persona>', views.detallePersonas, name='detallePersonas'),
    path('proveedores/registro', views.registroProveedores, name='registroProveedores'),
    path('seed', views.seed, name='seed'),
    path('personas/editar/<int:id_persona>', views.editarPersonas, name='editarPersonas'),
    path('proveedores', views.proveedores, name='proveedores')
]
