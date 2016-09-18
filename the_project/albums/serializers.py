from rest_framework import serializers
from .models import Album
from .models import Photo


class AlbumSerializer(serializers.ModelSerializer):
    """ A serializers for albums.
    Assumptions: No need to login for viewing albums
    """
    class Meta:
        """Meta class..
        Args:
        model: The model
        fields: The fields to be serilazied in model
        """
        model = Album
        fields = ('name', 'total_photo')


class PhotoSerializer(serializers.ModelSerializer):
    """ A serializers for the photos.
    Assumption: No need to login for viewing photos api.
    """
    class Meta:
        """Meta class..
        Args
        model: The model
        fields: The fields in the model to be serializered
        """
        model = Photo
        fields = ('org_link', 'photo', 'user', 'number_of_likes')


class SinglePhotoSerializer(serializers.ModelSerializer):
    """ A serializers for the single photo.
    Assumption: No need to login for viewing single photo api.
    """
    class Meta:
        """Meta class..
        Args
        model: The model
        fields: The fields in the model to be serializered
        """
        model = Photo
        fields = ('org_link', 'photo', 'user', 'album', 'number_of_likes')
