from rest_framework import serializers
from .models import Event, Gallery, Photo

class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = '__all__'
        
class GallerySerializer(serializers.ModelSerializer):
    
    photo = PhotoSerializer(many=True)
    
    class Meta:
        model = Gallery
        fields = '__all__'
        
class GalleryHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
    
    photo = PhotoSerializer(many=True)
    
    class Meta:
        model = Gallery
        fields = ('url', 'id')


class EventSerializer(serializers.ModelSerializer):
    
    gallery = GalleryHyperLinkedSerializer(many=True)
    
    class Meta:
        model = Event
        fields = '__all__'
