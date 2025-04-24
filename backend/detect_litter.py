import argparse
from ultralytics import YOLO
import os

def detect_litter(source, output):
    model = YOLO("ml_model/yolov8s.pt")

    results = model(source, save=True, project=os.path.dirname(output), name=os.path.basename(output))
    
    if os.path.isdir(results[0].save_dir):
        saved_file = list(results[0].save_dir.glob("*"))[0]
        os.rename(saved_file, output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, required=True, help='Path to input image/video')
    parser.add_argument('--output', type=str, required=True, help='Path to save processed media')
    args = parser.parse_args()

    detect_litter(args.source, args.output)
