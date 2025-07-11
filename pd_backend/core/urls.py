from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpeechSampleViewSet
from .views import upload_speech,upload_posture
from .views import HandwritingSampleViewSet
 
router = DefaultRouter()
router.register('speech', SpeechSampleViewSet)
router.register('images', HandwritingSampleViewSet)

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import home, upload_speech, upload_image

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_speech, name='upload'),
    path('upload-image/', upload_image, name='upload_image'),
    path('upload/posture/', upload_posture, name='upload_posture')
]
