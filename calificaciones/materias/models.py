from django.db import models
from calificaciones.bases.models import ClaseModelo

# Create your models here.
class Grado(ClaseModelo):
    nombre = models.CharField(max_length=20)

    def __str__(self):
            return '{}'.format(self.nombre)


class Materias(ClaseModelo):
    nombre = models.CharField(max_length=100,null=False)
    sigla = models.CharField(max_length=7,null=False)
    grado = models.ForeignKey(Grado,on_delete=models.CASCADE)

    def __str__(self):
            return '{},{}'.format(self.nombre,self.sigla)


class Turno(ClaseModelo):
    nombre = models.CharField(max_length=10)

    def __str__(self):
        return '{}'.format(self.nombre)

class Aulas(ClaseModelo):
    nombre = models.CharField(max_length=25, blank=True, null=True)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    def __str__(self):
        return '{},{}'.format(self.nombre ,self.turno)


class Gestion(ClaseModelo):
    gestion = models.DateField()

    @property
    def only_year(self):
        return self.gestion.strftime('%Y')

    def __str__(self):
        return '{}'.format(self.only_year)
        