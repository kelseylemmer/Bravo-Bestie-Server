"""View module for handling requests about episodess"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bravoapi.models import Book, Cast
from django.contrib.auth.models import User
from django.db.models import F


class BookView(ViewSet):
    """Bravo Bestie book view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single book

        Returns:
            Response -- JSON serialized book
        """
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def list(self, request):
        books = Book.objects.all()

        cast_id = request.query_params.get("cast")
        if cast_id:
            try:
                cast = Cast.objects.get(id=cast_id)
                books = books.filter(cast=cast)
            except Cast.DoesNotExist:
                return Response(
                    {"error": "Not found."},
                    status=status.HTTP_404_NOT_FOUND
                )

        # Sorting books by franchise when getting all
        if not cast_id:
            books = books.annotate(
                franchise_label=F('cast__franchises__label'))
            books = books.order_by('franchise_label', 'title')

        serialized = BookSerializer(books, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class BookCastSerializer(serializers.ModelSerializer):
    """JSON serializer for book
    """

    class Meta:
        model = Cast
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    """JSON serializer for book
    """

    cast = BookCastSerializer(many=False)

    class Meta:
        model = Book
        fields = ('id', 'title', 'pages', 'synopsis',
                  'publisher', 'img_url', 'publish_date', 'cast', 'purchase')
