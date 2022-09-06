from objects_constructor import UnitEnemy, UnitPlayer, UnitWeapon
from creator import create_random_enemy, create_random_weapon, open_and_load_db
from colorama import Fore, Style, init
import logging, sys


def try_to_enable_debug_mode () -> None :
    # Check if debug mode is on
    if (sys.argv[1] == '-d'):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
    else:
        logging.basicConfig(level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')


def conduct_player_turn (player: UnitPlayer, enemy: UnitEnemy) -> None:
    #Allow user to play his turn
    logging.debug(f'Value of boolan enemy and player hp > 0 {enemy.hp > 0 and player.hp > 0}')
    # Check if player and enemy are alive (hp > 0)
    if (enemy.hp > 0 and player.hp > 0):
        # Infinite loop until user provide correct input
        while True:
            print(str(f"{Fore.CYAN}Now it's your turn what do you want to do? type attack to attack enemy, heal to heal yourself, stats to display your stats, q to quit game or r to reload game{Style.RESET_ALL}"))   
            option: str = input(str())
            logging.debug(f'Value of option by input is: {option}')
            match option:
                # Attacking enemy by player
                case ("attack"):
                    # Run function of take_dmg_info by enemy from objects_contructor.py and print returning string, then breaks loop 
                    print(enemy.take_dmg_info(player.dmg))
                    break
                # Healing player object
                case("heal"):
                    # Run function of get_heal_dmg_info by player from objects_contructor.py heal_val is 10% of maxhp and print returning string, then breaks loop
                    print(player.get_heal_dmg_info(int(player.maxhp*0.1)))
                    break
                # Displaying player stats and returning to loop
                case("stats"):
                    print(player)
                # Quit game
                case("q"):
                    # Printing message of quiting game and quits
                    print(f'{Fore.RED}Quiting game{Style.RESET_ALL}')
                    quit()
                # Reaload game
                case("r"):
                    # Printing message of Reloading game and run play_game function 
                    print('Reloading Game')
                    play_game()


def conduct_enemy_turn (player: UnitPlayer, enemy: UnitEnemy) -> None:
    # Conduct enemy object play turn
    logging.debug(f'Value of boolan enemy and player hp > 0 {enemy.hp > 0 and player.hp > 0}')
    # Check if player and enemy are alive (hp > 0)    
    if(enemy.hp > 0 and player.hp > 0):
        logging.debug(f'Value of enemy ability to heal {enemy.a_heal}, enemy hp {enemy.hp} and condition to heal {enemy.a_heal and enemy.hp <= enemy.maxhp *0.2}')
        # Checking enemy HP if it's drop bellow 20% and enemy has ability to heal then enemy will heal instead od attacking player
        if(enemy.a_heal and enemy.hp <= enemy.maxhp *0.2):
            # Run function of healing dmg by enemy from object_contructor.py heal_val is 5% of maxhp and print returning string
            print(enemy.get_heal_dmg_info(int(enemy.maxhp*0.05)))
        # If enemy dont heal himself he deals enemy.dmg value to player
        else:
            # Run function of reciving dmg by player from objects_contructor.py and prints returning string
            print(player.take_dmg_info(enemy.dmg))    


def conduct_fight_with_enemy (player: UnitPlayer, enemy: UnitEnemy) -> bool:
    # Conduct fight until one of object hp drops to 0
    while True:
    # Infinite loop, until one of objects have health = 0
        conduct_player_turn(player, enemy)
        # Run player turn by running function conduct_player_turn
        logging.debug(f'Value of condition enemy.hp<=0: {enemy.hp <= 0}') 
        if(enemy.hp <= 0):
        # Cheks if enemy is still alive if not create var win and setting value as True and breaks loop 
            win: bool = True
            break
        # Run enemy turn by running function conduct_enemy_turn
        conduct_enemy_turn(player, enemy)
        logging.debug(f'Value of condition player.hp<=0: {player.hp <= 0}')
        # Cheks if player is still alive if not create var win and setting value as False and breaks loop 
        if(player.hp <= 0):
            win = False
            break
    logging.debug(f'Value of win var is: {win}')
    # Check value of win == True and return True value of function fight_with_enemy
    if (win):
        return True
    # Check value of win == False and return False value of function fight_with_enemy
    elif (win == False): 
        return False


def play_game() -> None :
    # Create variable data_base by loading data from json db
    data_base = open_and_load_db('stats.json')['unit']
    print(f"{Fore.CYAN}Welcome Adventure, In order to start your jurney please type your name of character{Style.RESET_ALL}")
    name_player = input(str())
    logging.debug(f"Value of input as name of player: {name_player}")
    # Create class instance with starting deafult value and name taken from input
    player: UnitPlayer = UnitPlayer(0, name_player[0].upper()+name_player[1:], 125, 205)
    logging.debug(player)
    print(f"{Fore.CYAN}Ah, so you are {player.name} your currently stats are:{Style.RESET_ALL} \n{Fore.GREEN}{player}{Style.RESET_ALL} \n{Fore.CYAN}It's time to face your first enemy{Style.RESET_ALL}")
    # Infinite loop to always pick random enemy and initilize fight with him and result of fight
    while True:
        # Set enemy object by runing function create_random_enemy from creator.py
        enemy: UnitEnemy = create_random_enemy(data_base)
        print(f"{Fore.RED}New enemy is: {enemy}{Style.RESET_ALL}")
        logging.debug(f'Value of next enemy is : {enemy}')
        # Create var fight_resault and settting bool value as result of fight_with_enemy function 
        fight_resault: bool = conduct_fight_with_enemy(player, enemy)
        logging.debug(f'Value of whole function fight_with_enemy: {fight_resault}')
        # Check if player wins fight or lose
        if (fight_resault == True):
            print(f'{Fore.CYAN}{player.name} has slain {enemy.name}. Congratulations !!{Style.RESET_ALL}')
            # Run function gain_exp from objects_constructor.py
            player.gain_exp(enemy.g_exp)
            # Set weapon object by runing function create_random_weapon from creator.py
            weapon: UnitWeapon = create_random_weapon(data_base)
            logging.debug(f'Weapon object is: {weapon}')
            print(f"{Fore.YELLOW}You have found {weapon.name} of stats dmg: {weapon.dmg} and hp: {weapon.hp}{Style.RESET_ALL}")
            # Infinite loop until user input is equal to 'equip' or 'noting'
            while True:
                print(f'{Fore.CYAN}What do you want to do with this weapon?\nType drop to drop current weapon, but remember when you drop weapon you will have no longer access to it\nType equip to equip found weapon\nType nothing to pass by this weapon\nType stats to see stats of your current weapon{Style.RESET_ALL}')
                # Set weapon_option as str of input entered by user
                weapon_option: str = input(str())
                logging.debug(f'Input value of weapon_option is: {weapon_option}')
                match weapon_option:
                    # Drops current equpit weapon
                    case('drop'):
                        logging.debug(f'Value of len(player.eq): {len(player.eq)}, bool value for len(player.eq) == 0: {len(player.eq) == 0} and bool value for len(player.eq) != 0: {len(player.eq) != 0}')
                        # Check if player object has any weapon equipt
                        if(len(player.eq) == 0):
                            print(f"{Fore.RED}You can't unequip weapon becouse you dont have any{Style.RESET_ALL}")  
                        # Unequipt current weapons
                        elif(len(player.eq) != 0):
                            print(player.ueq_weapon(player.eq[0][1], player.eq[0][2]))
                    # Equipt player with found weapon object
                    case ('equip'):
                        logging.debug(f'Value of len(player.eq): {len(player.eq)}, bool value for len(player.eq) == 0: {len(player.eq) == 0} and bool value for len(player.eq) != 0: {len(player.eq) != 0}')
                        # Check if player object has any weapon equipt
                        if(len(player.eq) == 0):
                            print(f'{Fore.MAGENTA}{player.eq_weapon(weapon.dmg, weapon.hp, weapon.name)}{Style.RESET_ALL}')
                            break
                        # Check if player object has any weapon equipt
                        elif(len(player.eq) != 0):
                            print(f"{Fore.RED}You can't equip another weapon first drop current{Style.RESET_ALL}")  
                    # Do nothing
                    case('nothing'):
                        print(f"{Fore.CYAN}You walked away from {weapon.name}{Style.RESET_ALL}")
                        break
                    # Display current equipt weapon stats
                    case('stats'):
                        logging.debug(f'Value of len(player.eq): {len(player.eq)}, bool value for len(player.eq) == 0: {len(player.eq) == 0} and bool value for len(player.eq) != 0: {len(player.eq) != 0}')
                        # Check if player object has any weapon equipt
                        if(len(player.eq) == 0):
                            print(f"{Fore.RED}You dont have any weapon{Style.RESET_ALL}")
                        # Print current weapons stats
                        elif(len(player.eq) != 0):
                            print(f"{Fore.MAGENTA}Your weapon is: {player.eq[0][0]}, dmg stats: {player.eq[0][1]}, dmg stats: {player.eq[0][2]}{Style.RESET_ALL}")
        # Player lose fight and reloads game
        elif (fight_resault == False):
            # Print message which enemy has defeted player and reluch whole function
            print(f"{enemy.name} has slain {player.name}. Don't worry game will reaload\nReloading Game")
            play_game()


def main() -> None:
    # Checks for debug mode and starts game
    if((len(sys.argv) >= 2)):
        try_to_enable_debug_mode()
    # Init for colorama
    init(convert = True)
    play_game()


if __name__ == '__main__':
    main()