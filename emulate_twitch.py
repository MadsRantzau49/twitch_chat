from rocket_league import *
import threading
import random


def emulator():
    rl = Rocket_League() 
    
    # Create a thread for the controller method
    controller_thread = threading.Thread(target=rl.controller)
    controller_thread.start()  # Start the controller in a separate thread

    while True:
        valid_inputs_char = ["w", "a", "d"]
        random_element = random.choice(valid_inputs_char)
        rl.new_input(random_element)
        rl.new_input("wwwwwwww")
          # Process the input message

# Start the emulator function
emulator()