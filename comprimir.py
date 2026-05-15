from PIL import Image
import os

carpeta = r'C:\guia_sexto\public\imagenes\len\dia1'

for nombre in os.listdir(carpeta):
    if nombre.lower().endswith(('.png', '.jpg', '.jpeg')):
        ruta = os.path.join(carpeta, nombre)
        img = Image.open(ruta)
        if img.width > 1200:
            img = img.resize((1200, int(img.height * (1200/img.width))), Image.LANCZOS)
        nombre_jpg = os.path.splitext(nombre)[0] + '.jpg'
        ruta_out = os.path.join(carpeta, nombre_jpg)
        img.convert('RGB').save(ruta_out, 'JPEG', quality=75)
        print('OK:', nombre_jpg)

print('LISTO')