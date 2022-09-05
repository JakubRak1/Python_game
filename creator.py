import numpy as np, logging, json
from objects_constructor import Unit, Weapon


def open_and_load_db (db_json: str) -> dict:
    # Open db_json file and creating and return variable data from db
    with open(f"{db_json}","r") as f:
        data = json.load(f)
    return data


def create_random_enemy(db: list) -> Unit:
    # Chose random from db enemy and returning him
    # Randomly picked number id of enemy
    id: int = np.random.randint(1,6)
    logging.debug(f'id of new enemy is: {id}')
    # Check for right id that not exced db
    if(id > 0 and id < 6):
        for entry in db:
            # Set current enemy as dict by id
            current_enemy :dict = entry['enemy'][f'id{id}']
            logging.debug(f'Dictonary of new enemy is {current_enemy}')
            # Set enemy_unit as object by id and current_enemy
            enemy_unit: Unit = Unit(int(id), current_enemy['name'], current_enemy['max_health'], current_enemy['attact'], current_enemy['ability_to_heal'], current_enemy['g_exp'])
            logging.debug(f'Object value of new enemy is {enemy_unit}')
        return enemy_unit
    # Wrong id
    else:
        print('Enemy id is not in range 1-5')
        quit()


def create_random_weapon(db: list) -> Weapon :
# Chose random from db weapon and returning it
    #Random piced type of weapon 1 - close combat, 2 - distance combat
    weapon_type: int = np.random.randint(1,3)
    logging.debug(f'Type of created weapon is: {weapon_type}')

    #if weapon type is close combat the id is random picked from 1 - 4
    if(weapon_type == 1):
        id: int = np.random.randint(1,5)
        logging.debug(f'The value of id new weapon is: {id}')
    #if weapon type is distance combat the id is random picked from 1 - 2
    elif(weapon_type == 2):
        id = np.random.randint(1,3)
        logging.debug(f'The value of id new weapon is: {id}')
    else: 
        print('Weapon type is not in range 1-2')
        quit()

    if ((weapon_type == 1 and id > 0 and id < 5) or (weapon_type == 2 and id > 0 and id < 3)):    
        for entry in db:
            # Set current_weapon as dict by id
            current_weapon :dict = entry['weapon']['id'+str(weapon_type)+str(id)]
            logging.debug(f'Dictonary of new weapon is {current_weapon}')
            # Set weapon_unit as object by id and current_enemy
            weapon_unit: Weapon = Weapon(int(str(weapon_type)+str(id)), current_weapon['name'], current_weapon['dmg'], current_weapon['health'])
            logging.debug(f'Object value of new weapon is {weapon_type}')
        return weapon_unit
    else: 
        print('Weapon type or id is out of range')
        quit()