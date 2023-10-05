from rest_framework import serializers
from .models import Event, Picture

class PictureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Picture
        fields = '__all__'      

class EventSerializer(serializers.ModelSerializer):
    
    pictures = PictureSerializer(many=True, read_only=True)
    
    class Meta:
        model = Event
        fields = '__all__'
