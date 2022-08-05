from pygame import *
from bottle import Bottle
from settings import *

from random import randint

bg_color = 243, 186, 219
W, H = 1000, 700

win = display.set_mode((W,H))
display.set_caption("python bottle")
icon_surface = image.load("icon.jpg")
display.set_icon(icon_surface) 

colors = list(colors_codes.keys())

def re_load():
    Bottle.bottles = []
    for i in range(5):
        Bottle((50+200*i,100), win, colors={1:{colors[randint(0, len(colors)-1)]:randint(50,200)},
                                            2:{colors[randint(0, len(colors)-1)]:randint(50,100)}})

firts_pick = None
second_pick = None

def loose():
    re_load()

def check_win():
    for bottle in Bottle.bottles:
        if len(bottle.colors) > 1: return False
    return True

re_load()
while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
        
        if e.type == MOUSEBUTTONDOWN:
            for bottle in Bottle.bottles:
                if bottle.rect.collidepoint(e.pos):
                    if firts_pick: 
                        second_pick = bottle
                        if firts_pick.move_top_to(second_pick) == "loose":
                            loose()
                        firts_pick, second_pick = None, None

                    else:
                        firts_pick = bottle
                        bottle.pick()

    win.fill(bg_color)

    for bottle in Bottle.bottles:
        bottle.draw()

    if check_win(): re_load()

    display.update()

