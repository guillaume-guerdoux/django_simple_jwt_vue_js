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

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        is_active = validated_data.pop('is_active', True)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class MovieSerializer(serializers.ModelSerializer):
    """ A serializer for the Movie Model """
    class Meta:
        model = Movie
        fields = ('id', 'name', 'stars', 'description', 'created')
