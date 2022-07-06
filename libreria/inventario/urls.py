from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('autores', views.autores, name='autores'),
    path('autores/registro', views.registroAutores, name='registroAutores'),
    path('autores/detalle/<int:id_autor>', views.detalleAutor, name='detalleAutor'),
    path('autores/editar/<int:id_autor>', views.editarAutor, name='editarAutor'),
    path('generos', views.generos, name='generos'),
    path('generos/registro', views.registroGeneros, name='registroGeneros'),
    path('generos/detalle/<int:id_genero>', views.detalleGenero, name='detalleGenero'),
    path('generos/editar/<int:id_genero>', views.editarGenero, name='editarGenero'),
    path('movimientos', views.movimientos, name='movimientos'),
    path('movimientos/registro', views.registroMovimientos, name='registroMovimientos'),
    path('movimientos/detalle/<int:id_movimiento>', views.detalleMovimiento, name='detalleMovimiento'),
    path('movimientos/editar/<int:id_movimiento>', views.editarMovimiento, name='editarMovimiento'),
    path('movimientos/editar/estado/<int:id_movimiento>', views.editarEstadoMovimiento, name='editarEstadoMovimiento'),
    path('movimientos/agregar/<int:id_movimiento>', views.agregarPublicacionMovimiento, name='agregarPublicacionMovimiento'),
    path('productos', views.productos, name='productos'),
    path('productos/registro', views.registroProductos, name='registroProductos'),
    path('productos/detalle/<int:id_publicacion>', views.detallePublicacion, name='detallePublicacion'),
    path('productos/editar/<int:id_publicacion>', views.editarPublicacion, name='editarPublicacion'),
    path('editoriales', views.editoriales, name='editoriales'),
    path('editoriales/registro', views.registroEditoriales, name='registroEditoriales'),
    path('personas/registro', views.registroPersonas, name='registroPersonas'),
    path('personas/detalle/<int:id_editorial>', views.detalleEditorial, name='detalleEditorial'),
    path('personas/editar/<int:id_editorial>', views.editarEditorial, name='editarEditorial'),
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
    path('bodegas/detalle/<int:id_bodega>', views.detalleBodegas, name='detalleBodegas'),
    path('bodegas/registro', views.registroBodegas, name='registroBodegas'),
    path('bodegas/editar/<int:id_bodega>',views.editarBodegas, name='editarBodegas'),
    path('compras/detalle/<int:id_compra>',views.detalleCompras,name='detalleCompras'),
    path('compras/editar/<int:id_compra>',views.editarCompras,name='editarCompras'),
    # path('compras/detalles',views.detalleCompras,)
    # URLS Pablo Cea
    path('proveedores/registro', views.registroProveedores, name='registroProveedores'),
    path('proveedores', views.proveedores, name='proveedores'),
    path('proveedores/detalle/<int:id_proveedor>', views.detalleProveedores, name='detalleProveedor'),
    path('pedidos/detalle', views.pedidos, name='pedidos'),
    path('pedidos/registro', views.registroPedidos, name='registroPedidos'),
]
