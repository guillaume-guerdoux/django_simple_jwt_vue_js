from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework import generics, permissions

from .models import Movie
from .serializers import UserSerializer, MovieSerializer

class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MovieList(generics.ListAPIView):
    """List and create movies """
    queryset = Movie.objects.all().order_by('name')
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )

class MovieCreate(generics.CreateAPIView):
    """List and create movies """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )


class MovieRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """Retrieve and update a movie"""
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated, )
