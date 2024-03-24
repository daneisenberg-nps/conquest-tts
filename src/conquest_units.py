import random

##################################
# class definitions

class Stand:
    def __init__(self, name, stand_data, special_rules = None):
        # initialize stand characteristics
        self.name: str = name
        self.move: int = self.get_closest_match(stand_data, 'move')
        self.volley: int = self.get_closest_match(stand_data, 'volley')
        self.clash: int = self.get_closest_match(stand_data, 'clash')
        self.attacks: int = self.get_closest_match(stand_data, 'attacks')
        self.wounds: int = self.get_closest_match(stand_data, 'wounds')
        self.resolve: int = self.get_closest_match(stand_data, 'resolve')
        self.defense: int = self.get_closest_match(stand_data, 'defense')
        self.evasion: int = self.get_closest_match(stand_data, 'evasion')

        # initialize stand special rules
        if special_rules:
            self.barrage_attacks: int = self.get_closest_match(special_rules['barrage'], 'attacks')

    # helper function if input data has typos
    def get_closest_match(self, data, target_key: str) -> int:
        target_key_lower = target_key.lower()
        for key in data:
            if key.lower() == target_key_lower:
                return data[key]
            elif key[0].lower() == target_key_lower[0]:
                return data[key] 
        return 0
    
    # dice rolling function
    def roll_dice(self, characteristic: str, num_rolls: int, isVerbose: bool = False) -> int:
        """
        Rolls a six-sided dice (d6) relative to the specified charastiric value.
        :param characteristic: The characteristic to roll for (e.g., clash)
        :param num_rolls: The numer of dice to roll
        """
        value = getattr(self, characteristic, 0)
        fail_count = 0
        success_count = 0
        for _ in range(num_rolls):
            roll_result = random.randint(1,6)
            if roll_result > value:
                fail_count += 1
            elif roll_result <= value:
                success_count += 1
        
        if isVerbose == True:
            print(f'Results for {num_rolls} rolls against {characteristic} of {value}')
            print(f'Num Successes: {success_count}')
            print(f'Num Failures: {fail_count}')
        
        return success_count, fail_count

    def attack_action(self, characteristic: str, num_stands: int, isVerbose: bool = False):
        fail_count = 0
        success_count = 0

        if characteristic == 'clash':
            num_rolls = self.attacks
        elif characteristic == 'volley':
            num_rolls = self.barrage_attacks
        else:
            raise ValueError(f'{characteristic} incorrect characteristic for an attack-type action, use clash or volley.')

        for _ in range(num_stands):
            num_success, num_fail = self.roll_dice(characteristic, num_rolls)
            fail_count += num_fail
            success_count += num_success

        if isVerbose == True:
            print(f'Results for {num_stands} stands of {self.name} completing a {characteristic} action')
            print(f'Num Successes: {success_count}')
            print(f'Num Failures: {fail_count}')
            print('')
        
    def display_characteristics(self):
        print('')
        print(f'Stand Characteristics:')
        print(f'Move: {self.move}')
        print(f'Volley: {self.volley}')
        print(f'Clash: {self.clash}')
        print(f'Attacks: {self.attacks}')
        print(f'Wounds: {self.wounds}')
        print(f'Resolve: {self.resolve}')
        print(f'Defense: {self.defense}')
        print(f'Evasion: {self.evasion}')
        print('')
        print(f'Special Rules:')
        print(f'Barrage: {self.barrage_attacks}')
        print('')


class Unit:
    def __init__(self, name: str, stands):
        self.name = name
        self.stands: object = stands
        
    def describe(self):
        unit_description = f'{self.name} is a unit consisting of the following stands:\n'
        for stand_name, quantity in self.stands.items():
            unit_description += f'- {stand_name}: {quantity}\n'
        return print(unit_description)
    
    def unit_attack_action(self, unit: object, characteristic: str, isVerbose: bool = False):
        num_stands = self.stands[unit.name]
        return unit.attack_action(characteristic, num_stands, isVerbose = True)





##########################
# Example data
legionaire_data = {
    'move': 5,
    'volley': 0,
    'clash': 2,
    'attacks': 4,
    'wounds': 4,
    'resolve': 0,
    'defense': 1,
    'evasion': 1,
}

archimandrite_data = {
    'move': 5,
    'volley': 0,
    'clash': 1,
    'attacks': 3,
    'wounds': 4,
    'resolve': 0,
    'defense': 1,
    'evasion': 2,
}

special_rules = {
    'barrage': {'attacks': 3, 'range': 20, 'ap': 2}
}


################################
# testing classes
legionaires = Stand(name = 'legionaires', stand_data = legionaire_data, special_rules = special_rules)
archimandrite = Stand(name = 'archimandrite', stand_data = archimandrite_data)

unit_composition = {}
units = {}

unit_composition[0] = {
    'legionaires': 5,
    'archimandrite': 1,
}

unit_composition[1] = {
    'legionaires': 3
}

for i in range(len(unit_composition)):
    name = 'legionaires_unit_' + str(i)
    units[i] = Unit(name = name, stands = unit_composition[i])
    units[i].describe()
    units[i].unit_attack_action(legionaires, 'clash', isVerbose = True)