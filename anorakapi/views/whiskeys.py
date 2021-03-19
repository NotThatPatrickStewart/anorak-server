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

        # Support filtering whiskeys by type
        #    http://localhost:8000/whiskeys?type=1
        #
        # That URL will retrieve all tabletop whiskeys
        whiskey_type = self.request.query_params.get('type', None)
        if whiskey_type is not None:
            whiskeys = whiskeys.filter(whiskeytype__id=whiskey_type)

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
        fields = ('id', 'title', 'list_img_url', 'region', 'price', 'whiskey_type')
        depth = 1
        