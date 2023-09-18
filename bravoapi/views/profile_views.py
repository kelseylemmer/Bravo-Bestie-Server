"""View module for handling requests about profiles"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Franchise, Profile
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class ProfileView(ViewSet):
    """Bravo Bestie profile view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single profile
        Returns:
            Response -- JSON serialized profile
        """

        profile = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all profiles

        Returns:
            Response -- JSON serialized list of profiles
        """
        profiles = Profile.objects.all()

        token = request.query_params.get("token", None)
        if token:
            user = Token.objects.get(key=token).user
            profiles = Profile.objects.get(user=user)
        serialized = ProfileSerializer(profiles)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def update(token, request, pk):
        """handles PUT requests for updating a Profile"""

        favorite_franchise = Franchise.objects.get(
            pk=request.data['favorite_franchise'])

        profile = Profile.objects.get(pk=pk)
        profile.user = request.auth.user
        profile.display_name = request.data["display_name"]
        profile.bio = request.data["bio"]
        profile.picture = request.data["picture"]
        profile.favorite_franchise = favorite_franchise

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
        fields = ('id', 'label', 'list_image')


class ProfileSerializer(serializers.ModelSerializer):
    """JSON serializer for Profile
    """

    favorite_franchise = ProfileFranchiseSerializer(many=False)
    user = ProfileUserSerializer(many=False)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'display_name', 'bio',
                  'picture', 'favorite_franchise')
