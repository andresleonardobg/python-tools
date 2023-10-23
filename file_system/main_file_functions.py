import os
import shutil

ruta_descargas = "C:/Users/USUARIO/Downloads/"
ext_texto = ['.docx','.txt','.doc','.pdf','.pptx']
ext_imagen = ['.png','.jpg','.jpeg','.gif']
ext_video = ['.mov','.mp4']
ext_ejecutables = ['.exe']

def ordenar(archivo, ext):

    for i in ext_texto:
        if ext == i:
            if os.path.isfile(ruta_descargas + archivo):
                shutil.move(ruta_descargas + archivo , ruta_descargas + 'texto', copy_function=shutil.copy)

    for i in ext_imagen:
        if ext == i:
            if os.path.isfile(ruta_descargas + archivo):
                shutil.move(ruta_descargas +  archivo , ruta_descargas + 'imagenes', copy_function=shutil.copy)

    for i in ext_video:
        if ext == i:
            if os.path.isfile(ruta_descargas + archivo):
                shutil.move(ruta_descargas +  archivo , ruta_descargas + 'videos', copy_function=shutil.copy)

    for i in ext_ejecutables:
        if ext == i:
            if os.path.isfile(ruta_descargas + archivo):
                shutil.move(ruta_descargas +  archivo , ruta_descargas + 'ejecutables', copy_function=shutil.copy)
    
    if ext != '':
        if os.path.isfile(ruta_descargas + archivo):
            shutil.move(ruta_descargas +  archivo, ruta_descargas + 'otros', copy_function=shutil.copy)


def main():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar(archivo, ext)

main()