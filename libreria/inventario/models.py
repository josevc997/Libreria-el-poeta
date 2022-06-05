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
        managed = False

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=30)

    def __str__(self):
        return u'%s' % (self.nombre_genero)

    class Meta:
        db_table = "genero"
        managed = False

class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True)
    nombre_editorial = models.CharField(max_length=30)
    correo_editorial = models.CharField(max_length=30, null=True)
    telefono_editorial = models.CharField(max_length=30, null=True)

    def __str__(self):
        return u'%s' % (self.nombre_editorial)

    class Meta:
        db_table = "editorial"
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

    def __str__(self):
        return u'%s' % (self.nombre)

    class Meta:
        db_table = "publicacion"
        managed = False

class Autor_Publicacion(models.Model):
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, db_column='id_autor')
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, db_column='id_publicacion')

    # def __str__(self):
    #     return u'%s' % (self.id_publicacion.nombre + " escrito por" + self.id_autor.pseudonimo_autor)

    class Meta:
        db_table = "autor_publicacion"
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
        managed = False