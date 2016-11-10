from django.db import models

# Create your models here.
class InfoGeneral(models.Model):
    nombre = models.CharField(max_length=50,
                default="juanito")
    apellido = models.CharField(max_length=50,
         default ="")
    telefono = models.CharField(max_length=20,
        )
    fecha_nacimiento = models.DateField()
    semetre = models.IntegerField()
    carrera = models.CharField(max_length=50)
    sexo_options = ( 
        ('f' , 'femenino',),
        ('m' , 'masculino'),
        )
    sexo = models.CharField(max_length=2,
            choices= sexo_options)
    direccion = models.CharField(max_length=100)
