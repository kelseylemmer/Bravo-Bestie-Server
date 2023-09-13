"""View module for handling requests about seasons"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Episode, Season, Franchise
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

    def list(self, request):
        """Handle GET requests to get all seasons

        Returns:
            Response -- JSON serialized list of seasons
        """
        seasons = Season.objects.all()

        franchise_id = request.query_params.get("franchise")
        if franchise_id:
            try:
                franchise = Franchise.objects.get(id=franchise_id)
                seasons = seasons.filter(franchise=franchise)
            except Franchise.DoesNotExist:
                return Response(
                    {"error": "Franchise not found."},
                    status=status.HTTP_404_NOT_FOUND
                )
        serialized = SeasonSerializer(seasons, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


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
