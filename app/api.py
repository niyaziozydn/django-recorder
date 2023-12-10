from rest_framework import viewsets
from app.models import Recording
from app.serializer import RecordingSerializer

from django.core.files.base import ContentFile
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView

class RecordingViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

    @parser_classes([FileUploadParser])
    def create(self, request, *args, **kwargs):
        video_blob = request.data.get('video')
        camera_blob = request.data.get('camera', None)

        video_file = ContentFile(video_blob.read(), name="video.mp4") if video_blob else None
        camera_file = ContentFile(camera_blob.read(), name="camera.mp4") if camera_blob else None

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(video=video_file, camera=camera_file)

        return Response(serializer.data)