from django.conf.urls import url
from .views import AlbumList
from .views import AlbumDetail
app_name = "albums"
urlpatterns = [
    url(r'^$', AlbumList.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)$', AlbumDetail.as_view(), name='album_detail'),
]
