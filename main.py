import pygame
from pyglet import gl
import random
from pyglet.window import key
from pyglet.window import Window
pyglet.graphics.Batch

obrazok = pygame.image.load('doodle.png')

#konstanty
co_x = 100
co_y = 50
SIRKA = 300
VYSKA = 550
stisknute_klavesy = set()
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

def stisk_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.add(("hore", 0))
    if symbol == key.S:
        stisknute_klavesy.add(("dole", 0))
    if symbol == key.UP:
        stisknute_klavesy.add(("hore", 1))
    if symbol == key.DOWN:
        stisknute_klavesy.add(("dole", 1))

def pusti_klavesnice(symbol, modifikatory):
    if symbol == key.W:
        stisknute_klavesy.discard(("hore", 0))
    if symbol == key.S:
        stisknute_klavesy.discard(("dole", 0))
    if symbol == key.UP:
        stisknute_klavesy.discard(("hore", 1))
    if symbol == key.DOWN:
        stisknute_klavesy.discard(("dole", 1))


window = pyglet.window.Window(width=SIRKA, height=VYSKA)
pyglet.app.run()


