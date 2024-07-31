from rest_framework import serializers

from apps.main_page.models.blocks_and_departments_model import Block, Department

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ['id','title', 'photo_url']
        
                
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id','name', 'description', 'photo_url', 'block', 'address']
        
        
class BlockDetailSerializer(serializers.ModelSerializer):
    departments = serializers.SerializerMethodField()
    
    class Meta:
        model = Block
        fields = ['id','title', 'departments']
        
    def get_departments(self, obj):
        departments = obj.departments.all()
        return DepartmentSerializer(departments, many=True).data
