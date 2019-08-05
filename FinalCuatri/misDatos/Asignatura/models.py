from django.db import models
from Profesor.models import Profesor

class Asignatura(models.Model):
    name_asignatura = models.CharField(max_length=254, null=False)
    delete_asignatura = models.BooleanField(default=False)


    class Meta:
        db_table = 'Asignatura'

    class ProfesorAsignatura(models.Model):
        asignatura = models.ForeignKey(Asignatura, NULL = False, on_delete = models.CASCADE)
        profesor = models.ForeignKey(Profesor, null = False, on_delete = models.CASCADE)

        class Mate:
            db_table: 'asipro'