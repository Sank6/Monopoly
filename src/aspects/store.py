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

properties = [
    1, 3, 5, 6, 8, 9, 11, 13, 14, 15, 16, 18, 19, 21, 23, 24, 25, 26, 27, 29, 31, 32, 34, 35, 37, 39
]

utilities = [
    12, 28
]

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
    'Community Chest',
    'Bond Street',
    'Liverpool Street Station',
    'Chance',
    'Park Lane',
    'Super Tax',
    'Mayfair'
]

property_info = [
  {
    "colour": "Brown",
    "index": 1,
    "name": "Old Kent Road",
    "value": 60,
    "house_price": 30
  },
  {
    "colour": "Brown",
    "index": 3,
    "name": "Whitechapel Road",
    "value": 60,
    "house_price": 30
  },
  {
    "colour": "Station",
    "index": 5,
    "name": "King's Cross station",
    "value": 200,
    "house_price": ""
  },
  {
    "colour": "Light blue",
    "index": 6,
    "name": "The Angel, Islington",
    "value": 100,
    "house_price": 50
  },
  {
    "colour": "Light blue",
    "index": 8,
    "name": "Euston Road",
    "value": 100,
    "house_price": 50
  },
  {
    "colour": "Light blue",
    "index": 9,
    "name": "Pentonville Road",
    "value": 120,
    "house_price": 60
  },
  {
    "colour": "Pink",
    "index": 11,
    "name": "Pall Mall",
    "value": 140,
    "house_price": 70
  },
  {
    "colour": "Pink",
    "index": 13,
    "name": "Whitehall",
    "value": 140,
    "house_price": 70
  },
  {
    "colour": "Pink",
    "index": 14,
    "name": "Northumberland Avenue",
    "value": 160,
    "house_price": 80
  },
  {
    "colour": "Station",
    "index": 15,
    "name": "Marylebone station",
    "value": 200,
    "house_price": ""
  },
  {
    "colour": "Orange",
    "index": 16,
    "name": "Bow Street",
    "value": 180,
    "house_price": 90
  },
  {
    "colour": "Orange",
    "index": 18,
    "name": "Marlborough Street",
    "value": 180,
    "house_price": 90
  },
  {
    "colour": "Orange",
    "index": 19,
    "name": "Vine Street",
    "value": 200,
    "house_price": 100
  },
  {
    "colour": "Red",
    "index": 21,
    "name": "Strand",
    "value": 220,
    "house_price": 110
  },
  {
    "colour": "Red",
    "index": 23,
    "name": "Fleet Street",
    "value": 220,
    "house_price": 110
  },
  {
    "colour": "Red",
    "index": 24,
    "name": "Trafalgar Square",
    "value": 240,
    "house_price": 120
  },
  {
    "colour": "Station",
    "index": 25,
    "name": "Fenchurch Street station",
    "value": 200,
    "house_price": ""
  },
  {
    "colour": "Yellow",
    "index": 26,
    "name": "Leicester Square",
    "value": 260,
    "house_price": 130
  },
  {
    "colour": "Yellow",
    "index": 27,
    "name": "Coventry Street",
    "value": 260,
    "house_price": 130
  },
  {
    "colour": "Yellow",
    "index": 29,
    "name": "Piccadilly",
    "value": 280,
    "house_price": 140
  },
  {
    "colour": "Green",
    "index": 31,
    "name": "Regent Street",
    "value": 300,
    "house_price": 150
  },
  {
    "colour": "Green",
    "index": 32,
    "name": "Oxford Street",
    "value": 300,
    "house_price": 150
  },
  {
    "colour": "Green",
    "index": 34,
    "name": "Bond Street",
    "value": 320,
    "house_price": 160
  },
  {
    "colour": "Station",
    "index": 35,
    "name": "Liverpool Street station",
    "value": 200,
    "house_price": ""
  },
  {
    "colour": "Dark blue",
    "index": 37,
    "name": "Park Lane",
    "value": 350,
    "house_price": 175
  },
  {
    "colour": "Dark blue",
    "index": 39,
    "name": "Mayfair",
    "value": 400,
    "house_price": 200
  }
]