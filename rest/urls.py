from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest.views import Index, DogViewSet, UserViewSet, ProfileViewSet, ActivityViewSet

# from rest.views import DogList, DogDetails

router = DefaultRouter()
router.register('dogs', DogViewSet, basename='dogs')
router.register('users', UserViewSet)
router.register('owners', ProfileViewSet, basename='owners')
router.register('activities', ActivityViewSet, basename='activities')

urlpatterns = [
    path('', Index),
    path('api/', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)