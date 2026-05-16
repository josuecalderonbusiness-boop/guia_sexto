from PIL import Image
import os

carpeta = r'C:\guia_sexto\public\imagenes\soc\dia5'

for nombre in os.listdir(carpeta):
    ext = os.path.splitext(nombre)[1].lower()
    if ext in ['.png', '.jpg', '.jpeg', '.webp', '.jfif']:
        ruta_original = os.path.join(carpeta, nombre)
        img = Image.open(ruta_original)
        if img.width > 1200:
            img = img.resize((1200, int(img.height * (1200/img.width))), Image.LANCZOS)
        nombre_jpg = os.path.splitext(nombre)[0] + '.jpg'
        ruta_jpg = os.path.join(carpeta, nombre_jpg)
        img.convert('RGB').save(ruta_jpg, 'JPEG', quality=75)
        if ruta_original != ruta_jpg:
            os.remove(ruta_original)
        print('OK:', nombre_jpg)

print('LISTO')