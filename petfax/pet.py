from flask import (Blueprint, render_template)
import json

'''
Displayin Data
Decoded JSON file : Save to avariable (pets)
Open and red  .json file 
pets variable loaded with data (pets.json file)
'''
pets = json.load(open('pets.json'))    #Pass the entire open function as an argument to json.load()
print(pets)


#Blueprint instance.
#/pets, The URL prefix that should be used for all routes attached to this blueprint
bp = Blueprint('pet', __name__, url_prefix="/pets")


#Define a route on the blueprint instance .
@bp.route('/')      #that goes to '/'
def index():        #method (funtion) for the route named index.

    '''
    Render index.html template
    Second argument: named as pets and,  pass it the pets variable that we just loaded with data.
    '''
    return render_template('pets/index.html', pets=pets)

@bp.route('/<int:id>')      
def show(id):        
    pet = pets[id - 1]

    return render_template('pets/show.html', pet=pet)