# preprocess.py

import os
from moviepy.editor import VideoFileClip

def cut_video_laterals(input_path: str, output_path: str,
                        crop_left: int = 500,
                        crop_right: int = 500,
                        crop_top: int = 50,
                        crop_bottom: int = 135) -> None:
    """
    Cuts lateral and vertical margins from a video and saves the output.

    Args:
        input_path (str): Path to the input video file.
        output_path (str): Path to save the cropped output video.
        crop_left (int): Pixels to crop from the left.
        crop_right (int): Pixels to crop from the right.
        crop_top (int): Pixels to crop from the top.
        crop_bottom (int): Pixels to crop from the bottom.
    """

    with VideoFileClip(input_path) as video:
        new_width = video.size[0] - (crop_left + crop_right)
        new_height = video.size[1] - (crop_top + crop_bottom)

        crop_region = (
            crop_left,
            crop_top,
            crop_left + new_width,
            crop_top + new_height
        )

        cropped_video = video.crop(
            x1=crop_region[0],
            y1=crop_region[1],
            x2=crop_region[2],
            y2=crop_region[3]
        )

        muted_video = cropped_video.without_audio()

        muted_video.write_videofile(output_path, codec="libx264", audio_codec='aac')


def batch_cut_videos(directory: str,
                      suffix: str = "_cut",
                      extension: str = ".mp4",
                      crop_left: int = 500,
                      crop_right: int = 500,
                      crop_top: int = 50,
                      crop_bottom: int = 135) -> None:
    """
    Applies cut_video_laterals to all videos in a directory.

    Args:
        directory (str): Root directory to search for videos.
        suffix (str): Suffix to add to the output filenames.
        extension (str): Video file extension.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                input_path = os.path.join(root, file)
                output_path = os.path.join(
                    root, file.replace(extension, f'{suffix}{extension}')
                )
                print(f"Processing: {input_path}")
                cut_video_laterals(
                    input_path, output_path,
                    crop_left, crop_right, crop_top, crop_bottom
                )
