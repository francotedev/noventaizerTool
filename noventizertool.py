import os
from PIL import Image, ImageFilter, ImageEnhance

def process_images(input_path):
    # Crear carpeta de salida
    output_path = os.path.join(input_path, "output")
    os.makedirs(output_path, exist_ok=True)

    # Extensiones soportadas
    supported_extensions = (".png", ".jpg", ".jpeg")

    for filename in os.listdir(input_path):
        if filename.lower().endswith(supported_extensions):
            file_path = os.path.join(input_path, filename)

            # Abrir imagen
            img = Image.open(file_path)
            has_alpha = img.mode == "RGBA"

            if has_alpha:
                # Separar canal alfa
                alpha = img.getchannel("A")

            # Cambiar relación de aspecto a 4:3
            width, height = img.size
            aspect_ratio = 4 / 3

            if width / height > aspect_ratio:
                new_width = int(height * aspect_ratio)
                new_height = height
            else:
                new_width = width
                new_height = int(width / aspect_ratio)

            img = img.crop(((width - new_width) // 2, (height - new_height) // 2, (width + new_width) // 2, (height + new_height) // 2))

            # Redimensionar a tamaño más pequeño para simular pixelado ligero
            img = img.resize((320, 240), resample=Image.NEAREST)

            # Volver a escalar a tamaño original
            img = img.resize((640, 480), resample=Image.NEAREST)

            # Aumentar saturación, contraste y ajustar tonos
            img = ImageEnhance.Color(img).enhance(5.0)  # Aumentar saturación
            img = ImageEnhance.Contrast(img).enhance(2.2)  # Aumentar contraste

            # Aplicar un filtro de realce de bordes (opcional)
            img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)

            # Ajustar tonalidades para exagerar azules y morados, sombras azules y luces verdes
            img = img.convert("RGB")
            pixels = img.load()
            for y in range(img.height):
                for x in range(img.width):
                    r, g, b = pixels[x, y]
                    # Intensificar luces verdes y sombras azules
                    if r + g + b > 500:  # Luces
                        g = min(int(g * 1.8), 255)
                        r = min(int(r * 1.2), 255)
                    elif r + g + b < 200:  # Sombras
                        b = min(int(b * 2.5), 255)
                        r = min(int(r * 0.8), 255)
                        g = min(int(g * 0.8), 255)
                    # Exagerar azules y morados
                    b = min(int(b * 1.8), 255)
                    if r < b and g < b:  # Enfatizar morados
                        r = min(int(r * 1.4), 255)
                    pixels[x, y] = (r, g, b)

            # Restaurar el canal alfa si existe
            if has_alpha:
                img = img.convert("RGBA")
                img.putalpha(alpha)

            # Guardar la imagen procesada
            output_file_path = os.path.join(output_path, filename)
            img.save(output_file_path)

    print(f"Procesamiento completado. Imágenes guardadas en: {output_path}")

# Ruta de entrada
input_path = input("Introduce el path de la carpeta con imágenes: ").strip()
process_images(input_path)