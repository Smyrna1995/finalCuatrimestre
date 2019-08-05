from django.db import models
from Asignatura.models import Asignatura
from django.utils import timezone

class Grupo(models.Model):
    name_grupo = models.CharField(max_length=254, null=False)
    delete_grupo = models.BooleanField(default=False)

    asignatura = models.ManyToManyField(Asignatura, related_name = "grupo", through = "gruas")
    alumnos = models.ManyToManyField(Alumnos, on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'Grupo'

class gruas (models.Model):
    grupo = models.ForeignKey(Grupo, null = False, on_delete = models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete = models.CASCADE)
    class Meta:
        db_table: 'gruas'


    