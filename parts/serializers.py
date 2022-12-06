from rest_framework import serializers
from parts.models import Part, TopWord

class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = '__all__'
        
class TopWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopWord
        fields = '__all__'