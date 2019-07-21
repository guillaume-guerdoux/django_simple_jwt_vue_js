from django.contrib.auth.models import User

from rest_framework import serializers

from .models import  Movie

class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        # Specify the model we are using
        model = User
        # Specify the fields that should be made accessible.
        # Mostly it is all fields in that model
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')

class MovieSerializer(serializers.ModelSerializer):
    """ A serializer for the Movie Model """
    class Meta:
        model = Movie
        fields = ('id', 'name', 'stars', 'description', 'created')
