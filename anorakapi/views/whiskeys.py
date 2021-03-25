"""View module for handling requests about whiskeys"""
from anorakapi.models.whiskey_tags import WhiskeyTag
from django.core.exceptions import ValidationError
from django.db.models import Max
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from anorakapi.models import Whiskey, Tag, WhiskeyTag, whiskey

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
        #find a whiskey by title here, so that the filter ˇ can filter on it instead of a hard-coded number
       
        max_count = Whiskey.objects.all()
        search = self.request.query_params.get('title', None) #search is coming back None, 'title' isn't right?
        if search is not None:
            max_count = WhiskeyTag.objects.filter(whiskey_id=search).aggregate(Max('normalized_count')) #finds the highest nomalized count for a particular whiskey
        print("search")
        print(search)
        print("max_count")
        print(max_count)
       
        tag = Tag.objects.get(relatedtag__normalized_count=max_count['normalized_count__max'], relatedtag__whiskey_id=166) #finds the id of the tag associated with that count
        print('tag')
        print(tag.title)
       
        if tag is not None:
            result = WhiskeyTag.objects.filter(tag_id=tag.id).aggregate(Max('normalized_count')) #finds the highest nomalized count for a particular tag  

            whiskeys = Whiskey.objects.filter(relatedwhiskey__normalized_count=result['normalized_count__max'], relatedwhiskey__tag_id=tag.id) #finds the whiskey object from the above result
            
        print("result")
        print(result)
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
    class Meta:
        model = Whiskey
        fields = ('id', 'title', 'list_img_url', 'region', 'price')
        depth = 1
        