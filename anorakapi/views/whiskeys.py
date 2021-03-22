"""View module for handling requests about whiskeys"""
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from anorakapi.models import Whiskey

class Whiskeys(ViewSet):

    def list(self, request):
        """Handle GET requests to whiskeys resource

        Returns:
            Response -- JSON serialized list of whiskeys
        """
        # Get all whiskey records from the database
        whiskeys = Whiskey.objects.all()

        serializer = WhiskeySerializer(
            whiskeys, many=True, context={'request': request})
        return Response(serializer.data)


class WhiskeySerializer(serializers.ModelSerializer):
    """JSON serializer for whiskeys

    Arguments:
        serializer type
    """
    class Meta:
        model = Whiskey
        fields = ('id', 'title', 'list_img_url', 'region', 'price')
        depth = 1
        