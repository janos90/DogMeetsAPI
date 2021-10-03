from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import Dog
from rest.serializers import DogSerializer


def Index(request):
    return HttpResponse("Hello World")


@api_view(['GET', 'POST'])
def dog_list(request):
    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def dog_details(request, pk):
    try:
        dog = Dog.objects.get(pk=pk)
    except Dog.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DogSerializer(dog)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        dog.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


# class DogList(APIView):
#     def get(self, request):
#         dogs = Dog.objects.all()
#         serializer = DogSerializer(dogs, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = DogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DogDetails(APIView):
#     def get_object(self, id):
#         try:
#             return Dog.objects.get(id=id)
#         except Dog.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, id):
#         dog = self.get_object(id)
#         serializer = DogSerializer(dog)
#         return Response(serializer.data)
#
#     def put(self, request, id):
#         dog = self.get_object(id)
#         serializer = DogSerializer(dog, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         dog = self.get_object(id)
#         dog.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class DogList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class DogDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)


class DogViewSet(viewsets.ViewSet):

    def list(self, request):
        Dogs = Dog.objects.all()
        serializer = DogSerializer(Dogs, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Dog.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = DogSerializer(article)
        return Response(serializer.data)

    def update(self, request, pk=None):
        dog = Dog.objects.get(pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        dog = Dog.objects.get(pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DogViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
