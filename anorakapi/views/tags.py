"""View module for handling requests about tags"""
from decimal import Context
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from anorakapi.models import Tag

class Tags(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single tag

        Returns:
            Response -- JSON serialized tag
        """

        try:
            tag = Tag.objects.get(pk=pk)
            serializer = TagSerializer(tag, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to tags resource

        Returns:
            Response -- JSON serialized list of tags
        """
        # Get all tag records from the database
        tags = Tag.objects.all()

        serializer = TagSerializer(
            tags, many=True, context={'request': request})
        return Response(serializer.data)


class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags

    Arguments:
        serializer type
    """
    class Meta:
        model = Tag
        fields = ('id', 'title')
        