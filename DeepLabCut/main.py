from config import (
    PROJECT_NAME, USER_NAME, DATE, WORKING_DIR, VIDEO_FOLDER,
    DO_TRAIN, DO_TEST, DO_PREPROCESS,
    CROP_LEFT, CROP_RIGHT, CROP_TOP, CROP_BOTTOM
)
from utils import get_video_files
from preprocess import batch_cut_videos
from train import train_model
from test import analyze_videos
import os

if __name__ == "__main__":
    project_folder = f"{PROJECT_NAME}-{USER_NAME}-{DATE}"
    project_path = os.path.join(WORKING_DIR, project_folder)
    config_path = os.path.join(project_path, 'config.yaml')

    video_dir = os.path.join(WORKING_DIR, VIDEO_FOLDER)

    if DO_PREPROCESS:
        print("\n--- Preprocessing Videos (Cropping) ---")
        batch_cut_videos(
            video_dir,
            suffix='_cut',
            crop_left=CROP_LEFT,
            crop_right=CROP_RIGHT,
            crop_top=CROP_TOP,
            crop_bottom=CROP_BOTTOM
        )
        print("Preprocessing completed.\n")
        video_files = get_video_files(video_dir, extension='_cut.mp4')
    else:
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
