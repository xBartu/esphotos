from .models import Photo


class TwitterAPI(object):
    """ The Twitter API to search #carnival hashtag. It's a kind of spider
    that searches the hashtag, download the images if it does not exist.
    TODOS:
    Implement the methods
    """

    def __init__(self):
        pass

    def search(self):
        """The search method, serching under Twitter search API
        Params
        url: the link of the REST API
        Returns
        json result of searches.
        Possible improvement is to record the last tweet ID. Ib that way,
        there will be more space in RAM and also the speed will be improved.
        """

    def is_downloadable(self, url):
        """To check the image was downloaded before by checking
        whether the url of picture is on database
        Params
        url: the url of the picture
        Returns
        True if it doesn't exist on db, else false
        """
        return True if not Photo.objects.filter(org_link=self.url) else False

    def download(self):
        """To download the photo if it doesn't exist according to
        is_downloadable method
        """
        pass
