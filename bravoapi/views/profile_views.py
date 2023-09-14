"""View module for handling requests about profiles"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Franchise, Profile
from django.contrib.auth.models import User


class ProfileView(ViewSet):
    """Bravo Bestie profile view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single profile
        Returns:
            Response -- JSON serialized profile
        """

        if "current" in request.query_params:
            profile = Profile.objects.get(user=request.auth.user.id)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all profiles

        Returns:
            Response -- JSON serialized list of profiles
        """
        profiles = Profile.objects.all()
        serialized = ProfileSerializer(profiles, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        """handles PUT requests for updating a Profile"""
        profile = Profile.objects.get(pk=pk)
        profile.user = User.objects.get(pk=request.data["user"])
        profile.display_name = request.data["display_name"]
        profile.bio = request.data["bio"]
        profile.picture = request.data["picture"]
        profile.favorite_franchise = request.data["favorite_franchise"]

        profile.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class ProfileFranchiseSerializer(serializers.ModelSerializer):
    """JSON serializer for Profile
    """

    class Meta:
        model = Franchise
        fields = ('id', 'label')


class ProfileSerializer(serializers.ModelSerializer):
    """JSON serializer for Profile
    """

    favorite_franchise = ProfileFranchiseSerializer(many=False)
    user = ProfileUserSerializer(many=False)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'display_name', 'bio',
                  'picture', 'favorite_franchise')
