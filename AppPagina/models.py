from django.db import models



# Create your models here.
class estudiante(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    foto = models.ImageField(upload_to='fotos_estudiantes/', verbose_name="Foto", null=True)
    clase = models.TextField(max_length=100, verbose_name="Clase", null=True) 

    def __str__(self):
        return self.nombre + " " + self.apellido
    
    def delete(self, ususing=None, keep_parents=False):
        if self.foto:
            self.foto.delete(self)
        super().delete() 