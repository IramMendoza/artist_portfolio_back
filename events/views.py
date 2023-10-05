from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import EventSerializer, PictureSerializer
from .models import Event, Picture
from django.http import Http404

class EventListView(ListAPIView):
    serializer_class = EventSerializer
    lookup_url_kwarg = 'artist'
    
    def get_queryset(self):
        artist = self.kwargs['artist']
        return Event.objects.filter(artist__name=artist)

class EventDetailView(RetrieveAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        event_id = self.kwargs['id']
        return Event.objects.filter(id=event_id)