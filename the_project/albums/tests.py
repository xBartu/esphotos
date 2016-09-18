from django.test import TestCase
from django.test.client import Client
from .models import Album
from .models import Photo


class AlbumTestCase(TestCase):
    """The Album Test Class.
    """
    def setUp(self):
        self.client = Client()
        Album.objects.create(name="tag")

    def test_album_is_created(self):
        """The test for checking the django created the class.
        In case, the api was changed
        """
        album = Album.objects.get(name="tag")
        self.assertEqual(album.name, "tag")
        self.assertEqual(album.total_photo, 0)

    def test_check_main_page(self):
        """Test to check main page is live
        """
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_check_album_page(self):
        """Test to check an album page is live
        """
        res = self.client.get("/1")
        self.assertEqual(res.status_code, 200)

    def test_check_api_main_page(self):
        """Test to check the api is live
        """
        res = self.client.get("/api/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()[0]["name"], "tag")
        self.assertEqual(res.json()[0]["total_photo"], 0)

    def test_check_album_page_api(self):
        """Test to check album page api
        Note: We cannot check if there is a photo,
        if there is, something must be wrong :)
        """
        res = self.client.get("/api/album/1")
        self.assertEqual(res.status_code, 200)


class PhotoTestCase(TestCase):
    """ Checking the functionality of photo creation
    """
    def setUp(self):
        """ Test set up
        """
        self.client = Client()
        Photo.objects.create_photo(
            "https://www.facebook.com/logo.jgp", None,
            "bartu", album
        )

    def check_photo_created(self):
        """ Test to check the photo was created correctly,
        and test also the number of photo was updated
        """
        photo = Photo.objects.get(pk=1)
        self.assertEqual(photo.album.name, "tag")
        self.assertEqual(photo.user, "bartu")
        self.assertEqual(photo.org_link, "https://www.facebook.com/logo.jgp")
        self.assertEqual(photo.album.total_photo, 1)

    def check_single_photo_api(self):
        """Test to check single photo API
        """
        res = self.client.get("/api/album/1/photo/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)
        self.assertEqual(
                res.json()[0]["org_link"], "https://www.facebook.com/logo.jgp"
        )
        self.assertEqual(res.json()[0]["user"], "Bartu")
        self.assertEqual(res.json()[0]["number_of_likes"], 0)

    def check_album_api_updated(self):
        """ Test to check whether the album was updated
        """
        res = self.client.get("/api/album/1")
        self.assertEqual(res.json()[0]["user"], "Bartu")
