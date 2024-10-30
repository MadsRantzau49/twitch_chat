from pynput.keyboard import Controller
import time
from find_open_game import find_open_game
import threading

class GameController:
    def __init__(self, queue_length=10):
        self.keyboard = Controller()
        self.queue_length = queue_length
        self.input_queue = []
        self.game = None

    def new_input(self, message):
        if self.is_string_too_long(message, 20):
            return
        if len(self.input_queue) >= self.queue_length:
            self.dequeue_input()
        self.enqueue_input(message)

    def controller(self):
        while True:
            if not self.input_queue:
                time.sleep(0.1)
                continue
            message = self.dequeue_input()
            self.process_message(message)

    def press_valid_string(self, message):
        for char in message:
            self.press_key(0, char, 0.3)
    
    def press_sequence(self, sequence):
        for key, duration in sequence:
            self.press_key(key, duration)

    def process_message(self, message):
        if message == "newgame":
            self.game = find_open_game()
            return
        if self.game:
            self.game.process_message(message)

    def press_key(self, timing, key, duration):
        time.sleep(timing)
        self.keyboard.press(key)
        time.sleep(duration)
        self.keyboard.release(key)



    def press_multiple_keys(self, sequence):
        threads = []
        
        for timing, key, duration in sequence:
            thread = threading.Thread(target=self.press_key, args=(timing, key, duration))
            threads.append(thread)
            thread.start()
    
        for thread in threads:
            thread.join()

    def enqueue_input(self, message):
        self.input_queue.append(message)

    def dequeue_input(self):
        return self.input_queue.pop(0)

    def is_string_too_long(self, message, max_length):
        return len(message) > max_length

    def print_queue(self):
        print(self.input_queue)

