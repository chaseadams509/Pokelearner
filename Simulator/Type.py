from enum import Enum

class Type(Enum):
  none = 0
  normal = 1
  fire = 2
  water = 3
  electric = 4
  grass = 5
  ice = 6
  fighting = 7
  poison = 8
  ground = 9
  flying = 10
  psychic = 11
  bug = 12
  rock = 13
  ghost = 14
  dragon = 15
  dark = 16
  steel = 17
  fairy = 18

TypeChart = [[1.0 for i in range(19)] for j in range(19)]
superEffective = []
notVeryEffective = []
immuneEffective = []

superEffective.append([Type.fire, Type.grass])
superEffective.append([Type.water, Type.fire])
superEffective.append([Type.grass, Type.water])
superEffective.append([Type.electric, Type.water])

notVeryEffective.append([Type.fire, Type.water])
notVeryEffective.append([Type.grass, Type.fire])
notVeryEffective.append([Type.water, Type.grass])
notVeryEffective.append([Type.electric, Type.grass])
notVeryEffective.append([Type.electric, Type.electric])
notVeryEffective.append([Type.grass, Type.grass])
notVeryEffective.append([Type.water, Type.water])
notVeryEffective.append([Type.fire, Type.fire])

for s in superEffective:
  TypeChart[s[0].value][s[1].value] = 2.0
for n in notVeryEffective:
  TypeChart[n[0].value][n[1].value] = 0.5
for i in immuneEffective:
  TypeChart[i[0].value][i[1].value] = 0.0

if __name__ == "__main__":
  print("Water->Electric: " + str(TypeChart[Type.water.value][Type.electric.value]))
  print("Water->Fire: " + str(TypeChart[Type.water.value][Type.fire.value]))
  print("Water->Water: " + str(TypeChart[Type.water.value][Type.water.value]))
