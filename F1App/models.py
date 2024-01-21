from django.db import models

# Create your models here.
from django.db import models

class Piloto(models.Model):

    def __str__(self):

        return f"{self.nombre} ---{self.equipo}"
    
    nombre = models.CharField(max_length=100)
    equipo = models.CharField(max_length=50)

class Carrera(models.Model):

    
    def __str__(self):

        return f"{self.piloto} --- {self.posicion} --- {self.vuelta_rapida}"
    
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)
    posicion = models.PositiveIntegerField()
    vuelta_rapida = models.BooleanField(default=False)

class Puntos(models.Model):

    def __str__(self):

        return f"{self.carrera} ---{self.puntos}"
    
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    puntos = models.PositiveIntegerField()