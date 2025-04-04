from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from .models import ActaEntrega, ActaObjetivo, ActaObservacion, ActaRecibidoPor, ActaArchivo


class ActaObjetivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActaObjetivo
        fields = '__all__'

class ActaObservacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActaObservacion
        fields = '__all__'

class ActaRecibidoPorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActaRecibidoPor
        fields = '__all__'

class ActaArchivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActaArchivo
        fields = '__all__'

class ActaEntregaSerializer(serializers.ModelSerializer):
    objetivos = ActaObjetivoSerializer(many=True, required=False)
    observaciones = ActaObservacionSerializer(many=True, required=False)
    recibidos_por = ActaRecibidoPorSerializer(many=True, required=False)
    archivos = ActaArchivoSerializer(many=True, required=False)

    class Meta:
        model = ActaEntrega
        fields = '__all__'