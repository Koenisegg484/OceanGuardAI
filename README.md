
# OceanGuardAI

OceanGuardAI is an AI-powered application designed to detect litter and waste from images and videos. It allows users to upload media files (images or videos), which are processed using a YOLO (You Only Look Once) model to detect litter in the uploaded content.

This project consists of a backend built using Django for the API and a frontend built using Angular for user interaction. It includes features like uploading images/videos, processing them with AI models, and displaying processed results.

---

## Features

- **Upload Image/Video**: Upload media files through the frontend.
- **Litter Detection**: Process images/videos using a YOLO model for litter detection.
- **Processed Output**: Displays the processed image/video with detected litter and relevant information.
- **Easy Setup**: Simple steps to set up the project locally.

---

## Tech Stack

- **Backend**: Django, Python
- **Frontend**: Angular
- **Machine Learning**: YOLO (Pretrained model for object detection)
- **Database**: SQLite (for local development)
- **Hosting**: Localhost for testing and development

---

## Prerequisites

Before you begin, ensure you have the following installed:

1. **Python**: Version 3.8 or higher
2. **Node.js**: Version 16 or higher
3. **Django**: Version 5.x
4. **Angular CLI**: Version 12 or higher
5. **YOLO Model**: A pretrained YOLO model file (e.g., `yolov3.weights` or similar)

---

## Setup

### 1. Backend Setup (Django)

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/OceanGuardAI.git
   cd OceanGuardAI/backend
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The backend API should now be running at `http://127.0.0.1:8000/`.


### 2. Frontend Setup (Angular)

1. Navigate to the `frontend` directory:

   ```bash
   cd ../frontend
   ```

2. Install the required Node.js dependencies:

   ```bash
   npm install
   ```

3. Start the Angular development server:

   ```bash
   ng serve
   ```

   The frontend should now be running at `http://localhost:4200/`.


### 3. YOLO Model Setup

1. Download the correct YOLO model weights and configuration file (e.g., `yolov3.weights` and `yolov3.cfg`).
2. Place these files in the appropriate directory within the backend (e.g., inside the `ml_model` folder).
3. Ensure the correct file path is referenced in the backend code.

---

## Usage

1. Navigate to the frontend URL (`http://localhost:4200/`).
2. Upload an image or video by clicking the "Upload Image or Video" button.
3. Wait for the file to be processed. The processed image or video with detected litter will appear as the processed output.

---

## Contributing

Feel free to fork this repository and contribute by creating pull requests. Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-name`)
6. Create a new pull request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

If you have any questions, feel free to contact me at [shivamc86@gmail.com](mailto:shivamc86@gmail.com).
