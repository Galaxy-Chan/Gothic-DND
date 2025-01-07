import random
#for dice

#creates class for 20 sided die
class Die:
    def __init__(self, sides=20):
        self.sides = sides
    def roll(self):
        return random.randint(1, self.sides)

#making print statement for test
def dieroll(Die):
    d20 = Die()
    result = d20.roll()
    print("You rolled a: ", result,"\n")

#creates character with only name input
class Char:
    def __init__(self):
        self.input_name = input(str("Whats your characters name?: "))
    def charname(self):
        print("Character name: ", self.input_name)

#makes dnd stats bound to character class
class Stats(Char):
    def __init__(self):
        print("\nMinimum stat 8, max 15.\n")
        while True:
          try:
            self.Strength = int(input("Strength?: "))
            if self.Strength >= 8 and self.Strength <= 15:
              break
            else:
              print("invalid input")
          except:
            print("invalid input.")
        while True:
          try:
            self.Dex = int(input("Dexterity?: "))
            if self.Dex >= 8 and self.Dex <= 15:
              break
            else:
              print("invalid input")
          except:
            print("invalid input.")
        while True:
          try:
            self.Const = int(input("Constistution?: "))
            if self.Const >= 8 and self.Const <= 15:
              break
            else:
              print("invalid input")
          except:
            print("invalid input.")
        while True:
          try:
            self.Intell = int(input("Intelligence?: "))
            if self.Intell >= 8 and self.Intell <= 15:
              break
            else:
              print("invalid input")
          except:
            print("invalid input.")
        while True:
          try:
            self.Wisdom = int(input("Wisdom?: "))
            if self.Wisdom >= 8 and self.Wisdom <= 15:
              break
            else:
              print("invalid input")
          except:
            print("invalid input.")
        while True:
          try:
            self.Charisma = int(input("Charisma?: "))
            if self.Charisma >= 8 and self.Charisma <= 15:
              break
            else:
              print("invalid input")
          except:
            print("invalid input.")

    def PrintBaseStats(self):
        print(f"Strength: {self.Strength}\nDexterity: {self.Dex}\nConstitution(endurance): {self.Const}\nIntelligence: {self.Intell}\nWisdom: {self.Wisdom}\nCharisma: {self.Charisma}\n")
        print("You have 27 points you may spend into these values! You may remove some points in others to put to other values.\n")

#creates gameplay rotates with character, die, and stats to be called
class GameplayRota(Stats, Char, Die):
    def __init__(self):
        character = Char()
        stats = Stats()
        character.charname()
        stats.PrintBaseStats()

#making definitions for small test loops
def Play():
    GameplayRota()

#testing the die rolling
def DieTest():
    dieroll(Die)

#small testing dynamic for myself, includes main screen after testing and stop point
def Testdynamics():
    user1 = input(str("Test die or play?: 1 = test, 2 = play\n"))
    if user1 == "1":
        DieTest()
        user2 = input(str("Main screen? 1=Y 2=N: "))
        if user2 == "1":
            Testdynamics()
        else:
            print("stopping.. ")
            pass
    else:
        Play()

Testdynamics()