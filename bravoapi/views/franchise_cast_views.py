"""View module for handling requests about franchises"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import FranchiseCast, Cast
from django.contrib.auth.models import User


class FranchiseCastView(ViewSet):
    """Bravo Bestie franchise cast view"""

    def list(self, request):
        """Handle GET requests to get all franchise cast

        Returns:
            Response -- JSON serialized list of franchise casts
        """
        franchise = self.request.query_params.get('franchise')

        if franchise is not None:
            franchise_cast = FranchiseCast.objects.filter(franchise=franchise)
        else:
            franchise_cast = FranchiseCast.objects.all()

        serialized = FranchiseCastSerializer(franchise_cast, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class FranchiseCastCastSerializer(serializers.ModelSerializer):
    """JSON serializer for Franchise cast cast members
    """

    class Meta:
        model = Cast
        fields = ('id', 'img_url', 'name')


class FranchiseCastSerializer(serializers.ModelSerializer):
    """JSON serializer for Franchise cast
    """
    cast = FranchiseCastCastSerializer(many=False)

    class Meta:
        model = FranchiseCast
        fields = ('id', 'franchise', 'cast')
