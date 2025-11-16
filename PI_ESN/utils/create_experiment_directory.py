import os
from datetime import datetime


def create_output_directory(base_name="PI_ESN_", root_path="./experiments"):
    """
    Dynamically creates a directory to store artifacts.

    - base_name: base name of the folder
    - root_path: location where the folder will be created
    - Returns the full path of the created folder
    """

    # Timestamp to avoid overwriting previous folders
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    folder_name = f"{base_name}_{timestamp}"
    full_path = os.path.join(root_path, folder_name)

    os.makedirs(full_path, exist_ok=True)

    print(f"Directory created at: {full_path}")
    return full_path
