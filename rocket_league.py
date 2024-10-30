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
            if not self.input_queue:
                time.sleep(0.1) 
                continue

            message = self.input_queue.pop(0)
            self.process_message(message)

    def process_message(self, message):
        valid_inputs = {"w", "a", "d", "s", "b", "j"}

        if message in valid_inputs:
            self.press_key(message, 0.3)
        elif message == "arial":
            self.arial()
        elif message == "frontflip":
            self.frontflip()
        else:
            self.press_valid_chars(message, valid_inputs)

    def press_valid_chars(self, message, valid_inputs):
        for char in message:
            if char in valid_inputs:
                self.press_key(char, 0.1)
            else:
                return

    def press_key(self,key,time_press):
        self.keyboard.press(key)
        time.sleep(time_press)
        self.keyboard.release(key)

    def is_string_too_long(self, message, max_length):
        return len(message) > max_length

    def print_queue(self):
        print(self.input_queue)

    def arial(self):
        arial_input = [
            ["j", 0.4],
            ["j", 0.4],
            ["s", 0.4],
            ["b", 4] 
        ]
        for input in arial_input:
            self.press_key(input[0],input[1])

    def frontflip():
        pass

