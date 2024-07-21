class Character:
    def __init__(self, name, race, abilities):
        self.name = name
        self.race = race
        self.abilities = abilities
        self.char_classes = {}
        self.level = 1
        self.experience = 0
        self.skills = {}
        self.successes = 0
        self.failures = 0
        self.background = ""
        self.alignment = ""
        self.player_name = ""
        self.inspiration = 0
        self.proficiency_bonus = 2
        self.saving_throws = {}
        self.skills_proficiencies = {}
        self.passive_perception = 0
        self.languages_and_proficiencies = ""
        self.armor_class = 10
        self.initiative = 0
        self.speed = 30
        self.max_hp = 10
        self.current_hp = 10
        self.temp_hp = 0
        self.hit_dice = "1d10"
        self.death_saves = {"successes": 0, "failures": 0}
        self.attacks_and_spellcasting = []
        self.equipment = []
        self.character_traits = ""
        self.ideals = ""
        self.bonds = ""
        self.flaws = ""
        self.features_and_traits = ""
        self.spells = []
        self.notes = ""
        self.skills = {}  # Новый атрибут для хранения навыков

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