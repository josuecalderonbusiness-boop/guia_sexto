from PIL import Image
import os

carpeta = r'C:\guia_sexto\public\imagenes\bio\dia2'

for nombre in os.listdir(carpeta):
    if nombre.lower().endswith('.png'):
        ruta_png = os.path.join(carpeta, nombre)
        img = Image.open(ruta_png)
        if img.width > 1200:
            img = img.resize((1200, int(img.height * (1200/img.width))), Image.LANCZOS)
        nombre_jpg = os.path.splitext(nombre)[0] + '.jpg'
        ruta_jpg = os.path.join(carpeta, nombre_jpg)
        img.convert('RGB').save(ruta_jpg, 'JPEG', quality=75)
        os.remove(ruta_png)
        print('OK:', nombre_jpg, '— PNG borrado')

print('LISTO')