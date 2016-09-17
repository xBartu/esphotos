from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Album
from .models import Photo


class AlbumList(ListView):
    """The Album List View as class based. This style chosed
    because less code is usually better. By considering the
    basic request, it is good to go.
    Assumption: There is no login is required. The album list
    is public.
    Args:
    model: It's the name of model which is accessed in template
    context_object_name: the model's name for templating
    """
    model = Album
    context_object_name = 'albums'


class AlbumDetail(ListView):
    """The Album Detail view as class based. It's still good fit
    for that view.
    Assumption: Pictures are public, no need for being logged in
    Args:
    template_name: the path way of the html template
    context_object_name: the model's name
    methods:
    get_queryset: provides the model acces in template
    """
    context_object_name = 'photos'
    template_name = 'albums/album_detail_list.html'

    def get_queryset(self):
        self.album = get_object_or_404(Album, pk=self.kwargs['pk'])
        return Photo.objects.filter(album=self.album).all()
