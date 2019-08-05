from django.db import models

from Profesor.models import Profesor
from Asignatura.models import Asignatura

class Profesor(models.Model):
    name_profesor = models.CharField(max_length=254, null=False)
    delete_profesor = models.BooleanField(default=False)

    class Meta:
        db_table = 'Profesor'
class proas(models.Model):
    asignatura = models.ForeignKey(Asignatura, on_delete = models.CASCADE)

    class Meta:
        db_table: 'proas'