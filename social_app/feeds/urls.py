from django.conf.urls import include
from django.urls import path
from .views import AddPostView, FeedsView


urlpatterns = [
    path('feeds', FeedsView.as_view(), name='feeds'),
    path('addpost',AddPostView.as_view(), name='addpost')
]