# main.py

from config import PROJECT_NAME, USER_NAME, DATE, WORKING_DIR, VIDEO_FOLDER, DO_TRAIN, DO_TEST
from utils import get_video_files
from train import train_model
from test import analyze_videos
import os

if __name__ == "__main__":
    project_folder = f"{PROJECT_NAME}-{USER_NAME}-{DATE}"
    project_path = os.path.join(WORKING_DIR, project_folder)
    config_path = os.path.join(project_path, 'config.yaml')

    video_dir = os.path.join(WORKING_DIR, VIDEO_FOLDER)
    video_files = get_video_files(video_dir)

    print("\n--- Videos to process ---")
    for vf in video_files:
        print(vf)

    if DO_TRAIN:
        print("\n--- Training Model ---")
        train_model(config_path)
        print("Training completed.")

    if DO_TEST:
        print("\n--- Analyzing Videos ---")
        analyze_videos(config_path, video_files)
        print("Analysis completed.")