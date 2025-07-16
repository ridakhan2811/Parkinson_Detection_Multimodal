from django.urls import path
from . import views
from .views import history_view

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('results/', views.results, name='results'),
    path('upload-assessment/', views.upload_assessment, name='upload_assessment'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('demo-video/', views.demo_video_view, name='demo_video'),
    path('spiral-detection/', views.spiral_detection, name='spiral_detection'),
    path('history/', views.history_view, name='history'),
    path('history/', history_view, name='assessment_history'),
    path('combined-detection/', views.combined_detection, name='combined_detection'),

    # ✅ New Voice Upload path
    path('voice-upload/', views.voice_upload_view, name='voice_upload'),

    # ✅ New Posture Video Upload path
    path('posture-upload/', views.posture_video_upload_view, name='posture_video_upload'),
]
