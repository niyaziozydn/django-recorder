from django.db import models

class Recording(models.Model):
    title = models.CharField(max_length=100,blank=True,null=True)
    video = models.FileField(upload_to='recordings/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    camera = models.FileField(upload_to='camera/', blank=True, null=True)

    def __str__(self):
        return str(self.created_at)
    