import random
from Battle import *

class RandTrainer(Trainer):
  def Act(self):
    return random.randint(0,3)

if __name__ == "__main__":
  print("Let's get ready to Battle!")
  bulba = AllPokemon.MakeNewPokemon(1, 50)
  bulba.SetMoves(["Vine Whip", "Tackle"])
  pika = AllPokemon.MakeNewPokemon(25, 50)
  pika.SetMoves(["Thunder Shock", "Tackle"])
  
  gary = RandTrainer("Gary", bulba)
  ash = RandTrainer("Ash", pika)

  randBattle = Battle(gary, ash)
  randBattle.Battle(20)

