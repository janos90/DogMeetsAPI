from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest.views import Index, dog_list, dog_details, DogViewSet

# from rest.views import DogList, DogDetails

router = DefaultRouter()
router.register('dogs', DogViewSet, basename='dogs')
urlpatterns = [
    path('', Index),
    path('dog/', dog_list),
    path('dog/<int:pk>', dog_details),

    # path('dog/', DogList.as_view())
    # path('dog/<int:pk>', DogDetails.as_view())

    path('api/', include(router.urls))
]