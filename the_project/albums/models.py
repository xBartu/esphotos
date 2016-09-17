from django.db import models


class Album(models.Model):
    """ Album model scheme for the project. Every albun can have many photos
    else it can be happy.
    Params
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
        return "{}".format(self.name)


class Photo(models.Model):
    """The photo model.
    Params
    org_link: the original url of the photo, going to use in
    dublicate detection process. I assume that the link cannot
    be longer than 300 chars.
    photo: The downloaded photo. There is a risk that the photo
    can be removed in the original server. To avoid that, we
    serve the photo in our status
    user = the user who uploaded the photo to twitter, assumed
    that there doesn't need to create a django user for it
    album = the album which the photo belongs to.
    """
    org_link = models.URLField(max_length=300)
    photo = models.ImageField(upload_to='albums/photos')
    user = models.CharField(max_length=60)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        """Returns
        the name of the user and id of the photo
        """
        return "{}-{}".format(self.user, self.pk)
