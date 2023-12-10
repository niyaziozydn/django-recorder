from django.contrib import admin

from app.models import Recording
class RecordingAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_size', 'camera_size', 'created_at')

    def video_size(self, obj):
        if obj.video:
            return f"{obj.video.size / 1024:.2f} KB"
        return "No File"

    video_size.short_description = 'Video Size (KB)'

    def camera_size(self, obj):
        if obj.camera:
            return f"{obj.camera.size / 1024:.2f} KB"
        return "No File"

    camera_size.short_description = 'Camera Size (KB)'

admin.site.register(Recording, RecordingAdmin)
