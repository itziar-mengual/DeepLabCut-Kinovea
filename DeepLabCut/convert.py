# convert.py

import os
import pandas as pd

def convert_h5_to_csv(file_path: str) -> None:
    """
    Converts a single .h5 file to .csv.

    Args:
        file_path (str): Path to the .h5 file.
    """
    try:
        df = pd.read_hdf(file_path)
        csv_file_path = file_path.replace('.h5', '.csv')
        df.to_csv(csv_file_path, index=False)
        print(f"Converted {file_path} to {csv_file_path}")
    except Exception as e:
        print(f"Failed to convert {file_path}: {e}")


def batch_convert_h5_to_csv(directory: str) -> None:
    """
    Converts all .h5 files in a directory (recursively) to .csv.

    Args:
        directory (str): Directory to search for .h5 files.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.h5'):
                file_path = os.path.join(root, file)
                convert_h5_to_csv(file_path)
