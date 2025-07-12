# detection_app/urls.py

from django.urls import path
from . import views # Import your views from the current app

urlpatterns = [
    path('', views.home, name='home'), # Maps the root URL of the app to the home view (your index.html)
    path('quiz/', views.quiz, name='quiz'), # Maps /quiz/ to the quiz view
    path('results/', views.results, name='results'), # URL for results page
    path('upload-assessment/', views.upload_assessment, name='upload_assessment'), # URL for upload page
    path('thank-you/', views.thank_you, name='thank_you'), # URL for thank you page
    path('register/', views.register_view, name='register'), # URL for registration page
    path('login/', views.login_view, name='login'), # URL for login page
    path('logout/', views.logout_view, name='logout'), # URL for logout
    path('demo-video/', views.demo_video_view, name='demo_video'), # URL for demo video page
]