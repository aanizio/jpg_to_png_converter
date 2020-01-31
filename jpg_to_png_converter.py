import sys
import os
from PIL import Image

def is_jpg_file(filename):
    return filename.endswith(".jpg") or filename.endswith(".jpeg")

def save_jpg_to_png(filename, source_folder, destination_folder):
    source_filename = os.path.join(source_folder, filename)
    no_ext_filename = os.path.splitext(filename)[0]
    png_filename = no_ext_filename + ".png"
    dest_filename = os.path.join(destination_folder, png_filename)

    im = Image.open(source_filename)
    im.save(dest_filename)

def convert_folder_jpg_to_png(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for file in os.listdir(source_folder):
        if not is_jpg_file(file):
            continue
        print(f"Converting {file}")
        save_jpg_to_png(file, source_folder, destination_folder)

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