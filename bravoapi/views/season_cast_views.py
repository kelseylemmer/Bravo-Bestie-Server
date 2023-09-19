"""View module for handling requests about profiles"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Franchise, Season, Role, Cast, SeasonCast
from django.db.models import F


class SeasonCastView(ViewSet):
    """Bravo Bestie season cast view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single season cast
        Returns:
            Response -- JSON serialized season cast
        """

        season_cast = SeasonCast.objects.get(pk=pk)
        serializer = SeasonCastSerializer(season_cast)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all season cast 

        Returns:
            Response -- JSON serialized list of season cast
        """
        franchise = self.request.query_params.get('franchise')

        if franchise is not None:
            season_cast = SeasonCast.objects.filter(
                season__franchise__id=franchise
            ).order_by('season')
        else:
            season_cast = SeasonCast.objects.all()

        serialized = SeasonCastSerializer(season_cast, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class SeasonCastRoleSerializer(serializers.ModelSerializer):
    """JSON serializer for Role
    """

    class Meta:
        model = Role
        fields = ('id', 'label')


class SeasonCastCastSerializer(serializers.ModelSerializer):
    """JSON serializer for Cast
    """

    class Meta:
        model = Cast
        fields = ('id', 'name', 'img_url', 'instagram', 'twitter')


class SeasonCastSeasonFranchiseSerializer(serializers.ModelSerializer):
    """JSON serializer for Franchise
    """

    class Meta:
        model = Franchise
        fields = ('id', 'label')


class SeasonCastSeasonSerializer(serializers.ModelSerializer):
    """JSON serializer for Season
    """
    franchise = SeasonCastSeasonFranchiseSerializer(many=False)

    class Meta:
        model = Season
        fields = ('id', 'season_number', 'franchise')


class SeasonCastSerializer(serializers.ModelSerializer):
    """JSON serializer for Season Cast
    """
    cast = SeasonCastCastSerializer(many=False)
    season = SeasonCastSeasonSerializer(many=False)
    role = SeasonCastRoleSerializer(many=False)

    class Meta:
        model = SeasonCast
        fields = ('id', 'cast', 'season', 'role')
