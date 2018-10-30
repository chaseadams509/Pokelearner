import random
from BaseTrainer import *

class Battle():
    Trainer1 = None
    Trainer2 = None
    Winner = 0

    def __init__(self, trainer1, trainer2):
      self.Trainer1 = trainer1
      self.Trainer2 = trainer2
      self.Winner = 0

    def Battle(self, max_turns):
      for i in range(max_turns):
        print("~~~Turn " + str(i))
        self.TakeTurn()
        if self.Winner != 0:
          break
      if self.Winner == 1:
        print("Trainer " + self.Trainer1.Name + " Won!")
      elif self.Winner == 2:
        print("Trainer " + self.Trainer2.Name + " Won!")
      else:
        print("There was no winner...")
      return

    def TakeTurn(self):
      action1 = self.Trainer1.Act()
      action2 = self.Trainer2.Act()
      if self.Trainer1.ActivePokemon.Speed > self.Trainer2.ActivePokemon.Speed:
        self.attack(self.Trainer1.ActivePokemon, action1, self.Trainer2.ActivePokemon)
        self.attack(self.Trainer2.ActivePokemon, action2, self.Trainer1.ActivePokemon)
      else: 
        self.attack(self.Trainer2.ActivePokemon, action2, self.Trainer1.ActivePokemon)
        self.attack(self.Trainer1.ActivePokemon, action1, self.Trainer2.ActivePokemon)
      self.checkForWinner()
      return

    def attack(self, pokemon1, attack, pokemon2):
      if pokemon1.CurrentHP <= 0:
        return
      move = pokemon1.Moves[attack]
      if not move:
        print(pokemon1.Name + "Didn't Move!")
        return
      print(pokemon1.Name + " used " + move.Name + "!")
      if move.Accuracy < 1.0 and move.Accuracy > 0.0:
        print("It could miss...")
        hit = random.random()
        if move.Accuracy < hit:
          print("The move missed!")
          return

      level = pokemon1.Level
      power = move.BasePower

      attackPower = 0
      defensePower = 0
      if move.Category == Category.physical:
        attackPower = pokemon1.Attack
        defensePower = pokemon2.Defense
      elif move.Category == Category.special:
        attackPower = pokemon1.SpAttack
        defensePower = pokemon2.SpDefense
      else:
        print("No damage!")
        return

      stab = 1.0
      if move.Type == pokemon1.Type1 or move.Type == pokemon1.Type2:
        print("\tSame-type attack bonus")
        stab = 1.5
      effectiveness = 1.0
      effectiveness *= TypeChart[move.Type.value][pokemon2.Type1.value]
      effectiveness *= TypeChart[move.Type.value][pokemon2.Type2.value]
      if effectiveness > 1.0:
        print("\tIt's super effective!")
      elif effectiveness <= 0.0:
        print("\tIt had no effect...")
      elif effectiveness < 1.0:
        print("\tIt's not very effective.")

      damage = self.calcDamage(power, level, attackPower, defensePower, stab, effectiveness)
      pokemon2.CurrentHP -= damage
      if pokemon2.CurrentHP <= 0:
        print( pokemon2.Name + " Fainted!")
        pokemon2.CurrentHP = 0
      return

    def calcDamage(self, pwr, lvl, atk, dff, stab, effective):
      rng = random.uniform(0.85, 1.00)
      lvlPower = ((2.0 * float(lvl)) / 5.0) + 2.0
      denom = lvlPower * float(pwr) * (float(atk) / float(dff))
      dmg = ( (denom / 50.0) + 2.0) * rng * stab * effective
      return int(dmg)
      
    def checkForWinner(self):
      if self.Trainer1.ActivePokemon.CurrentHP == 0:
        self.Winner = 2
      if self.Trainer2.ActivePokemon.CurrentHP == 0:
        self.Winner = 1
      return

if __name__ == "__main__":
  print("Let's get ready to Battle!")
  bulba = AllPokemon.MakeNewPokemon(1, 50)
  bulba.SetMoves(["Vine Whip", "Tackle"])
  pika = AllPokemon.MakeNewPokemon(25, 50)
  pika.SetMoves(["Thunder Shock", "Tackle"])
  
  gary = Trainer("Gary", bulba)
  ash = Trainer("Ash", pika)

  battle1 = Battle(gary, ash)
  battle1.Battle(20)

