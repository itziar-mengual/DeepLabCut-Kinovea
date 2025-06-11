# utils.py

import os

def get_video_files(directory, extension='.mp4'):
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
