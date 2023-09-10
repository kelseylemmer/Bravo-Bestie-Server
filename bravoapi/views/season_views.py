"""View module for handling requests about event"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Episode, Season
from django.contrib.auth.models import User


class SeasonView(ViewSet):
    """Bravo Bestie season view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single season
        Returns:
            Response -- JSON serialized season
        """

        season = Season.objects.get(pk=pk)
        serializer = SeasonSerializer(season)
        return Response(serializer.data)

    # def list(self, request):
    #     """Handle GET requests to get all seasons

    #     Returns:
    #         Response -- JSON serialized list of seasons
    #     """
    #     episodes = Episode.objects.all()

    #     season_id = request.query_params.get("season")
    #     if season_id:
    #         try:
    #             season = Season.objects.get(id=season_id)
    #             episodes = episodes.filter(season=season)
    #         except Season.DoesNotExist:
    #             return Response(
    #                 {"error": "Season not found."},
    #                 status=status.HTTP_404_NOT_FOUND
    #             )
    #     serialized = EpisodeSerializer(episodes, many=True)
    #     return Response(serialized.data, status=status.HTTP_200_OK)


class SeasonEpisodesSerializer(serializers.ModelSerializer):
    """JSON serializer for season episodes
    """

    class Meta:
        model = Episode
        fields = ('id', 'title', 'synopsis', 'runtime',
                  'episode', 'air_date')


class SeasonSerializer(serializers.ModelSerializer):
    """JSON serializer for Season
    """

    episodes = SeasonEpisodesSerializer(many=True)

    class Meta:
        model = Season
        fields = ('id', 'season_number', 'franchise', 'premier_date',
                  'episodes')
