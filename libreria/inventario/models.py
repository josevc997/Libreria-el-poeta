from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime

# Create your models here.
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombres_autor = models.CharField(max_length=150, null = True)
    apellidos_autor = models.CharField(max_length=150, null = True)
    correo_autor = models.CharField(max_length=150, null = True)
    nacionalidad_autor = models.CharField(max_length=150, null = True)
    pseudonimo_autor = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return u'%s' % (self.pseudonimo_autor)

    class Meta:
        db_table = "autor"
        verbose_name_plural = "autores"
        managed = False

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return u'%s' % (self.nombre_genero)

    class Meta:
        db_table = "genero"
        verbose_name_plural = "generos"
        managed = False

class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    nombre_editorial = models.CharField(max_length=150)
    correo_editorial = models.CharField(max_length=150, null=True)
    telefono_editorial = models.CharField(max_length=150, null=True)
    direccion_editorial = models.CharField(max_length=150, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return u'%s' % (self.nombre_editorial)

    class Meta:
        db_table = "editorial"
        verbose_name_plural = "editoriales"
        managed = False

class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, db_column='id_editorial')
    nombre = models.CharField(max_length=150)
    resumen = models.TextField()
    tipo_producto = models.CharField(max_length=150)
    edicion = models.CharField(max_length=150)
    fecha_publicacion = models.CharField(max_length=150)
    isbn = models.CharField(max_length=150)
    numero_serie = models.IntegerField()
    precio = models.IntegerField()
    autores = models.ManyToManyField(Autor, through='Autor_Publicacion')
    generos = models.ManyToManyField(Genero, through='Genero_Publicacion')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return u'%s' % (self.nombre)

    def fecha_publicacion_ddmmaa(self):
        fecha = datetime.datetime.strptime(self.fecha_publicacion, '%Y-%m-%d %H:%M:%S.%f')
        fecha_formateada = fecha.strftime("%m/%d/%Y")
        return fecha_formateada

    def fecha_publicacion_normal(self):
        fecha = datetime.datetime.strptime(self.fecha_publicacion, '%Y-%m-%d %H:%M:%S.%f')
        fecha_formateada = fecha.strftime("%m/%d/%Y")
        return fecha

    class Meta:
        db_table = "publicacion"
        verbose_name_plural = "publicaciones"
        managed = False

class Genero_Publicacion(models.Model):
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='id_genero')
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')

    # def __str__(self):
    #     return u'%s' % (self.id_publicacion.nombre + " escrito por" + self.id_genero.pseudonimo_genero)

    class Meta:
        db_table = "genero_publicacion"
        verbose_name_plural = "genero_publicaciones"
        managed = False

class Autor_Publicacion(models.Model):
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, db_column='id_autor')
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')

    # def __str__(self):
    #     return u'%s' % (self.id_publicacion.nombre + " escrito por" + self.id_autor.pseudonimo_autor)

    class Meta:
        db_table = "autor_publicacion"
        verbose_name_plural = "autor_publicaciones"
        managed = False

class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    nombre_bodega = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    comuna = models.CharField(max_length=150)
    telefono_bodega = models.CharField(max_length=150)
    publicaciones = models.ManyToManyField(Publicacion, through='Publicacion_Bodega')
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return u'%s' % (self.nombre_bodega)

    class Meta:
        db_table = "bodega"
        verbose_name_plural = "bodegas"
        managed = False

class Publicacion_Bodega(models.Model):
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega')
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')
    cantidad = models.IntegerField(null=True)
    
    # def __str__(self):
    #     return u'%s' % (self.id_publicacion.nombre + " escrito por" + self.id_autor.pseudonimo_autor)

    class Meta:
        db_table = "publicacion_bodega"
        verbose_name_plural = "publicacion_bodegas"
        managed = False

class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150, null=True)
    rut = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150, null=True)
    correo = models.CharField(max_length=150, null=True)
    telefono = models.CharField(max_length=150, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return u'%s' % (self.nombres)

    class Meta:
        db_table = "persona"
        verbose_name_plural = "personas"
        managed = False

class Perfil(AbstractUser):
    id = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='id_persona')
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega')
    username = models.CharField(max_length=150, unique=True)
    tipo_usuario = models.CharField(max_length=150)
    
    def __str__(self):
        return u'%s' % (self.username)

    USERNAME_FIELD = 'username'
    
    class Meta:
        db_table = "perfil"
        verbose_name_plural = "perfiles"
        managed = False


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=150, null=True)
    direccion_proveedor = models.CharField(max_length=150, null=True)
    comuna_proveedor = models.CharField(max_length=150, null=True)
    correo_proveedor = models.CharField(max_length=150, null=True)
    telefono_proveedor = models.CharField(max_length=150, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return u'%s' % (self.nombre_proveedor)

    class Meta:
        db_table = "proveedor"
        verbose_name_plural = "proveedores"
        managed = False

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id = models.ForeignKey(Perfil, on_delete=models.CASCADE, db_column='id')
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega')
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    fecha_pedido = models.CharField(max_length=150)
    total_pedido = models.CharField(max_length=150)
    publicaciones = models.ManyToManyField(Publicacion, through='Publicacion_Pedido')
    estado = models.CharField(max_length=150)

    def fecha_pedido_normal(self):
        fecha = datetime.datetime.strptime(self.fecha_pedido, '%Y-%m-%d %H:%M:%S.%f')
        return fecha

    def fecha_pedido_ddmmaa(self):
        fecha = datetime.datetime.strptime(self.fecha_pedido, '%Y-%m-%d %H:%M:%S.%f')
        fecha_formateada = fecha.strftime("%m/%d/%Y")
        return fecha_formateada
    
    class Meta:
        db_table = "pedido"
        verbose_name_plural = "pedidos"
        managed = False

class Publicacion_Pedido(models.Model):
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, db_column='id_pedido')
    cantidad = models.IntegerField(null=True)
    precio_proveedor = models.IntegerField(null=True)

    # def __str__(self):
    #     return u'%s' % (self.nombre_genero)
    
    class Meta:
        db_table = "publicacion_pedido"
        verbose_name_plural = "publicacion_pedidos"
        managed = False

class Compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega')
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='id_persona')
    total = models.IntegerField(null=True)
    metodo_pago = models.CharField(max_length=150)
    fecha_compra = models.CharField(max_length=150)
    publicaciones = models.ManyToManyField(Publicacion, through='Publicacion_Compra')
    estado = models.CharField(max_length=150)
    
    def fecha_compra_ddmmaa(self):
        fecha = datetime.datetime.strptime(self.fecha_compra, '%Y-%m-%d %H:%M:%S.%f')
        fecha_formateada = fecha.strftime("%m/%d/%Y")
        return fecha_formateada
    
    def fecha_compra_normal(self):
        fecha = datetime.datetime.strptime(self.fecha_compra, '%Y-%m-%d %H:%M:%S.%f')
        return fecha

    class Meta:
        db_table = "compra"
        verbose_name_plural = "compras"
        managed = False

class Publicacion_Compra(models.Model):
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE, db_column='id_compra')
    cantidad = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    
    def calculo_total(self):
        return (self.cantidad * self.precio) 

    class Meta:
        db_table = "publicacion_compra"
        verbose_name_plural = "publicacion_compras"
        managed = False

class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    id = models.ForeignKey(Perfil, on_delete=models.CASCADE, db_column='id')
    id_bodega_origen = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega_origen', related_name='bodega_origen')
    id_bodega_destino = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega_destino', related_name='bodega_destino')
    fecha_solicitud = models.CharField(max_length=150)
    estado = models.CharField(max_length=150)
    fecha_realizado = models.CharField(max_length=150)
    publicaciones = models.ManyToManyField(Publicacion, through='Publicacion_Movimiento')

    def fecha_solicitud_normal(self):
        fecha = datetime.datetime.strptime(self.fecha_solicitud, '%Y-%m-%d %H:%M:%S.%f')
        return fecha

    def fecha_solicitud_ddmmaa(self):
        fecha = datetime.datetime.strptime(self.fecha_solicitud, '%Y-%m-%d %H:%M:%S.%f')
        fecha_formateada = fecha.strftime("%m/%d/%Y")
        return fecha_formateada

    def fecha_realizado_normal(self):
        fecha = datetime.datetime.strptime(self.fecha_realizado, '%Y-%m-%d %H:%M:%S.%f')
        return fecha
        
    def fecha_realizado_ddmmaa(self):
        fecha = datetime.datetime.strptime(self.fecha_realizado, '%Y-%m-%d %H:%M:%S.%f')
        fecha_formateada = fecha.strftime("%m/%d/%Y")
        return fecha_formateada
    
    class Meta:
        db_table = "movimiento"
        verbose_name_plural = "movimientos"
        managed = False

class Publicacion_Movimiento(models.Model):
    id_movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE, db_column='id_movimiento')
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')
    cantidad = models.IntegerField(null=True)

    # def __str__(self):
    #     return u'%s' % (self.nombre_genero)
    
    class Meta:
        db_table = "publicacion_movimiento"
        verbose_name_plural = "publicacion_movimientos"
        managed = False