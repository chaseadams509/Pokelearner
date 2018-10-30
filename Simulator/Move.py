from Category import *
from Type import *

class Move():
  Name = ""
  BasePower = 0
  Accuracy = 1.0
  Type = Type.none
  PowerPoints = -1
  RemainingPP = -1
  Category = Category.none
  # Secondary  
  contact = False

  def __init__(self, name, power, acc, elem, pp, cat):
    self.Name = name
    self.BasePower = power
    self.Accuracy = acc
    self.Type = elem
    self.PowerPoints = pp
    self.RemainingPP = pp
    self.Category = cat
    return

  def __str__(self):
    output = ""
    output += self.Name + ":\n"
    output += "\tBase Power: " + str(self.BasePower) + "\n"
    output += "\tAccuracy: " + str(self.Accuracy) + "\n"
    output += "\tType: " + self.Type.name + "\n"
    output += "\tPP: " + str(self.RemainingPP) + " / " + str(self.PowerPoints) + "\n"
    output += "\tCategory: " + self.Category.name
    return output

  def Print(self):
    print(self)


class MoveList():
  Moveset = {}
  
  def __init__(self):
    self.Moveset = {}
    return

  def AddMove(self, name, power, acc, elem, pp, cat):
    newMove = Move(name, power, acc, elem, pp, cat)
    self.Moveset[name] = newMove
    return newMove

  def Get(self, name):
    return self.Moveset[name]

  def PrintAll(self):
    for move in self.Moveset:
      print(self.Moveset[move])

AllMoves = MoveList()
AllMoves.AddMove("Ember", 40, 1.0, Type.fire, 25, Category.special)
AllMoves.AddMove("Water Gun", 40, 1.0, Type.water, 25, Category.special)
AllMoves.AddMove("Vine Whip", 45, 1.0, Type.grass, 25, Category.physical)
AllMoves.AddMove("Thunder Shock", 40, 1.0, Type.electric, 30, Category.special)
AllMoves.AddMove("Tackle", 40, 1.0, Type.normal, 35, Category.physical)

if __name__ == "__main__":
  AllMoves.PrintAll()
