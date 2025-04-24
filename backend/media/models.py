from django.db import models

class MediaFile(models.Model):
    video = models.FileField(upload_to="uploads/videos/", null=True, blank=True)
    image = models.FileField(upload_to="uploads/images/", null=True, blank=True)
    processed_file = models.FileField(upload_to="outputs/processed/",    null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Media File {self.id} - {self.uploaded_at}"
