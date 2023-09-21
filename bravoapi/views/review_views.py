"""View module for handling requests about reviewss"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Review, Profile, Book
from rest_framework.authtoken.models import Token


class ReviewView(ViewSet):
    """Bravo Bestie review view"""

    def list(self, request):
        """Handle GET requests to get all reviews

        Returns:
            Response -- JSON serialized list of reviews
        """
        book = self.request.query_params.get('book')

        if book is not None:
            reviews = Review.objects.filter(book=book)
        else:
            reviews = Review.objects.all()

        serialized = ReviewSerializer(reviews, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        """Handle POST requests for creating a review

        Returns:
            Response -- JSON serialized review record
        """

        print(request.data)
        book = Book.objects.get(pk=request.data["book"])
        profile = Profile.objects.get(user=request.auth.user.id)

        review = Review.objects.create(
            profile=profile,
            book=book,
            review=request.data["review"]
        )

        serialized = ReviewSerializer(review, many=False)
        return Response(serialized.data, status=status.HTTP_201_CREATED)


class ReviewProfileSerializer(serializers.ModelSerializer):
    """JSON serializer for Review Profile
    """

    class Meta:
        model = Profile
        fields = ('id', 'full_name', 'picture')


class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for Review
    """

    profile = ReviewProfileSerializer(many=False)

    class Meta:
        model = Review
        fields = ('id', 'profile', 'book', 'review', 'date')
