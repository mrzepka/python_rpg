import random
from .magic import Spell

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attackHigh = atk + 10
        self.attackLow = atk - 10
        self.defense = df
        self.magic = magic
        self.actions = ['Attack', 'Magic', 'Items']
        self.items = items

    def generate_damage(self):
        return random.randrange(self.attackLow, self.attackHigh)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, healing):
        self.hp += healing
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 0
        print('ACTIONS')
        for item in self.actions:
            print(str(i)+':', item)
            i += 1

    def choose_magic(self):
        i = 0
        print('MAGIC')
        for spell in self.magic:
            print(str(i) + ':', spell.name, '( cost:', str(spell.cost), ')')
            i += 1

    def choose_item(self):
        i = 0
        print('ITEMS')
        for item in self.items:
            print(str(i) + '.', item['item'].name, ":", item['item'].desc, '(x', item['quantity'], ')')
            i += 1

    def get_stats(self):
        print('\n\n')
        print('NAME               HP                                 MP')
        print('                    _________________________         __________ ')
        print(bcolors.BOLD + self.name + '    ' +
              str(self.hp) + '/' + str(self.max_hp) +' |' + bcolors.OKGREEN + '/////////////////////////' + bcolors.ENDC + bcolors.BOLD +
              '| '+ str(self.mp) + '/' + str(self.max_mp) +' |' + bcolors.OKBLUE + '//////////' + bcolors.ENDC + bcolors.BOLD + '|' + bcolors.ENDC)