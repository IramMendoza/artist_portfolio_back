from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    type_artist = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='artist_image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    contact = models.OneToOneField('Contact', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20)
    phone_2 = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return self.email
    
class ArtistPhoto(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name='photos')
    caption = models.CharField(max_length=100, default='The Redlights')
    photo = models.ImageField(upload_to='artist_photo')
    
    def __str__(self):
        return self.artist.name + ' ' + self.caption + ' Photo'
    
######## ----------------
    