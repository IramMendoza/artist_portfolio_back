from rest_framework import serializers
from .models import Artist, Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    
    contact = ContactSerializer(required=False)
    
    class Meta:
        model = Artist
        fields = '__all__'