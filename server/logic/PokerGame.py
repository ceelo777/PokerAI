import random
from poker import Suit, Rank, Card

class PokerGame:

    def __init__(self, num_players, num_cards, input_deck, small_blind, big_blind, player_amounts):
        '''
        Basic info
        '''
        # Number of players + cards
        if (num_players * num_cards > len(self.deck)):
            raise ValueError("The combination of the number of players and the number of cards for each player does not match")
        self.num_players = num_players
        self.num_cards = num_cards
        # Small, big blind
        self.small_blind = small_blind
        self.big_blind = big_blind
        # Player starting amounts
        self.player_amounts = player_amounts
        self.deck = [Card(card) for card in input_deck]

        '''
        Fields to keep track of the playing field
        '''
        # Initialize pot of the game
        self.pot = 0
        # Cards on the table
        self.cardsOnTable = []
        # Index of card in deck
        self.deck_index = 0

        '''
        Stats
        '''
        # History of the Game (random chance event, check action, bet action)
        self.history = ""
    
    def resetRound(self):
        self.pot = 0
        self.cardsOnTable = []
        self.deck_index = 0
    
    def dealCards(self):
        # Distribute the cards to each player
        random.shuffle(self.deck)
        self.hands = [self.deck[self.num_cards * i: self.num_cards * (i + 1)] for i in range(self.num_players)]
        self.deck_index = self.num_players * self.num_cards
    
    def dealCardsOnTable(self, num_deal, num_burn):
        self.deck_index += num_burn
        for i in range(num_deal):
            if (deck_index > len(self.deck) - 1):
                raise ValueError("Ran out of cards")
            self.cardsOnTable.append(self.deck[deck_index])
            deck_index += 1

    def flop(self):
        self.dealCardsOnTable(3, 1)
    
    def turn(self):
        self.dealCardsOnTable(1, 1)
    
    def river(self):
        self.dealCardsOnTable(1, 1)

    def makeAction(self, player, action, amount):
        pass

    def isRoundEnd(self, history):
        pass

    def isGameEnd(self):
        return sum([1 if self.player_amounts[playerIndex] > 0 else 0 for playerIndex in self.player_amounts]) <= 1
    
    '''
    Getters and setters
    '''
    def get_num_players(self):
        return self.num_players
    
    def get_num_cards(self):
        return self.num_cards
    
    def get_small_blind(self):
        return self.small_blind
    
    def set_small_blind(self, small_blind):
        self.small_blind = small_blind
    
    def get_big_blind(self):
        return self.big_blind
    
    def set_big_blind(self, big_blind):
        self.big_blind = big_blind
    
    def get_player_amounts(self):
        return self.player_amounts
    
    def set_player_amounts(self, player_amounts):
        self.player_amounts = player_amounts
    
    def get_deck(self):
        return self.deck
    
    def set_deck(self, deck):
        self.deck = deck

    def get_pot(self):
        return self.pot
    
    def set_pot(self, pot):
        self.pot = pot

    def get_cardsOnTable(self):
        return self.cardsOnTable
    
    def set_cardsOnTable(self, cardsOnTable):
        self.cardsOnTable = cardsOnTable

    def get_history(self):
        return self.history
    
    def set_history(self, history):
        self.history = history
    
        
if __name__ == "__main__":
    # Kuhn Poker setup
    deck = ["Js", "Qs", "Ks"]
    game = PokerGame(
        num_players=2
        num_cards=1
        input_deck=deck
        small_blind=1
        big_blind=1
        player_amounts={"Alice": 2, "Bob": 2}
    )