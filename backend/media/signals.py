from django.db.models.signals import post_save
from django.dispatch import receiver
from.models import MediaFile
import os
import subprocess


@receiver(post_save, sender=MediaFile)
def run_yolo_on_media(sender, instance, created, **kwargs):
    if created:
        input_path = instance.image.path if instance.image else instance.video.path
        output_path = input_path.replace("uploads", "outputs/processed")
        
        subprocess.run([
            "python",
            "path_to_yolo_script.py",
            "--source", input_path,
            "--output", output_path
        ])
        
        instance.processed_file.name = output_path.replace("backend/", "")
        instance.save()