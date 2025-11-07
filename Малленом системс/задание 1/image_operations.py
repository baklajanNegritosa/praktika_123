import os  
from PIL import Image  
import shutil

def change_extension(image_path: str, new_extension: str) -> str:
    """Изменяет расширение изображения (PNG/JPG) и возвращает новый путь"""
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError("Файл не найден")
            
        valid_ext = ['jpg', 'jpeg', 'png']
        ext = new_extension.lower()
        if ext not in valid_ext:
            raise ValueError("Поддерживаются только JPG/PNG форматы")
            
        img = Image.open(image_path)
        base_path = os.path.splitext(image_path)[0]
        new_path = f"{base_path}.{ext}"
        
        if ext in ('jpg', 'jpeg'):
            img = img.convert("RGB")
            
        img.save(new_path)
        return new_path
        
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        return None

def move_image(image_path: str, destination: str) -> str:
    """Перемещает изображение в указанную папку"""
    try:
        if not os.path.exists(image_path):
            raise FileNotFoundError("Исходный файл не найден")
            
        os.makedirs(destination, exist_ok=True)
        filename = os.path.basename(image_path)
        new_path = os.path.join(destination, filename)
        
        shutil.move(image_path, new_path)
        return new_path
        
    except Exception as e:
        print(f"Ошибка перемещения: {e}")  
        return None
