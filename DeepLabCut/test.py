# test.py

import deeplabcut

def analyze_videos(config_path, video_files, shuffle=1):
    deeplabcut.analyze_videos(config_path, video_files, shuffle=shuffle, save_as_csv=True)
    deeplabcut.create_labeled_video(config_path, video_files, shuffle=shuffle)
    deeplabcut.plot_trajectories(config_path, video_files, shuffle=shuffle)
    deeplabcut.extract_outlier_frames(config_path, video_files, shuffle=shuffle)
