from pynput.keyboard import Controller
import time

class Rocket_League:
    def __init__(self):
        self.keyboard = Controller()
        self.queue_length = 10
        self.input_queue = [] 

    def new_input(self,message):
        if self.is_string_too_long(message,10):
            return
        if len(self.input_queue) >= self.queue_length:
            self.input_queue.pop(0)
        # Add the new element to the end of the list
        self.input_queue.append(message)

    def controller(self):
        while True:
        # List of valid inputs
            if len(self.input_queue) == 0:
                pass
            else:
                message = self.input_queue[0]
                print(f"input= {message}\ntype={type(message)}")
                self.input_queue.pop(0)
                valid_inputs_char = ["w", "a", "d", "s", "b", "j"]

                if message in valid_inputs_char:
                    self.press_key(message,0.3)
                elif message == "arial":
                    self.arial()
                elif message == "frontflip":
                    self.frontflip
                else:
                    for char in message:
                        if char in valid_inputs_char:
                            self.press_key(char,0.1)

    def press_key(self,key,time_press):
        self.keyboard.press(key)
        time.sleep(time_press)
        self.keyboard.release(key)

    def is_string_too_long(self, message, max_length):
        return len(message) > max_length
    
    def print_queue(self):
        print(self.input_queue)

    def arial():
        pass
    def frontflip():
        pass

