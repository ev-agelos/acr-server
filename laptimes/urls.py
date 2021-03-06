"""Url patterns for the laptimes package."""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.laptimes, name='laptimes'),
    url(r'^me$', views.user_laptimes, name='user_laptimes'),
    url(r'^setup/(?P<setup_id>\d+)$', views.download_setup, name='download_setup'),
]
