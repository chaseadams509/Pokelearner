from Pokemon import *

class Trainer():
    Name = ""
    Pokemon1 = None
    #Pokemon2
    #Pokemon3
    #Pokemon4
    #Pokemon5
    #Pokemon6
    ActivePokemon = None

    def __init__(self, name, pokemon):
      self.Name = name
      self.Pokemon1 = pokemon
      self.ActivePokemon = self.Pokemon1

    def Act(self):
      return 0
