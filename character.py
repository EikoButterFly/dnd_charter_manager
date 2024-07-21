class Character:
    def __init__(self, name, race, abilities, char_classes=None, level=1, experience=0, skills=None, successes=0, failures=0, background="", alignment="", player_name="", inspiration=0, proficiency_bonus=2, saving_throws=None, skills_proficiencies=None, passive_perception=0, languages_and_proficiencies="", armor_class=10, initiative=0, speed=30, max_hp=10, current_hp=10, temp_hp=0, hit_dice="1d10", death_saves=None, attacks_and_spellcasting=None, equipment=None, character_traits="", ideals="", bonds="", flaws="", features_and_traits="", spells=None, notes=""):
        self.name = name
        self.race = race
        self.abilities = abilities
        self.char_classes = char_classes if char_classes else {}
        self.level = level
        self.experience = experience
        self.skills = skills if skills else {}
        self.successes = successes
        self.failures = failures
        self.background = background
        self.alignment = alignment
        self.player_name = player_name
        self.inspiration = inspiration
        self.proficiency_bonus = proficiency_bonus
        self.saving_throws = saving_throws if saving_throws else {}
        self.skills_proficiencies = skills_proficiencies if skills_proficiencies else {}
        self.passive_perception = passive_perception
        self.languages_and_proficiencies = languages_and_proficiencies
        self.armor_class = armor_class
        self.initiative = initiative
        self.speed = speed
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.temp_hp = temp_hp
        self.hit_dice = hit_dice
        self.death_saves = death_saves if death_saves else {"successes": 0, "failures": 0}
        self.attacks_and_spellcasting = attacks_and_spellcasting if attacks_and_spellcasting else []
        self.equipment = equipment if equipment else []
        self.character_traits = character_traits
        self.ideals = ideals
        self.bonds = bonds
        self.flaws = flaws
        self.features_and_traits = features_and_traits
        self.spells = spells if spells else []
        self.notes = notes

    def __repr__(self):
        return f"<Character(name={self.name}, race={self.race}, abilities={self.abilities}, classes={self.char_classes})>"

    def update_ability(self, ability, value):
        if ability in self.abilities:
            self.abilities[ability] = value
        else:
            print(f"Способность {ability} не существует.")

    def add_class(self, char_class, level):
        self.char_classes[char_class] = level

    def add_experience(self, exp):
        self.experience += exp
        self.level_up()

    def level_up(self):
        if self.experience >= 1000 * self.level:
            self.level += 1
            print(f"{self.name} повысил уровень до {self.level}!")

    def record_success(self):
        self.successes += 1

    def record_failure(self):
        self.failures += 1