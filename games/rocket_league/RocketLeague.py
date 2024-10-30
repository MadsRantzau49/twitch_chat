from GameController import GameController
import os
from functools import partial

class RocketLeague(GameController):
    def process_message(self, message):
        self.valid_inputs = {"w", "a", "s", "d", "b", "j"}
        self.valid_functions = {
            "aerial": partial(self.run_sequence, "aerial.txt"),
            "frontflip": partial(self.run_sequence, "frontflip.txt"),
            "kickoffc": partial(self.run_sequence, "kickoff_center.txt"),
            "kickoffl": partial(self.run_sequence, "kickoff_left.txt"),
            "kickoffr": partial(self.run_sequence, "kickoff_right.txt"),
            "kickoffcl": partial(self.run_sequence, "kickoff_center_left.txt"),
            "kickoffcr": partial(self.run_sequence, "kickoff_center_right.txt")
        }
        if len(message) == 1 and message in self.valid_inputs:
            self.press_key(0, message, 0.5)
        elif message in self.valid_functions:
            self.valid_functions[message]()  # Now this will call the function
        else:
            self.press_valid_string(message)

    def run_sequence(self, file):
        sequence = eval(open(os.path.join(os.path.dirname(__file__), file)).read().strip())
        self.press_multiple_keys(sequence)
