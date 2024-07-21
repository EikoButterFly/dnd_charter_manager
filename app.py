from flask import Flask, render_template, request, redirect, url_for, session
from character import Character
from classes import get_available_classes, class_features
from races import races
from utils.file_utils import load_characters, save_characters
import random
from skills import skill_attributes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Загрузка персонажей из файла
characters = load_characters()

@app.route('/')
def index():
    return render_template('index.html', characters=characters)

@app.route('/character/<int:character_id>')
def character_detail(character_id):
    character = characters[character_id]
    return render_template('character_detail.html', character=character, character_id=character_id)

@app.route('/character/<int:character_id>/edit', methods=['GET', 'POST'])
def edit_character(character_id):
    character = characters[character_id]
    if request.method == 'POST':
        character.name = request.form['name']
        character.race = request.form['race']
        character.abilities["strength"] = int(request.form['strength'])
        character.abilities["dexterity"] = int(request.form['dexterity'])
        character.abilities["constitution"] = int(request.form['constitution'])
        character.abilities["intelligence"] = int(request.form['intelligence'])
        character.abilities["wisdom"] = int(request.form['wisdom'])
        character.abilities["charisma"] = int(request.form['charisma'])
        character.player_name = request.form['player_name']
        character.inspiration = int(request.form['inspiration'])
        character.proficiency_bonus = int(request.form['proficiency_bonus'])
        character.armor_class = int(request.form['armor_class'])
        character.initiative = int(request.form['initiative'])
        character.speed = int(request.form['speed'])
        character.max_hp = int(request.form['max_hp'])
        character.current_hp = int(request.form['current_hp'])
        character.temp_hp = int(request.form['temp_hp'])
        character.hit_dice = request.form['hit_dice']
        character.death_saves["successes"] = int(request.form['death_saves_successes'])
        character.death_saves["failures"] = int(request.form['death_saves_failures'])
        
        character.saving_throws = {
            save: int(value) for save, value in request.form.items() if save.startswith('saving_throws_')
        }
        
        character.skills = {
            skill: int(value) for skill, value in request.form.items() if skill.startswith('skills_')
        }

        character.passive_perception = int(request.form['passive_perception'])
        character.languages_and_proficiencies = request.form['languages_and_proficiencies']
        character.character_traits = request.form['character_traits']
        character.ideals = request.form['ideals']
        character.bonds = request.form['bonds']
        character.flaws = request.form['flaws']
        character.features_and_traits = request.form['features_and_traits']
        character.notes = request.form['notes']

        character.attacks_and_spellcasting = request.form.getlist('attacks_and_spellcasting[]')
        character.equipment = request.form.getlist('equipment[]')
        character.spells = request.form.getlist('spells[]')
        
        save_characters(characters)
        return redirect(url_for('character_detail', character_id=character_id))
    
    return render_template('edit_character.html', character=character, character_id=character_id)

def generate_random_abilities():
    abilities = []
    for _ in range(6):
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        abilities.append(sum(rolls))
    return abilities

@app.route('/add_character', methods=['GET', 'POST'])
def add_character():
    if request.method == 'POST':
        name = request.form['name']
        race = request.form['race']
        
        abilities = generate_random_abilities()
        session['abilities'] = abilities
        
        new_character = Character(name, race, {})
        available_classes = get_available_classes({attr: max(abilities) for attr in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']})
        return render_template('choose_class.html', character=new_character, available_classes=available_classes, abilities=abilities, class_features=class_features)
    return render_template('add_character.html', races=races)

@app.route('/choose_class', methods=['POST'])
def choose_class():
    name = request.form['name']
    race = request.form['race']
    abilities = {
        "strength": int(request.form['strength']),
        "dexterity": int(request.form['dexterity']),
        "constitution": int(request.form['constitution']),
        "intelligence": int(request.form['intelligence']),
        "wisdom": int(request.form['wisdom']),
        "charisma": int(request.form['charisma']),
    }

    new_character = Character(name, race, abilities)
    available_classes = get_available_classes(abilities)
    return render_template('choose_class.html', character=new_character, available_classes=available_classes, abilities=abilities, class_features=class_features)

@app.route('/choose_skills', methods=['POST'])
def choose_skills():
    name = request.form['name']
    race = request.form['race']
    
    # Отладочные сообщения
    print(f"Name: {name}")
    print(f"Race: {race}")
    print(f"Form Data: {request.form}")

    abilities = {
        "strength": int(request.form.get('strength', 0) or 0),
        "dexterity": int(request.form.get('dexterity', 0) or 0),
        "constitution": int(request.form.get('constitution', 0) or 0),
        "intelligence": int(request.form.get('intelligence', 0) or 0),
        "wisdom": int(request.form.get('wisdom', 0) or 0),
        "charisma": int(request.form.get('charisma', 0) or 0),
    }

    selected_class = request.form['class']
    skills = request.form.getlist('skills')

    new_character = Character(name, race, abilities)
    new_character.add_class(selected_class, 1)

    for skill in skills:
        skill_attr = skill_attributes[skill]
        new_character.skills[skill] = abilities[skill_attr]

    characters.append(new_character)
    save_characters(characters)
    return redirect(url_for('index'))

@app.route('/finalize_character', methods=['POST'])
def finalize_character():
    name = request.form['name']
    race = request.form['race']
    
    # Отладочные сообщения
    print(f"Name: {name}")
    print(f"Race: {race}")
    print(f"Form Data: {request.form}")

    abilities = {
        "strength": int(request.form.get('strength', 0) or 0),
        "dexterity": int(request.form.get('dexterity', 0) or 0),
        "constitution": int(request.form.get('constitution', 0) or 0),
        "intelligence": int(request.form.get('intelligence', 0) or 0),
        "wisdom": int(request.form.get('wisdom', 0) or 0),
        "charisma": int(request.form.get('charisma', 0) or 0),
    }

    selected_class = request.form['class']
    skills = request.form.getlist('skills')

    new_character = Character(name, race, abilities)
    new_character.add_class(selected_class, 1)

    for skill in skills:
        skill_attr = skill_attributes[skill]
        new_character.skills[skill] = abilities[skill_attr]

    characters.append(new_character)
    save_characters(characters)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
