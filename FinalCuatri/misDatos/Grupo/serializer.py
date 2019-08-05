#Agregando librerias fram
from rest_framework import routers, serializers, viewsets

from Grupo.Models import Grupo

class GrupoSerializer(serializer.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ('__all__')