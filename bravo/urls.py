"""
URL configuration for bravo project.

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from bravoapi.views import EpisodeView, SeasonView, FranchiseView, register_user

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'episodes', EpisodeView, 'episode')
router.register(r'seasons', SeasonView, 'season')
router.register(r'franchises', FranchiseView, 'franchise')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('', include(router.urls))
]
