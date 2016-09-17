from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Album
from .models import Photo


class AlbumList(ListView):
    model = Album
    context_object_name = 'albums'


class AlbumDetail(ListView):
    context_object_name = 'photos'
    template_name = 'albums/album_detail_list.html'

    def get_queryset(self):
        self.album = get_object_or_404(Album, pk=self.kwargs['pk'])
        return Photo.objects.filter(album=self.album).all()
