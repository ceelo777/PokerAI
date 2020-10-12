import random
from poker import Suit, Rank, Card

class PokerGame:

    def __init__(self, numPlayers):
        # Jack, Queen, King    
        self.jack = Rank('J')
        self.queen = Rank('Q')
        self.king = Rank('K')
        deck = [jack, queen, king]       

        # Distribute the cards to each player
        random.shuffle(deck)
        self.deck = deck
        self.hands = deck[:numPlayers]

        # Initialize pot of the game
        self.pot = 0

        # History of the Game (random chance event, check action, bet action)
        self.history = "rr"

        # Cards on the table
        self.cardsOnTable = []

        # Small, big blind
        self.smallBlind = ""
        self.bigBlind = ""        

    def get_info_set(i_map, card, history):
        key = card + " " + history
        if key not in i_map:            
            info_set = InformationSet(key, 3)
            i_map[key] = info_set
            return info_set
        return i_map[key]

    
    def makeAction(self, player, action, amount):
        pass

    def isTerminal(self, history):
        pass

    # def getBestAction(self, player):
    #     pass