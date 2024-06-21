from heic2png import HEIC2PNG
import os
import easygui

get_files = easygui.diropenbox()

for index, file in enumerate(os.listdir(get_files)):
    origin_file = os.path.join(get_files, file)
    name, ext = os.path.splitext(file)
    final_file = os.path.join(get_files, f"{name}.png")

    if os.path.isfile(origin_file):
        heic_img = HEIC2PNG(
            origin_file, quality=90
        )  # Specify the quality of the converted image
        heic_img.save(final_file)  # The converted image will be saved as `test.png`

        os.remove(origin_file)
    print(index)
