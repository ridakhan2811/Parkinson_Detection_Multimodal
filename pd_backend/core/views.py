from rest_framework import viewsets
from .serializers import SpeechSampleSerializer
from django.shortcuts import render
from .models import SpeechSample,PostureSample,HandwritingSample
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .tasks import analyze_image
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .serializers import (
    SpeechSampleSerializer,
    PostureSampleSerializer,
    HandwritingSampleSerializer,
)
def home(request):
    return render(request, 'core/home.html')

@login_required
def upload_speech(request):
    return render(request, 'core/upload.html')

@login_required
def upload_image(request):
    return render(request, 'core/upload_image.html')

@login_required
def upload_speech(request):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        SpeechSample.objects.create(user=request.user, audio_file=request.FILES['audio_file'])
        return render(request, 'upload.html', {
            'message': 'Upload successful!',
            'samples': SpeechSample.objects.filter(user=request.user)
        })

    samples = SpeechSample.objects.filter(user=request.user)
    return render(request, 'core/upload.html', {'samples': samples})

@login_required
def upload_posture(request):
    if request.method == 'POST' and request.FILES.get('image_file'):
        PostureSample.objects.create(user=request.user, image_file=request.FILES['image_file'])
    samples = PostureSample.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'core/upload_posture.html', {'samples': samples})

class SpeechSampleViewSet(viewsets.ModelViewSet):
    queryset = SpeechSample.objects.all()
    serializer_class = SpeechSampleSerializer

class PostureSampleViewSet(viewsets.ModelViewSet):
    queryset = PostureSample.objects.all()
    serializer_class = PostureSampleSerializer

class HandwritingSampleViewSet(viewsets.ModelViewSet): 
    queryset = HandwritingSample.objects.all()
    serializer_class = HandwritingSampleSerializer

@login_required
def upload_handwriting(request):
    if request.method == 'POST' and request.FILES.get('image_file'):
        HandwritingSample.objects.create(user=request.user, image_file=request.FILES['image_file'])
    samples = HandwritingSample.objects.filter(user=request.user).order_by('-uploaded_at')
    return render(request, 'core/upload_handwriting.html', {'samples': samples})
