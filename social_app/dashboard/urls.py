from django.conf.urls import include
from django.urls import path
from .views import SignUpView, DashboardView


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls"),name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', DashboardView.as_view(), name='dashboard')
]