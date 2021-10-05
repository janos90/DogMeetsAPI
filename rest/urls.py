from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest.views import Index, DogViewSet, UserViewSet, OwnerViewSet, ActivityViewSet

# from rest.views import DogList, DogDetails

router = DefaultRouter()
router.register('dogs', DogViewSet, basename='dogs')
router.register('users', UserViewSet)
router.register('owners', OwnerViewSet, basename='owners')
router.register('activities', ActivityViewSet, basename='events')

urlpatterns = [
    path('', Index),
    path('api/', include(router.urls))
]