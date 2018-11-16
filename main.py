#Things to add: pp (just add tackle_pp etc variables, ez), accuracy, critical hits, type matchups, exp
#Some sort of temporary hp system I guess
#The opponents hits back
#Text along the lines of "*pokemon* used tackle!"

# Pokemon basic battle sim or smth
import math
import random

def dmgcalc(LVL, (SP)ATK, (SP)DEF, PWR = 40):
  opponents_pkmn[1] -= int((((((2 * LVL) / 5 + 2) * PWR * (SP)ATK) / (SP)DEF) / 50 + 2) * random.uniform(0.85, 1))

def dmgtext(HP):
  if HP <= 0:
    print("Your opponent's Pokémon has 0 HP left.")
  else:
    print("Your opponent's Pokémon has", opponents_pkmn[1], "HP left.")


#stats are ordered [0] = LVL, [1] = HP, [2] = ATK, [3] = DEF, [4] = SP.ATK, [5] = SP.DEF, [6] = SPD
your_pkmn =      [100, 100, 100, 100, 100, 100, 100]

opponents_pkmn = [100, 100, 100, 100, 100, 100, 100]


print("Pokemans batteru")
a = 0
r = 0
while a == 0:
  r += 1
  first = input("1: Attack, 2: Run")
  print()
  if first == "1":
    print("1: Tackle, 2: Water Gun")
    choice = input("Choose attack:")
    print()
    if choice == "1": #tackle
      dmgcalc(your_pkmn[0], your_pkmn[1], opponents_pkmn[2], 40)
      dmgtext(opponents_pkmn[1])
    elif choice == "2": #water gun
      dmgcalc(your_pkmn[0], your_pkmn[3], opponents_pkmn[4], 40)
      dmgtext(opponents_pkmn[1])
  elif first == "2":
    print("Too slow")
  else:
    print('Write either "1" or "2"')
  if opponents_pkmn[1] <= 0:
    print("You won!")
    break

print("Hackerman")
