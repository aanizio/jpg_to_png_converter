import sys
import os
from PIL import Image

def is_jpg_file(filename):
    return filename.endswith(".jpg") or filename.endswith(".jpeg")

def jpg_to_png_path(filename, source_folder, destination_folder):
    source_filepath = os.path.join(source_folder, filename)
    no_ext_filename = os.path.splitext(filename)[0]
    png_filename = no_ext_filename + ".png"
    dest_filepath = os.path.join(destination_folder, png_filename)
    return (source_filepath, dest_filepath)

def save_image(source_path, destination_path):
    im = Image.open(source_path)
    im.save(destination_path)

def create_dir_if_not_exists(path):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

def save_jpg_file_to_png(filename, source_folder, destination_folder):
    SOURCE_IDX, DEST_IDX = (0, 1)
    filepaths = jpg_to_png_path(file, source_folder, destination_folder)
    print(f"Converting {file}")
    save_image(filepaths[SOURCE_IDX], filepaths[DEST_IDX])

def convert_folder_jpg_to_png(source_folder, destination_folder):
    create_dir_if_not_exists(destination_folder)
    for file in os.listdir(source_folder):
        if not is_jpg_file(file):
            continue
    save_jpg_file_to_png(file, source_folder, destination_folder)

def main():
    REQUIRED_LEN_ARGS = 3
    SOURCE_ARG = 1
    DEST_ARG = 2

    print("JPG to PNG Converter")

    if len(sys.argv) != REQUIRED_LEN_ARGS:
        print("Provide source and destination folder as arguments")
        return

    source_folder = sys.argv[SOURCE_ARG]
    destination_folder = sys.argv[DEST_ARG]

    if not os.path.exists(source_folder):
        print("Provide a valid source folder path")
        return

    convert_folder_jpg_to_png(source_folder, destination_folder)

if __name__ == "__main__":
    main()