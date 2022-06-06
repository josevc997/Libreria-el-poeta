from django.contrib import admin
from .models import Bodega, Compra, Editorial, Genero, Genero_Publicacion, Movimiento, Pedido, Perfil, Persona, Proveedor, Publicacion, Autor, Autor_Publicacion, Publicacion_Bodega, Publicacion_Compra, Publicacion_Movimiento, Publicacion_Pedido

class Autor_Publicacion_Inline(admin.StackedInline):
    model = Autor_Publicacion
    extra = 1

class Genero_Publicacion_Inline(admin.StackedInline):
    model = Genero_Publicacion
    extra = 1

class Publicacion_Bodega_Inline(admin.StackedInline):
    model = Publicacion_Bodega
    extra = 1

class Publicacion_Compra_Inline(admin.StackedInline):
    model = Publicacion_Compra
    extra = 1

class Publicacion_Movimiento_Inline(admin.StackedInline):
    model = Publicacion_Movimiento
    extra = 1

class Publicacion_Pedido_Inline(admin.StackedInline):
    model = Publicacion_Pedido
    extra = 1

class Pedido_Admin(admin.ModelAdmin):
    inlines = (Publicacion_Pedido_Inline,)

class Movimiento_Admin(admin.ModelAdmin):
    inlines = (Publicacion_Movimiento_Inline,)

class Compra_Admin(admin.ModelAdmin):
    inlines = (Publicacion_Compra_Inline,)

class Bodega_Admin(admin.ModelAdmin):
    inlines = (Publicacion_Bodega_Inline,)

class Genero_Admin(admin.ModelAdmin):
    inlines = (Genero_Publicacion_Inline,)

class Autor_Admin(admin.ModelAdmin):
    inlines = (Autor_Publicacion_Inline,)

class Publicacion_Admin(admin.ModelAdmin):
    inlines = (Autor_Publicacion_Inline, Genero_Publicacion_Inline, Publicacion_Bodega_Inline, Publicacion_Compra_Inline, Publicacion_Movimiento_Inline, Publicacion_Pedido_Inline, )

# Register your models here.
admin.site.register(Autor, Autor_Admin)
admin.site.register(Genero, Genero_Admin)
admin.site.register(Editorial)
admin.site.register(Publicacion, Publicacion_Admin)
admin.site.register(Genero_Publicacion)
admin.site.register(Autor_Publicacion)
admin.site.register(Bodega, Bodega_Admin)
admin.site.register(Publicacion_Bodega)
admin.site.register(Persona)
admin.site.register(Perfil)
admin.site.register(Proveedor)
admin.site.register(Pedido, Pedido_Admin)
admin.site.register(Publicacion_Pedido)
admin.site.register(Compra, Compra_Admin)
admin.site.register(Publicacion_Compra)
admin.site.register(Movimiento, Movimiento_Admin)
admin.site.register(Publicacion_Movimiento)