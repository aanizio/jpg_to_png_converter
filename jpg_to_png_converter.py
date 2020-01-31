import sys
import os
from PIL import Image

def is_jpg_file(filename):
    return filename.endswith(".jpg") or filename.endswith(".jpeg")

def save_jpg_to_png(source, destination):
    im = Image.open(source)
    im.save(destination)

def convert_folder_jpg_to_png(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for file in os.listdir(source_folder):
        if not is_jpg_file(file):
            continue
        png_filename = os.path.splitext(file)[0] + ".png"
        dest_filename = os.path.join(destination_folder, png_filename)
        source_filename = os.path.join(source_folder, file)
        print(f"Converting {file}")
        save_jpg_to_png(source_filename, dest_filename)

def main():
    REQUIRED_LEN_ARGS = 3
    SOURCE_ARG = 1
    DEST_ARG = 2

    print("JPG to PNG Converter")

    if len(sys.argv) != REQUIRED_LEN_ARGS:
        print("Provide source and destination folder as parameters")
        return

    source_folder = sys.argv[SOURCE_ARG]
    destination_folder = sys.argv[DEST_ARG]

    if not os.path.exists(source_folder):
        print("Provide a valid source folder path")
        return

    convert_folder_jpg_to_png(source_folder, destination_folder)

if __name__ == "__main__":
    main()