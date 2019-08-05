#Agregando librerias fram
from rest_framework import routers, serializers, viewsets

from Asignatura.Models import Asisgnatura
class AsignaturaSerializer(serializer.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = ('__all__')