# from pynput.mouse import Controller
from pynput.keyboard import Controller

def mousecontroller():
    my_mouse = Controller()
    my_mouse.position = (1000, 200)

def keyboardcontroller():
    my_keyboard = Controller()
    my_keyboard.type('Hello brother, I am happy for you ')
