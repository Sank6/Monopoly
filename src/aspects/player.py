import random

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
    def __init__(self, board):
        # Board data
        self.board = board
        self.board.players.append(self)
        self.player_id = len(self.board.players)

        # Position on the board from 0-39
        self.position = 0

        # Starting money
        self.money = 1500

        # Status: 1 = Playing, 0 = Out
        self.status = 1

    def move(self):
        dice = roll()
        if dice != False:
            self.position = (self.position + dice)  % 40
        else: # Jail
            self.position = 10
        
        if self.position == 30:
            self.position = 10

    def pay(self, x):
        self.money -= x
        if self.money < 0:
            self.status = 0

    def chance_community_chest(self):
        location = self.board.squares[self.position]

        pile = None
        if location == "Chance":
            pile = "chance_set"
        elif location == "Community":
            pile = "community_set"
        
        if pile != None:
            card = getattr(self.board, pile)[0]
            getattr(self.board, pile).append(card)
            getattr(self.board, pile).pop(0)

            starting = self.position

            # Movement
            if card["action"] == "move" or card["action"] == "move+":
                self.position = card["value"]
            elif card["action"] == "back":
                self.position = self.position - card["value"]

            # Money
            if card["action"] == "move+" and self.position < starting:
                self.money += 200

            if card["action"] == "pay":
                self.pay(card["value"])
            
            if card["action"] == "receive":
                self.money += card["value"]

    def play(self):
        starting = self.position
        self.move()

        if self.position < starting:
            self.money += 200

        self.chance_community_chest()

        self.position = self.position % 40