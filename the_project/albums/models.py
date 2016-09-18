# Strong assumption: The user model is need to be created. In that use,
# there is no need the user model. In production, you can use classic user
# model of django
from django.db import models


class Album(models.Model):
    """ Album model scheme for the project. Every albun can have many photos
    else it can be happy.
    Args
    name: the name of the album, assumed that the max length for the name is
    25 chars.
    total_photo: the number of the photos in album
    """
    name = models.CharField(max_length=25)
    total_photo = models.PositiveIntegerField(default=0)

    def __str__(self):
        """ Returns
        The name of the photo
        """
        return "{}- {}".format(self.name, self.pk)


class PhotoManager(models.Manager):
    """Photo Menager that contains helper methods for
    Photo model
    Methods
    create_photo: a method to create Photo Object and
    saves it to db
    """
    def create_photo(self, org_link, photo, user, album):
        """ Creating the Photo object and saving to the database
        Params:
        org_link: the original URL
        photo: photo object
        user: the name of the user who the photo belongs to
        album: Album object that the photo relates to
        """
        photo = self.create(
            org_link=org_link, photo=photo, user=user, album=album
        )
        return photo


class Photo(models.Model):
    """The photo model.
    Args
    org_link: the original url of the photo, going to use in
    dublicate detection process. I assume that the link cannot
    be longer than 300 chars.
    photo: The downloaded photo. There is a risk that the photo
    can be removed in the original server. To avoid that, we
    serve the photo in our status
    user: the user who uploaded the photo to twitter, assumed
    that there doesn't need to create a django user for it
    album: the album which the photo belongs to.
    objects: It's the photo create Manager
    creaated_at: the adding/storing time of photo
    number_of_likes: the number of likes were gotten by photo
    """
    org_link = models.URLField(verbose_name='The Original Url', max_length=300)
    photo = models.ImageField(upload_to='albums/photos')
    user = models.CharField(max_length=60)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    number_of_likes = models.PositiveIntegerField(default=0)
    objects = PhotoManager()

    def __str__(self):
        """Returns
        the name of the user and id of the photo
        """
        return "{}-{}".format(self.user, self.pk)


class PhotoLike(models.Model):
    """The model for storing the likes
    Args
    photo: the photo object
    user: who liked the photo
    is_liked: whether the action user was liked, it's not good idea to delete
    the object from the database for unlike operation
    """
    photo = models.ForeignKey('Photo', on_delete=models.CASCADE)
    user = models.CharField(max_length=60)
    is_liked = models.BooleanField(default=True)

    def __str__(self):
        """The functioni to make objects name understable for admin panel.
        """
        return "{}-{}-{}".format(self.user, self.is_liked, self.photo.pk)
