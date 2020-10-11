from aspects.store import chance, community, board, properties, utilities

chance_set = list(chance.values())
community_set = list(community.values())

class Board:
    def __init__(self, player_count=4):
        self.players = []

        # Card piles
        self.chance_set = chance_set
        self.community_set = community_set

        # Places on the board
        self.squares = board
        self.owned_properties = dict.fromkeys(properties + utilities)