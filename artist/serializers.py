from rest_framework import serializers
from .models import Artist, Contact, ArtistPhoto

class ArtistPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistPhoto
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        

class ArtistSerializer(serializers.ModelSerializer):
    
    contact = ContactSerializer(required=False)
    
    photos = ArtistPhotoSerializer(many=True, required=False)
    
    class Meta:
        model = Artist
        fields = '__all__'
        
##########-------------------------
