from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest.models import Dog, Profile, Activity
from rest.permissions import IsOwnerOrReadOnly, UserPermission
from rest.serializers import DogSerializer, UserSerializer, ActivitySerializer, ProfileSerializer


def Index(request):
    return HttpResponse("This is the index for an API")


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
    authentication_classes = (TokenAuthentication,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication,)


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    authentication_classes = (TokenAuthentication,)
