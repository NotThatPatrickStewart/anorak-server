"""View module for handling requests about whiskeys"""
from anorakapi.models.whiskey_tags import WhiskeyTag
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from anorakapi.models import Whiskey, Tag, WhiskeyTag

class Whiskeys(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single whiskey

        Returns:
            Response -- JSON serialized whiskey instance
        """

        try:
            whiskey = Whiskey.objects.get(pk=pk)
            serializer = WhiskeySerializer(whiskey, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to whiskeys resource

        Returns:
            Response -- JSON serialized list of whiskeys
        """
        # Get all whiskey records from the database
        whiskeys = Whiskey.objects.all()

        # Support filtering whiskeys by tag
        tag = self.request.query_params.get('whiskey_id', None)
        if tag is not None:
            whiskeys = whiskeys.filter(tag__id=tag)

        serializer = WhiskeySerializer(
            whiskeys, many=True, context={'request': request})
        return Response(serializer.data)

class WhiskeyTagSerializer(serializers.ModelSerializer):
    """JSON serializer for whiskey tags"""
    class Meta:
        model = WhiskeyTag
        fields = ('id', 'normalized_count')

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags"""
    tag = WhiskeyTagSerializer(many=False)
    class Meta:
        model = Tag
        fields = ('id', 'title', 'tag')
        depth = 1

class WhiskeySerializer(serializers.ModelSerializer):
    """JSON serializer for whiskeys"""
    class Meta:
        model = Whiskey
        fields = ('id', 'title', 'list_img_url', 'region', 'price')
        depth = 1

# class WhiskeySerializer(serializers.ModelSerializer):
#     """JSON serializer for whiskeys"""
#     whiskey = WhiskeyTagSerializer(many=False)
#     class Meta:
#         model = Whiskey
#         fields = ('id', 'title', 'list_img_url', 'region', 'price', 'whiskey')
#         depth = 1
        