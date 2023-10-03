from django.db import models

class Event(models.Model):
    venue = models.CharField(max_length=120, unique=True)
    location = models.CharField(max_length=120)
    description = models.TextField(max_length=300)
    date = models.DateField()
    event_image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    
    def __str__(self):
        return self.venue
    
class Gallery(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='gallery')
    
    def __str__(self):
        return self.event.venue + ' Gallery'
    
class Photo(models.Model):
    
    ENCLOSURE_CHOICES = [
        ('vertical', 'Vertical'),
        ('horizontal', 'Horizontal'),
        ('cuadrado', 'Cuadrado'),
    ]
        
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=120)
    enclosure = models.CharField(max_length=20, choices=ENCLOSURE_CHOICES)
    gallery = models.OneToOneField(Gallery, on_delete=models.CASCADE, related_name='photo')
    
    
    def __str__(self):
        return self.gallery.event.venue + ' ' + self.caption