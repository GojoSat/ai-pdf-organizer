"""
AI Office Tool — File Organizer (demo)
Author: Wick Chen
License: MIT

Simple demo script: organizes files in a folder into subfolders by file extension.
Usage:
    python file_organizer.py /path/to/your/folder
"""

import os
import shutil
import sys

def organize_by_extension(folder):
    folder = os.path.abspath(folder)
    if not os.path.isdir(folder):
        print("Folder does not exist:", folder)
        return
    for fname in os.listdir(folder):
        fpath = os.path.join(folder, fname)
        if os.path.isfile(fpath):
            ext = os.path.splitext(fname)[1].lower().strip('.')
            if not ext:
                ext = 'no_ext'
            target_dir = os.path.join(folder, ext)
            os.makedirs(target_dir, exist_ok=True)
            shutil.move(fpath, os.path.join(target_dir, fname))
    print("Organization complete. Check subfolders in:", folder)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide folder path. Example: python file_organizer.py ./test_files")
    else:
        organize_by_extension(sys.argv[1])
