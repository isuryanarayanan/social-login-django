from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class GoogleOAuthSerializer(serializers.Serializer):
    oauth_token = serializers.CharField(max_length=550)

    username = serializers.CharField(max_length=250, read_only=True)
    email = serializers.CharField(max_length=550, read_only=True)
    provider = serializers.CharField(
        max_length=250, read_only=True, default="google")

    def validate(self, data):
        # Validate oauth_token with google and try and get the details of the user
        username = "usernamE"
        email = "emaiL"
        return {
            'username': username,
            'email': email,
            'provider': data.get('provider')
        }


class GoogleOAuthView(APIView):
    """ Google social authenticaion api """

    permission_classes = ()

    response = None
    response_code = None

    def post(self, request):
        """ post request handler which accepts a token """
        serializer = GoogleOAuthSerializer(data=request.data)
        if serializer.is_valid():

            # If user email exists as an account authenticate the user and return tokens

            # else if user does not exist create an account and then return token

            self.response = serializer.data
            self.response_code = 200
        else:
            self.response = serializer.errors
            self.response_code = 400

        return Response(self.response, self.response_code)
