"""View module for handling requests about profile episodes"""
from rest_framework import serializers
from bravoapi.models import ProfileEpisode, Episode, Season, Franchise
from django.http import HttpResponseServerError
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Profile, ProfileEpisode, Episode, Season, Franchise
from django.contrib.auth.models import User


class ProfileProfileEpisodeView(ViewSet):
    """Bravo Bestie profile episode view"""

    def list(self, request):
        """Handle GET requests to profile episodes resource
        Returns:
            Response -- JSON serialized list of posts
        """

        profile_episodes = []
        profile_episodes = ProfileEpisode.objects.order_by('episode')
        profile = Profile.objects.get(user=request.auth.user.id)

        if "current" in request.query_params:

            profile_episodes = profile_episodes.filter(profile=profile)

        serializer = ProfileEpisodesSerializer(profile_episodes, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        profileEpisode = ProfileEpisode.objects.get(pk=pk)
        profileEpisode.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST requests for creating a profile episode

        Returns:
            Response -- JSON serialized profile episode record
        """
        episode = Episode.objects.get(pk=request.data["episode"])
        profile = Profile.objects.get(user=request.auth.user.id)

        new_profile_episode = ProfileEpisode()

        new_profile_episode.profile = profile
        new_profile_episode.episode = episode
        new_profile_episode.save()

        serialized = ProfileEpisodesSerializer(new_profile_episode, many=False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class ProfileEpisodeEpisodeSerializer(serializers.ModelSerializer):
    """JSON serializer for Profile episodes - episodes"""

    class Meta:
        model = Episode
        fields = ('id', 'title', 'episode')


class ProfileEpisodeSeasonSerializer(serializers.ModelSerializer):
    """JSON serializer for Profile episodes - episode season"""

    class Meta:
        model = Season
        fields = ('id', 'season_number')


class ProfileEpisodeFranchiseSerializer(serializers.ModelSerializer):
    """JSON serializer for Profile episodes - episode season franchise"""

    class Meta:
        model = Franchise
        fields = ('id', 'label')


class ProfileEpisodesSerializer(serializers.ModelSerializer):
    """JSON serializer for Profile episodes"""

    franchise = ProfileEpisodeFranchiseSerializer(
        many=False, source='episode.season.franchise')
    season = ProfileEpisodeSeasonSerializer(
        many=False, source='episode.season')
    episode = ProfileEpisodeEpisodeSerializer()

    class Meta:
        model = ProfileEpisode
        fields = ('profile', 'franchise', 'season', 'episode')
