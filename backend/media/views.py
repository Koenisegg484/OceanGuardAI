import uuid
import os
from rest_framework import viewsets
from rest_framework.response import Response
from django.conf import settings
from django.http import Http404, FileResponse
from .models import MediaFile
from .serializers import MediaFileSerializer
from ml_model.detect_litter import detect_litter


ALLOWED_FILE_TYPES = ['image/jpeg', 'image/png', 'video/mp4']
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB limit


def get_processed_file(request, filename):
    file_path = os.path.join(settings.BASE_DIR, 'outputs', 'processed', filename)
    if not os.path.exists(file_path):
        raise Http404("Processed file not found.")
    return FileResponse(open(file_path, 'rb'), content_type='image/jpeg')


class MediaFileViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        # Check if either video or image exists
        input_file = instance.video or instance.image
        if not input_file:
            return

        input_path = input_file.path  # Get the full file path
        filename = os.path.basename(input_path)
        name, ext = os.path.splitext(filename)

        # Define the custom output directory
        output_dir = os.path.join(settings.BASE_DIR, 'outputs', 'processed')
        os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

        # Create a unique filename to avoid collisions
        output_filename = f"{name}_{uuid.uuid4().hex[:8]}_processed{ext}"
        output_path = os.path.join(output_dir, output_filename)

        # Run the litter detection model
        detect_litter(input_path, output_path)

        # Save the relative path of the processed file to the database
        instance.processed_file.name = os.path.relpath(output_path, settings.MEDIA_ROOT)
        instance.save()

        # Optionally, return a response with the processed file URL or some other data
        return instance  # You can customize the return as needed
