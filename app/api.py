from rest_framework import viewsets
from app.models import Recording
from app.serializer import RecordingSerializer

from django.core.files.base import ContentFile
from rest_framework.response import Response
from rest_framework.decorators import parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
import ffmpeg

class RecordingViewSet(viewsets.ModelViewSet):
    queryset = Recording.objects.all()
    serializer_class = RecordingSerializer

    @parser_classes([FileUploadParser])
    def create(self, request, *args, **kwargs):
        video_blob = request.data.get('video')
        camera_blob = request.data.get('camera', None)

        video_file = ContentFile(video_blob.read(), name="video.mp4") if video_blob else None
        camera_file = ContentFile(camera_blob.read(), name="camera.mp4") if camera_blob else None

        if video_file:
            input_file_path = video_file.temporary_file_path()
            output_file_path = 'squeezed_video.mp4'  
            ffmpeg.input(input_file_path).output(output_file_path, crf=23).run(overwrite_output=True)

            with open(output_file_path, 'rb') as squeezed_video_file:
                video_file = ContentFile(squeezed_video_file.read(), name="squeezed_video.mp4")

        if camera_file:
            input_file_path = camera_file.temporary_file_path()
            output_file_path = 'squeezed_camera.mp4'  
            ffmpeg.input(input_file_path).output(output_file_path, crf=23).run(overwrite_output=True)

            with open(output_file_path, 'rb') as squeezed_camera_file:
                camera_file = ContentFile(squeezed_camera_file.read(), name="squeezed_camera.mp4")

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(video=video_file, camera=camera_file)

        return Response(serializer.data)
