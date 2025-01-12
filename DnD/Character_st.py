#creates character with only name input
class Char:
    def __init__(self):
        self.input_name = input(str("Whats your characters name?: "))
    def charname(self):
        print("Character name: ", self.input_name)

#makes dnd stats bound to character class
class Stats(Char):
    def __init__(self):
        PointValue = 27
        print("\nMinimum stat 8, max 15.")
        print("You have 27 points to spend into these values.")
        while True:
          try:
            self.Strength = int(input("Strength?: "))
            if self.Strength >= 8 and self.Strength <= 15:
              PointValue = PointValue - (self.Strength - 8)
              print(f"You have {PointValue} points left!\n")
              break
            else:
              print("invalid input")
          except:
            print("invalid input.")
          
        while True:
          try:
            self.Dex = int(input("Dexterity?: "))
            if self.Dex >= 8 and self.Dex <= 15:
              PointValue = PointValue - (self.Dex - 8)
              print(f"You have {PointValue} points left!\n")
              break
            else:
              print("invalid input")
          except:
            print("invalid input.")
        while True:
          try:
            self.Const = int(input("Constistution?: "))
            if self.Const >= 8 and self.Const <= 15:
              PointValue = PointValue - (self.Const - 8)
              print(f"You have {PointValue} points left!\n")
              break
            else:
              print("invalid input")
          except:
            print("invalid input.")
        while True:
          try:
            self.Intell = int(input("Intelligence?: "))
            if self.Intell >= 8 and self.Intell <= 15:
              if PointValue - (self.Intell -8) < 8:
                print("You don't have enough points for that!")
              else:
                PointValue = PointValue - (self.Intell - 8)
                print(f"You have {PointValue} points left!")
                break
          except:
            print("invalid input.")
        while True:
          try:
            self.Wisdom = int(input("Wisdom?: "))
            if self.Wisdom >= 8 and self.Wisdom <= 15:
              if PointValue - (self.Wisdom -8) < 8:
                print("You don't have enough points for that!")
              else:
                PointValue = PointValue - (self.Wisdom - 8)
                print(f"You have {PointValue} points left!")
                break
            else:
              print("invalid input")
          except:
            print("invalid input.")
        while True:
          try:
            self.Charisma = int(input("Charisma?: "))
            if self.Charisma >= 8 and self.Charisma <= 15:
              if PointValue - (self.Charisma -8) < 8:
                print("You don't have enough points for that!")
              else:
                PointValue = PointValue - (self.Charisma - 8)
                print(f"You have {PointValue} points left!")
                break
            else:
              print("invalid input")
          except:
            print("invalid input.")

    def PrintBaseStats(self, PointValue):
        print(f"Strength: {self.Strength}\nDexterity: {self.Dex}\nConstitution(endurance): {self.Const}\nIntelligence: {self.Intell}\nWisdom: {self.Wisdom}\nCharisma: {self.Charisma}\n")
        print(f"You have a remainder of {PointValue} points!")
