import os
import easygui

get_files = easygui.diropenbox()
new_ext = input('Extension: ')

for index, file in enumerate(os.listdir(get_files)):
    origin_file = os.path.join(get_files, file)
    name, ext = os.path.splitext(file)
    if os.path.isfile(origin_file):
        if ext:
            dist_file = os.path.join(get_files, f"{name}.{new_ext}")
            os.rename(origin_file, dist_file)
            print(f"{name}: archivo con extensión")
        else:
            dist_file = os.path.join(get_files, f"{file}.{new_ext}")
            os.rename(origin_file, dist_file)
            print(f"{name}: archivo sin ext")
    else:
        print(f"{name}: no es un archivo")

# TODO: option to change de file ext