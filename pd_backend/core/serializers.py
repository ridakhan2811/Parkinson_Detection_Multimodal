from rest_framework import serializers
from .models import SpeechSample
from .models import SpeechSample, PostureSample, HandwritingSample

class SpeechSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeechSample
        fields = '__all__'

from .models import HandwritingSample
class HandwritingSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HandwritingSample
        fields = '__all__'

class PostureSampleSerializer(serializers.ModelSerializer):  
    class Meta:
        model = PostureSample
        fields = '__all__'