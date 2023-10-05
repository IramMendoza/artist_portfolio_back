from django.contrib import admin
from .models import Artist, Contact, ArtistPhoto

admin.site.register(Artist)
admin.site.register(Contact)
admin.site.register(ArtistPhoto)