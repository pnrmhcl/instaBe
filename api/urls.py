from django.urls import path

from api.views import get_user, get_user_media, get_single_media, get_user_media_count

urlpatterns = [
    path('get-user', get_user, name="get-user"),
    path('get-user-media', get_user_media, name="get-user-media"),
    path('get-single-media/<int:media_id>', get_single_media, name="get-single-media"),
    path('get-user-media-count', get_user_media_count, name="get-user-media-count")
]
