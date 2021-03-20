"""View module for handling requests about tags"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from anorakapi.models import Tag

class Tags(ViewSet):

    def list(self, request):
        """Handle GET requests to tags resource

        Returns:
            Response -- JSON serialized list of tags
        """
        # Get all tag records from the database
        tags = Tag.objects.all()

        # Support filtering tags by type
        #    http://localhost:8000/tags?type=1
        #
        # That URL will retrieve all tabletop tags
        tag_type = self.request.query_params.get('type', None)
        if tag_type is not None:
            tags = tags.filter(tagtype__id=tag_type)

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
        fields = ('id', 'title', 'tag_type')
        depth = 1
        