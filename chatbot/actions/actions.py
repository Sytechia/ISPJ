import requests
import ast
import pyodbc
import os, sys
# path = '../ISPJ'
# os.chdir(path)
# print(os.getcwd())
import sys
sys.path.insert(0, '../ISPJ')
print(os.getcwd())
path = '../'
os.chdir(path)
print(os.getcwd())
from controllers import session_id
# imp
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

# Database #
server = 'ispj-database.database.windows.net'
database = 'ISPJ Database'
username = 'Peter'
password = 'p@ssw0rd'
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)

cursor = conn.cursor()

# Constructs an sql query with any number of parameters passed in for query to be constructued #
"""
For insert, delete, update statements 
"""
def constructAndExecuteQuery(query, *args):
    cursor.execute(query, *args)
    conn.commit()

"""
For select statements
"""
def query(query, *args):
    try:
        cursor.execute(query, *args)
        result = cursor.fetchall()
    except: 
        result = []
    return result

""" Action games """

class AddActionSkyrim(Action): 

    def name(self) -> Text: 
        return "action_addSkyrim"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "The Elder Scrolls V: Skyrim")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "The Elder Scrolls V: Skyrim")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddActionGrandTheftAutoV(Action): 

    def name(self) -> Text: 
        return "action_addGTA"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "GTA V")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "GTA V")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddActionFantasy(Action): 

    def name(self) -> Text: 
        return "action_addFantasy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Final Fantasy VII Remake")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Final Fantasy VII Remake")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

""" Adventure games """

class AddAdventureMinecraft(Action): 

    def name(self) -> Text: 
        return "adventure_addMinecraft"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Minecraft")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Minecraft")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddAdventureUncharted(Action): 

    def name(self) -> Text: 
        return "adventure_addUncharted"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Uncharted 4: A Thief's End")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Uncharted 4: A Thief's End")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddAdventureAssassinCreed(Action): 

    def name(self) -> Text: 
        return "adventure_addAssassin"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Assassin's Creed Odyssey")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Assassin's Creed Odyssey")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

"""Horror Games"""

class AddHorrorResidentEvil3(Action): 

    def name(self) -> Text: 
        return "horror_addResident"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Resident Evil 3")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Resident Evil 3")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddHorrorTheLastOfUs(Action): 

    def name(self) -> Text: 
        return "horror_addTheLastOfUs"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "The Last of Us Part II")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "The Last of Us Part II")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddHorrorPhasmophobia(Action): 

    def name(self) -> Text: 
        return "horror_addPhasmophobia"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Phasmophobia")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Phasmophobia")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

"""Indie Games"""

class AddIndieStardewValley(Action): 

    def name(self) -> Text: 
        return "indie_addStardewValley"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Stardew Valley")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Stardew Valley")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddIndieOvercooked2(Action): 

    def name(self) -> Text: 
        return "indie_addOvercooked2"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Overcooked 2")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Overcooked 2")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddIndieFallGuys(Action): 

    def name(self) -> Text: 
        return "indie_addFallGuys"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Fall Guys: Ultimate Knockout")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Fall Guys: Ultimate Knockout")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

"""Multiplayer Games"""

class AddMultiplayerAnimalCrossing(Action): 

    def name(self) -> Text: 
        return "multiplayer_addAnimalCrossing"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Animal Crossing: New Horizons")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Animal Crossing: New Horizons")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddMultiplayerCOD(Action): 

    def name(self) -> Text: 
        return "multiplayer_addCOD"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Call of Duty: Black Ops Cold War")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Call of Duty: Black Ops Cold War")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

class AddMultiplayerPUBG(Action): 

    def name(self) -> Text: 
        return "multiplayer_addPUBG"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "PlayerUnknown's Battlegrounds")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "PlayerUnknown's Battlegrounds")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")
        return []

"""Racing Games"""

class AddRacingMarioKart8(Action): 

    def name(self) -> Text: 
        return "racing_addMarioKart8"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Mario Kart 8")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Mario Kart 8")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

class AddRacingForza(Action): 

    def name(self) -> Text: 
        return "racing_addForza"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Forza Horizon 4")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Forza Horizon 4")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

class AddRacingDirt(Action): 

    def name(self) -> Text: 
        return "racing_addDirt"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Dirt 4")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Dirt 4")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

"""RPG games"""
class AddRPGWitcher(Action): 

    def name(self) -> Text: 
        return "rpg_addWitcher"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "The Witcher 3: Wild Hunt")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "The Witcher 3: Wild Hunt")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

class AddRPGPersona(Action): 

    def name(self) -> Text: 
        return "rpg_addPersona"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Persona 5 Strikers")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Persona 5 Strikers")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

class AddRPGZelda(Action): 

    def name(self) -> Text: 
        return "rpg_addZelda"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "The Legend of Zelda: Breath of the Wild")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "The Legend of Zelda: Breath of the Wild")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

"""Simulation Games"""

class AddSimulationSims(Action): 

    def name(self) -> Text: 
        return "simulation_addSims"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "The Sims 4")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "The Sims 4")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

class AddSimulationWWE(Action): 

    def name(self) -> Text: 
        return "simulation_addWWE"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "WWE 2K Battlegrounds")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "WWE 2K Battlegrounds")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

class AddSimulationFifa(Action): 

    def name(self) -> Text: 
        return "simulation_addfifa"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "FIFA 21")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "FIFA 21")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

"""sports games"""
class AddSportsNBA(Action): 

    def name(self) -> Text: 
        return "sport_addNBA"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "NBA 2K20")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "NBA 2K20")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

class AddSportsFifa(Action): 

    def name(self) -> Text: 
        return "sport_addFifa"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "FIFA 21")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "FIFA 21")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")

class AddSportsRocketLeague(Action): 

    def name(self) -> Text: 
        return "sport_addRocketLeague"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        data = requests.get('http://localhost:5000/getUserID').text
        print(data)
        latest_cart_id = query('SELECT * FROM cart')
        if latest_cart_id == []:
            latest_cart_id = 1
        else:
            latest_cart_id = (latest_cart_id[-1][0] + 1)
        product = query('SELECT * FROM products WHERE prod_name=?', "Rocket League")[0]
        item_platform = 'PS4'
        existing_game = query('SELECT * FROM cart WHERE user_id=? AND prod_name=?',data, "Rocket League")
        if existing_game != []:
            text = "You have added this game before"
        else:
            constructAndExecuteQuery('INSERT INTO cart VALUES(?,?,?,?,?,?,?)',latest_cart_id,1,product[2],product[3],product[5],data, item_platform)
            text = "Product have been added :)"
        dispatcher.utter_message(text=f"{text}")