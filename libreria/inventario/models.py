from django.db import models

# Create your models here.
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombres_autor = models.CharField(max_length=30, null = True)
    apellidos_autor = models.CharField(max_length=30, null = True)
    correo_autor = models.CharField(max_length=30, null = True)
    nacionalidad_autor = models.CharField(max_length=30, null = True)
    pseudonimo_autor = models.CharField(max_length=30)

    def __str__(self):
        return u'%s' % (self.pseudonimo_autor)

    class Meta:
        db_table = "autor"
        verbose_name_plural = "autores"
        managed = False

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=30)

    def __str__(self):
        return u'%s' % (self.nombre_genero)

    class Meta:
        db_table = "genero"
        verbose_name_plural = "generos"
        managed = False

class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    nombre_editorial = models.CharField(max_length=30)
    correo_editorial = models.CharField(max_length=30, null=True)
    telefono_editorial = models.CharField(max_length=30, null=True)
    direccion_editorial = models.CharField(max_length=30, null=True)

    def __str__(self):
        return u'%s' % (self.nombre_editorial)

    class Meta:
        db_table = "editorial"
        verbose_name_plural = "editoriales"
        managed = False

class Publicacion(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, db_column='id_editorial')
    nombre = models.CharField(max_length=30)
    resumen = models.TextField()
    tipo_producto = models.CharField(max_length=30)
    edicion = models.CharField(max_length=30)
    fecha_publicacion = models.CharField(max_length=30)
    isbn = models.CharField(max_length=30)
    numero_serie = models.IntegerField()
    precio = models.IntegerField()
    autores = models.ManyToManyField(Autor, through='Autor_Publicacion')
    generos = models.ManyToManyField(Genero, through='Genero_Publicacion')

    def __str__(self):
        return u'%s' % (self.nombre)

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
    nombre_bodega = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    comuna = models.CharField(max_length=30)
    telefono_bodega = models.CharField(max_length=30)
    publicaciones = models.ManyToManyField(Publicacion, through='Publicacion_Bodega')
    
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
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30, null=True)
    rut = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30, null=True)
    correo = models.CharField(max_length=30, null=True)
    telefono = models.CharField(max_length=30, null=True)

    def __str__(self):
        return u'%s' % (self.nombres)

    class Meta:
        db_table = "persona"
        verbose_name_plural = "personas"
        managed = False

class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='id_persona')
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega')
    nombre_usuario = models.CharField(max_length=30)
    clave = models.CharField(max_length=30)
    tipo_usuario = models.CharField(max_length=30)
    
    def __str__(self):
        return u'%s' % (self.nombre_usuario)
    
    class Meta:
        db_table = "perfil"
        verbose_name_plural = "perfiles"
        managed = False


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=30, null=True)
    direccion_proveedor = models.CharField(max_length=30, null=True)
    comuna_proveedor = models.CharField(max_length=30, null=True)
    correo_proveedor = models.CharField(max_length=30, null=True)
    telefono_proveedor = models.CharField(max_length=30, null=True)

    def __str__(self):
        return u'%s' % (self.nombre_proveedor)

    class Meta:
        db_table = "proveedor"
        verbose_name_plural = "proveedores"
        managed = False

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, db_column='id_perfil')
    id_bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega')
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, db_column='id_proveedor')
    fecha_pedido = models.CharField(max_length=30)
    total_pedido = models.CharField(max_length=30)
    publicaciones = models.ManyToManyField(Publicacion, through='Publicacion_Pedido')

    # def __str__(self):
        # return u'%s' % (self.nombre_genero)
    
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
    metodo_pago = models.CharField(max_length=30)
    fecha_compra = models.CharField(max_length=30)
    publicaciones = models.ManyToManyField(Publicacion, through='Publicacion_Compra')
    
    # def __str__(self):
    #     return u'%s' % (self.nombre_genero)

    class Meta:
        db_table = "compra"
        verbose_name_plural = "compras"
        managed = False

class Publicacion_Compra(models.Model):
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')
    id_compra = models.ForeignKey(Compra, on_delete=models.CASCADE, db_column='id_compra')
    cantidad = models.IntegerField(null=True)
    precio = models.IntegerField(null=True)
    
    # def __str__(self):
    #     return u'%s' % (self.nombre_genero)

    class Meta:
        db_table = "publicacion_compra"
        verbose_name_plural = "publicacion_compras"
        managed = False

class Movimiento(models.Model):
    id_movimiento = models.AutoField(primary_key=True)
    id_perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, db_column='id_perfil')
    id_bodega_origen = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega_origen', related_name='bodega_origen')
    id_bodega_destino = models.ForeignKey(Bodega, on_delete=models.CASCADE, db_column='id_bodega_destino', related_name='bodega_destino')
    fecha_solicitud = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    fecha_realizado = models.CharField(max_length=30)
    publicaciones = models.ManyToManyField(Publicacion, through='Publicacion_Movimiento')

    # def __str__(self):
    #     return u'%s' % (self.nombre_genero)
    
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