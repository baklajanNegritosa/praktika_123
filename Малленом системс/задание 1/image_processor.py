from image_operations import change_extension, move_image

def process_conversion():
    """Обрабатывает запрос пользователя на конвертацию"""
    print("\n=== Конвертер изображений ===")
    image_path = input("Введите путь к изображению: ").strip()
    new_ext = input("Введите новое расширение (jpg/png): ").strip().lower()
    
    result = change_extension(image_path, new_ext)
    if result:
        print(f"Успешно! Новый файл: {result}")
        return result  
    return None

def process_movement():
    """Обрабатывает запрос пользователя на перемещение"""
    print("\n=== Перемещение изображения ===")
    image_path = input("Введите путь к изображению: ").strip()
    dest_folder = input("Введите папку назначения: ").strip()
    
    result = move_image(image_path, dest_folder)
    if result:
        print(f"Успешно! Изображение перемещено в: {result}")
    return result
