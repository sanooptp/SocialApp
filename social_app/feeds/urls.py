from django.conf.urls import include
from django.urls import path
from .views import FeedsView


urlpatterns = [
    path('feeds', FeedsView.as_view(), name='feeds')
]