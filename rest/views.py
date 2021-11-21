from django.contrib.auth.models import User
from django.shortcuts import HttpResponse
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response

from rest.models import Dog, Profile, Activity
from rest.permissions import IsOwnerOrReadOnly, UserPermission
from rest.serializers import DogSerializer, UserSerializer, ActivitySerializer, ProfileSerializer


def Index(request):
    return HttpResponse("This is the index for an API")

class getUser(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # authentication_classes = (TokenAuthentication,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (UserPermission,)
    # authentication_classes = (TokenAuthentication,)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # authentication_classes = (TokenAuthentication,)


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # authentication_classes = (TokenAuthentication,)


class attendEvent(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def patch(self, request):
        userid = request.data["user_id"]
        activityid = request.data["post_id"]
        user = User.objects.get(id=userid)
        activity = Activity.objects.get(id=activityid)
        if (activity.participants.add(user)):
            # send_mail(
            #     'Subject here',
            #     'Here is the message.',
            #     'songl08@wairaka.com',
            #     ['gabriel_sl19798@hotmail.com'],
            #     fail_silently=False,
            # )
            activity.save()

            return Response(status=HTTP_200_OK)

        return Response(status=HTTP_400_BAD_REQUEST)

class disAttendEvent(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def patch(self, request):
        userid = request.data["user_id"]
        activityid = request.data["post_id"]
        user = User.objects.get(id=userid)
        activity = Activity.objects.get(id=activityid)
        if (activity.participants.remove(user)):
            # send_mail(
            #     'Subject here',
            #     'Here is the message.',
            #     'songl08@wairaka.com',
            #     ['gabriel_sl19798@hotmail.com'],
            #     fail_silently=False,
            # )
            activity.save()

            return Response(status=HTTP_200_OK)

        return Response(status=HTTP_400_BAD_REQUEST)

