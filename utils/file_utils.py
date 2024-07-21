import json
from character import Character

def load_characters(filepath='data/characters.json'):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            characters_data = json.load(file)
            characters = [Character(**data) for data in characters_data]
            return characters
    except FileNotFoundError:
        return []

def save_characters(characters, filepath='data/characters.json'):
    with open(filepath, 'w', encoding='utf-8') as file:
        characters_data = [character.__dict__ for character in characters]
        json.dump(characters_data, file, ensure_ascii=False, indent=4)