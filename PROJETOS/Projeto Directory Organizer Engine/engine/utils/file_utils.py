from pathlib import Path
import os

def get_unique_path(path: Path) -> Path:
    """
    Returns a unique path by adding a suffix (1), (2), etc. if the file already exists.
    """
    if not path.exists():
        return path

    parent = path.parent
    stem = path.stem
    extension = path.suffix
    
    counter = 1
    while True:
        new_name = f"{stem} ({counter}){extension}"
        new_path = parent / new_name
        if not new_path.exists():
            return new_path
        counter += 1

def categorize_file(extension: str, categories: dict, default: str) -> str:
    """
    Returns the category name based on the file extension.
    """
    ext_lower = extension.lower()
    for category, extensions in categories.items():
        if ext_lower in extensions:
            return category
    return default
