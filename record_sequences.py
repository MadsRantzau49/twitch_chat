from pynput import keyboard
import time

# Flag to indicate whether logging is enabled
logging_enabled = False
start_time = None  # To track the start time of key presses
sequence = []  # To store the sequence of key presses
press_times = {}  # To store the press times of each key

def toggle_logging():
    global logging_enabled, start_time
    logging_enabled = not logging_enabled
    if logging_enabled:
        start_time = time.time()  # Set the start time when logging starts
        print("Logging started.")
    else:
        print("Logging stopped. Sequence recorded:", sequence)

def on_press(key):
    global start_time, press_times

    try:
        # Stop listener if 'esc' key is pressed
        if key == keyboard.Key.esc:
            toggle_logging()
            return False
        if key == keyboard.KeyCode.from_char('l'):
            toggle_logging()
            return  # Do not log 'l' key press
        elif not logging_enabled:
            return  # Do not log if logging is not enabled

        # Record the press event with elapsed time
        elapsed_time = time.time() - start_time
        if key not in press_times:  # Only store if the key is not already pressed
            press_times[key] = elapsed_time  # Store the press time for this key
            print(f"Pressed {key} at {elapsed_time:.2f}s")

    except Exception as e:
        print(f"Error on_press: {e}")

def on_release(key):
    global sequence, press_times

    try:
        if not logging_enabled:
            return  # Do not log if logging is not enabled

        # Check if the released key was pressed before
        if key in press_times:
            press_start_time = press_times.pop(key)  # Remove and get the press time
            elapsed_time = time.time() - start_time
            press_duration = elapsed_time - press_start_time
            
            # Add the recorded sequence in the specified format
            sequence.append((press_start_time, key.char if hasattr(key, 'char') else str(key), press_duration))
            print(f"Released {key} for {press_duration:.2f}s (start at {press_start_time:.2f}s)")

    except Exception as e:
        print(f"Error on_release: {e}")

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Print the recorded sequence when the listener stops
print("Recorded sequence:", sequence)
