import random
from poker import Suit, Rank, Card

class PokerGame:

    def __init__(self, num_players, num_cards, input_deck, small_blind, big_blind, player_amounts):
        if (num_players * num_cards > len(input_deck)):
            raise ValueError(f"There aren't enough cards in the deck for {num_players} players to have {num_cards} cards")
        '''
        Number of players in the game (to start)
        '''
        self.num_players = num_players

        '''
        Number of cards per player
        '''
        self.num_cards = num_cards
        
        '''
        Initial small blind
        '''
        self.small_blind = small_blind

        '''
        Initial big blind
        '''
        self.big_blind = big_blind

        '''
        Player starting amounts. Should include each player's name mapped to starting amounts
        e.g. {Alice: 1000, Bob: 1000, Chris: 1500}
        '''
        self.player_amounts = player_amounts

        # '''
        # Active Players
        # '''
        # self.active_players = []                

        '''
        Initialize player order and dealers
        '''
        self.player_order = player_amounts.keys()
        self.dealer_index = 0
        self.curr_player = 0

        '''
        Game deck initialized with the Card class from the poker package
        '''
        self.deck = [Card(card) for card in input_deck]

        '''
        Fields to keep track of the playing field
        '''
        # Initialize pot of the game
        self.pot = [0]
        # Players who go all in
        self.allIn_players = []
        # Current bet
        self.bet = 0
        # Cards on the table
        self.cardsOnTable = []
        # Index of card in deck
        self.deck_index = 0

        # Bets of each player
        self.player_bets = {player: 0 for player in player_amounts}

        '''
        Stats
        '''
        # History of the Game (random chance event, check action, bet action)
        self.history = ""
    
    def startRound(self):
        """
        Start a new round
        """
        self.pot = [0]
        self.allIn_players = []
        self.bet = 0
        self.cardsOnTable = []
        self.deck_index = 0
        self.dealer_index = (self.dealer_index - 1) % len(self.player_order)
        self.curr_player = (self.dealer_index - 3) % len(self.player_order)   
        self.player_bets = {player: 0 for player in self.player_amounts}        

    def dealCards(self):
        """
        Deal cards to the players
        """
        random.shuffle(self.deck)
        self.hands = [self.deck[self.num_cards * i: self.num_cards * (i + 1)] for i in range(self.num_players)]
        self.deck_index = self.num_players * self.num_cards
    
    def dealCardsOnTable(self, num_deal, num_burn=0):
        """
        Deal cards on the table
        Can specify a number of cards to burn
        """
        self.deck_index += num_burn
        for i in range(num_deal):
            if (deck_index > len(self.deck) - 1):
                raise ValueError("Ran out of cards")
            self.cardsOnTable.append(self.deck[deck_index])
            deck_index += 1
        
    """
    Some commonly used terms in poker to deal cards
    """
    def flop(self):
        self.dealCardsOnTable(3, 1)
    
    def turn(self):
        self.dealCardsOnTable(1, 1)
    
    def river(self):
        self.dealCardsOnTable(1, 1)

    
    def makeAction(self, player, action, raise_amount=0):
        if player not in self.active_players:
            raise ValueError(f"{player} is out of the round and can't make an action")

        if (self.active_players.index(player) != self.curr_player):
            raise ValueError(f"it is not {player}'s turn.")

        # variable - how much is being bet right now 
        # if someone checks - see if they have enough to match that variable (0)
        # raise(rR, rA), check(check: c), fold(f)
        if (action == "f"):
            del self.player_bets[player]
        elif (action == "c"):
            amount_added = self.bet - self.player_bets[player]
            if (self.player_amounts[player] < amount_added):
                raise ValueError(f"{player} does not have enough money to check")
            self.player_amounts[player] -= amount_added
            self.pot[-1] += amount_added
            self.player_bets[player] = self.bet
        elif (action == "r"):
            # raise action
            amount = (self.bet + raise_amount) - self.player_bets[player]
            if (self.player_amounts[player] < amount):
                raise ValueError(f"the player does not have enough money to raise")
            self.player_amounts[player] -= amount
            pot += amount
            self.bet += raise_amount
            self.player_bets[player] = self.bet
            
            # all-in logic :weary:
            

        else:
            raise ValueError("Action is not recognized, try again")
    
    def finishRound(self):
        """
        if the round is done
        """
        # TODO: change this logic to account for all in players
        amount_to_give = self.pot / len(self.active_players)
        for player in self.active_players:
            self.player_amounts[player] += amount_to_give

    def isRoundEnd(self):
        return len(self.active_players) == 1
        
    def isGameEnd(self):
        return sum([1 if self.player_amounts[playerIndex] > 0 else 0 for playerIndex in self.player_amounts]) <= 1
    
        
if __name__ == "__main__":
    # Kuhn Poker setup
    kp_deck = ["Js", "Qs", "Ks"]
    kp_game = PokerGame(
        num_players=2,
        num_cards=1,
        input_deck=kp_deck,
        small_blind=1,
        big_blind=1,
        player_amounts={"Alice": 2, "Bob": 2},
    )

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
'''