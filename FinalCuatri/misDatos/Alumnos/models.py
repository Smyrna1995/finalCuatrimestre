from django.db import models
from django.utils import timezone

class Alumnos(models.Model):
    name_alumno = models.CharField(max_length=254, null=False)
    matricula_alumno = models.IntegerField(null=False)
    delete_alumno = models.BooleanField(default=False)
   
class Meta:
      db_table = 'Alumnos'