"""View module for handling requests about whiskeys"""
from anorakapi.models.whiskey_tags import WhiskeyTag
from django.core.exceptions import ValidationError
from django.db.models import Max
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
        # tag = whiskeys.filter(relatedwhiskey__normalized_count=11)
        max_count = WhiskeyTag.objects.filter(whiskey_id=166).aggregate(Max('normalized_count'))
        print("max_count")
        print(max_count)
        tag = Tag.objects.get(relatedtag__normalized_count=max_count['normalized_count__max'], relatedtag__whiskey_id=166)
        print('tag')
        print(tag.title)
        if tag is not None:
            whiskeys = list(whiskeys.filter(relatedwhiskey__tag_id__title=tag.title))
        print("whiskeys")
        print(whiskeys)

        serializer = WhiskeySerializer(
            whiskeys, many=True, context={'request': request})
        return Response(serializer.data)

class TagSerializer(serializers.ModelSerializer):
    """JSON serializer for tags"""
    class Meta:
        model = Tag
        fields = ('id', 'title')
        depth = 1

class WhiskeySerializer(serializers.ModelSerializer):
    """JSON serializer for whiskeys"""
    tags = TagSerializer(many=True)
    class Meta:
        model = Whiskey
        fields = ('id', 'title', 'list_img_url', 'region', 'price')
        depth = 2

# class WhiskeyTagSerializer(serializers.ModelSerializer):
#     """JSON serializer for whiskey tags"""
#     class Meta:
#         model = WhiskeyTag
#         fields = ('id',)
#         depth = 2
        