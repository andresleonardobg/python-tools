import os
import easygui
from PIL import Image
from datetime import datetime

get_files = easygui.diropenbox()
ext_or_full_name = input('1. Nombre completo | 2. Solo la extension: ')

if ext_or_full_name == '1':
        new_name = input('Nuevo nombre del archivo: ')
        task_to_do = input('1. Redimensionar Imagenes | 2. Renombrar archivos ')
else:
        ext_ext = input('tipo de extension: ')

current_date = datetime.today().strftime('%d%m%Y')

def change_size_images(archivo, name, date, index, size):
        if archivo.lower().endswith((".jpg", ".jpeg", ".png")):
                ruta_completa = os.path.join(get_files, archivo)
                imagen = Image.open(ruta_completa)
                imagen_redimensionada = imagen.resize((size, size), Image.LANCZOS)
                imagen_redimensionada.save(os.path.join(get_files, f"{name}-{date}-{index}.jpg"))
                os.unlink(ruta_completa)
                

def change_name_file(file, new_name, index, ext = "jpg"):
        if ext_or_full_name == '1':
                origin_file = os.path.join(get_files, file)
                dist_file = os.path.join(get_files, f"{new_name}-{current_date}-{index}.jpg")
                os.rename(origin_file, dist_file)
        else:
                origin_file = os.path.join(get_files, file)
                dist_file = os.path.join(get_files, f"{file}.{ext}")
                os.rename(origin_file, dist_file)

def changes_files(name, date):
        size_new_image = 2000

        for index, archivo in enumerate(os.listdir(get_files)):
                if task_to_do == '1':
                        change_size_images(archivo, name, date, index, size_new_image)
                
                if task_to_do == '2':
                        change_name_file(archivo, new_name, index, ext_ext)
                
        print(index)
        

if new_name:
        changes_files(new_name.strip(), current_date)


#TODO: get name to the folder