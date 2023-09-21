"""
URL configuration for bravo project.

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from bravoapi.views import (EpisodeView, SeasonView, FranchiseView, register_user,
                            login_user, ProfileProfileEpisodeView, ProfileView, SeasonCastView,
                            ReviewView, FranchiseProfileEpisodeView, FranchiseCastView, CastView, BookView)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'episodes', EpisodeView, 'episode')
router.register(r'seasons', SeasonView, 'season')
router.register(r'casts', CastView, 'cast')
router.register(r'franchises', FranchiseView, 'franchise')
router.register(r'profileepisodes',
                ProfileProfileEpisodeView, 'profileEpisode')
router.register(r'profiles', ProfileView, 'profile')
router.register(r'profileepisode',
                FranchiseProfileEpisodeView, 'profile episode')
router.register(r'seasoncast',
                SeasonCastView, 'season cast')
router.register(r'franchisecast',
                FranchiseCastView, 'franchise cast')
router.register(r'books',
                BookView, 'book')
router.register(r'reviews',
                ReviewView, 'book')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_user),
    path('register', register_user),
    path('', include(router.urls)),  # Include the router's URLs
]
