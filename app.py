from flask import Flask, render_template, request, redirect, url_for
from character import Character
from classes import get_available_classes
from utils.file_utils import load_characters, save_characters

app = Flask(__name__)

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
        character.notes = request.form['notes']
        save_characters(characters)
        return redirect(url_for('character_detail', character_id=character_id))
    return render_template('edit_character.html', character=character, character_id=character_id)

@app.route('/add_character', methods=['GET', 'POST'])
def add_character():
    if request.method == 'POST':
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
        return render_template('choose_class.html', character=new_character, available_classes=available_classes, character_id=len(characters))
    return render_template('add_character.html')

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
    for char_class in request.form.getlist('classes'):
        new_character.add_class(char_class, 1)

    characters.append(new_character)
    save_characters(characters)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)