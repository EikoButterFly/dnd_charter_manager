class_requirements = {
    "Бард": {"charisma": 8},
    "Варвар": {"strength": 12},
    "Воин": {"strength": 10, "dexterity": 10},
    "Волшебник": {"intelligence": 6},
    "Друид": {"wisdom": 8},
    "Жрец": {"wisdom": 8},
    "Колдун": {"charisma": 8},
    "Монах": {"dexterity": 8, "wisdom": 8},
    "Паладин": {"strength": 10, "charisma": 10},
    "Плут": {"dexterity": 8},
    "Следопыт": {"dexterity": 10, "wisdom": 10},
    "Чародей": {"charisma": 6}
}

def get_available_classes(abilities):
    available_classes = []
    for char_class, requirements in class_requirements.items():
        if all(abilities.get(attr, 0) >= value for attr, value in requirements.items()):
            available_classes.append(char_class)
    return available_classes