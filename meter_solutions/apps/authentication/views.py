import json

from django.core import serializers
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.authentication.user_serializer import RegistrationSerializer

from apps.authentication.user_serializer import LoginSerializer

from apps.authentication.user_serializer import UserSerializer

from apps.authentication.models import User


class RegistrationAPIView(APIView):
    """
    Registers a new user.
    """
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer

    def post(self, request):
        """
        Creates a new User object.
        Username, email, and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'token': serializer.data.get('token', None),
            },
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(APIView):
    """
    Logs in an existing user.
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        """
        Checks is user exists.
        Email and password are required.
        Returns a JSON web token.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserAPIView(APIView):
    """
    Returns in an existing user.
    """

    def post(self, request):
        mail = request.data.get('email', False)
        usr = User.objects.filter(email=mail)
        usr_values = list(usr.values())
        user_result = {
            'id': usr_values[0].get('id'),
            'email': usr_values[0].get('email'),
            'username': usr_values[0].get('username'),
            'groups': usr_values[0].get('groups')
        }
        return Response(user_result, status=status.HTTP_200_OK)