from django.views.generic import ListView
from .models import Album


class AlbumList(ListView):
    model = Album
