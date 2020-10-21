from InformationSet import InformationSet
import numpy as np

class Model:
    
    def __init__(self, history, num_cards):
        self.history = ""                
        self.num_actions = 2
        self.pr_1 = 1
        self.pr_2 = 1
        self.pr_c = 1
        
        self.card_1 = -1
        self.card_2 = -1

        self.info_map = {}
        self.iterations = 10000
        self.expected_game_value = 0

        self.num_cards = num_cards
        self.n_possibilities = self.num_cards * (self.num_cards - 1)

        for i in range(self.iterations):
            # Add CFR to expected game value
            self.expected_game_value += self.cfr(self.info_map, self.history, self.card_1, self.card_2, self.pr_1, self.pr_2, self.pr_c)
            # expected_game_value += [insert cfr call here]            
            for i_set in info_map:
                i_set.next_strategy()
        self.expected_game_value /= iterations

        display_results(self.expected_game_value, self.info_map)


    # recursive method -- check for base case
    def cfr(self, i_map, history, card_1, card_2, pr_1, pr_2, pr_c):
        # if we've reached a chance node
        if (self.is_chance_node(history)):
            return self.chance_util(i_map)

        # if we've reached a terminal node (game is finished)
        if (self.is_terminal_node(history)):
            return self.terminal_util(history, card_1, card_2)

        # Calculate the length of history to find whose turn it is
        history_len = len(history)        
        
        # Check whose turn it is (0 for Player 1, and 1 for Player 2)
        player_1_turn = history_len % 2 == 0

        # Get the information set
        info_set = self.get_info_set(i_map, card_1 if not player_1_turn else card_2, history)

        # Get the appropriate strategy from the information set
        info_set_strategy = info_set.strategy        

        # Update the reach probabilities accordingly
        if player_1_turn:
            info_set.reach_pr += pr_1
        else:
            info_set.reach_pr += pr_2
        
        # Counterfactual utility per action
        action_utils = np.zeros(self.num_actions)

        # Run through all the possibile actions (in Kuhn Poker, it is just check and bet)
        for i, action in enumerate(["c", "b"]):
            next_history = history + action
            if player_1_turn:
                action_utils[i] = -1 * self.cfr(i_map, next_history, card_1, card_2, pr_1 * info_set_strategy[i], pr_2, pr_c)
            else:
                action_utils[i] = -1 * self.cfr(i_map, next_history, card_1, card_2, pr_1, pr_2 * info_set_strategy[i], pr_c)

        # Utility of information sets
        util = sum(action_utils * info_set_strategy)
        regrets = action_utils - util
        if player_1_turn:
            info_set.regret_sum += pr_2 * pr_c * regrets
        else:
            info_set.regret_sum += pr_1 * pr_c * regrets
        
        return util


    def get_info_set(self, i_map, card, history):
        key = f"{card} {history}"
        if key not in i_map:            
            info_set = InformationSet(key, 3)
            i_map[key] = info_set
            return info_set
        return i_map[key]

    def is_chance_node(self, history):
        return history == ""
    
    def chance_util(self, i_map):
        expected_value = 0
        for i in range(self.num_cards):
            for j in range(self.num_cards):
                if i != j:
                    expected_value += self.cfr(i_map, "rr", i, j, 1, 1, 1 / self.n_possibilities)  # TODO: fix this method call
        return expected_value / n_possibilities
    
    def is_terminal_node(self, history):
        terminal_nodes = ["rrcbc", "rrcc", "rrcbb", "rrbc", "rrbb"]
        return history in terminal_nodes
    
    def terminal_util(self, history, card_1, card_2):
        # Initialize length of history to find whose turn it is
        n = len(history)

        this_card = card_1 if (n % 2 == 0) else card_2
        opp_card = card_2 if (n % 2 == 1) else card_1

        # If last player folds, we win
        if (history == "rrcbc" or history == "rrbc"):
            return 1

        # If both players check, greater card wins
        if (history == "rrcc"):
            if (this_card > opp_card):
                return 1
            return -1
        
        # If both players bet, greater card wins with double reward/loss
        if (history == "rrcbb" or history == "rrbb"):
            if (this_card > opp_card):
                return 2
            return -2
    
    def card_str(self, card):
        if card == 0:
            return "J"
        elif card == 1:
            return "Q"
        return "K"
    
    def display_results(self, ev, i_map):
        print("Player 1 Expected Value: {}".format(ev))
        print("Player 2 Expected Value: {}".format(-1 * ev))

        print()
        print("Player 1 Strategies: ")
        sorted_items = sorted(i_map.items(), key=lambda x: x[0])
        for _, v in filter(lambda x: len(x[0]) % 2 == 0, sorted_items):
            print(v)
        print()
        print("Player 2 Strategies: ")
        for _, v in filter(lambda x : len(x[0]) % 2 == 1, sorted_items):
            print(v)

if __name__ == "__main__":
    # call functionality here
    test_model = Model("", 3)