from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=120)
    venue = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    description = models.CharField(max_length=300)
    date = models.DateField()
    event_image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Gallery(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.event.name + ' Gallery'
    
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
    
    
    def __str__(self):
        return self.gallery.event.name + ' caption'