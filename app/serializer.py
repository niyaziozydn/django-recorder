from rest_framework import serializers

from app.models import Recording




class RecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recording
        fields = '__all__'
