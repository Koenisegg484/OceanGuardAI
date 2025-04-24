import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';

interface UploadResponse {
  id: number;
  video: string | null;
  image: string | null;
  processed_file: string | null;
  uploaded_at: string;
}

@Component({
  selector: 'app-upload',
  templateUrl: './upload.component.html',
  styleUrls: ['./upload.component.css'],
  standalone: true,
  imports: [CommonModule, HttpClientModule]
})
export class UploadComponent {
  selectedFile!: File;
  processedUrl: string | null = null;
  isImage: boolean = true;
  isUploading: boolean = false;
  uploadError: string | null = null;

  finalProcessedUrl: string | null = null;

  constructor(private http: HttpClient) {}

  onFileSelected(event: Event) {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (file) {
      this.selectedFile = file;
      const reader = new FileReader();
      reader.onload = () => {
        this.processedUrl = reader.result as string;
        this.isImage = file.type.startsWith('image');
      };
      reader.readAsDataURL(file);
    }
  }

  uploadImage() {
    if (!this.selectedFile) {
      alert("No file selected!");
      return;
    }

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    if (this.isImage) {
      formData.append('image', this.selectedFile);
    } else {
      formData.append('video', this.selectedFile);
    }

    this.isUploading = true;
    this.uploadError = null;

    this.http.post<UploadResponse>('http://127.0.0.1:8000/api/media/', formData).subscribe({
      next: (res) => {
        console.log('Upload success', res);
        this.isUploading = false;
        
        this.finalProcessedUrl = res.processed_file;
      },
      error: (err) => {
        console.error('Upload failed', err);
        this.isUploading = false;
        this.uploadError = 'Upload failed. Please try again.';
      }
    });

  }
}