from the_project import settings
from .twitter import TwitterAPI
twitter = TwitterAPI()
twitter.walker().apply_async(countdown=1200)
