"""
URL configuration for bravo project.

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from bravoapi.views import EpisodeView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'episodes', EpisodeView, 'episode')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
