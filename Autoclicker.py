import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

print("STARTING...")

# Here is the key you need to press for the autoclicker to start. By default, we use "p".
TOGGLE_KEY = KeyCode(char="p")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.02)  # 0.05
        

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

print(f"\nSTARTED. Press {TOGGLE_KEY} to auto click!")

with Listener(on_press=toggle_event) as listener:
    listener.join()


