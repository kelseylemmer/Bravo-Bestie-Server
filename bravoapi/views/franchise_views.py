"""View module for handling requests about event"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Franchise, Season
from django.contrib.auth.models import User


class FranchiseView(ViewSet):
    """Bravo Bestie franchise view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single franchise
        Returns:
            Response -- JSON serialized franchise
        """

        franchise = Franchise.objects.get(pk=pk)
        serializer = FranchiseSerializer(franchise)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all franchises

        Returns:
            Response -- JSON serialized list of franchises
        """
        franchises = Franchise.objects.all()
        serialized = FranchiseSerializer(franchises, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class FranchiseSeasonsSerializer(serializers.ModelSerializer):
    """JSON serializer for franchise seasons
    """

    class Meta:
        model = Season
        fields = ('id', 'season_number', 'premier_date')


class FranchiseSerializer(serializers.ModelSerializer):
    """JSON serializer for Franchise
    """

    seasons = FranchiseSeasonsSerializer(many=True)

    class Meta:
        model = Franchise
        fields = ('id', 'label', 'abbreviation', 'series_premier',
                  'seasons')
