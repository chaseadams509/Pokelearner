from Move import *

class Pokemon():
  Number = 0
  Name = ""
  Type1 = Type.none
  Type2 = Type.none
  Level = 0
  BaseHP = 0
  BaseATK = 0
  BaseDEF = 0
  BaseSPATK = 0
  BaseSPDEF = 0
  BaseSPEED = 0
  PossibleMoves = AllMoves.Moveset
  
  CurrentHP = 0
  HP = 0
  Attack = 0
  Defense = 0
  SpAttack = 0
  SpDefense = 0
  Speed = 0
  Moves = [None, None, None, None]
  #Ability
  #Nature
  #HeldItem
  #IVs 
  #EVs

  def __init__(self, name, number, type1, type2, hp, atk, dff, spatk, spdef, spd, lvl = 5):
    self.Name = name
    self.Number = number
    self.Type1 = type1
    self.Type2 = type2
    self.Level =  lvl
    self.BaseHP = hp
    self.BaseATK = atk
    self.BaseDEF = dff
    self.BaseSPATK = spatk
    self.BaseSPDEF = spdef
    self.BaseSPEED = spd
    self.PossibleMoves = AllMoves.Moveset
    self.Moves = [None, None, None, None]
    self.__updateStats()

  def SetPossibleMoves(self, moves):
    self.PossibleMoves = {}
    for move in moves:
      if isinstance(move, str):
        move = AllMoves.Get(move)
      self.PossibleMoves[move.Name] = move

  def New(self, level):
    newPokemon = Pokemon(self.Name, self.Number, self.Type1, self.Type2, 
                    self.BaseHP, self.BaseATK, self.BaseDEF, 
                    self.BaseSPATK, self.BaseSPDEF, self.BaseSPEED, 
                    level)
    newPokemon.PossibleMoves = self.PossibleMoves
    return newPokemon

  def AddMove(self, move, ndx):
    if isinstance(move, str):
      move = AllMoves.Get(move)
    if move and isinstance(ndx, int) and ndx < 4 and ndx >= 0:
      if not move.Name in self.PossibleMoves:
        raise ValueError("Move " + move.Name + " was not found in possible moves")
      self.Moves[ndx] = move
      return
    raise ValueError("Move was not found passed properly")

  def SetMoves(self, moves):
    for ndx, move in enumerate(moves):
      if isinstance(move, str):
        move = AllMoves.Get(move)
      if not move.Name in self.PossibleMoves:
        raise ValueError("Move " + move.Name + " was not found in possible moves")
      self.Moves[ndx] = move

  def __updateStats(self):
    self.__calcHP()
    self.Attack = self.__calcStat(self.BaseATK)
    self.Defense = self.__calcStat(self.BaseDEF)
    self.SpAttack = self.__calcStat(self.BaseSPATK)
    self.SpDefense = self.__calcStat(self.BaseSPDEF)
    self.Speed = self.__calcStat(self.BaseSPEED)
    self.CurrentHP = self.HP

  def __calcHP(self):
    self.HP = int((2 * self.BaseHP * self.Level) / 100) + self.Level + 10
    return self.HP

  def __calcStat(self, base):
    return int((2 * base * self.Level) / 100) + 5

  def __str__(self):
    output = ""
    output += self.Name + ":  #" + str(self.Number) + "\n"
    output += "\tType: " + str(self.Type1.name) + " / "  + str(self.Type2.name) + "\n"
    output += "\tLevel: " + str(self.Level) + "\n"
    output += "\tHP: " + str(self.CurrentHP) + " / " + str(self.HP) + "\n"
    output += "\tAttack          : " + str(self.Attack) + "\n"
    output += "\tDefense         : " + str(self.Defense) + "\n"
    output += "\tSpecial Attack  : " + str(self.SpAttack) + "\n"
    output += "\tSpecial Defense : " + str(self.SpDefense) + "\n"
    output += "\tSpeed           : " + str(self.Speed) + "\n"
    output += "\tMoves: \n"
    for move in self.Moves:
      if move: 
        output += "\t\t" + str(move.Name) + "\n"
    return output

  def Print(self):
    print(self)

class PokemonList():
  Pokemonset = {}
  Pokedex = {}
  
  def __init__(self):
    self.Pokemonset = {}
    self.Pokedex = {}
    return

  def AddSpecies(self, name, number, type1, type2, hp, atk, dff, spatk, spdef, spd):
    newPokemon = Pokemon(name, number, type1, type2, hp, atk, dff, spatk, spdef, spd)
    self.Pokemonset[name] = newPokemon
    self.Pokedex[number] = name
    return

  def SetSpeciesMoves(self, name, moves):
    if isinstance(name, int):
      name = self.Pokedex[name]
    species = self.Pokemonset[name]
    species.SetPossibleMoves(moves)
    return
    

  def MakeNewPokemon(self, name, level):
    if isinstance(name, int):
      name = self.Pokedex[name]
    species = self.Pokemonset[name]
    newEntry = species.New(level)
    return newEntry

AllPokemon = PokemonList()
AllPokemon.AddSpecies("Bulbasaur", 1, Type.grass, Type.poison, 45, 49, 49, 65, 65, 45)
AllPokemon.SetSpeciesMoves("Bulbasaur", ["Tackle", "Vine Whip"])
AllPokemon.AddSpecies("Charmander", 4, Type.fire, Type.none, 39, 52, 43, 60, 50, 65)
AllPokemon.SetSpeciesMoves("Charmander", ["Tackle", "Ember"])
AllPokemon.AddSpecies("Squirtle", 6, Type.water, Type.none, 44, 48, 65, 50, 64, 43)
AllPokemon.SetSpeciesMoves("Squirtle", ["Tackle", "Water Gun"])
AllPokemon.AddSpecies("Pikachu", 25, Type.electric, Type.none, 35, 55, 40, 50, 50, 90)
AllPokemon.SetSpeciesMoves("Pikachu", ["Tackle", "Thunder Shock"])

if __name__ == "__main__":
  pika = AllPokemon.MakeNewPokemon(25, 50)
  pika.SetMoves(["Tackle", "Thunder Shock"])
  bulba = AllPokemon.MakeNewPokemon(1, 50)
  bulba.SetMoves(["Tackle", "Vine Whip"])
  char = AllPokemon.MakeNewPokemon(4, 50)
  char.SetMoves(["Tackle", "Ember"])
  squirt = AllPokemon.MakeNewPokemon(6, 50)
  squirt.SetMoves(["Tackle", "Water Gun"])
  
  print(bulba)
  print(char)
  print(squirt)
  print(pika)
  
