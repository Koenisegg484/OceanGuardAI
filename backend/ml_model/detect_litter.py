import argparse
from ultralytics import YOLO
import os
from pathlib import Path

def detect_litter(source, output):
    model = YOLO(str(Path(__file__).resolve().parent / "yolov8s.pt"))

    results = model(source, save=True, project=Path(output).parent, name=Path(output).stem)

    result_dir = Path(output).parent / Path(output).stem
    saved_files = list(result_dir.glob("*"))
    if saved_files:
        saved_files[0].rename(output)
        result_dir.rmdir()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, required=True, help='Path to input image/video')
    parser.add_argument('--output', type=str, required=True, help='Path to save processed media')
    args = parser.parse_args()

    detect_litter(args.source, args.output)
