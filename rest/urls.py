from django.urls import path
from rest_framework.routers import DefaultRouter

from rest.views import Index, dog_list, dog_details

router = DefaultRouter()

urlpatterns = [
    path('', Index),
    path('dog/', dog_list),
    path('dog/<int:pk>', dog_details)
]