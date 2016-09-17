import oauth2
import json
from io import BytesIO as bio
from urllib.request import urlopen as uo
from django.core.files import File
from .models import Photo


class TwitterAPI(object):
    """ The Twitter API to search #carnival hashtag. It's a kind of spider
    that searches the hashtag, download the images if it does not exist.
    TODOS:
    Built tests..
    """

    def __init__(self, consumer_key, consumer_secret, key, secret):
        """An constructor for the class
        Params
        consumer_secret: API App Consumer Secret
        consumer_key: API App Consumer Key
        secret: API User Secret
        key: API User Key
        """
        self.consumer_secret = consumer_secret
        self.consumer_key = consumer_key
        self.secret = secret
        self.key = key

    def search(self):
        """The search method, serching under Twitter search API
        Params
        url: the link of the REST API
        Returns
        json result of searches.
        Possible improvement is to record the last tweet ID. Ib that way,
        there will be more space in RAM and also the speed will be improved.
        Warning:The method was also used in twitter dev guide..
        """
        consumer = oauth2.Consumer(
                key=self.consumer_key, secret=self.consumer_secret
        )
        token = oauth2.Token(key=self.key, secret=self.secret)
        response, content = oauth2.Client(consumer, token).request(
                'https://api.twitter.com/1.1/search/tweets.json?q=%23carnival&filter=images&count=100',
                method='GET', body=b'', headers=None
        )
        statutes = json.loads(content.decode())["statutes"]
        return (response, statutes)

    def is_downloadable(url):
        """To check the image was downloaded before by checking
        whether the url of picture is on database
        Params
        url: the url of the picture
        Returns
        True if it doesn't exist on db, else false
        """
        return True if not Photo.objects.filter(org_link=url) else False

    def add_photo(self, user, url):
        """To add and download the photo if it doesn't exist according to
        is_downloadable method
        TODO: add form to valid the data
        """
        if self.is_downloadable(url):
            name = url.split('/')[-1]
            the_file = bio(uo(url).read())
            photo = Photo()
            photo.org_link = url
            photo.user = user
            photo.photo.save(name, File(the_file))

    def walker(self):
        """ Walking through the tweets, and send the info
        the download method
        Paarams
        tweets: the tweets from search api as json in a list
        """
        tweets = self.search()
        for tweet in tweets:
            self.add_photo(
                    tweet["user"]["name"],
                    tweet["extended_entities"]["media"][0]["media_url"]
            )
