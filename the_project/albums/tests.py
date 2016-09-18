from django.test import TestCase
from .models import Album
from .models import Photo


class AlbumTestCase(TestCase):
    """The Album Test Class.
    """
    def setUp(self):
        album = Album.objects.get(name="tag")
        if album: # in case it exists
            album.remove()
        Album.objects.create(name="album")

    def test_album_is_created(self):
        """The test for checking the django created the class.
        In case, the api was changed
        """
        album = Album.objects.get(name="tag")
        self.assertEqual(album.name, "tag")
        self.assertEqual(album.total_photo, 0)


class PhotoTestCase(TestCase):
    """ Checking the functionality of photo creation
    """
    pass
