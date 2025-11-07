from image_processor import process_conversion, process_movement

def show_menu():
    print("\n=== Главное меню ===")
    print("1. Конвертировать изображение")
    print("2. Переместить изображение")
    print("3. Выход")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == "1":
            process_conversion()
        elif choice == "2":
            process_movement()
        elif choice == "3":
            print("Выход из программы")
            break  
        else:
            print("Ошибка: введите 1, 2 или 3")

if __name__ == "__main__":
    main()
