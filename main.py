from character import Character
from utils.file_utils import load_characters, save_characters

def main():
    characters = load_characters()
    
    while True:
        print("\nМеню:")
        print("1. Создать нового персонажа")
        print("2. Показать всех персонажей")
        print("3. Сохранить и выйти")
        choice = input("Выберите опцию: ")

        if choice == "1":
            new_character = Character.create_character()
            characters.append(new_character)
        elif choice == "2":
            for character in characters:
                print(character)
        elif choice == "3":
            save_characters(characters)
            print("Персонажи сохранены. Выход.")
            break
        else:
            print("Неправильный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
