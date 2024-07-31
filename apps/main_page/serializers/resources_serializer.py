from rest_framework import serializers
from apps.main_page.models.resources_model import Journal, Link, Report

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id','title', 'url']
        
class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id','title', 'url']

        
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id','title', 'url']
