"""View module for handling requests about episodess"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Cast
from django.contrib.auth.models import User


class CastView(ViewSet):
    """Bravo Bestie cast view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single cast member

        Returns:
            Response -- JSON serialized cast member
        """

        cast = Cast.objects.get(pk=pk)
        serializer = CastSerializer(cast)
        return Response(serializer.data)


class CastSerializer(serializers.ModelSerializer):
    """JSON serializer for cast
    """

    class Meta:
        model = Cast
        fields = ('id', 'name', 'img_url', 'instagram',
                  'twitter', 'bio')
