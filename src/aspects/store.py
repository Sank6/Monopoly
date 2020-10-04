def general_repairs(houses, hotels):
    return 25 * houses + 100 * hotels

def street_repairs(houses, hotels):
    return 40 * houses + 115 * hotels

def birthday(playercount):
    return 10 * playercount

chance = {
    'Advance to "Go"': {
        "action": "move+",
        "value": 0
    },
    'Go to jail. Move directly to jail. Do not pass "Go". Do not collect £200': {
        "action": "move",
        "value": 10
    },
    'Advance to Pall Mall. If you pass "Go" collection £200': {
        "action": "move+",
        "value": 11
    },
    'Take a trip to Marylebone Station and if you pass "Go" collect £200': {
        "action": "move+",
        "value": 5
    },
    'Advance to Trafalgar Square. If you pass "Go" collect £200': {
        "action": "move+",
        "value": 24
    },
    'Advance to Mayfair': {
        "action": "move",
        "value": 39
    },
    'Go back three spaces': {
        "action": "back",
        "value": 3
    },
    'Make general repairs on all of your houses. For each house pay £25. For each hotel pay £100': {
        "action": "payf",
        "value": general_repairs
    },
    'You are assessed for street repairs: £40 per house, £115 per hotel': {
        "action": "payf",
        "value": street_repairs
    },
    'Pay school fees of £150': {
        "action": "pay",
        "value": 150
    },
    '"Drunk in charge" fine £20': {
        "action": "pay",
        "value": 20
    },
    'Speeding fine £15': {
        "action": "pay",
        "value": 15
    },
    'Your building loan matures. Receive £150': {
        "action": "receive",
        "value": 150
    },
    'You have won a crossword competition. Collect £100': {
        "action": "receive",
        "value": 100
    },
    'Bank pays you dividend of £50': {
        "action": "receive",
        "value": 50
    },
    'Get out of jail free. This card may be kept until needed or sold': {
        "action": "jail card",
        "value": None
    },
}

community = {
    'Advance to "Go"': {
        "action": "move+",
        "value": 0
    },
    'Go back to Old Kent Road': {
        "action": "move",
        "value": 1
    },
    'Go to jail. Move directly to jail. Do not pass "Go". Do not collect £200': {
        "action": "move",
        "value": 10
    },
    'Pay hospital £100': {
        "action": "pay",
        "value": 100
    },
    'Doctor\'s fee. Pay £50': {
        "action": "pay",
        "value": 50
    },
    'Pay your insurance premium £50': {
        "action": "pay",
        "value": 50
    },
    'Bank error in your favour. Collect £200': {
        "action": "receive",
        "value": 200
    },
    'Annuity matures. Collect £100': {
        "action": "receive",
        "value": 100
    },
    'You inherit £100': {
        "action": "receive",
        "value": 100
    },
    'From sale of stock you get £50': {
        "action": "receive",
        "value": 50
    },
    'Receive interest on 7% preference shares: £25': {
        "action": "receive",
        "value": 25
    },
    'Income tax refund. Collect £20': {
        "action": "receive",
        "value": 20
    },
    'You have won second prize in a beauty contest. Collect £10': {
        "action": "receive",
        "value": 10
    },
    'It is your birthday. Collect £10 from each player': {
        "action": "receivef",
        "value": birthday
    },
    'Get out of jail free. This card may be kept until needed or sold': {
        "action": "jail card",
        "value": None
    },
    'Pay a £10 fine or take a "Chance"': {
        "action": "pay",
        "value": 10
    }
}

board = [
    'Go',
    'Old Kent Road',
    'Community Chest',
    'Whitechapel Road',
    'Income Tax',
    'Marylebone Station',
    'The Angel Islington',
    'Chance',
    'Euston Road',
    'Pentonville Road',
    'Jail',
    'Pall Mall',
    'Electric Company',
    'Whitehall',
    'Northumberland Avenue',
    'Fenchurch Street Station',
    'Bow Street',
    'Community Chest',
    'Marlborough Street',
    'Vine Street',
    'Free Parking',
    'Strand',
    'Chance',
    'Fleet Street',
    'Trafalgar Square',
    'King’s Cross Station',
    'Leicester Square',
    'Coventry Street',
    'Water Works',
    'Piccadilly',
    'Go to Jail',
    'Regent Street',
    'Oxford Street',
    'Bond Street',
    'Liverpool Street Station',
    'Chance',
    'Park Lane',
    'Super Tax',
    'Mayfair'
]