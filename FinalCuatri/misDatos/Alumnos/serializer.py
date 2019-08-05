#Agregando librerias fram
from rest_framework import routers, serializers, viewsets

from Alumnos.Models import Alumnos
class AlumnoSerializer(serializer.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ('__all__')