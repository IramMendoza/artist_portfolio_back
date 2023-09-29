from rest_framework.generics import RetrieveAPIView
from .models import Artist
from .serializers import ArtistSerializer

class ArtistRetrieveAPIView(RetrieveAPIView):
    serializer_class = ArtistSerializer
    lookup_field = 'name'

    def get_queryset(self):
        artist_name = self.kwargs['name']
        queryset = Artist.objects.filter(name=artist_name)
        return queryset