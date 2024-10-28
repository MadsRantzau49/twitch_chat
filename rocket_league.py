from pynput.keyboard import Controller
import time

def rocket_league_input(input_key):
    # Initialize the keyboard controller
    keyboard = Controller()

    # List of valid inputs
    valid_inputs = ["w", "a", "d", "s", "b", "j"]

    if input_key in valid_inputs:
        keyboard.press(input_key)  # Press the key down
        time.sleep(0.5)  # Hold it down for 1 second
        keyboard.release(input_key)  # Release the key

