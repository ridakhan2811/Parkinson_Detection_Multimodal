from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings 

class User(AbstractUser):
    is_researcher = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
    )


class SpeechSample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='speech/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class HandwritingSample(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='handwriting/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    prediction = models.CharField(max_length=50, null=True, blank=True)

class PostureSample(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image_file = models.ImageField(upload_to='posture/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    prediction = models.CharField(max_length=50, null=True, blank=True)
