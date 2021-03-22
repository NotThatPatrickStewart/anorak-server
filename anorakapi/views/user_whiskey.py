"""View module for handling requests about user_whiskeys"""
from anorakapi.models.whiskey import Whiskey
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from anorakapi.models import UserWhiskey, Whiskey

class UserWhiskeys(ViewSet):

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized user_whiskey instance
        """

        # Create a new Python instance of the UserWhiskey class
        # and set its properties from what was sent in the
        # body of the request from the client.
        
        user_whiskey = UserWhiskey()
        user_whiskey.user = request.auth.user
        user_whiskey.title = request.data["title"]
        user_whiskey.list_img_url = request.data["list_img_url"]
        user_whiskey.notes = request.data["notes"]
        user_whiskey.rating = request.data["rating"]

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed in the body of the request.
        whiskey = Whiskey.objects.get(pk=request.data["whiskey_id"])
        user_whiskey.whiskey = whiskey

        # Try to save the new user_whiskey to the database, then
        # serialize the user_whiskey instance as JSON, and send the
        # JSON as a response to the client request
        try:
            user_whiskey.save()
            serializer = UserWhiskeySerializer(user_whiskey, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    def retrieve(self, request, pk=None):
        """Handle GET requests for single user_whiskey

        Returns:
            Response -- JSON serialized user_whiskey instance
        """
        try:
            # `pk` is a parameter to this function, and
            # Django parses it from the URL route parameter
            #   http://localhost:8000/user_whiskeys/2
            #
            # The `2` at the end of the route becomes `pk`
            user_whiskey = UserWhiskey.objects.get(pk=pk)
            serializer = UserWhiskeySerializer(user_whiskey, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"reason": ex.message}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Handle PUT requests for a user_whiskey

        Returns:
            Response -- Empty body with 204 status code
        """
        # Do mostly the same thing as POST, but instead of
        # creating a new instance of UserWhiskey, get the user_whiskey record
        # from the database whose primary key is `pk`

        user_whiskey = UserWhiskey.objects.get(pk=pk)
        # user_whiskey = UserWhiskey.objects.get(user = request.auth.user)
        user_whiskey.user = request.auth.user
        user_whiskey.title = request.data["title"]
        user_whiskey.list_img_url = request.data["list_img_url"]
        user_whiskey.notes = request.data["notes"]
        user_whiskey.rating = request.data["rating"]

        whiskey = Whiskey.objects.get(pk=request.data["whiskey_id"])
        user_whiskey.whiskey = whiskey
        user_whiskey.save()

        # 204 status code means everything worked but the
        # server is not sending back any data in the response
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single user_whiskey

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            user_whiskey = UserWhiskey.objects.get(pk=pk)
            user_whiskey.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except UserWhiskey.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to user_whiskeys resource

        Returns:
            Response -- JSON serialized list of user_whiskeys
        """
        # Get all user_whiskey records from the database
        user_whiskeys = UserWhiskey.objects.all()

        serializer = UserWhiskeySerializer(user_whiskeys, many=True, context={'request': request})
        return Response(serializer.data)


class UserWhiskeySerializer(serializers.ModelSerializer):
    """JSON serializer for user_whiskeys"""
    class Meta:
        model = UserWhiskey
        fields = ('id', 'title', 'list_img_url', 'notes', 'rating')
        depth = 1
        