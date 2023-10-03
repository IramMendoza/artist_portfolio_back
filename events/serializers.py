from rest_framework import serializers
from .models import Event, Gallery, Photo

class PhotoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Photo
        fields = '__all__'
        
class GallerySerializer(serializers.ModelSerializer):
    
    photo = PhotoSerializer()
    
    class Meta:
        model = Gallery
        fields = '__all__'
        
class GalleryHyperLinkedSerializer(serializers.HyperlinkedModelSerializer):
        
    class Meta:
        model = Gallery
        fields = ('url', 'pk', 'photo')
        extra_kwargs = {
            'Photo': { 'view_name': 'gallery-detail', 'lookup_field': 'pk' }
        }
        


class EventSerializer(serializers.ModelSerializer):
    
    gallery = GallerySerializer()
    
    class Meta:
        model = Event
        fields = '__all__'
