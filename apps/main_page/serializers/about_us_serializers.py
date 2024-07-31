from ..models.about_us_models import (AboutUs,
                                      Charter,
                                      Directorate,
                                      History)
from rest_framework import serializers


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['description', 'about_ncomid']


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id','description', 'about_ncomid']

class CharterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charter
        fields = ['id','files', 'about_ncomid']


class DirectorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directorate
        fields = ['id','name', 'description', 'photo', 'about_ncomid']



