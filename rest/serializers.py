from rest_framework import serializers
from .models import Dog, Owner, Activity


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'name', 'breed', 'height', 'weight', 'birthday', 'anniversary', 'owner', 'image']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = ['id', 'user', 'image', 'phone', 'bio']


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'participants', 'dogs', 'location', 'startTime']
