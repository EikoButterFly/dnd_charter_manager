class_requirements = {
    "Бард": {"charisma": 13},
    "Варвар": {"strength": 13},
    "Воин": {"strength": 13, "dexterity": 13},
    "Волшебник": {"intelligence": 13},
    "Друид": {"wisdom": 13},
    "Жрец": {"wisdom": 13},
    "Изобретатель": {"intelligence": 13},
    "Колдун": {"charisma": 13},
    "Монах": {"dexterity": 13, "wisdom": 13},
    "Паладин": {"strength": 13, "charisma": 13},
    "Плут": {"dexterity": 13},
    "Следопыт": {"dexterity": 13, "wisdom": 13},
    "Чародей": {"charisma": 13}
}

def get_available_classes(abilities):
    available_classes = []
    for char_class, requirements in class_requirements.items():
        if all(abilities.get(attr, 0) >= value for attr, value in requirements.items()):
            available_classes.append(char_class)
    return available_classes