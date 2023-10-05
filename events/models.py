from django.db import models
from artist.models import Artist

class Event(models.Model):
    venue = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=120)
    description = models.TextField(max_length=300)
    date = models.DateField()
    event_image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='events')
    
    def __str__(self):
        return self.venue
    
class Picture(models.Model):
    
    ENCLOSURE_CHOICES = [
        ('vertical', 'Vertical'),
        ('horizontal', 'Horizontal'),
        ('square', 'Square'),
    ]
        
    picture = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=120, default='The Redlights')
    enclosure = models.CharField(max_length=20, choices=ENCLOSURE_CHOICES)
    event = models.ForeignKey(Event,  related_name='pictures', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.event.venue + ' ' + self.caption