'''
    Program: attack.py
    Function: Handles all attack features of RPG combat
    Author: Matt Rzepka
'''
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item



#Create black magic
fire = Spell('Fire', 10, 100, 'black')
thunder = Spell('Thunder', 10, 100, 'black')
blizzard = Spell('Blizzard', 10, 100, 'black')
meteor = Spell('Meteor', 20, 200, 'black')
quake = Spell('Quake', 14, 140, 'black')

#Create white magic
cure = Spell('Cure', 12, 120, 'white')
cura = Spell('Cure', 18, 200, 'white')

#Create items
potion = Item('Potion', 'potion', 'heals 50 hp', 50)
hi_potion = Item('Hi-Potion', 'potion', 'heals 100 hp', 100)
super_potion = Item('Super-Potion', 'potion', 'heals 500 hp', 500)
elixer = Item('Elixer', 'elixer', 'fully restores hp and mp of one party member', 9999)
mega_elixer = Item('Mega-Elixer', 'elixer', 'fully restores hp and mp of all party members', 9999)

grenade = Item('Grenade', 'attack', 'deals 500 damage', 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [{'item': potion, 'quantity': 5},
                {'item': hi_potion, 'quantity': 5},
                {'item': super_potion, 'quantity': 5},
                {'item': elixer, 'quantity': 5},
                {'item': mega_elixer, 'quantity': 5},
                {'item': grenade, 'quantity': 5}]

player1 = Person('Valos', 3260, 65, 60, 34, player_spells, player_items)
player2 = Person('Nick ', 4160, 65, 60, 34, player_spells, player_items)
player3 = Person('Robot', 2890, 65, 60, 34, player_spells, player_items)
enemy = Person('Baddy McBadbat', 6000, 65, 45, 25, [], [])

players = [player1, player2, player3]

running = True

while running:
    print('======================')

    for player in players:
        player.get_stats()
        player.choose_action()
        choice = int(input('Choose an action '))

        if choice == 0:
            damage = player.generate_damage()
            enemy.take_damage(damage)
            print('You attacked for', damage,
                  'points of damage.')
        elif choice == 1:
            player.choose_magic()
            magic_choice = int(input('Choose a spell'))

            spell = player.magic[magic_choice]
            magic_damage = spell.generate_magic_damage()
            if spell.cost > player.get_mp():
                print(bcolors.FAIL + '\nNot enough MP' + bcolors.ENDC)
                continue
            if spell.type == 'white':
                player.heal(magic_damage)
            else:
                enemy.take_damage(magic_damage)

            player.reduce_mp(spell.cost)
            print(bcolors.OKBLUE + '\n' + spell.name + (' heals' if spell.type =='white' else ' deals'),
                  str(magic_damage), 'points of damage', bcolors.ENDC)

        elif choice == 2:
            player.choose_item()
            item_choice = int(input('Choose an item'))

            item = player.items[item_choice]['item']

            if player.items[item_choice]['quantity']:
                player.items[item_choice]['quantity'] -= 1
                print('You have ' + str(player.items[item_choice]['quantity']) + ' of', item.name, 'remaining')
            else:
                print('You do not have any more of', item.name, 'to use!')
                continue

            if item.type == 'potion':
                player.heal(item.property)
                print(bcolors.OKGREEN + 'healed for', item.property, 'with', item.name)
            elif item.type == 'elixer':
                player.hp = player.max_hp
                player.mp = player.max_mp
                print(bcolors.OKGREEN + str(item.name), 'fully restores hp and mp' + bcolors.ENDC)
            elif item.type == 'attack':
                enemy.take_damage(item.property)
                print(bcolors.FAIL + str(item.name) + 'deals', item.property, 'damage' + bcolors.ENDC)


        enemy_damage = enemy.generate_damage()
        player.take_damage(enemy_damage)
        print(bcolors.FAIL + 'Enemy attacked for', enemy_damage,
              'points of damage.' + bcolors.ENDC)

    print('=====================')
    print('Enemy HP:' + bcolors.FAIL + str(enemy.get_hp()), '/', str(enemy.get_max_hp()) + bcolors.ENDC)
    print('Your HP:' + bcolors.OKGREEN +  str(player.get_hp()), '/', str(player.get_max_hp()) + bcolors.ENDC)
    print('Your MP: ' + bcolors.OKBLUE + str(player.get_mp()), '/', str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + 'You Win!' + bcolors.ENDC)
        running = False
    if player.get_hp() == 0:
        print(bcolors.FAIL + 'You Lose!' + bcolors.ENDC)
        running = False

# print(bcolors.FAIL + bcolors.BOLD + 'AN ENEMY ATTACKS!' + bcolors.ENDC)
