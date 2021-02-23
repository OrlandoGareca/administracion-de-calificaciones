from django.db import models
from calificaciones.users.models import User

class ClaseModelo(models.Model):
    estado= models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User,on_delete=models.CASCADE)
    um = models.IntegerField(blank=True,null=True)

    class Meta:
        abstract=True
