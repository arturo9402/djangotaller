from django.db import models

# Create your models here.
class InfoGeneral(models.Model):
    nombre = models.CharField(max_length=50,default="Juanito")
    apellido = models.CharField(max_length=50,default="")
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    semestre =models.IntegerField()
    carrera= models.CharField(max_length=50)
    SEXO_OPTIONS = (
        ('F', 'Femenino'),
        ('M','Masculino'),
        )
    sexo= models.CharField(max_length=2,choices=SEXO_OPTIONS)
    direccion=models.CharField(max_length=100)
    estatura=models.CharField(max_length=50,default="")
