from django.db import models

# Create your models here.
    
class Paciente(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    paterno = models.CharField(max_length=200, null=True, blank=True)
    materno = models.CharField(max_length=200, null=True, blank=True)   
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return '{}'.format(self.nombre)