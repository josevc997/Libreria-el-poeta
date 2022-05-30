from django.db import models

# Create your models here.
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