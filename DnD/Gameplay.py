from Character_st import*
from Lore_Story import*
from Rooms import*
import random

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

def DieTest():
    dieroll(Die)

#creates gameplay rotates with character, die, and stats to be called
class GameplayRota(Stats, Char, Die):
    def __init__(self):
        character = Char()
        stats = Stats()
        character.charname()
        stats.PrintBaseStats()

def Play():
    GameplayRota()
    
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