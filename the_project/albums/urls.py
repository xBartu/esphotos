from django.conf.urls import url
from .views import AlbumList
from .views import AlbumDetail
from .views import AlbumViewSet
from .views import AlbumDetailViewSet
from .views import SinglePhotoViewSet

app_name = "albums"
urlpatterns = [
    url(r'^$', AlbumList.as_view(), name="index"),
    url(r'^(?P<pk>[0-9]+)$', AlbumDetail.as_view(), name='album_detail'),
    url(r'^api/$', AlbumViewSet.as_view()),
    url(r'^api/album/(?P<album_id>[0-9]+)', AlbumDetailViewSet.as_view()),
    url(r'^api/album/?P<album_id>[0-9]+/photo/?P<pk>[0-9]+',
        SinglePhotoViewSet.as_view()),
]
