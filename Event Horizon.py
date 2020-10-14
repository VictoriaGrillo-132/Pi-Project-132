import os
from tkinter import *
from datetime import datetime



#current version of the game
TITLE = "Event Horizon"
VERSION = 0.0
LAST_UPDATE = datetime.fromtimestamp(os.path.getmtime(__file__))
AUTHOR = 'JA, ID, VG'


#setting screen size
width = 900
height = 500
window= Tk()
window.geometry('{}x{}'.format(width, height))
window.title(TITLE)
