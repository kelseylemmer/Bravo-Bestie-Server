from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from bravoapi.models import Profile, Franchise


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    # If authentication was successful, respond with their token
    if authenticated_user is not None and authenticated_user.is_active:
        token = Token.objects.get(user=authenticated_user)

        data = {
            'valid': True,
            'token': token.key
        }
        return Response(data)
    else:
        data = {'valid': False}
        return Response(data)


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
        request -- The full HTTP request object
    '''

    email = request.data.get('email', None)
    first_name = request.data.get('first_name', None)
    last_name = request.data.get('last_name', None)
    password = request.data.get('password', None)
    display_name = request.data['display_name']
    bio = request.data['bio']
    picture = request.data.get('picture', 'https://i.imgur.com/qhgJMUC.png')
    favorite_franchise = Franchise.objects.get(
        pk=request.data['favorite_franchise'])

    if email is not None\
            and first_name is not None \
            and last_name is not None \
            and password is not None:

        try:
            new_user = User.objects.create_user(
                username=request.data['email'],
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )

            profile = Profile.objects.create(
                user=new_user,
                display_name=display_name,
                bio=bio,
                picture=picture,
                favorite_franchise=favorite_franchise
            )

        except IntegrityError:
            return Response(
                {'message': 'An account with that email already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        token = Token.objects.create(user=profile.user)
        # Return the token to the client
        data = {'token': token.key}
        return Response(data)

    return Response({'message': 'You must provide email, password, first_name, and last_name'}, status=status.HTTP_400_BAD_REQUEST)
