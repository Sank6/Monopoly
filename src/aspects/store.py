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
    "Colour": "Brown",
    "Index": 1,
    "Name": "Old Kent Road",
    "Value (£)": 60,
    "House price (£)": 30
  },
  {
    "Colour": "Brown",
    "Index": 3,
    "Name": "Whitechapel Road",
    "Value (£)": 60,
    "House price (£)": 30
  },
  {
    "Colour": "Station",
    "Index": 5,
    "Name": "King's Cross station",
    "Value (£)": 200,
    "House price (£)": ""
  },
  {
    "Colour": "Light blue",
    "Index": 6,
    "Name": "The Angel, Islington",
    "Value (£)": 100,
    "House price (£)": 50
  },
  {
    "Colour": "Light blue",
    "Index": 8,
    "Name": "Euston Road",
    "Value (£)": 100,
    "House price (£)": 50
  },
  {
    "Colour": "Light blue",
    "Index": 9,
    "Name": "Pentonville Road",
    "Value (£)": 120,
    "House price (£)": 60
  },
  {
    "Colour": "Pink",
    "Index": 11,
    "Name": "Pall Mall",
    "Value (£)": 140,
    "House price (£)": 70
  },
  {
    "Colour": "Pink",
    "Index": 13,
    "Name": "Whitehall",
    "Value (£)": 140,
    "House price (£)": 70
  },
  {
    "Colour": "Pink",
    "Index": 14,
    "Name": "Northumberland Avenue",
    "Value (£)": 160,
    "House price (£)": 80
  },
  {
    "Colour": "Station",
    "Index": 15,
    "Name": "Marylebone station",
    "Value (£)": 200,
    "House price (£)": ""
  },
  {
    "Colour": "Orange",
    "Index": 16,
    "Name": "Bow Street",
    "Value (£)": 180,
    "House price (£)": 90
  },
  {
    "Colour": "Orange",
    "Index": 18,
    "Name": "Marlborough Street",
    "Value (£)": 180,
    "House price (£)": 90
  },
  {
    "Colour": "Orange",
    "Index": 19,
    "Name": "Vine Street",
    "Value (£)": 200,
    "House price (£)": 100
  },
  {
    "Colour": "Red",
    "Index": 21,
    "Name": "Strand",
    "Value (£)": 220,
    "House price (£)": 110
  },
  {
    "Colour": "Red",
    "Index": 23,
    "Name": "Fleet Street",
    "Value (£)": 220,
    "House price (£)": 110
  },
  {
    "Colour": "Red",
    "Index": 24,
    "Name": "Trafalgar Square",
    "Value (£)": 240,
    "House price (£)": 120
  },
  {
    "Colour": "Station",
    "Index": 25,
    "Name": "Fenchurch Street station",
    "Value (£)": 200,
    "House price (£)": ""
  },
  {
    "Colour": "Yellow",
    "Index": 26,
    "Name": "Leicester Square",
    "Value (£)": 260,
    "House price (£)": 130
  },
  {
    "Colour": "Yellow",
    "Index": 27,
    "Name": "Coventry Street",
    "Value (£)": 260,
    "House price (£)": 130
  },
  {
    "Colour": "Yellow",
    "Index": 29,
    "Name": "Piccadilly",
    "Value (£)": 280,
    "House price (£)": 140
  },
  {
    "Colour": "Green",
    "Index": 31,
    "Name": "Regent Street",
    "Value (£)": 300,
    "House price (£)": 150
  },
  {
    "Colour": "Green",
    "Index": 32,
    "Name": "Oxford Street",
    "Value (£)": 300,
    "House price (£)": 150
  },
  {
    "Colour": "Green",
    "Index": 34,
    "Name": "Bond Street",
    "Value (£)": 320,
    "House price (£)": 160
  },
  {
    "Colour": "Station",
    "Index": 35,
    "Name": "Liverpool Street station",
    "Value (£)": 200,
    "House price (£)": ""
  },
  {
    "Colour": "Dark blue",
    "Index": 37,
    "Name": "Park Lane",
    "Value (£)": 350,
    "House price (£)": 175
  },
  {
    "Colour": "Dark blue",
    "Index": 39,
    "Name": "Mayfair",
    "Value (£)": 400,
    "House price (£)": 200
  }
]