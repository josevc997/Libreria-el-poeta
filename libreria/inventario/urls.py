from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('autores', views.autores, name='autores'),
    path('autores/registro', views.registroAutores, name='registroAutores'),
    path('autores/detalle/<int:id_autor>', views.detalleAutor, name='detalleAutor'),
    path('autores/editar/<int:id_autor>', views.editarAutor, name='editarAutor'),
    path('productos', views.productos, name='productos'),
    path('productos/registro', views.registroProductos, name='registroProductos'),
    path('productos/detalle/<int:id_publicacion>', views.detallePublicacion, name='detallePublicacion'),
    path('productos/editar/<int:id_publicacion>', views.editarPublicacion, name='editarPublicacion'),
    path('editoriales', views.editoriales, name='editoriales'),
    path('editoriales/registro', views.registroEditoriales, name='registroEditoriales'),
    path('personas/registro', views.registroPersonas, name='registroPersonas'),
    path('personas/lista', views.listaPersonas, name='listaPersonas'),
    path('personas/detalle/<int:id_persona>', views.detallePersonas, name='detallePersonas'),
    path('seed', views.seed, name='seed'),
    path('personas/editar/<int:id_persona>', views.editarPersonas, name='editarPersonas'),
    path('login', views.loginPerfil, name='login'),
    path('logout', views.logoutPerfil, name='logout'),
    path('perfiles', views.perfiles, name='perfiles'),
    path('perfiles/registro', views.registroPerfil, name='registroPerfil'),
    path('perfiles/preregistro', views.preregistroPerfil, name='preregistroPerfil'),
    path('perfiles/<int:perfil_id>', views.detallePerfiles, name='detallePerfiles'),
    path('perfiles/editar/<int:id_perfil>', views.editarPerfil, name='editarPerfil'),
    path('perfiles/cambiarEstado/<int:id_perfil>', views.cambiarEstadoPerfil, name='cambiarEstadoPerfil'),
    # URLS Bruno Pozo
    path('compras/registro',views.registroCompras,name='registroCompras'),
    path('compras',views.listaCompras, name='compras'),
    path('bodegas', views.bodegas, name='bodegas'),
    path('bodegas/<int:bodega_id>', views.detalleBodegas, name='detalleBodegas'),
    path('bodegas/registro', views.registroBodegas, name='registroBodegas'),
    # path('compras/detalles',views.detalleCompras,)
    # URLS Pablo Cea
    path('proveedores/registro', views.registroProveedores, name='registroProveedores'),
    path('proveedores', views.proveedores, name='proveedores'),
]
