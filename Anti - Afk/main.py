import keyboard
import time
while "app run":
    time.sleep(3)
    keyboard.press("w")
    keyboard.press("a")
    keyboard.press("s")
    keyboard.press("d")

    if  keyboard.is_pressed('space'):
        app = crash
    else:
        pass
    time.sleep(5)
    keyboard.press("w")
    keyboard.press("a")
    keyboard.press("s")
    time.sleep(2)
    keyboard.press("d")
