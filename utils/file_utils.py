import json
from character import Character

def load_characters(filename="data/characters.json"):
    try:
        with open(filename, "r") as file:
            characters_data = json.load(file)
            return [Character(**data) for data in characters_data]
    except FileNotFoundError:
        return []

def save_characters(characters, filename="data/characters.json"):
    with open(filename, "w") as file:
        json.dump([char.__dict__ for char in characters], file, indent=4)
