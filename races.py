races = {
    "Dragonborn": {
        "description": "Драконорожденные происходят от великой расы драконов.",
        "bonuses": {"strength": 2, "charisma": 1},
        "speed": 30,
        "features": ["Draconic Ancestry", "Breath Weapon", "Damage Resistance"]
    },
    "Dwarf": {
        "description": "Дварфы известны своей стойкостью и мастерством в кузнечном деле.",
        "bonuses": {"constitution": 2},
        "speed": 25,
        "features": ["Darkvision", "Dwarven Resilience", "Stonecunning"]
    },
    "Elf": {
        "description": "Эльфы известны своим изяществом и долголетием.",
        "bonuses": {"dexterity": 2},
        "speed": 30,
        "features": ["Darkvision", "Keen Senses", "Fey Ancestry", "Trance"]
    },
    "Gnome": {
        "description": "Гномы - это маленькие и изобретательные существа.",
        "bonuses": {"intelligence": 2},
        "speed": 25,
        "features": ["Darkvision", "Gnome Cunning"]
    },
    "Half-Elf": {
        "description": "Полуэльфы сочетают в себе черты людей и эльфов.",
        "bonuses": {"charisma": 2, "choice": 1},
        "speed": 30,
        "features": ["Darkvision", "Fey Ancestry", "Skill Versatility"]
    },
    "Half-Orc": {
        "description": "Полуорки обладают силой и выносливостью своих орочьих предков.",
        "bonuses": {"strength": 2, "constitution": 1},
        "speed": 30,
        "features": ["Darkvision", "Savage Attacks", "Relentless Endurance"]
    },
    "Halfling": {
        "description": "Полурослики известны своим везением и скрытностью.",
        "bonuses": {"dexterity": 2},
        "speed": 25,
        "features": ["Lucky", "Brave", "Halfling Nimbleness"]
    },
    "Human": {
        "description": "Люди - это наиболее адаптивная и амбициозная раса.",
        "bonuses": {"choice": 1},
        "speed": 30,
        "features": []
    },
    "Tiefling": {
        "description": "Тифлинги обладают демоническим происхождением.",
        "bonuses": {"charisma": 2, "intelligence": 1},
        "speed": 30,
        "features": ["Darkvision", "Hellish Resistance", "Infernal Legacy"]
    },
    "Aarakocra": {
        "description": "Ааракокра - это крылатые существа, живущие в высоких горах.",
        "bonuses": {"dexterity": 2, "wisdom": 1},
        "speed": 25, "fly": 50,
        "features": ["Flight", "Talons"]
    },
    "Genasi": {
        "description": "Генази обладают элементальным происхождением.",
        "bonuses": {"constitution": 2},
        "speed": 30,
        "features": ["Darkvision", "Elemental Affinity"]
    },
    "Goliath": {
        "description": "Голиафы - это могучие и выносливые горные воины.",
        "bonuses": {"strength": 2, "constitution": 1},
        "speed": 30,
        "features": ["Natural Athlete", "Stone's Endurance", "Powerful Build"]
    },
    "Aasimar": {
        "description": "Аасимары обладают божественным происхождением.",
        "bonuses": {"charisma": 2},
        "speed": 30,
        "features": ["Darkvision", "Celestial Resistance", "Healing Hands", "Light Bearer"]
    },
    "Bugbear": {
        "description": "Багбиры - это крупные и сильные гуманоиды.",
        "bonuses": {"strength": 2, "dexterity": 1},
        "speed": 30,
        "features": ["Darkvision", "Long-Limbed", "Powerful Build", "Sneaky", "Surprise Attack"]
    },
    "Firbolg": {
        "description": "Фирболги - это миролюбивые лесные существа.",
        "bonuses": {"wisdom": 2, "strength": 1},
        "speed": 30,
        "features": ["Firbolg Magic", "Hidden Step", "Powerful Build", "Speech of Beast and Leaf"]
    },
    "Goblin": {
        "description": "Гоблины - это маленькие и хитрые существа.",
        "bonuses": {"dexterity": 2, "constitution": 1},
        "speed": 30,
        "features": ["Darkvision", "Fury of the Small", "Nimble Escape"]
    },
    "Hobgoblin": {
        "description": "Хобгоблины - это воинственные и дисциплинированные гуманоиды.",
        "bonuses": {"constitution": 2, "intelligence": 1},
        "speed": 30,
        "features": ["Darkvision", "Martial Training", "Saving Face"]
    },
    "Kenku": {
        "description": "Кенку - это крылатые гуманоиды, лишенные способности летать.",
        "bonuses": {"dexterity": 2, "wisdom": 1},
        "speed": 30,
        "features": ["Expert Forgery", "Kenku Training", "Mimicry"]
    },
    "Kobold": {
        "description": "Кобольды - это маленькие драконоподобные существа.",
        "bonuses": {"dexterity": 2, "strength": -2},
        "speed": 30,
        "features": ["Darkvision", "Grovel, Cower, and Beg", "Pack Tactics", "Sunlight Sensitivity"]
    },
    "Lizardfolk": {
        "description": "Ящеролюды - это гуманоиды, обладающие чертами рептилий.",
        "bonuses": {"constitution": 2, "wisdom": 1},
        "speed": 30,
        "features": ["Bite", "Cunning Artisan", "Hold Breath", "Hunter's Lore", "Natural Armor", "Hungry Jaws"]
    },
    "Orc": {
        "description": "Орки - это сильные и свирепые воины.",
        "bonuses": {"strength": 2, "constitution": 1, "intelligence": -2},
        "speed": 30,
        "features": ["Darkvision", "Aggressive", "Powerful Build", "Primal Intuition"]
    },
    "Tabaxi": {
        "description": "Табакси - это кошкоподобные гуманоиды.",
        "bonuses": {"dexterity": 2, "charisma": 1},
        "speed": 30,
        "features": ["Darkvision", "Feline Agility", "Cat's Claws", "Cat's Talent"]
    },
    "Triton": {
        "description": "Тритоны - это водные гуманоиды, живущие в океанах.",
        "bonuses": {"strength": 1, "constitution": 1, "charisma": 1},
        "speed": 30, "swim": 30,
        "features": ["Amphibious", "Control Air and Water", "Emissary of the Sea", "Guardian of the Depths"]
    },
    "Yuan-ti Pureblood": {
        "description": "Юань-ти чистокровные - это гуманоиды со змееподобными чертами.",
        "bonuses": {"charisma": 2, "intelligence": 1},
        "speed": 30,
        "features": ["Darkvision", "Innate Spellcasting", "Magic Resistance", "Poison Immunity"]
    },
    "Changeling": {
        "description": "Меняющие облик могут изменять свою внешность по желанию.",
        "bonuses": {"charisma": 2, "choice": 1},
        "speed": 30,
        "features": ["Change Appearance", "Unsettling Visage", "Divergent Persona"]
    },
    "Kalashtar": {
        "description": "Калаштары - это люди, обладающие связью с духами.",
        "bonuses": {"wisdom": 2, "charisma": 1},
        "speed": 30,
        "features": ["Dual Mind", "Mental Discipline", "Mind Link", "Severed from Dreams"]
    },
    "Shifter": {
        "description": "Меняющиеся - это гуманоиды, обладающие способностью временно усиливать свои физические черты.",
        "bonuses": {"dexterity": 1},
        "speed": 30,
        "features": ["Darkvision", "Shifting"]
    },
    "Warforged": {
        "description": "Войнорожденные - это искусственные создания, наделенные разумом.",
        "bonuses": {"constitution": 2, "choice": 1},
        "speed": 30,
        "features": ["Constructed Resilience", "Sentry's Rest", "Integrated Protection", "Specialized Design"]
    },
    "Gith": {
        "description": "Гит - это гуманоиды из астральных планов, разделенные на две подрасы: гитъянки и гитцераи.",
        "bonuses": {"intelligence": 1},
        "speed": 30,
        "features": ["Decadent Mastery", "Martial Prodigy", "Githyanki Psionics", "Githzerai Psionics"]
    },
    "Centaur": {
        "description": "Кентавры - это существа с телом лошади и верхней частью тела человека.",
        "bonuses": {"strength": 2, "wisdom": 1},
        "speed": 40,
        "features": ["Charge", "Hooves", "Equine Build", "Survivor"]
    },
    "Loxodon": {
        "description": "Локсодоны - это гуманоиды, напоминающие слонов.",
        "bonuses": {"constitution": 2, "wisdom": 1},
        "speed": 30,
        "features": ["Powerful Build", "Loxodon Serenity", "Natural Armor", "Trunk", "Keen Smell"]
    },
    "Minotaur": {
        "description": "Минотавры - это гуманоиды с головой быка и мощным телом.",
        "bonuses": {"strength": 2, "constitution": 1},
        "speed": 30,
        "features": ["Horns", "Goring Rush", "Hammering Horns", "Imposing Presence"]
    },
    "Simic Hybrid": {
        "description": "Симические гибриды - это существа, измененные магией и наукой.",
        "bonuses": {"constitution": 2, "choice": 1},
        "speed": 30,
        "features": ["Animal Enhancement"]
    },
    "Vedalken": {
        "description": "Ведалкены - это гуманоиды, известные своим интеллектом и логикой.",
        "bonuses": {"intelligence": 2, "wisdom": 1},
        "speed": 30,
        "features": ["Vedalken Dispassion", "Tireless Precision", "Partially Amphibious"]
    },
    "Verdan": {
        "description": "Верданы - это гуманоиды, измененные фейской магией.",
        "bonuses": {"charisma": 2, "constitution": 1},
        "speed": 30,
        "features": ["Black Blood Healing", "Limited Telepathy", "Persuasive"]
    },
    "Locathah": {
        "description": "Локатахи - это водные гуманоиды, обладающие рыбоподобными чертами.",
        "bonuses": {"strength": 2, "dexterity": 1},
        "speed": 30, "swim": 30,
        "features": ["Natural Armor", "Observant & Athletic", "Leviathan Will", "Limited Amphibiousness"]
    },
    "Grung": {
        "description": "Груны - это маленькие амфибийные гуманоиды.",
        "bonuses": {"dexterity": 2, "constitution": 1},
        "speed": 25, "climb": 25,
        "features": ["Poison Immunity", "Amphibious", "Poisonous Skin", "Arboreal Alertness"]
    },
    "Satyr": {
        "description": "Сатиры - это фейские существа, обладающие чертами козлов.",
        "bonuses": {"charisma": 2, "dexterity": 1},
        "speed": 35,
        "features": ["Fey", "Magic Resistance", "Ram", "Mirthful Leaps", "Reveler"]
    },
    "Leonin": {
        "description": "Леонины - это львоподобные гуманоиды.",
        "bonuses": {"constitution": 2, "strength": 1},
        "speed": 35,
        "features": ["Darkvision", "Claws", "Hunter's Instincts", "Daunting Roar"]
    },
    "Fairy": {
        "description": "Феи - это маленькие фейские существа, обладающие магическими способностями.",
        "bonuses": {"dexterity": 2, "charisma": 1},
        "speed": 30, "fly": 30,
        "features": ["Fairy Magic", "Fey Passage"]
    },
    "Harengon": {
        "description": "Харенгоны - это кроликоподобные гуманоиды.",
        "bonuses": {"dexterity": 2, "constitution": 1},
        "speed": 30,
        "features": ["Hare-Trigger", "Leporine Senses", "Lucky Footwork", "Rabbit Hop"]
    },
    "Owlin": {
        "description": "Оулины - это совоподобные гуманоиды.",
        "bonuses": {"dexterity": 2, "wisdom": 1},
        "speed": 30, "fly": 30,
        "features": ["Darkvision", "Silent Feathers"]
    }
}