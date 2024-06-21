import os
import easygui
import fitz


def pdf_to_image():
    get_files = easygui.diropenbox()

    for index, file in enumerate(os.listdir(get_files)):
        file_path = os.path.join(get_files, file)
        print(file)
        if os.path.isfile(file_path):
            doc = fitz.open(file_path)
            name, ext = os.path.splitext(file)
            for i, page in enumerate(doc):
                pix = page.get_pixmap()
                print(f"{get_files}\ {name}.png")
                pix.save(f"{get_files}\ {name}.png")

pdf_to_image()
