"""View module for handling requests about event"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Episode
from django.contrib.auth.models import User


class EpisodeView(ViewSet):
    """Bravo Bestie episode view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single episde

        Returns:
            Response -- JSON serialized episode
        """

        episode = Episode.objects.get(pk=pk)
        serializer = EpisodeSerializer(episode)
        return Response(serializer.data)


class EpisodeSerializer(serializers.ModelSerializer):
    """JSON serializer for episode
    """

    class Meta:
        model = Episode
        fields = ('id', 'title', 'synopsis', 'runtime',
                  'season', 'episode', 'air_date')
