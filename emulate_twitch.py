from games.rocket_league.RocketLeague import *
import threading
import random


def emulator():
    rl = RocketLeague() 
    
    # Create a thread for the controller method
    threading.Thread(target=rl.controller).start()

    while True:
        valid_inputs_char = ["w", "a", "d","w","w","w","w","w","w"]
        random_element = random.choice(valid_inputs_char)
        rl.new_input(random_element)
        # rl.new_input("wwwwwwww")w
          # Process the input message

# Start the emulator function
time.sleep(5)
emulator()
