"""View module for handling requests about episodess"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Episode, Season, Franchise
from django.contrib.auth.models import User


class EpisodeView(ViewSet):
    """Bravo Bestie episode view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single episode

        Returns:
            Response -- JSON serialized episode
        """

        episode = Episode.objects.get(pk=pk)
        serializer = EpisodeSerializer(episode)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all episodes

        Returns:
            Response -- JSON serialized list of episodes
        """
        episodes = Episode.objects.all()

        season_id = request.query_params.get("season")
        if season_id:
            try:
                season = Season.objects.get(id=season_id)
                episodes = episodes.filter(season=season)
            except Season.DoesNotExist:
                return Response(
                    {"error": "Season not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
        serialized = EpisodeSerializer(episodes, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class SeasonFranchiseSerializer(serializers.ModelSerializer):
    """JSON serializer for season franchise
    """

    class Meta:
        model = Franchise
        fields = ('label', 'id')


class EpisodeSeasonSerializer(serializers.ModelSerializer):
    """JSON serializer for episode season
    """

    franchise = SeasonFranchiseSerializer(many=False)

    class Meta:
        model = Season
        fields = ('season_number', 'franchise', 'premier_date', 'id')


class EpisodeSerializer(serializers.ModelSerializer):
    """JSON serializer for episode
    """

    season = EpisodeSeasonSerializer(many=False)

    class Meta:
        model = Episode
        fields = ('id', 'title', 'synopsis', 'runtime',
                  'season', 'episode', 'air_date')
