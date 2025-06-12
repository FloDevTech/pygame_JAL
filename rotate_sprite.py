from PIL import Image
import os

def rotate_sprite(image_path, angle):
    # Abrir la imagen
    img = Image.open(image_path)
    
    # Rotar la imagen
    rotated_img = img.rotate(angle, expand=True)
    
    # Crear el nombre del archivo de salida
    base_name = os.path.splitext(image_path)[0]
    extension = os.path.splitext(image_path)[1]
    output_path = f"{base_name}_rotated{extension}"
    
    # Guardar la imagen rotada
    rotated_img.save(output_path)
    print(f"Imagen rotada guardada como: {output_path}")

# Ejemplo de uso
if __name__ == "__main__":
    # Ruta de tu imagen
    sprite_path = "sprites/personaje1/basic_move.png"
    
    # Ángulo de rotación (en grados)
    angle = 90  # Puedes cambiar este valor para rotar a diferentes ángulos
    
    rotate_sprite(sprite_path, angle) 