from pypokerengine.api.emulator import Emulator
from pypokerengine.engine import player
from pypokerengine.utils.game_state_utils import restore_game_state, attach_hole_card, attach_hole_card_from_deck

import uuid

emulator = Emulator()
emulator.set_game_rule(nb_player=2, max_round=10, sb_amount=5, ante_amount=0)

class OneActionModel(BasePokerPlayer):

    FOLD, CALL, MIN_RAISE, MAX_RAISE = 0, 1, 2, 3

    def set_action(self, action):
        self.action = action

    def declare_action(self, valid_actions, hole_card, round_state):
        if self.FOLD == self.action:
            return valid_actions[0]['action'], valid_actions[0]['amount']
        elif self.CALL == self.action:
            return valid_actions[1]['action'], valid_actions[1]['amount']
        elif self.MIN_RAISE == self.action:
            return valid_actions[2]['action'], valid_actions[2]['amount']['min']
        elif self.MAX_RAISE == self.action:
            return valid_actions[2]['action'], valid_actions[2]['amount']['max']
        else:
            raise Exception("Invalid action [ %s ] is set" % self.action)

players_raw_info = {
    "Alice": 1000,
    "Bob": 1000,
}

players_info = {uuid.uuid4(): {"name": name, "stack": stack} for (name, stack) in players_raw_info.items()}
initial_game_state = emulator.generate_initial_game_state(players_info)

# def setup_game_state(round_state, my_hole_card):
#     game_state = restore_game_state(round_state)
#     for player_info in round_state['seats']:
#         if uuid == self.uuid:
#             # Hole card of my player should be fixed. Because we know it.
#             game_state = attach_hole_card(game_state, uuid, my_hole_card)
#         else:
#             # We don't know hole card of opponents. So attach them at random from deck.
#             game_state = attach_hole_card_from_deck(game_state, uuid)