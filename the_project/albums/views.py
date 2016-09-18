from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.views.generic import ListView
from .models import Album
from .models import Photo
from .serializers import AlbumSerializer
from .serializers import PhotoSerializer
from .serializers import SinglePhotoSerializer


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


class AlbumViewSet(generics.ListAPIView):
    """API Endpoint that user can view albums in the db
    Args
    queryset: The model for being serializered
    serializer_class: the class from serializer.py
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetailViewSet(generics.ListAPIView):
    """API Endpoint that user can view the photos of the whole photos in
    a album
    Returns
    the whole photo objects
    """
    serializer_class = PhotoSerializer

    def get_queryset(self):
        self.album = get_object_or_404(Album, pk=self.kwargs["album_id"])
        queryset = Photo.objects.filter(album=self.album).all()
        return queryset


class SinglePhotoViewSet(generics.ListAPIView):
    """API endpoint that user can view the single photo
    according to pk of the photo
    Args
    serialzier_class: the class from serializer.py
    Methods:
    get_queryset: The model for being serializered will be
    returned
    """
    serializer_class = SinglePhotoSerializer

    def get_queryset(self):
        """ A method  to get photo object
        Returns
        the object according to pk of the Photo
        """
        queryset = Photo.objects.get(pk=self.kwargs["pk"])
        return queryset
