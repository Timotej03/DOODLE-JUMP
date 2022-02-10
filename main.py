import pyglet
from pyglet import gl
import random
from pyglet.window import key
from pyglet.window import Window
pyglet.graphics.Batch
w1 = pyglet.window.Window()
w1.set_visible(False)
w2 = pyglet.window.Window()
w2.set_visible(False)
#konstanty
co_x = 100
co_y = 50
SIRKA = 300
VYSKA = 550

#lopta
velkost_lopty = 25
rychlost_lopty = 1000 #px/s
FARBA = (50, 225, 30)

#ostrovceky
SIRKA_OSTROVU = 25
VYSKA_OSTROVU = 5

#FONT
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30




window = pyglet.window.Window(width=SIRKA,height=VYSKA)






pyglet.app.run()


