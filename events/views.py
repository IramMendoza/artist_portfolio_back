from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import EventSerializer, GallerySerializer
from .models import Event, Gallery

class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class EventRetrieveAPIView(RetrieveAPIView):
    serializer_class = EventSerializer
    
    def get_object(self):
        return Event.objects.get(pk=self.kwargs['event_pk'])
    
class GalleryRetrieveAPIView(RetrieveAPIView):
    serializer_class = GallerySerializer

    def get_object(self):
        return Gallery.objects.get(pk=self.kwargs['event_pk'])
