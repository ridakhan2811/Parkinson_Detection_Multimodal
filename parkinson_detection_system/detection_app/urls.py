from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('quiz/', views.quiz, name='quiz'),  # Quiz form page
    path('results/', views.results, name='results'),  # (Optional) results with full symptom+analysis output
    path('upload-assessment/', views.upload_assessment, name='upload_assessment'),  # Handles quiz + prediction logic
    path('thank-you/', views.thank_you, name='thank_you'),  # Thank you page after quiz
    path('register/', views.register_view, name='register'),  # Register
    path('login/', views.login_view, name='login'),  # Login
    path('logout/', views.logout_view, name='logout'),  # Logout
    path('demo-video/', views.demo_video_view, name='demo_video'),  # Demo video
]
