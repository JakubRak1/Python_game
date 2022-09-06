import logging
from colorama import Fore, Style


class Unit:
    def __init__(self, id: int, name: str, dmg: int) -> None:
    # Constructor to create Unit object 
        self.id: int= id
        self.name: str = name
        self.dmg: int = dmg
    

class UnitWeapon(Unit):
    # Class refers only to weapon object
    def __init__(self, id: int, name: str, dmg: int, hp: int) -> None:
        # Constructor to create UnitWeapon object 
        super().__init__(id, name, dmg)
        self.hp: int = hp


    def __repr__(self) -> str:
        return (f'<Weapon id: {self.id}, name: {self.name}, dmg: {self.dmg}, hp: {self.hp}>')


class UnitEnemy(Unit):
    # Class refers only to enemy object
    def __init__(self, id: int, name: str, maxhp: int, dmg: int, a_heal: bool, g_exp: int) -> None:
        # Constructor to create UnitEnemy object
        super().__init__(id, name, dmg)
        self.hp: int = maxhp
        self.maxhp: int = maxhp
        self.a_heal: bool = a_heal
        self.g_exp: int = g_exp


    def __repr__(self) -> str:
        return(f"{Fore.RED}New enemy is: Enemy Name: {self.name.upper()}, HP:{self.hp}, DMG:{self.dmg}{Style.RESET_ALL}")


    def take_dmg_info (self, dmg_taken: int) -> str:
        # Self object receive damage that decrease hp
        logging.debug(f'{self.name} Hp value before substraction: {self.hp}, attack dmg value: {dmg_taken}')
        # Substrack dmg_taken value from self.hp 
        self.hp -= dmg_taken
        logging.debug(f'{self.name} Hp value after substraction: {self.hp}, bool value of hp<=0 {self.hp <= 0}')
        # Prevent to display minus hp
        if (self.hp <= 0):
            logging.debug(f'{self.name} Hp value after reaching 0 and bellow is: {self.hp}')
            # Change hp to value 0 if its equal or below 0
            self.hp = 0
            logging.debug(f'{self.name} Hp value after reseting to not get minus value: {self.hp}')
        return(f'{Fore.RED}{self.name} have taken {dmg_taken} dmg{Style.RESET_ALL}')

    
    def get_heal_dmg_info (self, heal_val: int) -> str:
        # Self object recover hp by heal_val
        logging.debug(f'{self.name} HP value before sums: {self.hp}, heal_val value: {heal_val}')
        # Adds to self.hp heal_val
        self.hp += heal_val
        logging.debug(f'{self.name} HP value after sums: {self.hp}')
        logging.debug(f'Bool value of self.hp > self.maxhp: {self.hp > self.maxhp}')
        # Checks if self.hp is bigger than self.maxhp
        if (self.hp > self.maxhp):
            # Set self.hp as self.maxhp
            self.hp = self.maxhp
            logging.debug(f'Value of self.hp after seting as self.maxhp :{self.hp} and self.maxhp value: {self.maxhp}')
        return(f'{Fore.GREEN}{self.name} have healed {heal_val} dmg{Style.RESET_ALL}')


class UnitPlayer(Unit):
    # Class refers only to player object
    def __init__(self, id: int, name: str, maxhp: int, dmg: int, a_heal: bool = True) -> None:
        # Constructor to create UnitPlayer object
        super().__init__(id, name, dmg)
        self.hp: int = maxhp
        self.maxhp: int = maxhp
        self.a_heal: bool = a_heal
        self.exp: int = 0
        self.advance: int = 100
        self.eq: list[str, int, int] = []
    

    def __repr__(self) -> str:
        return (f'<Player id: {self.id}, name: {self.name}, hp: {self.hp}, dmg: {self.dmg}, exp: {self.exp}, needed exp to level up: {self.advance}>')
    

    def take_dmg_info (self, dmg_taken: int) -> str:
        # Self object receive damage that decrease hp
        logging.debug(f'{self.name} Hp value before substraction: {self.hp}, attack dmg value: {dmg_taken}')
        # Substrack dmg_taken value from self.hp 
        self.hp -= dmg_taken
        logging.debug(f'{self.name} Hp value after substraction: {self.hp}, bool value of hp<=0 {self.hp <= 0}')
        # Prevent to display minus hp
        if (self.hp <= 0):
            logging.debug(f'{self.name} Hp value after reaching 0 and bellow is: {self.hp}')
            # Change hp to value 0 if its equal or below 0
            self.hp = 0
            logging.debug(f'{self.name} Hp value after reseting to not get minus value: {self.hp}')
        return(f'{Fore.RED}{self.name} have taken {dmg_taken} dmg{Style.RESET_ALL}')

    
    def get_heal_dmg_info (self, heal_val: int) -> str:
        # Self object recover hp by heal_val
        logging.debug(f'{self.name} HP value before sums: {self.hp}, heal_val value: {heal_val}')
        # Adds to self.hp heal_val
        self.hp += heal_val
        logging.debug(f'{self.name} HP value after sums: {self.hp}')
        logging.debug(f'Bool value of self.hp > self.maxhp: {self.hp > self.maxhp}')
        # Checks if self.hp is bigger than self.maxhp
        if (self.hp > self.maxhp):
            # Set self.hp as self.maxhp
            self.hp = self.maxhp
            logging.debug(f'Value of self.hp after seting as self.maxhp :{self.hp} and self.maxhp value: {self.maxhp}')
        return(f'{Fore.GREEN}{self.name} have healed {heal_val} dmg{Style.RESET_ALL}')


    def gain_exp (self, exp_gain: int) -> str:
        # Self object receive exp
        logging.debug(f'{self.name} EXP value before sums: {self.exp}, exp_gain value: {exp_gain}')
        # Increase self.exp by exp_gain and prints str of message who gained and how much exp
        self.exp += exp_gain
        logging.debug(f'{self.name} EXP value aftre sums: {self.exp}')
        print(f'{Fore.YELLOW}{self.name} have gain {exp_gain} exp{Style.RESET_ALL}')
        logging.debug(f'Bool value of self.advance <= self.exp: {self.advance <= self.exp}')
        # After reaching self.advance increase advance, dmg, maxhp by 20%
        if(self.advance<= self.exp):
            logging.debug(f'Values before adding level self.advance: {self.advance} self.dmg: {self.dmg}, self.hp: {self.maxhp}, self.exp: {self.exp}')
            # Increase stats, sets self.exp to 0 and prints str of successful advance to new level
            self.advance = int(self.advance*1.2)
            self.dmg = int(self.dmg*1.2)
            self.maxhp = int(self.maxhp*1.2)
            self.exp = 0 
            logging.debug(f'Values after adding level self.advance: {self.advance} self.dmg: {self.dmg}, self.hp: {self.maxhp}, self.exp: {self.exp}')
            print(f'{Fore.YELLOW}You have lvl up!! Congratulations!!{Style.RESET_ALL}')
        # Requirement not met
        elif(self.advance>self.exp):
            print(f'{Fore.CYAN}You must gather more exp to lvl up{Style.RESET_ALL}')


    def eq_weapon (self, dmg: int, hp: int, name: str) -> str:
        # Add to self.eq another list of weapon and change stats of dmg, hp
        logging.debug(f'Bool value of len(self.eq)>0: {len(self.eq)>0}')
        # Checks if self.eq is empty or not
        if(len(self.eq)>0):
            return (f"{Fore.CYAN}You can't equip new weapon while holding: {self.eq[0]}{Style.RESET_ALL}")
        # Adds stats of weapon to self.object and append to list of self.eq
        else:
            logging.debug(f'Values before adding weapon object self.dmg: {self.dmg}, self.hp: {self.hp}, self.eq: {self.eq}, Weapon stats are dmg: {dmg}, hp: {hp}, name: {name}')
            self.dmg += dmg
            self.maxhp += hp
            self.eq.append([name, dmg, hp])
            logging.debug(f'Values after adding weapon object self.dmg: {self.dmg}, self.hp: {self.hp}, self.eq: {self.eq}')
            return(f"You are now holding {name}")


    def ueq_weapon (self, dmg: int, hp: int) -> str:
        # Substrack from self.eq list weapon and change stats of dmg, hp
        logging.debug(f'Values before substrack weapon object self.dmg: {self.dmg}, self.hp: {self.hp}, self.eq: {self.eq}, Weapon stats are dmg: {dmg}, hp: {hp}')
        self.dmg -= dmg
        self.maxhp -= hp
        uneqiped = self.eq.pop()
        logging.debug(f'Values after substrack weapon object self.dmg: {self.dmg}, self.hp: {self.hp}, self.eq: {self.eq}')
        return(f"{Fore.RED}You dropped {uneqiped[0]}{Style.RESET_ALL}")