import random
from aspects.store import *

chance_set = list(chance.values())
community_set = list(community.values())

def roll(count=0, doubles=0):
    if doubles == 3:
        return False
    roll_count = 0
    double_roll = False
    for _ in range(2):
        choice = random.choice([1, 2, 3, 4, 5, 6])
        if roll_count == choice:
            double_roll = True
        roll_count += choice
    
    if double_roll:
        again = roll(count + roll_count, doubles + 1)
        return again
    else:
        return count + roll_count

class Player:
    def __init__(self):
        # Position on the board from 0-39
        self.position = 0

    def move(self):
        dice = roll()
        if dice != False:
            self.position = (self.position + dice)  % 39
        else: # Jail
            self.position = 10
        
        if self.position == 30:
            self.position = 10

    def play(self):
        self.move()
        location = board[self.position]

        pile = None
        if location == "Chance":
            pile = chance_set
        elif location == "Community":
            pile = community_set
        
        if pile != None:
            card = pile[0]
            pile.append(pile[0])
            pile.pop(0)
            if (card["action"] == "move" or card["action"] == "move+"):
                self.position = card["value"]
            elif (card["action"] == "back"):
                self.position = self.position - card["value"]
        
        self.position = self.position % 39
        p = str(self.position)
        if len(p) == 1:
            p = "0" + p
        return p + ". " + board[self.position]