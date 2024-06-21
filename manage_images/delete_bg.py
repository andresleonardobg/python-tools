import os
import easygui
from PIL import Image
from rembg import remove

'''
open dir that has image files remove his background and create a new folder with his name then move the original image and the image with the background removed to this folder
'''

get_dir_path = easygui.diropenbox()


# functions
def create_dir(original_dir, file):
    name, ext = os.path.splitext(file)
    new_dir_name = os.path.join(original_dir, name)
    try:
        os.mkdir(new_dir_name)
    except OSError as error:
        print("error al crear nueva carpeta")
        print(error)

    return new_dir_name


def remove_bg(file, dir_to_save):
    input_file = Image.open(file)
    output_file = remove(input_file)
    output_file.save(f"{dir_to_save}_bg.png")


def move_file(file, new_dir):
    print(f"mover: {file}")
    print(f"nuevo destino: {new_dir}")
    os.rename(file, f"{new_dir}.png")


for index, file in enumerate(os.listdir(get_dir_path)):
    # get file
    origin_file = os.path.join(get_dir_path, file)
    name, ext = os.path.splitext(file)

    if os.path.isfile(origin_file):
        # new dir with the name of the file
        new_dir = create_dir(get_dir_path, file)
        new_dir_file = os.path.join(new_dir.rstrip(), name)
        print(new_dir_file + name + ext)
        # remove bg from image
        remove_bg(origin_file, new_dir_file)
        # move original file to new dir
        move_file(origin_file, new_dir_file)
