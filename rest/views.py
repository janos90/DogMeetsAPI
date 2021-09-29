from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest.models import Dog
from rest.serializers import DogSerializer


def Index(request):
    return HttpResponse("Hello World")


@csrf_exempt
def dog_list(request):
    if request.method == 'GET':
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def dog_details(request, pk):
    try:
        dog = Dog.objects.get(pk=pk)
    except Dog.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DogSerializer(dog)
        return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        dog.delete()
        return HttpResponse(status=204)
