import random, collections

possibilities = [1, 2, 3, 4, 5, 6]

# Rolling two dice accounts for probabilities in dice rolls
# Eg, rolling a "2" is less common than a "7", because there's only one way to roll a "2"
# This usually evens out in a game as long as Monopoly, but "realistic".
def roll(dice=2):
    roll_count = 0
    for _ in range(dice):
        roll_count += random.choice(possibilities)
    return roll_count

# Simple test to check that the probabilities of dice rolls are proportionate
def test(num=10000):
    roll_store = {}
    for _ in range(num):
        roll = roll()
        if roll in roll_store.keys():
            roll_store[roll] += 1
        else:
            roll_store[roll] = 1

    for key in sorted(roll_store):
        print("%s: %s" % (key, roll_store[key]))

