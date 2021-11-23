from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from rest.views import Index, DogViewSet, UserViewSet, ProfileViewSet, ActivityViewSet, getUser, attendEvent, \
    disAttendEvent

# from rest.views import DogList, DogDetails

router = DefaultRouter()
router.register('dogs', DogViewSet, basename='dogs')
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet, basename='profiles')
router.register('activities', ActivityViewSet, basename='activities')

urlpatterns = [
    path('', Index),
    path('api/', include(router.urls)),
    path('api/getuser/', getUser.as_view()),
    path('api/attendevent/', attendEvent.as_view()),
    path('api/disattendevent/', disAttendEvent.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/password/reset/confirm/<slug:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)