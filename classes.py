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

class_features = {
    "Бард": {
        "description": "Барды используют магию через музыку и слова.",
        "features": ["Spellcasting", "Bardic Inspiration"]
    },
    "Варвар": {
        "description": "Варвары - это дикие воины, обладающие огромной силой и выносливостью.",
        "features": ["Rage", "Unarmored Defense"]
    },
    "Воин": {
        "description": "Воины - это мастера ближнего боя и разнообразных боевых искусств.",
        "features": ["Fighting Style", "Second Wind"]
    },
    "Волшебник": {
        "description": "Волшебники изучают магические заклинания и манипулируют магией.",
        "features": ["Spellcasting", "Arcane Recovery"]
    },
    "Друид": {
        "description": "Друиды черпают свои силы из природы и используют магию для изменения формы.",
        "features": ["Druidic", "Spellcasting"]
    },
    "Жрец": {
        "description": "Жрецы черпают свои силы от божественных существ и используют магию для лечения и защиты.",
        "features": ["Spellcasting", "Divine Domain"]
    },
    "Изобретатель": {
        "description": "Изобретатели используют свою смекалку и технологии для создания магических предметов.",
        "features": ["Magic Item Tinkering"]
    },
    "Колдун": {
        "description": "Колдуны черпают свои силы от мистических патронов и используют магию через силу воли.",
        "features": ["Otherworldly Patron", "Pact Magic"]
    },
    "Монах": {
        "description": "Монахи используют внутреннюю энергию для улучшения своих боевых навыков и защиты.",
        "features": ["Unarmored Defense", "Martial Arts"]
    },
    "Паладин": {
        "description": "Паладины - это священные воины, посвященные защите добра и справедливости.",
        "features": ["Divine Sense", "Lay on Hands"]
    },
    "Плут": {
        "description": "Плуты - это мастера скрытности и ловкости рук.",
        "features": ["Sneak Attack", "Thieves' Cant"]
    },
    "Следопыт": {
        "description": "Следопыты - это мастера охоты и изучения природы.",
        "features": ["Favored Enemy", "Natural Explorer"]
    },
    "Чародей": {
        "description": "Чародеи черпают свои магические силы из врожденных способностей.",
        "features": ["Spellcasting", "Sorcerous Origin"]
    }
}

def get_available_classes(abilities):
    available_classes = []
    for char_class, requirements in class_requirements.items():
        if all(abilities.get(attr, 0) >= value for attr, value in requirements.items()):
            available_classes.append(char_class)
    return available_classes