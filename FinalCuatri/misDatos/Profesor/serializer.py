#Agregando librerias fram
from rest_framework import routers, serializers, viewsets

from Profesor.Models import Profesor 

class ProfesorSerializer(serializer.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ('__all__')