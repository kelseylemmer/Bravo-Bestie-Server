"""View module for handling requests about profile episodes"""
from django.http import HttpResponseServerError
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Profile, ProfileEpisode
from django.contrib.auth.models import User


class ProfileEpisodeView(ViewSet):
    """Bravo Bestie profile episode view"""

    def list(self, request):
        """Handle GET requests to profile episodes resource
        Returns:
            Response -- JSON serialized list of posts
        """

        profile_episodes = []
        profile_episodes = ProfileEpisode.objects.all()
        profile = Profile.objects.get(user=request.auth.user.id)

        if "current" in request.query_params:

            profile_episodes = profile_episodes.filter(profile=profile)

        serializer = ProfileEpisodesSerializer(profile_episodes, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        profileEpisode = ProfileEpisode.objects.get(pk=pk)
        profileEpisode.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ProfileEpisodesSerializer(serializers.ModelSerializer):
    """JSON serializer for Profile episodes
    """

    class Meta:
        model = ProfileEpisode
        fields = ('id', 'profile', 'episode')
