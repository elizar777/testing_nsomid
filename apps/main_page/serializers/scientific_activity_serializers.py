from ..models.scientific_activity_models import (ScientificActivity,
                                                 ScientificActivityContent)
from rest_framework import serializers


class ScientificActContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificActivityContent
        fields = ['id','title']


class ScientificActSerializer(serializers.ModelSerializer):
    content = ScientificActContentSerializer(many=True)
    class Meta:
        model = ScientificActivity
        fields = 'id title content'.split()





